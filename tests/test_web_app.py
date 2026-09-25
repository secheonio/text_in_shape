from src.sgape_in_text.web_app import create_app


def test_web_app_index_page_returns_200():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"shape" in response.data.lower()


def test_web_app_includes_trim_tool_button():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert "트림".encode("utf-8") in response.data


def test_web_app_includes_trim_cut_geometry_logic():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"clipPolygonByCut" in response.data
    assert b"isTrimIntersectionBoundedSegment" in response.data


def test_web_app_includes_trim_hover_highlight_logic():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"trimHoverTarget" in response.data


def test_web_app_includes_shape_color_controls_and_open_shape_fill_logic():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"strokeColor" in response.data
    assert b"fillColor" in response.data
    assert b"shape.closed" in response.data
    assert b"transparent" in response.data


def test_web_app_includes_default_drawing_color_state():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"defaultStrokeColor" in response.data
    assert b"defaultFillColor" in response.data


def test_web_app_includes_precise_eyedropper_sampling_with_magnifier():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"eyedropperMagnifier" in response.data
    assert b"sampleCanvasColorFromPoint" in response.data
    assert b"currentEyedropperKind" in response.data


def test_web_app_new_shapes_default_to_no_fill_until_closed_shape_is_filled():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"shape.fill = 'transparent'" in response.data
    assert b"typeof shape.fill === 'undefined' || shape.fill === null || shape.fill === ''" in response.data


def test_web_app_trim_uses_neighbor_intersections_only():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"MAX_TRIM_NEIGHBOR_DISTANCE" in response.data
    assert b"MAX_TRIM_NEIGHBOR_SEGMENT_GAP" in response.data


def test_web_app_uses_ctrl_t_to_toggle_trim_tool():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"event.ctrlKey && event.key && event.key.toLowerCase() === 't'" in response.data
    assert b"toggleTrimTool()" in response.data
