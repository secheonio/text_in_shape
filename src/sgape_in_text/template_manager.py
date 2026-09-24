from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import Optional

from .models import TemplateDocument


class TemplateManager:
    """Template save/load utility for the .sit format."""

    @staticmethod
    def save_template(document: TemplateDocument, file_path: str | Path) -> str:
        path = Path(file_path)
        if path.suffix.lower() != ".sit":
            path = path.with_suffix(".sit")

        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("document.json", json.dumps(document.to_dict(), ensure_ascii=False, indent=2))

        return str(path)

    @staticmethod
    def load_template(file_path: str | Path) -> TemplateDocument:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Template file not found: {path}")

        with zipfile.ZipFile(path, "r") as archive:
            if "document.json" not in archive.namelist():
                raise ValueError("Invalid .sit template: missing document.json")
            data = json.loads(archive.read("document.json").decode("utf-8"))
        return TemplateDocument.from_dict(data)

    @staticmethod
    def export_json(document: TemplateDocument, file_path: str | Path) -> str:
        path = Path(file_path)
        path.write_text(json.dumps(document.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
        return str(path)

    @staticmethod
    def import_json(file_path: str | Path) -> TemplateDocument:
        data = json.loads(Path(file_path).read_text(encoding="utf-8"))
        return TemplateDocument.from_dict(data)
