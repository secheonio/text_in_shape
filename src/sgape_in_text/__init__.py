"""Backward-compatible package export for the legacy package name."""

from __future__ import annotations

__all__ = ["EditorApp", "Paper", "ShapeItem", "TemplateDocument", "create_app"]


def __getattr__(name: str):
    if name == "EditorApp":
        from .editor import EditorApp
        return EditorApp
    if name in {"Paper", "ShapeItem", "TemplateDocument"}:
        from .models import Paper, ShapeItem, TemplateDocument
        return {
            "Paper": Paper,
            "ShapeItem": ShapeItem,
            "TemplateDocument": TemplateDocument,
        }[name]
    if name == "create_app":
        from .web_app import create_app
        return create_app
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(__all__)
