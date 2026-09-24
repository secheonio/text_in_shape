from src.sgape_in_text.web_app import create_app


def test_web_app_index_page_returns_200():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"shape" in response.data.lower()
