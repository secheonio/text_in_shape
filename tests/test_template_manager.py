import json
import zipfile
from pathlib import Path

from src.sgape_in_text.models import Paper, ShapeItem, TemplateDocument
from src.sgape_in_text.template_manager import TemplateManager


def test_template_save_and_load(tmp_path: Path):
    document = TemplateDocument(
        paper=Paper(width=2100, height=2970, name="A4"),
        shapes=[
            ShapeItem(
                id="shape_1",
                type="rectangle",
                x=100,
                y=150,
                width=500,
                height=200,
                text="Hello",
            )
        ],
    )

    path = tmp_path / "demo.sit"
    TemplateManager.save_template(document, path)

    assert path.exists()
    with zipfile.ZipFile(path, "r") as archive:
        payload = json.loads(archive.read("document.json").decode("utf-8"))
        assert payload["paper"]["name"] == "A4"
        assert payload["shapes"][0]["text"] == "Hello"

    loaded = TemplateManager.load_template(path)
    assert loaded.paper.name == "A4"
    assert loaded.shapes[0].text == "Hello"


def test_document_json_round_trip():
    document = TemplateDocument(
        paper=Paper(width=1000, height=1000, name="Square"),
        shapes=[
            ShapeItem(
                id="shape_2",
                type="circle",
                x=20,
                y=20,
                width=200,
                height=200,
                text="Sample",
            )
        ],
    )
    payload = document.to_dict()
    restored = TemplateDocument.from_dict(payload)
    assert restored.shapes[0].type == "circle"
    assert restored.shapes[0].text == "Sample"
