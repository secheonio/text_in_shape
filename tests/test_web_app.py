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
    assert b"\xe2\x9c\x82" in response.data or b"\xed\x8a\xb8\xed\x8b\xb4" in response.data
    assert b"data-tool=\"trim\"" in response.data


def test_web_app_uses_cad_shape_toolbar_for_line_circle_arc_polygon_freeform():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"shape-mode-button" in response.data
    assert b"data-shape-kind=\"line\"" in response.data
    assert b"data-shape-kind=\"circle\"" in response.data
    assert b"data-shape-kind=\"arc\"" in response.data
    assert b"data-shape-kind=\"polygon\"" in response.data
    assert b"data-shape-kind=\"freeform\"" in response.data
    assert b"data-shape-kind=\"polyline\"" not in response.data
    assert b"shape-side-btn" not in response.data


def test_web_app_uses_projected_trim_edge_logic():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"nearestPointOnSegment" in response.data
    assert b"pointOnSegment" in response.data


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


def test_web_app_includes_object_select_click_logic():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"selectObjectAtPoint" in response.data
    assert b"getObjectSelectTarget" in response.data
    assert b"isPointInShape" in response.data
    assert b"event.shiftKey" in response.data


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


def test_web_app_uses_node_based_trim_boundaries():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"getTrimNodeCandidates" in response.data
    assert b"resolveTrimCutBoundary" in response.data


def test_web_app_includes_rotation_handle_logic_for_selected_shapes():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"rotation" in response.data.lower()
    assert b"getSelectionHandles" in response.data
    assert b"mode: 'rotate'" in response.data


def test_web_app_commits_rotation_from_input_on_enter_and_ignores_global_delete_keys_in_fields():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"rotationDegreesInput.addEventListener('keydown'" in response.data
    assert b"rotationDegreesInput.addEventListener('focus'" in response.data
    assert b"event.target.id === 'rotationDegrees'" in response.data
    assert b"target.matches('input, textarea, select')" in response.data


def test_web_app_uses_grouped_selection_bounds_for_multi_resize_and_rotate():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"getSelectionBounds" in response.data
    assert b"getSelectionHandlesForSelection" in response.data
    assert b"dragState.shapeIds" in response.data


def test_web_app_uses_cad_style_shape_modes_only():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"data-shape-kind=\"line\"" in response.data
    assert b"data-shape-kind=\"circle\"" in response.data
    assert b"data-shape-kind=\"arc\"" in response.data
    assert b"data-shape-kind=\"polygon\"" in response.data
    assert b"data-shape-kind=\"freeform\"" in response.data
    assert b"data-shape-kind=\"polyline\"" not in response.data


def test_web_app_uses_centered_paper_metrics_and_float_window_defaults():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"getPaperCenter" in response.data
    assert b"applyPropertyWindowDefaults" in response.data
    assert b"aria-expanded" in response.data


def test_web_app_keeps_selected_paper_label_when_swapping_orientation():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"currentPaper && currentPaper.label && currentPaper.label !== 'Custom'" in response.data
    assert b"paperSelect.value = selectedPaperName;" in response.data
    assert b"label: selectedPaperName" in response.data


def test_web_app_includes_trim_cut_keep_and_reconstruction_logic():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"collectTrimTargetCandidates" in response.data
    assert b"classifyTrimSide" in response.data
    assert b"reconstructTrimmedShape" in response.data
