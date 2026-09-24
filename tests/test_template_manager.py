import json
import zipfile
from pathlib import Path

from PIL import Image

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


def test_template_background_image_round_trip(tmp_path: Path):
    background = tmp_path / "background.png"
    Image.new("RGB", (100, 100), color="blue").save(background)

    document = TemplateDocument(
        paper=Paper(width=2100, height=2970, name="A4"),
        shapes=[],
        background_image=str(background),
    )

    template_path = tmp_path / "with_background.sit"
    TemplateManager.save_template(document, template_path)

    with zipfile.ZipFile(template_path, "r") as archive:
        assert "background.png" in archive.namelist()

    loaded = TemplateManager.load_template(template_path)
    assert loaded.background_image is not None
    assert Path(loaded.background_image).exists()


def test_shape_move_by_updates_position():
    shape = ShapeItem(
        id="shape_drag",
        type="rectangle",
        x=10,
        y=20,
        width=100,
        height=80,
    )

    shape.move_by(25, -5)

    assert shape.x == 35
    assert shape.y == 15


def test_shape_resize_by_updates_dimensions():
    shape = ShapeItem(
        id="shape_resize",
        type="rectangle",
        x=10,
        y=20,
        width=100,
        height=80,
    )

    shape.resize_by(30, 20)

    assert shape.width == 130
    assert shape.height == 100
