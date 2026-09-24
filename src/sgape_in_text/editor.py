from __future__ import annotations

import json
import os
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, simpledialog
from typing import Optional

from PIL import Image, ImageTk

from .models import Paper, ShapeItem, TemplateDocument
from .template_manager import TemplateManager


class EditorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Sgape-in-Text")
        self.geometry("1400x900")
        self.configure(bg="#f0f0f0")

        self.paper = Paper()
        self.document = TemplateDocument(paper=self.paper)
        self.selected_shape: Optional[ShapeItem] = None
        self.shape_id_counter = 1
        self.image_path: Optional[str] = None

        self._build_ui()
        self._reset_canvas()

    def _build_ui(self) -> None:
        toolbar = tk.Frame(self, bg="#d9d9d9", padx=8, pady=6)
        toolbar.pack(side="top", fill="x")

        tk.Button(toolbar, text="용지 선택", command=self.choose_paper).pack(side="left", padx=4)
        tk.Button(toolbar, text="사각형", command=lambda: self.add_shape("rectangle")).pack(side="left", padx=4)
        tk.Button(toolbar, text="원", command=lambda: self.add_shape("circle")).pack(side="left", padx=4)
        tk.Button(toolbar, text="타원", command=lambda: self.add_shape("ellipse")).pack(side="left", padx=4)
        tk.Button(toolbar, text="이미지 불러오기", command=self.load_image).pack(side="left", padx=4)
        tk.Button(toolbar, text="텍스트 입력", command=self.open_text_dialog).pack(side="left", padx=4)
        tk.Button(toolbar, text="저장 (.sit)", command=self.save_template).pack(side="left", padx=4)
        tk.Button(toolbar, text="불러오기 (.sit)", command=self.load_template).pack(side="left", padx=4)

        content = tk.Frame(self)
        content.pack(fill="both", expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(content, bg="#ffffff", width=1000, height=700, highlightthickness=1, highlightbackground="#999999")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        properties = tk.Frame(content, width=280, bg="#efefef")
        properties.pack(side="right", fill="y")

        tk.Label(properties, text="도형 속성", font=("Arial", 12, "bold"), bg="#efefef").pack(anchor="w", padx=10, pady=(10, 5))

        self.shape_title_var = tk.StringVar(value="")
        tk.Label(properties, textvariable=self.shape_title_var, bg="#efefef").pack(anchor="w", padx=10, pady=(0, 8))

        self.text_entry = tk.Text(properties, width=30, height=10)
        self.text_entry.pack(padx=10, pady=5)
        self.text_entry.bind("<FocusOut>", lambda event: self.update_selected_text())

        tk.Label(properties, text="폰트 크기", bg="#efefef").pack(anchor="w", padx=10)
        self.font_size_var = tk.StringVar(value="40")
        tk.Entry(properties, textvariable=self.font_size_var, width=10).pack(anchor="w", padx=10, pady=(0, 8))

        tk.Button(properties, text="적용", command=self.apply_shape_text_settings).pack(anchor="w", padx=10, pady=8)

    def choose_paper(self) -> None:
        options = {
            "A4": (2100, 2970),
            "A5": (1480, 2100),
            "Letter": (2159, 2794),
            "Custom": None,
        }

        choice = ask_paper_choice(self)
        if not choice:
            return

        if choice == "Custom":
            width = simpledialog.askinteger("사용자 지정 용지", "가로(px)", initialvalue=2100, minvalue=100)
            height = simpledialog.askinteger("사용자 지정 용지", "세로(px)", initialvalue=2970, minvalue=100)
            if width and height:
                self.paper = Paper(width=width, height=height, name="Custom")
        else:
            width, height = options[choice]
            self.paper = Paper(width=width, height=height, name=choice)

        self.document = TemplateDocument(paper=self.paper)
        self._reset_canvas()

    def _reset_canvas(self) -> None:
        self.canvas.delete("all")
        self.canvas.create_rectangle(10, 10, self.paper.width, self.paper.height, outline="#444444", width=2)
        self.canvas.create_text(self.paper.width / 2, 20, text=f"{self.paper.name} {self.paper.width}x{self.paper.height}", fill="#555555")

    def add_shape(self, shape_type: str) -> None:
        shape = ShapeItem(
            id=f"shape_{self.shape_id_counter}",
            type=shape_type,
            x=150 + (self.shape_id_counter * 30),
            y=130 + (self.shape_id_counter * 20),
            width=300,
            height=180,
            stroke="#000000",
            fill="#ffffff",
        )
        self.shape_id_counter += 1
        self.document.shapes.append(shape)
        self.selected_shape = shape
        self._draw_shapes()

    def _draw_shapes(self) -> None:
        self.canvas.delete("all")
        self.canvas.create_rectangle(10, 10, self.paper.width, self.paper.height, outline="#444444", width=2)

        if self.image_path:
            try:
                image = Image.open(self.image_path)
                image = image.resize((int(self.paper.width), int(self.paper.height)))
                photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, anchor="nw", image=photo)
                self.canvas.image = photo
            except Exception:
                self.image_path = None

        for shape in self.document.shapes:
            if shape.type == "rectangle":
                rect = self.canvas.create_rectangle(shape.x, shape.y, shape.x + shape.width, shape.y + shape.height, outline=shape.stroke, fill=shape.fill, width=2)
            elif shape.type == "circle":
                rect = self.canvas.create_oval(shape.x, shape.y, shape.x + shape.width, shape.y + shape.height, outline=shape.stroke, fill=shape.fill, width=2)
            elif shape.type == "ellipse":
                rect = self.canvas.create_oval(shape.x, shape.y, shape.x + shape.width, shape.y + shape.height, outline=shape.stroke, fill=shape.fill, width=2)
            else:
                rect = self.canvas.create_rectangle(shape.x, shape.y, shape.x + shape.width, shape.y + shape.height, outline=shape.stroke, fill=shape.fill, width=2)

            if shape is self.selected_shape:
                self.canvas.itemconfig(rect, width=4)

            if shape.text:
                inner_width = max(shape.width - shape.padding * 2, 40)
                self.canvas.create_text(
                    shape.x + shape.width / 2,
                    shape.y + shape.height / 2,
                    text=shape.text,
                    fill=shape.text_color,
                    font=(shape.font_family, shape.font_size),
                    anchor="center",
                    width=inner_width,
                    justify="center",
                )

    def on_canvas_click(self, event: tk.Event) -> None:
        for shape in reversed(self.document.shapes):
            if shape.contains_point(event.x, event.y):
                self.selected_shape = shape
                self._update_selection_ui()
                self._draw_shapes()
                return
        self.selected_shape = None
        self._update_selection_ui()

    def _update_selection_ui(self) -> None:
        if self.selected_shape is None:
            self.shape_title_var.set("선택된 도형 없음")
            self.text_entry.delete("1.0", "end")
            self.font_size_var.set("40")
            return

        self.shape_title_var.set(f"{self.selected_shape.type} #{self.selected_shape.id}")
        self.text_entry.delete("1.0", "end")
        self.text_entry.insert("1.0", self.selected_shape.text)
        self.font_size_var.set(str(self.selected_shape.font_size))

    def update_selected_text(self) -> None:
        if self.selected_shape is None:
            return
        self.selected_shape.text = self.text_entry.get("1.0", "end").strip()
        self._draw_shapes()

    def apply_shape_text_settings(self) -> None:
        if self.selected_shape is None:
            messagebox.showwarning("알림", "먼저 도형을 선택해주세요.")
            return
        try:
            self.selected_shape.font_size = int(self.font_size_var.get())
        except ValueError:
            messagebox.showwarning("알림", "폰트 크기는 숫자로 입력해주세요.")
            return
        self.selected_shape.text = self.text_entry.get("1.0", "end").strip()
        self._draw_shapes()

    def open_text_dialog(self) -> None:
        if self.selected_shape is None:
            messagebox.showwarning("알림", "먼저 도형을 선택해주세요.")
            return
        self.text_entry.focus_set()
        self.text_entry.select_range(0, "end")

    def load_image(self) -> None:
        file_path = filedialog.askopenfilename(title="이미지 선택", filetypes=[("이미지", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if not file_path:
            return
        self.image_path = file_path
        self.document.background_image = file_path
        self._draw_shapes()

    def save_template(self) -> None:
        file_path = filedialog.asksaveasfilename(
            title="템플릿 저장",
            defaultextension=".sit",
            filetypes=[("Sgape-in-Text 템플릿", "*.sit")],
        )
        if not file_path:
            return
        try:
            saved = TemplateManager.save_template(self.document, file_path)
            messagebox.showinfo("저장 완료", f"템플릿이 저장되었습니다.\n{saved}")
        except Exception as exc:  # pragma: no cover - UI feedback
            messagebox.showerror("저장 실패", str(exc))

    def load_template(self) -> None:
        file_path = filedialog.askopenfilename(title="불러오기", filetypes=[("Sgape-in-Text 템플릿", "*.sit")])
        if not file_path:
            return
        try:
            self.document = TemplateManager.load_template(file_path)
            self.paper = self.document.paper
            self.image_path = self.document.background_image
            self.selected_shape = self.document.shapes[0] if self.document.shapes else None
            self._draw_shapes()
            self._update_selection_ui()
            messagebox.showinfo("불러오기 완료", "템플릿을 불러왔습니다.")
        except Exception as exc:  # pragma: no cover - UI feedback
            messagebox.showerror("불러오기 실패", str(exc))


def ask_paper_choice(parent: tk.Misc) -> Optional[str]:
    top = tk.Toplevel(parent)
    top.title("용지 선택")
    top.transient(parent)
    top.grab_set()
    top.geometry("240x180")

    choice = tk.StringVar(value="A4")
    for option in ["A4", "A5", "Letter", "Custom"]:
        tk.Radiobutton(top, text=option, variable=choice, value=option).pack(anchor="w", padx=12, pady=4)

    result: Optional[str] = None

    def on_confirm() -> None:
        nonlocal result
        result = choice.get()
        top.destroy()

    tk.Button(top, text="확인", command=on_confirm).pack(pady=10)
    top.wait_window()
    return result
