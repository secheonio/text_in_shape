from __future__ import annotations

from flask import Flask, render_template_string


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template_string("""
        <!doctype html>
        <html lang="ko">
        <head>
            <meta charset="utf-8">
            <title>Text in Shape</title>
            <style>
                :root {
                    --paper-bg: #fff;
                    --ink: #1a1a1a;
                    --panel: #f5f5f5;
                    --primary: #2563eb;
                    --line: #d0d0d0;
                }
                * { box-sizing: border-box; }
                body {
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: #ececec;
                    color: var(--ink);
                    overflow: hidden;
                }
                .toolbar {
                    position: sticky;
                    top: 0;
                    z-index: 20;
                    display: flex;
                    gap: 10px;
                    flex-wrap: wrap;
                    padding: 12px 16px;
                    background: #dfe3e8;
                    border-bottom: 1px solid var(--line);
                    align-items: center;
                }
                .toolbar button,
                .toolbar select,
                .toolbar input {
                    border: 1px solid #b8c0cc;
                    background: white;
                    padding: 8px 14px;
                    border-radius: 6px;
                    cursor: pointer;
                    font-size: 14px;
                    transition: all 0.15s ease;
                }
                .toolbar button.tool-btn {
                    font-weight: 600;
                    background: white;
                }
                .toolbar button.tool-shape { background: #e0f2fe; border-color: #7dd3fc; }
                .toolbar button.tool-text { background: #fef3c7; border-color: #fbbf24; }
                .toolbar button.tool-save { background: #ede9fe; border-color: #a78bfa; }
                .toolbar button.tool-load { background: #fee2e2; border-color: #f87171; }
                .toolbar button.tool-apply { background: #dbeafe; border-color: #60a5fa; }
                .toolbar button.is-active {
                    outline: 2px solid rgba(37, 99, 235, 0.75);
                    outline-offset: 1px;
                    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.12), 0 4px 10px rgba(37, 99, 235, 0.18);
                    transform: translateY(-1px);
                    filter: brightness(1.04);
                }
                .toolbar button.tool-shape.is-active { background: #bae6fd; border-color: #0284c7; }
                .toolbar button.tool-text.is-active { background: #fde68a; border-color: #d97706; }
                .toolbar button.tool-save.is-active { background: #ddd6fe; border-color: #7c3aed; }
                .toolbar button.tool-load.is-active { background: #fecaca; border-color: #dc2626; }
                .toolbar button.tool-apply.is-active { background: #bfdbfe; border-color: #2563eb; }
                .toolbar button:hover { filter: brightness(0.98); }
                .workspace {
                    display: flex;
                    gap: 16px;
                    padding: 16px;
                    height: calc(100vh - 72px);
                    overflow: hidden;
                }
                .canvas-panel {
                    flex: 1;
                    background: #ececec;
                    border: none;
                    border-radius: 10px;
                    min-height: 720px;
                    position: relative;
                    overflow: hidden;
                }
                .canvas {
                    width: 100%;
                    height: 100%;
                    min-height: 720px;
                    display: block;
                    background: transparent;
                    border: none;
                    border-radius: 10px;
                }
                .sidebar {
                    width: 300px;
                    background: var(--panel);
                    border: 1px solid var(--line);
                    border-radius: 10px;
                    padding: 16px;
                }
                .sidebar h3 {
                    margin: 0 0 12px 0;
                    font-size: 18px;
                }
                .field {
                    margin-bottom: 12px;
                }
                label {
                    display: block;
                    margin-bottom: 6px;
                    font-weight: 600;
                }
                input, textarea {
                    width: 100%;
                    padding: 8px 10px;
                    border: 1px solid #c7c7c7;
                    border-radius: 6px;
                    font-size: 14px;
                }
                textarea {
                    min-height: 120px;
                    resize: vertical;
                }
            </style>
        </head>
        <body>
            <div class="toolbar">
                <label for="paperSelect" style="font-weight:600;">용지 선택</label>
                <select id="paperSelect">
                    <option value="A4">A4</option>
                    <option value="A5">A5</option>
                    <option value="Letter">Letter</option>
                    <option value="BusinessCard">명함</option>
                    <option value="Custom">사용자 지정</option>
                </select>
                <div style="display:flex; gap:6px; align-items:center; flex-wrap:wrap;">
                    <input id="customPaperWidth" type="number" min="50" value="210" step="1" placeholder="가로(mm)" style="width:90px;" />
                    <span>x</span>
                    <input id="customPaperHeight" type="number" min="50" value="297" step="1" placeholder="세로(mm)" style="width:90px;" />
                    <button type="button" id="swapPaperOrientation" class="tool-btn tool-apply" title="가로/세로 전환">↔</button>
                </div>
                <button type="button" class="tool-btn tool-shape" data-tool="circle">원</button>
                <button type="button" class="tool-btn tool-shape" data-tool="freeform">자유형</button>
                <select id="polygonSides" title="다각형 변의 수" style="min-width:110px;">
                    <option value="3">3각</option>
                    <option value="4" selected>4각</option>
                    <option value="4-diamond">마름모</option>
                    <option value="5">5각</option>
                    <option value="6">6각</option>
                    <option value="7">7각</option>
                    <option value="8">8각</option>
                    <option value="9">9각</option>
                    <option value="10">10각</option>
                    <option value="11">11각</option>
                    <option value="12">12각</option>
                    <option value="13">13각</option>
                    <option value="14">14각</option>
                    <option value="15">15각</option>
                    <option value="16">16각</option>
                    <option value="17">17각</option>
                    <option value="18">18각</option>
                    <option value="19">19각</option>
                    <option value="20">20각</option>
                    <option value="21">21각</option>
                    <option value="22">22각</option>
                    <option value="23">23각</option>
                    <option value="24">24각</option>
                </select>
                <button type="button" class="tool-btn tool-text" data-tool="text">텍스트 입력</button>
                <button type="button" class="tool-btn tool-save" data-tool="save">저장 (.sit)</button>
                <button type="button" class="tool-btn tool-load" data-tool="load">불러오기 (.sit)</button>
            </div>

            <div class="workspace">
                <div class="canvas-panel">
                    <canvas id="editorCanvas" class="canvas" width="1000" height="700"></canvas>
                </div>

                <aside class="sidebar">
                    <h3>도형 속성</h3>
                    <div class="field">
                        <label>선택된 도형</label>
                        <div id="selectedShape">없음</div>
                    </div>
                    <div class="field">
                        <label>텍스트</label>
                        <textarea id="shapeText">text in shape</textarea>
                    </div>
                    <div class="field">
                        <label>폰트 크기</label>
                        <input id="fontSize" type="number" value="40" min="8" max="200" />
                    </div>
                    <button type="button" id="applySettings">설정 적용</button>
                </aside>
            </div>

            <script>
                const canvas = document.getElementById('editorCanvas');
                const paperSelect = document.getElementById('paperSelect');
                const customPaperWidthInput = document.getElementById('customPaperWidth');
                const customPaperHeightInput = document.getElementById('customPaperHeight');
                const ctx = canvas.getContext('2d');

                const PAPER_MM = {
                    A4: { width: 210, height: 297, label: 'A4' },
                    A5: { width: 148, height: 210, label: 'A5' },
                    Letter: { width: 216, height: 279, label: 'Letter' },
                    BusinessCard: { width: 92, height: 52, label: '명함' },
                };

                const paperSizes = {
                    A4: { width: 2100, height: 2970, label: 'A4' },
                    A5: { width: 1480, height: 2100, label: 'A5' },
                    Letter: { width: 2159, height: 2794, label: 'Letter' },
                    BusinessCard: { width: 920, height: 520, label: '명함' },
                };

                const STORAGE_KEY = 'shape_in_text_editor_state_v1';
                let currentPaper = { ...paperSizes.A4 };
                const shapes = [
                    { id: 'shape_1', type: 'polygon', x: 120, y: 140, width: 260, height: 180, sides: 6, text: 'shape in text', fill: '#ffffff', stroke: '#222222' }
                ];
                let selectedShapeId = 'shape_1';
                let currentTool = null;
                let freeDrawingPoints = [];
                let isDrawingFreeform = false;
                let hoverHandleName = null;
                let dragState = null;
                let activeDraftShape = null;
                let paperDragState = null;
                const polygonSidesSelect = document.getElementById('polygonSides');
                let polygonSides = Number(polygonSidesSelect.value) || 6;

                const PAPER_MARGIN_MM = 3;
                const PAPER_MARGIN_PIXELS = PAPER_MARGIN_MM * 10;
                const PAN_SPEED = 1.0;
                let paperZoom = 1;
                let paperPan = { x: 0, y: 0 };
                let isLandscapeMode = true;

                function normalizePaperSize(value) {
                    const num = Number(value);
                    return Number.isFinite(num) && num > 0 ? num : 2100;
                }

                function clampZoom(value) {
                    const num = Number(value);
                    if (!Number.isFinite(num) || num <= 0) return 1;
                    return Math.min(20, Math.max(0.2, num));
                }

                function normalizePaperState() {
                    if (!currentPaper || !Number.isFinite(Number(currentPaper.width)) || !Number.isFinite(Number(currentPaper.height))) {
                        currentPaper = { ...paperSizes.A4 };
                    }
                    currentPaper.width = normalizePaperSize(currentPaper.width);
                    currentPaper.height = normalizePaperSize(currentPaper.height);
                    paperZoom = clampZoom(paperZoom);
                    if (!paperPan || !Number.isFinite(Number(paperPan.x)) || !Number.isFinite(Number(paperPan.y))) {
                        paperPan = { x: 0, y: 0 };
                    }
                    paperPan.x = Math.min(5000, Math.max(-5000, Number(paperPan.x) || 0));
                    paperPan.y = Math.min(5000, Math.max(-5000, Number(paperPan.y) || 0));
                }

                function normalizeShapeForStorage(shape) {
                    if (!shape || typeof shape !== 'object') return null;
                    const normalized = { ...shape };
                    const x = Number(shape.x);
                    const y = Number(shape.y);
                    const width = Number(shape.width);
                    const height = Number(shape.height);
                    if (!Number.isFinite(x) || !Number.isFinite(y) || !Number.isFinite(width) || !Number.isFinite(height)) {
                        return null;
                    }
                    normalized.x = Math.min(Math.max(x, -200000), 200000);
                    normalized.y = Math.min(Math.max(y, -200000), 200000);
                    normalized.width = Math.min(Math.max(Math.abs(width), 4), Math.max(4000, currentPaper.width * 2));
                    normalized.height = Math.min(Math.max(Math.abs(height), 4), Math.max(4000, currentPaper.height * 2));
                    return normalized;
                }

                function saveEditorState() {
                    normalizePaperState();
                    const state = {
                        currentPaper,
                        shapes: shapes.map(shape => normalizeShapeForStorage(shape)).filter(Boolean),
                        selectedShapeId,
                        paperZoom,
                        paperPan,
                        polygonSides,
                        paperSelectValue: paperSelect.value
                    };
                    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
                }

                function loadEditorState() {
                    try {
                        const raw = localStorage.getItem(STORAGE_KEY);
                        if (!raw) return false;
                        const state = JSON.parse(raw);
                        if (!state || !Array.isArray(state.shapes)) return false;

                        currentPaper = state.currentPaper || { ...paperSizes.A4 };
                        normalizePaperState();
                        shapes.splice(0, shapes.length, ...state.shapes
                            .map(shape => normalizeShapeForStorage(shape))
                            .filter(Boolean));
                        selectedShapeId = state.selectedShapeId && shapes.some(shape => shape.id === state.selectedShapeId)
                            ? state.selectedShapeId
                            : null;
                        paperZoom = clampZoom(state.paperZoom);
                        paperPan = {
                            x: Number(state.paperPan && Number.isFinite(Number(state.paperPan.x)) ? state.paperPan.x : 0),
                            y: Number(state.paperPan && Number.isFinite(Number(state.paperPan.y)) ? state.paperPan.y : 0)
                        };
                        normalizePaperState();
                        polygonSides = Number(state.polygonSides) || 6;
                        polygonSidesSelect.value = String(polygonSides);
                        if (state.paperSelectValue) {
                            paperSelect.value = state.paperSelectValue;
                        }
                        if (paperSelect.value === 'Custom') {
                            customPaperWidthInput.value = currentPaper.width / 10;
                            customPaperHeightInput.value = currentPaper.height / 10;
                        } else {
                            customPaperWidthInput.value = currentPaper.width / 10;
                            customPaperHeightInput.value = currentPaper.height / 10;
                        }
                        clampPaperPan();
                        return true;
                    } catch (error) {
                        currentPaper = { ...paperSizes.A4 };
                        paperPan = { x: 0, y: 0 };
                        paperZoom = 1;
                        shapes.splice(0, shapes.length, { id: 'shape_1', type: 'polygon', x: 120, y: 140, width: 260, height: 180, sides: 6, text: 'shape in text', fill: '#ffffff', stroke: '#222222' });
                        selectedShapeId = 'shape_1';
                        return false;
                    }
                }

                window.addEventListener('beforeunload', saveEditorState);
                window.addEventListener('pagehide', saveEditorState);
                document.addEventListener('visibilitychange', () => {
                    if (document.visibilityState === 'hidden') {
                        saveEditorState();
                    }
                });

                function updateOrientationButton() {
                    const orientationButton = document.getElementById('swapPaperOrientation');
                    if (!orientationButton) return;
                    orientationButton.textContent = isLandscapeMode ? '↔' : '↕';
                    orientationButton.title = isLandscapeMode ? '현재 가로 모드, 클릭하면 세로로 전환' : '현재 세로 모드, 클릭하면 가로로 전환';
                }

                function resizeCanvasToPaper() {
                    const totalWidth = currentPaper.width + PAPER_MARGIN_PIXELS * 2;
                    const totalHeight = currentPaper.height + PAPER_MARGIN_PIXELS * 2;
                    canvas.width = totalWidth;
                    canvas.height = totalHeight;
                    canvas.style.width = '100%';
                    canvas.style.height = 'auto';
                    canvas.style.maxHeight = '75vh';
                    canvas.style.objectFit = 'contain';
                }

                function drawShape(shape) {
                    ctx.strokeStyle = shape.stroke;
                    ctx.fillStyle = shape.fill;
                    ctx.lineWidth = selectedShapeId === shape.id ? 4 : 2;

                    if (shape.type === 'freeform') {
                        if (shape.points && shape.points.length > 1) {
                            ctx.beginPath();
                            ctx.moveTo(shape.points[0].x, shape.points[0].y);
                            for (let i = 1; i < shape.points.length; i++) {
                                ctx.lineTo(shape.points[i].x, shape.points[i].y);
                            }
                            ctx.stroke();
                        }
                        return;
                    }

                    if (shape.type === 'polygon' || shape.type === 'diamond') {
                        const cx = shape.x + shape.width / 2;
                        const cy = shape.y + shape.height / 2;
                        const radiusX = shape.width / 2;
                        const radiusY = shape.height / 2;
                        const sides = Number(shape.sides) || polygonSides || 6;
                        const effectiveSides = shape.type === 'diamond' ? 4 : sides;
                        const startAngle = shape.type === 'diamond' ? -Math.PI / 2 : (effectiveSides === 4 ? -Math.PI / 4 : -Math.PI / 2);
                        ctx.beginPath();
                        for (let i = 0; i < effectiveSides; i++) {
                            const angle = (Math.PI * 2 / effectiveSides) * i + startAngle;
                            const px = cx + Math.cos(angle) * radiusX;
                            const py = cy + Math.sin(angle) * radiusY;
                            if (i === 0) {
                                ctx.moveTo(px, py);
                            } else {
                                ctx.lineTo(px, py);
                            }
                        }
                        ctx.closePath();
                        ctx.fill();
                        ctx.stroke();
                    } else if (shape.type === 'circle' || shape.type === 'ellipse') {
                        const centerX = shape.x + shape.width / 2;
                        const centerY = shape.y + shape.height / 2;
                        ctx.beginPath();
                        ctx.ellipse(centerX, centerY, Math.max(shape.width / 2, 1), Math.max(shape.height / 2, 1), 0, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.stroke();
                    }

                    if (selectedShapeId === shape.id) {
                        const handles = getResizeHandles(shape);
                        const activeHandleName = dragState && dragState.mode === 'resize' && dragState.shapeId === shape.id ? dragState.handle : null;
                        handles.forEach(handle => {
                            const isHovered = handle.name === hoverHandleName && !activeHandleName;
                            const isActive = handle.name === activeHandleName;
                            const visualSize = isHovered ? handle.size + 8 : isActive ? handle.size + 4 : handle.size;
                            const halfSize = visualSize / 2;
                            const fillColor = isActive ? '#0f3dbe' : isHovered ? '#dbeafe' : '#ffffff';
                            const strokeColor = isActive ? '#081f63' : '#1f6feb';
                            ctx.fillStyle = fillColor;
                            ctx.strokeStyle = strokeColor;
                            ctx.lineWidth = isActive ? 2.5 : 2;
                            ctx.fillRect(handle.x - halfSize, handle.y - halfSize, visualSize, visualSize);
                            ctx.strokeRect(handle.x - halfSize, handle.y - halfSize, visualSize, visualSize);
                        });
                    }

                    if (shape.text) {
                        ctx.fillStyle = '#111111';
                        ctx.font = '40px Arial';
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';
                        ctx.fillText(shape.text, shape.x + shape.width / 2, shape.y + shape.height / 2, shape.width - 40);
                    }
                }

                function clampZoom(value) {
                    return Number.isFinite(value) && value > 0 ? value : 0.05;
                }

                function getPaperFrame() {
                    const width = currentPaper.width * paperZoom;
                    const height = currentPaper.height * paperZoom;
                    return {
                        x: PAPER_MARGIN_PIXELS + paperPan.x,
                        y: PAPER_MARGIN_PIXELS + paperPan.y,
                        width,
                        height
                    };
                }

                function clampPaperPan() {
                    if (!Number.isFinite(paperPan.x)) {
                        paperPan.x = 0;
                    }
                    if (!Number.isFinite(paperPan.y)) {
                        paperPan.y = 0;
                    }
                }

                function getCanvasPoint(event) {
                    const rect = canvas.getBoundingClientRect();
                    const x = (event.clientX - rect.left) * (canvas.width / rect.width);
                    const y = (event.clientY - rect.top) * (canvas.height / rect.height);
                    const frame = getPaperFrame();
                    return {
                        x: (x - frame.x) / paperZoom,
                        y: (y - frame.y) / paperZoom
                    };
                }

                function clampCircleDraft(centerX, centerY, radiusX, radiusY) {
                    const maxRadiusX = Math.max(0, Math.min(centerX, currentPaper.width - centerX));
                    const maxRadiusY = Math.max(0, Math.min(centerY, currentPaper.height - centerY));
                    const safeRadiusX = Math.min(Math.abs(radiusX), maxRadiusX || 1);
                    const safeRadiusY = Math.min(Math.abs(radiusY), maxRadiusY || 1);
                    return {
                        x: centerX - safeRadiusX,
                        y: centerY - safeRadiusY,
                        width: safeRadiusX * 2,
                        height: safeRadiusY * 2,
                        centerX,
                        centerY
                    };
                }

                function buildRegularPolygonDraft(centerX, centerY, radius, sides, shapeType) {
                    const safeRadius = Math.max(8, Math.min(radius, Math.max(1, currentPaper.width), Math.max(1, currentPaper.height)));
                    const x = centerX - safeRadius;
                    const y = centerY - safeRadius;
                    return {
                        id: `shape_${Date.now()}`,
                        type: shapeType === 'diamond' ? 'diamond' : 'polygon',
                        x,
                        y,
                        width: safeRadius * 2,
                        height: safeRadius * 2,
                        sides,
                        shapeType,
                        centerX,
                        centerY,
                        radius: safeRadius,
                        text: '',
                        fill: '#ffffff',
                        stroke: '#222222'
                    };
                }

                function getShapeAtPoint(point) {
                    for (const shape of [...shapes].reverse()) {
                        if (shape.type === 'freeform' && shape.points) continue;
                        if (
                            point.x >= shape.x &&
                            point.x <= shape.x + shape.width &&
                            point.y >= shape.y &&
                            point.y <= shape.y + shape.height
                        ) {
                            return shape;
                        }
                    }
                    return null;
                }

                function getShapeVertices(shape) {
                    if (shape.type === 'polygon' || shape.type === 'diamond') {
                        const cx = shape.x + shape.width / 2;
                        const cy = shape.y + shape.height / 2;
                        const radiusX = shape.width / 2;
                        const radiusY = shape.height / 2;
                        const sides = Number(shape.sides) || 6;
                        const effectiveSides = shape.type === 'diamond' ? 4 : sides;
                        const startAngle = shape.type === 'diamond' ? -Math.PI / 2 : (effectiveSides === 4 ? -Math.PI / 4 : -Math.PI / 2);
                        return Array.from({ length: effectiveSides }, (_, index) => {
                            const angle = (Math.PI * 2 / effectiveSides) * index + startAngle;
                            return {
                                x: cx + Math.cos(angle) * radiusX,
                                y: cy + Math.sin(angle) * radiusY
                            };
                        });
                    }

                    if (shape.type === 'circle' || shape.type === 'ellipse') {
                        const cx = shape.x + shape.width / 2;
                        const cy = shape.y + shape.height / 2;
                        const rx = Math.max(shape.width / 2, 1);
                        const ry = Math.max(shape.height / 2, 1);
                        return Array.from({ length: 48 }, (_, index) => {
                            const angle = (Math.PI * 2 / 48) * index;
                            return {
                                x: cx + Math.cos(angle) * rx,
                                y: cy + Math.sin(angle) * ry
                            };
                        });
                    }

                    if (shape.type === 'freeform' && Array.isArray(shape.points)) {
                        return shape.points.map(point => ({ x: point.x, y: point.y }));
                    }

                    return [
                        { x: shape.x, y: shape.y },
                        { x: shape.x + shape.width, y: shape.y },
                        { x: shape.x + shape.width, y: shape.y + shape.height },
                        { x: shape.x, y: shape.y + shape.height }
                    ];
                }

                function pointToSegmentDistance(point, a, b) {
                    const dx = b.x - a.x;
                    const dy = b.y - a.y;
                    if (dx === 0 && dy === 0) {
                        return Math.hypot(point.x - a.x, point.y - a.y);
                    }
                    const t = Math.max(0, Math.min(1, ((point.x - a.x) * dx + (point.y - a.y) * dy) / (dx * dx + dy * dy)));
                    const cx = a.x + t * dx;
                    const cy = a.y + t * dy;
                    return Math.hypot(point.x - cx, point.y - cy);
                }

                function getShapeBorderHit(shape, point) {
                    if (!shape) return false;

                    if (shape.type === 'freeform' && Array.isArray(shape.points) && shape.points.length > 1) {
                        for (let i = 1; i < shape.points.length; i++) {
                            if (pointToSegmentDistance(point, shape.points[i - 1], shape.points[i]) <= 8) {
                                return true;
                            }
                        }
                        return false;
                    }

                    if (shape.type === 'circle' || shape.type === 'ellipse') {
                        const cx = shape.x + shape.width / 2;
                        const cy = shape.y + shape.height / 2;
                        const rx = Math.max(shape.width / 2, 1);
                        const ry = Math.max(shape.height / 2, 1);
                        const dx = point.x - cx;
                        const dy = point.y - cy;
                        const normalized = (dx * dx) / (rx * rx) + (dy * dy) / (ry * ry);
                        return Math.abs(normalized - 1) <= 0.16;
                    }

                    const vertices = getShapeVertices(shape);
                    for (let i = 0; i < vertices.length; i++) {
                        const start = vertices[i];
                        const end = vertices[(i + 1) % vertices.length];
                        if (pointToSegmentDistance(point, start, end) <= 8) {
                            return true;
                        }
                    }
                    return false;
                }

                function getResizeHandles(shape) {
                    const handleSize = 12;
                    const hitRadius = 18;
                    return [
                        { name: 'nw', x: shape.x, y: shape.y },
                        { name: 'n', x: shape.x + shape.width / 2, y: shape.y },
                        { name: 'ne', x: shape.x + shape.width, y: shape.y },
                        { name: 'w', x: shape.x, y: shape.y + shape.height / 2 },
                        { name: 'e', x: shape.x + shape.width, y: shape.y + shape.height / 2 },
                        { name: 'sw', x: shape.x, y: shape.y + shape.height },
                        { name: 's', x: shape.x + shape.width / 2, y: shape.y + shape.height },
                        { name: 'se', x: shape.x + shape.width, y: shape.y + shape.height }
                    ].map(point => ({ ...point, size: handleSize, hitRadius }));
                }

                function isResizeHandleHit(shape, point) {
                    const handles = getResizeHandles(shape);
                    const hit = handles.find(handle =>
                        Math.abs(point.x - handle.x) <= handle.hitRadius &&
                        Math.abs(point.y - handle.y) <= handle.hitRadius
                    );
                    return hit ? hit.name : null;
                }

                function resizeShapeFromHandle(shape, handleName, dx, dy) {
                    const minSize = 30;
                    const original = { x: shape.x, y: shape.y, width: shape.width, height: shape.height };
                    const next = { x: original.x, y: original.y, width: original.width, height: original.height };

                    switch (handleName) {
                        case 'nw':
                            next.x = Math.min(original.x + dx, original.x + original.width - minSize);
                            next.y = Math.min(original.y + dy, original.y + original.height - minSize);
                            next.width = original.x + original.width - next.x;
                            next.height = original.y + original.height - next.y;
                            break;
                        case 'n':
                            next.y = Math.min(original.y + dy, original.y + original.height - minSize);
                            next.height = original.y + original.height - next.y;
                            break;
                        case 'ne':
                            next.y = Math.min(original.y + dy, original.y + original.height - minSize);
                            next.width = Math.max(minSize, original.width + dx);
                            next.height = original.y + original.height - next.y;
                            break;
                        case 'w':
                            next.x = Math.min(original.x + dx, original.x + original.width - minSize);
                            next.width = original.x + original.width - next.x;
                            break;
                        case 'e':
                            next.width = Math.max(minSize, original.width + dx);
                            break;
                        case 'sw':
                            next.x = Math.min(original.x + dx, original.x + original.width - minSize);
                            next.width = original.x + original.width - next.x;
                            next.height = Math.max(minSize, original.height + dy);
                            break;
                        case 's':
                            next.height = Math.max(minSize, original.height + dy);
                            break;
                        case 'se':
                            next.width = Math.max(minSize, original.width + dx);
                            next.height = Math.max(minSize, original.height + dy);
                            break;
                        default:
                            return original;
                    }

                    return next;
                }

                function applySnapToShape(shapeId, x, y, width, height) {
                    const SNAP_SIZE = 10;
                    const SNAP_DISTANCE = 12;
                    const snappedX = Math.round(x / SNAP_SIZE) * SNAP_SIZE;
                    const snappedY = Math.round(y / SNAP_SIZE) * SNAP_SIZE;

                    let finalX = snappedX;
                    let finalY = snappedY;

                    for (const other of shapes) {
                        if (other.id === shapeId) continue;
                        const candidateXs = [other.x, other.x + other.width];
                        const candidateYs = [other.y, other.y + other.height];

                        for (const candidateX of candidateXs) {
                            if (Math.abs(x - candidateX) <= SNAP_DISTANCE) finalX = candidateX;
                            if (Math.abs((x + width) - candidateX) <= SNAP_DISTANCE) finalX = candidateX - width;
                        }

                        for (const candidateY of candidateYs) {
                            if (Math.abs(y - candidateY) <= SNAP_DISTANCE) finalY = candidateY;
                            if (Math.abs((y + height) - candidateY) <= SNAP_DISTANCE) finalY = candidateY - height;
                        }
                    }

                    return { x: finalX, y: finalY };
                }

                function drawPaper() {
                    normalizePaperState();
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    ctx.fillStyle = '#ececec';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);

                    const frame = getPaperFrame();
                    const paperX = Number.isFinite(frame.x) ? frame.x : 0;
                    const paperY = Number.isFinite(frame.y) ? frame.y : 0;
                    const paperWidth = Number.isFinite(frame.width) && frame.width > 0 ? frame.width : Math.max(1, currentPaper.width * paperZoom);
                    const paperHeight = Number.isFinite(frame.height) && frame.height > 0 ? frame.height : Math.max(1, currentPaper.height * paperZoom);

                    ctx.fillStyle = '#ffffff';
                    ctx.fillRect(paperX, paperY, paperWidth, paperHeight);

                    ctx.strokeStyle = '#444';
                    ctx.lineWidth = 2;
                    ctx.strokeRect(paperX, paperY, paperWidth, paperHeight);

                    ctx.strokeStyle = '#444';
                    ctx.lineWidth = 2;
                    ctx.strokeRect(paperX, paperY, paperWidth, paperHeight);

                    for (const shape of shapes) {
                        const adjustedShape = { ...shape };
                        if (adjustedShape.type !== 'freeform' && typeof adjustedShape.x === 'number') {
                            adjustedShape.x = shape.x * paperZoom + paperX;
                            adjustedShape.y = shape.y * paperZoom + paperY;
                            adjustedShape.width = shape.width * paperZoom;
                            adjustedShape.height = shape.height * paperZoom;
                        }
                        if (adjustedShape.type === 'freeform' && Array.isArray(adjustedShape.points)) {
                            adjustedShape.points = adjustedShape.points.map(point => ({
                                x: point.x * paperZoom + paperX,
                                y: point.y * paperZoom + paperY
                            }));
                        }
                        drawShape(adjustedShape);
                    }

                    if (activeDraftShape) {
                        const draft = { ...activeDraftShape };
                        draft.x = activeDraftShape.x * paperZoom + paperX;
                        draft.y = activeDraftShape.y * paperZoom + paperY;
                        draft.width = activeDraftShape.width * paperZoom;
                        draft.height = activeDraftShape.height * paperZoom;
                        drawShape(draft);
                    }

                    if (isDrawingFreeform && freeDrawingPoints.length > 1) {
                        ctx.beginPath();
                        ctx.moveTo(freeDrawingPoints[0].x * paperZoom + paperX, freeDrawingPoints[0].y * paperZoom + paperY);
                        for (let i = 1; i < freeDrawingPoints.length; i++) {
                            ctx.lineTo(freeDrawingPoints[i].x * paperZoom + paperX, freeDrawingPoints[i].y * paperZoom + paperY);
                        }
                        ctx.strokeStyle = '#222';
                        ctx.lineWidth = 2;
                        ctx.stroke();
                    }
                }

                const MM_TO_PIXEL = 10;

                function mmToPixel(value) {
                    const num = Number(value);
                    if (!Number.isFinite(num) || num <= 0) return 0;
                    return Math.round(num * MM_TO_PIXEL);
                }

                function syncCustomInputsToSelectedPaper() {
                    const selected = paperSelect.value;
                    const preset = PAPER_MM[selected];
                    if (selected !== 'Custom' && preset) {
                        customPaperWidthInput.value = preset.width;
                        customPaperHeightInput.value = preset.height;
                    }
                }

                function applyPaperSelection(name) {
                    if (name === 'Custom') {
                        const widthMm = Number(customPaperWidthInput.value || 210);
                        const heightMm = Number(customPaperHeightInput.value || 297);
                        currentPaper = {
                            width: mmToPixel(widthMm),
                            height: mmToPixel(heightMm),
                            label: 'Custom'
                        };
                    } else {
                        const preset = PAPER_MM[name] || paperSizes[name];
                        currentPaper = {
                            width: preset.width * (name === 'Letter' ? 10 : 10),
                            height: preset.height * 10,
                            label: name
                        };
                        if (name === 'A4' || name === 'A5' || name === 'Letter' || name === 'BusinessCard') {
                            customPaperWidthInput.value = preset.width;
                            customPaperHeightInput.value = preset.height;
                        }
                    }
                    clampPaperPan();
                    resizeCanvasToPaper();
                    drawPaper();
                    saveEditorState();
                }

                function applyCustomPaperInputs() {
                    const widthMm = Number(customPaperWidthInput.value || 210);
                    const heightMm = Number(customPaperHeightInput.value || 297);
                    isLandscapeMode = widthMm >= heightMm;
                    paperSelect.value = 'Custom';
                    currentPaper = {
                        width: mmToPixel(widthMm),
                        height: mmToPixel(heightMm),
                        label: 'Custom'
                    };
                    clampPaperPan();
                    resizeCanvasToPaper();
                    drawPaper();
                    updateOrientationButton();
                    saveEditorState();
                }

                document.getElementById('swapPaperOrientation').addEventListener('click', () => {
                    const currentWidth = Number(customPaperWidthInput.value || 210);
                    const currentHeight = Number(customPaperHeightInput.value || 297);
                    customPaperWidthInput.value = currentHeight;
                    customPaperHeightInput.value = currentWidth;
                    isLandscapeMode = currentHeight >= currentWidth;
                    applyCustomPaperInputs();
                });

                customPaperWidthInput.addEventListener('input', () => {
                    if (paperSelect.value === 'Custom') {
                        applyCustomPaperInputs();
                    }
                });

                customPaperHeightInput.addEventListener('input', () => {
                    if (paperSelect.value === 'Custom') {
                        applyCustomPaperInputs();
                    }
                });

                updateOrientationButton();

                function setActiveToolButton(toolName) {
                    document.querySelectorAll('.tool-btn').forEach((button) => {
                        const isActive = button.dataset.tool === toolName;
                        button.classList.toggle('is-active', isActive);
                    });
                }

                function addShape(type) {
                    currentTool = type;
                    if (type === 'freeform') {
                        isDrawingFreeform = false;
                        freeDrawingPoints = [];
                    }
                    if (type === 'circle') {
                        activeDraftShape = null;
                    }
                    setActiveToolButton(type);
                }

                function getSelectedPolygonConfig() {
                    const value = polygonSidesSelect.value;
                    if (value === '4-diamond') {
                        return { sides: 4, shapeType: 'diamond' };
                    }
                    const sides = Number(value) || 6;
                    return { sides, shapeType: 'polygon' };
                }

                polygonSidesSelect.addEventListener('change', (event) => {
                    const config = getSelectedPolygonConfig();
                    polygonSides = config.sides;
                    currentTool = 'polygon';
                    activeDraftShape = null;
                    setActiveToolButton('polygon');
                    polygonSidesSelect.dataset.shapeType = config.shapeType;
                });

                const shapeButtons = Array.from(document.querySelectorAll('.tool-shape'));
                shapeButtons[0].addEventListener('click', () => addShape('circle'));
                shapeButtons[1].addEventListener('click', () => addShape('freeform'));

                document.querySelector('[data-tool="text"]').addEventListener('click', () => {
                    currentTool = 'text';
                    setActiveToolButton('text');
                });

                document.querySelector('[data-tool="save"]').addEventListener('click', () => {
                    currentTool = 'save';
                    setActiveToolButton('save');
                });

                document.querySelector('[data-tool="load"]').addEventListener('click', () => {
                    currentTool = 'load';
                    setActiveToolButton('load');
                });

                canvas.addEventListener('mousedown', (event) => {
                    const point = getCanvasPoint(event);
                    const frame = getPaperFrame();
                    const insidePaper = point.x >= 0 && point.x <= currentPaper.width && point.y >= 0 && point.y <= currentPaper.height;
                    const rect = canvas.getBoundingClientRect();
                    const canvasPoint = {
                        x: (event.clientX - rect.left) * (canvas.width / rect.width),
                        y: (event.clientY - rect.top) * (canvas.height / rect.height)
                    };
                    const onCanvasBackground = !insidePaper && canvasPoint.x >= 0 && canvasPoint.x <= canvas.width && canvasPoint.y >= 0 && canvasPoint.y <= canvas.height;

                    if (currentTool === 'freeform') {
                        isDrawingFreeform = true;
                        freeDrawingPoints = [{ x: point.x, y: point.y }];
                        drawPaper();
                        return;
                    }

                    if (currentTool === 'polygon') {
                        const config = getSelectedPolygonConfig();
                        const radius = 8;
                        activeDraftShape = buildRegularPolygonDraft(point.x, point.y, radius, polygonSides, config.shapeType);
                        drawPaper();
                        return;
                    }

                    if (currentTool === 'circle') {
                        const draftType = event.shiftKey ? 'ellipse' : 'circle';
                        activeDraftShape = {
                            id: `shape_${Date.now()}`,
                            type: draftType,
                            x: point.x,
                            y: point.y,
                            width: 0,
                            height: 0,
                            centerX: point.x,
                            centerY: point.y,
                            text: '',
                            fill: '#ffffff',
                            stroke: '#222222'
                        };
                        drawPaper();
                        return;
                    }

                    const handleName = shapes
                        .map(shape => ({ shape, handleName: isResizeHandleHit(shape, point) }))
                        .find(result => result.handleName);

                    if (handleName) {
                        const { shape, handleName: activeHandle } = handleName;
                        selectedShapeId = shape.id;
                        hoverHandleName = activeHandle;
                        dragState = {
                            mode: 'resize',
                            shapeId: shape.id,
                            handle: activeHandle,
                            startX: point.x,
                            startY: point.y,
                            original: { ...shape }
                        };
                        document.getElementById('selectedShape').textContent = shape.id;
                        drawPaper();
                        return;
                    }

                    const borderShape = [...shapes].reverse().find(shape => getShapeBorderHit(shape, point));
                    if (borderShape) {
                        selectedShapeId = borderShape.id;
                        dragState = {
                            mode: 'move',
                            shapeId: borderShape.id,
                            startX: point.x,
                            startY: point.y,
                            original: { ...borderShape }
                        };
                        document.getElementById('selectedShape').textContent = borderShape.id;
                        document.getElementById('shapeText').value = borderShape.text;
                        document.getElementById('fontSize').value = '40';
                        drawPaper();
                        return;
                    }

                    const targetShape = getShapeAtPoint(point);
                    if (targetShape) {
                        selectedShapeId = targetShape.id;
                        document.getElementById('selectedShape').textContent = targetShape.id;
                        document.getElementById('shapeText').value = targetShape.text;
                        document.getElementById('fontSize').value = '40';
                        drawPaper();
                        return;
                    }

                    if ((insidePaper || onCanvasBackground) && !currentTool) {
                        paperDragState = {
                            startX: event.clientX,
                            startY: event.clientY,
                            startPanX: paperPan.x,
                            startPanY: paperPan.y,
                            moved: false
                        };
                        selectedShapeId = null;
                        document.getElementById('selectedShape').textContent = '없음';
                        drawPaper();
                        return;
                    }

                    selectedShapeId = null;
                    document.getElementById('selectedShape').textContent = '없음';
                    drawPaper();
                });

                function updateHoverHandle(point) {
                    const shape = selectedShapeId ? shapes.find(item => item.id === selectedShapeId) : null;
                    if (!shape) {
                        if (hoverHandleName) {
                            hoverHandleName = null;
                            drawPaper();
                        }
                        return;
                    }

                    const nextHandle = isResizeHandleHit(shape, point);
                    if (nextHandle !== hoverHandleName) {
                        hoverHandleName = nextHandle;
                        drawPaper();
                    }
                }

                canvas.addEventListener('mouseleave', () => {
                    if (hoverHandleName) {
                        hoverHandleName = null;
                        drawPaper();
                    }
                });

                canvas.addEventListener('mouseout', (event) => {
                    if (event.relatedTarget && canvas.contains(event.relatedTarget)) {
                        return;
                    }
                    if (hoverHandleName) {
                        hoverHandleName = null;
                        drawPaper();
                    }
                });

                canvas.addEventListener('mousemove', (event) => {
                    const pointer = getCanvasPoint(event);

                    if (paperDragState) {
                        const dx = event.clientX - paperDragState.startX;
                        const dy = event.clientY - paperDragState.startY;
                        if (!paperDragState.moved && (Math.abs(dx) > 4 || Math.abs(dy) > 4)) {
                            paperDragState.moved = true;
                        }
                        if (!paperDragState.moved) {
                            return;
                        }
                        paperPan.x = paperDragState.startPanX + dx * PAN_SPEED;
                        paperPan.y = paperDragState.startPanY + dy * PAN_SPEED;
                        clampPaperPan();
                        drawPaper();
                        saveEditorState();
                        return;
                    }

                    if (!dragState) {
                        updateHoverHandle(pointer);
                    }

                    if (dragState) {
                        const shape = shapes.find(item => item.id === dragState.shapeId);
                        if (!shape) return;

                        const dragPoint = getCanvasPoint(event);
                        const dx = dragPoint.x - dragState.startX;
                        const dy = dragPoint.y - dragState.startY;

                        if (dragState.mode === 'move') {
                            const snapped = applySnapToShape(shape.id, dragState.original.x + dx, dragState.original.y + dy, shape.width, shape.height);
                            shape.x = snapped.x;
                            shape.y = snapped.y;
                        } else {
                            const resized = resizeShapeFromHandle(dragState.original, dragState.handle, dx, dy);
                            shape.x = resized.x;
                            shape.y = resized.y;
                            shape.width = resized.width;
                            shape.height = resized.height;
                        }

                        drawPaper();
                        saveEditorState();
                        return;
                    }

                    if (activeDraftShape && currentTool === 'circle') {
                        const centerX = activeDraftShape.centerX ?? activeDraftShape.x;
                        const centerY = activeDraftShape.centerY ?? activeDraftShape.y;
                        const circlePoint = getCanvasPoint(event);
                        const dx = circlePoint.x - centerX;
                        const dy = circlePoint.y - centerY;

                        if (event.shiftKey) {
                            const radiusX = Math.abs(dx);
                            const radiusY = Math.abs(dy);
                            const constrained = clampCircleDraft(centerX, centerY, radiusX, radiusY);
                            activeDraftShape.type = 'ellipse';
                            activeDraftShape.x = constrained.x;
                            activeDraftShape.y = constrained.y;
                            activeDraftShape.width = constrained.width;
                            activeDraftShape.height = constrained.height;
                            activeDraftShape.centerX = constrained.centerX;
                            activeDraftShape.centerY = constrained.centerY;
                        } else {
                            const radius = Math.max(Math.abs(dx), Math.abs(dy));
                            const constrained = clampCircleDraft(centerX, centerY, radius, radius);
                            activeDraftShape.type = 'circle';
                            activeDraftShape.x = constrained.x;
                            activeDraftShape.y = constrained.y;
                            activeDraftShape.width = constrained.width;
                            activeDraftShape.height = constrained.height;
                            activeDraftShape.centerX = constrained.centerX;
                            activeDraftShape.centerY = constrained.centerY;
                        }
                        drawPaper();
                        return;
                    }

                    if (activeDraftShape && currentTool === 'polygon') {
                        const centerX = activeDraftShape.centerX;
                        const centerY = activeDraftShape.centerY;
                        const polygonPoint = getCanvasPoint(event);
                        const radius = Math.max(8, Math.hypot(polygonPoint.x - centerX, polygonPoint.y - centerY));
                        const maxSafeRadius = Math.min(
                            Math.max(1, centerX),
                            Math.max(1, currentPaper.width - centerX),
                            Math.max(1, centerY),
                            Math.max(1, currentPaper.height - centerY)
                        );
                        const safeRadius = Math.min(radius, maxSafeRadius);
                        const draft = buildRegularPolygonDraft(centerX, centerY, safeRadius, polygonSides, activeDraftShape.shapeType || 'polygon');
                        activeDraftShape = { ...activeDraftShape, ...draft };
                        drawPaper();
                        return;
                    }

                    if (!isDrawingFreeform || currentTool !== 'freeform') return;
                    freeDrawingPoints.push({ x: pointer.x, y: pointer.y });
                    drawPaper();
                });

                canvas.addEventListener('mouseup', () => {
                    if (paperDragState) {
                        const didMove = paperDragState.moved;
                        paperDragState = null;
                        drawPaper();
                        if (didMove) {
                            saveEditorState();
                        }
                        return;
                    }

                    if (dragState) {
                        dragState = null;
                        hoverHandleName = null;
                        drawPaper();
                        return;
                    }

                    if (activeDraftShape && currentTool === 'circle') {
                        const shape = {
                            ...activeDraftShape,
                            id: `shape_${Date.now()}`
                        };
                        shape.x = Math.max(0, Math.min(shape.x, currentPaper.width));
                        shape.y = Math.max(0, Math.min(shape.y, currentPaper.height));
                        shape.width = Math.max(4, Math.min(shape.width, currentPaper.width - shape.x));
                        shape.height = Math.max(4, Math.min(shape.height, currentPaper.height - shape.y));
                        if (shape.width > 4 && shape.height > 4) {
                            shapes.push(shape);
                            selectedShapeId = shape.id;
                            document.getElementById('selectedShape').textContent = shape.id;
                        }
                        activeDraftShape = null;
                        currentTool = null;
                        setActiveToolButton(null);
                        drawPaper();
                        saveEditorState();
                        return;
                    }

                    if (activeDraftShape && currentTool === 'polygon') {
                        const shape = {
                            ...activeDraftShape,
                            id: `shape_${Date.now()}`,
                            type: activeDraftShape.type || 'polygon',
                            x: activeDraftShape.x,
                            y: activeDraftShape.y,
                            width: activeDraftShape.width,
                            height: activeDraftShape.height,
                            sides: polygonSides,
                            shapeType: activeDraftShape.shapeType || 'polygon',
                            points: []
                        };
                        if (shape.width > 8 && shape.height > 8) {
                            shapes.push(shape);
                            selectedShapeId = shape.id;
                            document.getElementById('selectedShape').textContent = shape.id;
                        }
                        activeDraftShape = null;
                        currentTool = null;
                        setActiveToolButton(null);
                        drawPaper();
                        saveEditorState();
                        return;
                    }

                    if (isDrawingFreeform && currentTool === 'freeform') {
                        const shape = {
                            id: `shape_${Date.now()}`,
                            type: 'freeform',
                            points: freeDrawingPoints,
                            fill: '#ffffff',
                            stroke: '#222222',
                            text: ''
                        };
                        shapes.push(shape);
                        selectedShapeId = shape.id;
                        document.getElementById('selectedShape').textContent = shape.id;
                        isDrawingFreeform = false;
                        freeDrawingPoints = [];
                        currentTool = null;
                        setActiveToolButton(null);
                        drawPaper();
                        saveEditorState();
                    }
                });

                canvas.addEventListener('click', (event) => {
                    const point = getCanvasPoint(event);
                    const handleName = shapes
                        .map(shape => ({ shape, handleName: isResizeHandleHit(shape, point) }))
                        .find(result => result.handleName);
                    if (handleName) {
                        const { shape } = handleName;
                        selectedShapeId = shape.id;
                        document.getElementById('selectedShape').textContent = shape.id;
                        drawPaper();
                        return;
                    }

                    for (const shape of [...shapes].reverse()) {
                        if (shape.type === 'freeform' && shape.points) {
                            const hit = shape.points.some((item) => Math.abs(item.x - point.x) <= 6 && Math.abs(item.y - point.y) <= 6);
                            if (hit) {
                                selectedShapeId = shape.id;
                                document.getElementById('selectedShape').textContent = shape.id;
                                drawPaper();
                                return;
                            }
                            continue;
                        }

                        if (point.x >= shape.x && point.x <= shape.x + shape.width && point.y >= shape.y && point.y <= shape.y + shape.height) {
                            selectedShapeId = shape.id;
                            document.getElementById('selectedShape').textContent = shape.id;
                            document.getElementById('shapeText').value = shape.text;
                            document.getElementById('fontSize').value = '40';
                            drawPaper();
                            return;
                        }
                    }
                    selectedShapeId = null;
                    document.getElementById('selectedShape').textContent = '없음';
                    drawPaper();
                });

                canvas.addEventListener('wheel', (event) => {
                    if (event.ctrlKey) {
                        return;
                    }

                    const rect = canvas.getBoundingClientRect();
                    const pointerX = (event.clientX - rect.left) * (canvas.width / rect.width);
                    const pointerY = (event.clientY - rect.top) * (canvas.height / rect.height);
                    const frame = getPaperFrame();
                    const insidePaper = pointerX >= frame.x && pointerX <= frame.x + frame.width &&
                        pointerY >= frame.y && pointerY <= frame.y + frame.height;

                    if (!insidePaper) {
                        return;
                    }

                    event.preventDefault();
                    const delta = event.deltaY || event.wheelDelta || 0;
                    const nextZoom = clampZoom(paperZoom * (delta > 0 ? 0.9 : 1.1));
                    const localX = (pointerX - frame.x) / paperZoom;
                    const localY = (pointerY - frame.y) / paperZoom;

                    paperZoom = nextZoom;
                    paperPan.x = pointerX - localX * paperZoom - PAPER_MARGIN_PIXELS;
                    paperPan.y = pointerY - localY * paperZoom - PAPER_MARGIN_PIXELS;
                    clampPaperPan();
                    drawPaper();
                    saveEditorState();
                }, { passive: false });

                document.getElementById('applySettings').addEventListener('click', () => {
                    const shape = shapes.find(s => s.id === selectedShapeId);
                    if (!shape) return;
                    shape.text = document.getElementById('shapeText').value;
                    drawPaper();
                });

                paperSelect.addEventListener('change', (event) => {
                    if (event.target.value === 'Custom') {
                        syncCustomInputsToSelectedPaper();
                    }
                    applyPaperSelection(event.target.value);
                });

                document.addEventListener('keydown', (event) => {
                    if ((event.ctrlKey && event.key === 'F10') || (!event.ctrlKey && event.key === 'F12')) {
                        event.preventDefault();
                        event.stopPropagation();
                        paperPan = { x: 0, y: 0 };
                        paperZoom = 1;
                        clampPaperPan();
                        drawPaper();
                        saveEditorState();
                        return;
                    }

                    if ((event.key === 'Delete' || event.key === 'Backspace') && selectedShapeId) {
                        const idx = shapes.findIndex(shape => shape.id === selectedShapeId);
                        if (idx >= 0) {
                            shapes.splice(idx, 1);
                            selectedShapeId = null;
                            document.getElementById('selectedShape').textContent = '없음';
                            document.getElementById('shapeText').value = '';
                            drawPaper();
                            saveEditorState();
                        }
                    }
                });

                const restored = loadEditorState();
                if (!restored) {
                    syncCustomInputsToSelectedPaper();
                    applyPaperSelection('A4');
                } else {
                    paperSelect.value = currentPaper.label === 'Custom' ? 'Custom' : paperSelect.value;
                    if (paperSelect.value === 'Custom') {
                        customPaperWidthInput.value = currentPaper.width / 10;
                        customPaperHeightInput.value = currentPaper.height / 10;
                    }
                    resizeCanvasToPaper();
                    clampPaperPan();
                    drawPaper();
                }
            </script>
        </body>
        </html>
        """)

    return app
