import tkinter as tk

from src.sgape_in_text.editor import EditorApp
from src.sgape_in_text.models import ShapeItem


def test_select_then_drag_moves_shape():
    root = tk.Tk()
    root.withdraw()
    try:
        app = EditorApp()
        app.withdraw()

        shape = ShapeItem(id="shape_1", type="rectangle", x=10, y=20, width=100, height=80)
        app.document.shapes.append(shape)

        click_event = type("Event", (), {"x": 50, "y": 30})()
        app.on_canvas_click(click_event)
        assert app.selected_shape is shape
        assert app.dragging_shape is None

        second_click = type("Event", (), {"x": 60, "y": 40})()
        app.on_canvas_click(second_click)
        assert app.dragging_shape is shape

        drag_event = type("Event", (), {"x": 90, "y": 90})()
        app.on_canvas_drag(drag_event)

        assert shape.x == 40
        assert shape.y == 70
    finally:
        root.destroy()
