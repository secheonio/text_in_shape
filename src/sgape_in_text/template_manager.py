from __future__ import annotations

import json
import tempfile
import zipfile
from pathlib import Path

from .models import TemplateDocument


class TemplateManager:
    """Template save/load utility for the .sit format."""

    @staticmethod
    def save_template(document: TemplateDocument, file_path: str | Path) -> str:
        path = Path(file_path)
        if path.suffix.lower() != ".sit":
            path = path.with_suffix(".sit")

        payload = document.to_dict()
        background_path = Path(document.background_image) if document.background_image else None

        if background_path and background_path.exists():
            payload["background_image"] = "background.png"
        else:
            payload["background_image"] = None

        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("document.json", json.dumps(payload, ensure_ascii=False, indent=2))
            if background_path and background_path.exists():
                archive.write(background_path, arcname="background.png")

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

            if "background.png" in archive.namelist():
                extract_dir = Path(tempfile.mkdtemp(prefix="sgape_in_text_"))
                archive.extract("background.png", extract_dir)
                data["background_image"] = str(extract_dir / "background.png")

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
