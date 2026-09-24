from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Paper:
    width: int = 2100
    height: int = 2970
    name: str = "A4"


@dataclass
class ShapeItem:
    id: str
    type: str
    x: float
    y: float
    width: float
    height: float
    stroke: str = "#222222"
    fill: str = "#ffffff"
    text: str = ""
    text_color: str = "#111111"
    font_size: int = 40
    font_family: str = "Arial"
    padding: float = 30.0

    def contains_point(self, px: float, py: float) -> bool:
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height

    def move_by(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def resize_by(self, dw: float, dh: float) -> None:
        self.width += dw
        self.height += dh


@dataclass
class TemplateDocument:
    paper: Paper
    shapes: List[ShapeItem] = field(default_factory=list)
    background_image: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "paper": {
                "width": self.paper.width,
                "height": self.paper.height,
                "name": self.paper.name,
            },
            "background_image": self.background_image,
            "shapes": [
                {
                    "id": s.id,
                    "type": s.type,
                    "x": s.x,
                    "y": s.y,
                    "width": s.width,
                    "height": s.height,
                    "stroke": s.stroke,
                    "fill": s.fill,
                    "text": s.text,
                    "text_color": s.text_color,
                    "font_size": s.font_size,
                    "font_family": s.font_family,
                    "padding": s.padding,
                }
                for s in self.shapes
            ],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "TemplateDocument":
        paper = Paper(
            width=data.get("paper", {}).get("width", 2100),
            height=data.get("paper", {}).get("height", 2970),
            name=data.get("paper", {}).get("name", "A4"),
        )
        shapes = [
            ShapeItem(
                id=s.get("id", "shape"),
                type=s.get("type", "rectangle"),
                x=s.get("x", 0),
                y=s.get("y", 0),
                width=s.get("width", 200),
                height=s.get("height", 120),
                stroke=s.get("stroke", "#222222"),
                fill=s.get("fill", "#ffffff"),
                text=s.get("text", ""),
                text_color=s.get("text_color", "#111111"),
                font_size=s.get("font_size", 40),
                font_family=s.get("font_family", "Arial"),
                padding=s.get("padding", 30.0),
            )
            for s in data.get("shapes", [])
        ]
        return cls(paper=paper, shapes=shapes, background_image=data.get("background_image"))
