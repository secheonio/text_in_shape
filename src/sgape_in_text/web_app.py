from __future__ import annotations

from flask import Flask, render_template_string


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template_string(r"""
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
                .toolbar button.tool-trim { background: #dcfce7; border-color: #22c55e; }
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
                .color-picker-control {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                }
                .color-sample-button {
                    border: 1px solid #cbd5e1;
                    background: #f8fafc;
                    color: #0f172a;
                    border-radius: 6px;
                    padding: 7px 10px;
                    font-size: 15px;
                    line-height: 1;
                    font-weight: 700;
                    cursor: pointer;
                    white-space: nowrap;
                    transition: all 0.12s ease;
                    min-width: 34px;
                    text-align: center;
                }
                .color-sample-button.is-active {
                    background: #dbeafe;
                    border-color: #60a5fa;
                    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.12);
                }
                .toolbar button.tool-shape.is-active { background: #bae6fd; border-color: #0284c7; }
                .toolbar button.tool-trim.is-active { background: #bbf7d0; border-color: #15803d; }
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
                .color-row {
                    display: flex;
                    gap: 10px;
                    align-items: center;
                }
                .color-field-stack {
                    display: flex;
                    flex-direction: column;
                    gap: 8px;
                    align-items: flex-start;
                }
                input[type="color"] {
                    width: 56px;
                    height: 38px;
                    padding: 0;
                    border: 1px solid #c7c7c7;
                    border-radius: 6px;
                    background: #fff;
                    cursor: pointer;
                    opacity: 1;
                    position: static;
                }
                .color-picker-wrap {
                    display: inline-flex;
                    align-items: center;
                    width: 56px;
                    height: 38px;
                    border-radius: 8px;
                    box-shadow: 0 0 0 1px rgba(148, 163, 184, 0.4);
                    transition: box-shadow 0.12s ease, transform 0.12s ease;
                }
                .color-picker-wrap.is-active {
                    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.65), 0 0 0 5px rgba(147, 197, 253, 0.22);
                    transform: translateY(-1px);
                }
                .color-picker-control {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                }
                .color-sample-button {
                    width: 34px;
                    height: 34px;
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    border: 1px solid #cbd5e1;
                    background: #f8fafc;
                    color: #0f172a;
                    border-radius: 8px;
                    font-size: 17px;
                    cursor: pointer;
                    transition: all 0.12s ease;
                    padding: 0;
                    line-height: 1;
                }
                .color-sample-button.is-active {
                    background: #dbeafe;
                    border-color: #60a5fa;
                    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.12);
                }
                .recent-color-row {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 6px;
                    max-width: 220px;
                }
                .recent-color-swatch {
                    width: 18px;
                    height: 18px;
                    border-radius: 4px;
                    border: 1px solid rgba(15, 23, 42, 0.2);
                    cursor: pointer;
                    background: #000;
                    position: relative;
                    overflow: hidden;
                    transition: transform 0.12s ease, box-shadow 0.12s ease;
                    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.4);
                }
                .recent-color-swatch.is-transparent {
                    background:
                        linear-gradient(45deg, rgba(148, 163, 184, 0.18) 25%, transparent 25%) 0 0 / 10px 10px,
                        linear-gradient(-45deg, rgba(148, 163, 184, 0.18) 25%, transparent 25%) 0 0 / 10px 10px,
                        linear-gradient(90deg, #ffffff 0%, #ffffff 50%, #f8fafc 50%, #f8fafc 100%);
                    border-color: rgba(15, 23, 42, 0.35);
                }
                .recent-color-swatch.is-transparent::before,
                .recent-color-swatch.is-transparent::after {
                    content: '';
                    position: absolute;
                    left: 50%;
                    top: 50%;
                    width: 1.7px;
                    height: 140%;
                    background: rgba(220, 38, 38, 0.9);
                    border-radius: 999px;
                    transform-origin: center;
                }
                .recent-color-swatch.is-transparent::before {
                    transform: translate(-50%, -50%) rotate(45deg);
                }
                .recent-color-swatch.is-transparent::after {
                    transform: translate(-50%, -50%) rotate(-45deg);
                }
                .recent-color-swatch:hover {
                    transform: translateY(-1px);
                    box-shadow: 0 4px 8px rgba(15, 23, 42, 0.12);
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
                <button type="button" class="tool-btn tool-trim" data-tool="trim">트림</button>
                <button type="button" class="tool-btn tool-save" data-tool="save">저장 (.sit)</button>
                <button type="button" class="tool-btn tool-load" data-tool="load">불러오기 (.sit)</button>
            </div>

            <div class="workspace">
                <div class="canvas-panel" style="position: relative;">
                    <canvas id="editorCanvas" class="canvas" width="1000" height="700"></canvas>
                    <canvas id="eyedropperMagnifier" width="160" height="160" style="position:absolute; left:18px; top:18px; display:none; z-index:40; pointer-events:none; border:2px solid rgba(15,23,42,0.9); border-radius:12px; box-shadow:0 20px 30px rgba(15,23,42,0.2); background:rgba(255,255,255,0.92);"></canvas>
                    <div id="textEditorOverlay" style="position:absolute; display:none; z-index:30; pointer-events:auto; background:rgba(255,255,255,0.96); border:1px solid #cbd5e1; border-radius:10px; box-shadow:0 10px 25px rgba(15,23,42,0.12); padding:6px;">
                        <textarea id="shapeTextEditor" rows="4" style="width:220px; min-height:80px; resize:vertical; font-size:15px; line-height:1.4; border:1px solid #cbd5e1; border-radius:8px; padding:8px;"> </textarea>
                    </div>
                </div>

                <aside class="sidebar">
                    <h3>도형 속성</h3>
                    <div class="field">
                        <label>선택된 도형</label>
                        <div id="selectedShape">없음</div>
                    </div>
                    <div class="field">
                        <label>그리려는 선 색</label>
                        <div class="color-row">
                            <div class="color-field-stack">
                                <div class="color-picker-control">
                                    <div class="color-picker-wrap is-active" id="strokeColorWrap">
                                        <input id="defaultStrokeColor" type="color" value="#222222" aria-label="선 색" />
                                    </div>
                                    <button type="button" class="color-sample-button" data-tool="eyedropper" data-kind="stroke" title="선 색상 추출" aria-label="선 색상 추출">🎯</button>
                                </div>
                                <div class="recent-color-row" id="recentStrokeColors"></div>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>그리려는 도형 내부 색</label>
                        <div class="color-row">
                            <div class="color-field-stack">
                                <div class="color-picker-control">
                                    <div class="color-picker-wrap" id="fillColorWrap">
                                        <input id="defaultFillColor" type="color" value="#ffffff" aria-label="도형 내부 색" />
                                    </div>
                                    <button type="button" class="color-sample-button" data-tool="eyedropper" data-kind="fill" title="도형 내부 색상 추출" aria-label="도형 내부 색상 추출">🎯</button>
                                </div>
                                <div class="recent-color-row" id="recentFillColors"></div>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>폰트 크기</label>
                        <input id="fontSize" type="number" value="40" min="8" max="200" />
                    </div>
                </aside>
            </div>

            <script>
                const canvas = document.getElementById('editorCanvas');
                const eyedropperMagnifier = document.getElementById('eyedropperMagnifier');
                const eyedropperMagnifierCtx = eyedropperMagnifier ? eyedropperMagnifier.getContext('2d') : null;
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
                let defaultStrokeColor = '#222222';
                let defaultFillColor = '#ffffff';
                const recentColorHistory = {
                    stroke: ['#222222', '#000000', '#ef4444', '#3b82f6', '#10b981', '#f59e0b', '#ffffff', 'transparent'],
                    fill: ['#ffffff', '#f8fafc', '#facc15', '#fca5a5', '#93c5fd', '#86efac', '#0f172a', 'transparent']
                };
                let currentPaper = { ...paperSizes.A4 };
                const shapes = [
                    { id: 'shape_1', type: 'polygon', x: 120, y: 140, width: 260, height: 180, sides: 6, text: 'shape in text', fill: 'transparent', stroke: '#222222', closed: true }
                ];
                let selectedShapeId = 'shape_1';
                let currentTool = null;
                let currentEyedropperKind = null;
                let freeDrawingPoints = [];
                let isDrawingFreeform = false;
                let hoverHandleName = null;
                let trimHoverTarget = null;
                let dragState = null;
                let activeDraftShape = null;
                let paperDragState = null;
                let textEditorShapeId = null;
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
                        paperSelectValue: paperSelect.value,
                        defaultStrokeColor,
                        defaultFillColor,
                        recentColorHistory
                    };
                    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
                }

                function isHexColor(value) {
                    return typeof value === 'string' && /^#[0-9A-Fa-f]{6}$/.test(value);
                }

                function isTransparentColor(value) {
                    return value === 'transparent' || value === 'none' || value === 'transparent';
                }

                function normalizeColorForPicker(value) {
                    if (isTransparentColor(value)) {
                        return '#ffffff';
                    }
                    return isHexColor(value) ? value : '#000000';
                }

                function loadEditorState() {
                    try {
                        const raw = localStorage.getItem(STORAGE_KEY);
                        if (!raw) return false;
                        const state = JSON.parse(raw);
                        if (!state || !Array.isArray(state.shapes)) return false;

                        defaultStrokeColor = isHexColor(state.defaultStrokeColor) ? state.defaultStrokeColor : '#222222';
                        defaultFillColor = isHexColor(state.defaultFillColor) ? state.defaultFillColor : '#ffffff';
                        if (state.recentColorHistory && state.recentColorHistory.stroke) {
                            recentColorHistory.stroke = state.recentColorHistory.stroke.filter(color => isHexColor(color) || isTransparentColor(color)).slice(0, 8);
                        }
                        if (state.recentColorHistory && state.recentColorHistory.fill) {
                            recentColorHistory.fill = state.recentColorHistory.fill.filter(color => isHexColor(color) || isTransparentColor(color)).slice(0, 8);
                        }
                        if (!recentColorHistory.stroke.length) {
                            recentColorHistory.stroke = ['#222222', '#000000', '#ef4444', '#3b82f6', '#10b981', '#f59e0b', '#ffffff', 'transparent'];
                        }
                        if (!recentColorHistory.fill.length) {
                            recentColorHistory.fill = ['#ffffff', '#f8fafc', '#facc15', '#fca5a5', '#93c5fd', '#86efac', '#0f172a', 'transparent'];
                        }
                        currentPaper = state.currentPaper || { ...paperSizes.A4 };
                        normalizePaperState();
                        shapes.splice(0, shapes.length, ...state.shapes
                            .map(shape => normalizeShapeForStorage(shape))
                            .filter(Boolean)
                            .map(shape => ({ ...shape, closed: shape.closed !== false && shape.type !== 'freeform' ? true : shape.closed ?? false })));
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
                        document.getElementById('defaultStrokeColor').value = defaultStrokeColor;
                        document.getElementById('defaultFillColor').value = defaultFillColor;
                        clampPaperPan();
                        return true;
                    } catch (error) {
                        currentPaper = { ...paperSizes.A4 };
                        paperPan = { x: 0, y: 0 };
                        paperZoom = 1;
                        defaultStrokeColor = '#222222';
                        defaultFillColor = '#ffffff';
                        shapes.splice(0, shapes.length, { id: 'shape_1', type: 'polygon', x: 120, y: 140, width: 260, height: 180, sides: 6, text: 'shape in text', fill: 'transparent', stroke: '#222222', closed: true });
                        selectedShapeId = 'shape_1';
                        document.getElementById('defaultStrokeColor').value = defaultStrokeColor;
                        document.getElementById('defaultFillColor').value = defaultFillColor;
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

                function shapeIsClosed(shape) {
                    if (!shape || typeof shape !== 'object') return true;
                    if (shape.closed === false) return false;
                    return shape.type !== 'freeform' || shape.closed === true;
                }

                function wrapTextForShape(shape, text) {
                    const value = (text || '').replace(/\r\n/g, '\n');
                    if (!value) return [''];
                    const fontSize = Number(document.getElementById('fontSize').value) || 40;
                    const maxWidth = Math.max(40, shape.width - 28);
                    ctx.save();
                    ctx.font = `${fontSize}px Arial`;
                    const lines = [];
                    let current = '';
                    for (let i = 0; i < value.length; i++) {
                        const char = value[i];
                        if (char === '\n') {
                            lines.push(current);
                            current = '';
                            continue;
                        }
                        const candidate = current + char;
                        if (ctx.measureText(candidate).width > maxWidth && current.length > 0) {
                            lines.push(current);
                            current = char;
                        } else {
                            current = candidate;
                        }
                    }
                    if (current.length > 0 || lines.length === 0) {
                        lines.push(current);
                    }
                    ctx.restore();
                    return lines;
                }

                function getOrderedClosedShapes() {
                    return shapes.filter(shape => shapeIsClosed(shape));
                }

                function getTextCapacity(shape) {
                    const fontSize = Number(document.getElementById('fontSize').value) || 40;
                    const maxCharsPerLine = Math.max(4, Math.floor((Math.max(40, shape.width - 30)) / (fontSize * 0.56)));
                    const maxLines = Math.max(1, Math.floor((shape.height - 18) / (fontSize * 1.3)));
                    return maxCharsPerLine * maxLines;
                }

                function splitTextForShape(text, maxChars) {
                    const normalized = (text || '').replace(/\r\n/g, '\n');
                    if (!normalized) return { chunk: '', remainder: '' };
                    if (normalized.length <= maxChars) {
                        return { chunk: normalized, remainder: '' };
                    }

                    const boundary = normalized.lastIndexOf(' ', maxChars);
                    const splitIndex = boundary > maxChars * 0.45 ? boundary : maxChars;
                    const chunk = normalized.slice(0, splitIndex).trimEnd();
                    const remainder = normalized.slice(splitIndex).trimStart();
                    return { chunk, remainder };
                }

                function distributeTextFlow(shapeId, fullText) {
                    const ordered = getOrderedClosedShapes();
                    const startIndex = ordered.findIndex(shape => shape.id === shapeId);
                    if (startIndex < 0) return;

                    let remainder = (fullText || '').replace(/\r\n/g, '\n');
                    for (let index = startIndex; index < ordered.length; index++) {
                        const shape = ordered[index];
                        if (index > startIndex) {
                            shape.text = '';
                        }
                        if (!remainder.trim()) {
                            shape.text = '';
                            continue;
                        }

                        const capacity = getTextCapacity(shape);
                        const { chunk, remainder: nextRemainder } = splitTextForShape(remainder, capacity);
                        shape.text = chunk || '';
                        remainder = nextRemainder;

                        if (!remainder) {
                            break;
                        }
                    }

                    for (let index = ordered.length - 1; index > startIndex; index--) {
                        if (ordered[index] && ordered[index].id !== shapeId && !ordered[index].text) {
                            ordered[index].text = '';
                        }
                    }
                }

                function drawTextFlowConnector(shape) {
                    const ordered = getOrderedClosedShapes();
                    const index = ordered.findIndex(item => item.id === shape.id);
                    if (index < 0 || index >= ordered.length - 1) return;
                    const nextShape = ordered[index + 1];
                    if (!shape.text || !nextShape || !nextShape.text) return;

                    const from = { x: shape.x + shape.width, y: shape.y + shape.height * 0.5 };
                    const to = { x: nextShape.x, y: nextShape.y + nextShape.height * 0.5 };
                    ctx.save();
                    ctx.setLineDash([7, 5]);
                    ctx.strokeStyle = 'rgba(14, 116, 144, 0.72)';
                    ctx.lineWidth = 1.5;
                    ctx.beginPath();
                    ctx.moveTo(from.x, from.y);
                    ctx.lineTo(to.x, to.y);
                    ctx.stroke();

                    const angle = Math.atan2(to.y - from.y, to.x - from.x);
                    const headLength = 8;
                    ctx.beginPath();
                    ctx.moveTo(to.x, to.y);
                    ctx.lineTo(to.x - headLength * Math.cos(angle - Math.PI / 6), to.y - headLength * Math.sin(angle - Math.PI / 6));
                    ctx.lineTo(to.x - headLength * Math.cos(angle + Math.PI / 6), to.y - headLength * Math.sin(angle + Math.PI / 6));
                    ctx.closePath();
                    ctx.fillStyle = 'rgba(14, 116, 144, 0.72)';
                    ctx.fill();
                    ctx.restore();
                }

                function drawShape(shape) {
                    ctx.strokeStyle = shape.stroke || '#222222';
                    ctx.lineWidth = selectedShapeId === shape.id ? 4 : 2;

                    if (shape.type === 'freeform') {
                        if (shape.points && shape.points.length > 1) {
                            ctx.beginPath();
                            ctx.moveTo(shape.points[0].x, shape.points[0].y);
                            for (let i = 1; i < shape.points.length; i++) {
                                ctx.lineTo(shape.points[i].x, shape.points[i].y);
                            }
                            if (shapeIsClosed(shape) && shape.points.length > 2) {
                                ctx.closePath();
                                ctx.fillStyle = shape.fill && shape.fill !== 'transparent' ? shape.fill : 'transparent';
                                ctx.fill();
                            } else {
                                ctx.fillStyle = 'transparent';
                            }
                            ctx.stroke();
                        }
                        return;
                    }

                    const isClosed = shapeIsClosed(shape);
                    ctx.fillStyle = isClosed && shape.fill && shape.fill !== 'transparent' ? shape.fill : 'transparent';

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
                        if (isClosed) {
                            ctx.fill();
                        }
                        ctx.stroke();
                    } else if (shape.type === 'circle' || shape.type === 'ellipse') {
                        const centerX = shape.x + shape.width / 2;
                        const centerY = shape.y + shape.height / 2;
                        ctx.beginPath();
                        ctx.ellipse(centerX, centerY, Math.max(shape.width / 2, 1), Math.max(shape.height / 2, 1), 0, 0, Math.PI * 2);
                        if (isClosed) {
                            ctx.fill();
                        }
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
                        const fontSize = Number(document.getElementById('fontSize').value) || 40;
                        const lines = wrapTextForShape(shape, shape.text);
                        ctx.fillStyle = '#111111';
                        ctx.font = `${fontSize}px Arial`;
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';
                        const lineHeight = fontSize * 1.2;
                        const startY = shape.y + shape.height / 2 - ((lines.length - 1) * lineHeight) / 2;
                        lines.forEach((line, index) => {
                            ctx.fillText(line, shape.x + shape.width / 2, startY + index * lineHeight, shape.width - 36);
                        });
                        drawTextFlowConnector(shape);
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
                        fill: 'transparent',
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

                    if (currentTool === 'trim' && trimHoverTarget && trimHoverTarget.segment) {
                        ctx.save();
                        ctx.strokeStyle = '#9fe8a9';
                        ctx.lineWidth = 8;
                        ctx.lineJoin = 'round';
                        ctx.lineCap = 'round';
                        ctx.beginPath();
                        ctx.moveTo(trimHoverTarget.segment.a.x * paperZoom + paperX, trimHoverTarget.segment.a.y * paperZoom + paperY);
                        ctx.lineTo(trimHoverTarget.segment.b.x * paperZoom + paperX, trimHoverTarget.segment.b.y * paperZoom + paperY);
                        ctx.stroke();
                        ctx.restore();
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

                function rgbaToHex(r, g, b) {
                    return `#${[r, g, b].map(channel => Math.max(0, Math.min(255, channel)).toString(16).padStart(2, '0')).join('')}`;
                }

                function getRenderedPixelAtPaperPoint(point) {
                    const frame = getPaperFrame();
                    const pixelX = Math.max(0, Math.min(canvas.width - 1, Math.round(point.x * paperZoom + frame.x)));
                    const pixelY = Math.max(0, Math.min(canvas.height - 1, Math.round(point.y * paperZoom + frame.y)));
                    const { data } = ctx.getImageData(pixelX, pixelY, 1, 1);
                    return {
                        x: pixelX,
                        y: pixelY,
                        r: data[0],
                        g: data[1],
                        b: data[2],
                        a: data[3]
                    };
                }

                function sampleCanvasColorFromPoint(point) {
                    const base = getRenderedPixelAtPaperPoint(point);
                    if (base.a >= 2) {
                        return rgbaToHex(base.r, base.g, base.b);
                    }

                    let bestColor = rgbaToHex(base.r, base.g, base.b);
                    let bestDistance = Number.POSITIVE_INFINITY;
                    const searchRadius = 16;

                    for (let radius = 0; radius <= searchRadius; radius += 1) {
                        for (let dx = -radius; dx <= radius; dx += 1) {
                            for (let dy = -radius; dy <= radius; dy += 1) {
                                if (Math.hypot(dx, dy) > radius + 0.5) {
                                    continue;
                                }
                                const sampleX = Math.max(0, Math.min(canvas.width - 1, base.x + dx));
                                const sampleY = Math.max(0, Math.min(canvas.height - 1, base.y + dy));
                                const { data } = ctx.getImageData(sampleX, sampleY, 1, 1);
                                if (data[3] < 2) {
                                    continue;
                                }
                                const candidate = rgbaToHex(data[0], data[1], data[2]);
                                const distance = Math.hypot(dx, dy);
                                if (distance < bestDistance) {
                                    bestColor = candidate;
                                    bestDistance = distance;
                                }
                            }
                        }
                        if (bestDistance < Number.POSITIVE_INFINITY) {
                            return bestColor;
                        }
                    }

                    return bestColor;
                }

                function resolveEyedropperColor(point) {
                    return sampleCanvasColorFromPoint(point);
                }

                function updateEyedropperMagnifier(point) {
                    if (!eyedropperMagnifier || !eyedropperMagnifierCtx || !point || currentTool !== 'eyedropper') {
                        eyedropperMagnifier.style.display = 'none';
                        return;
                    }

                    const frame = getPaperFrame();
                    const rect = canvas.getBoundingClientRect();
                    const localX = (point.x * paperZoom + frame.x) * (rect.width / canvas.width);
                    const localY = (point.y * paperZoom + frame.y) * (rect.height / canvas.height);
                    const magnifierSize = 120;
                    const cropHalf = 22;
                    const cropX = Math.max(0, Math.min(canvas.width - 1, Math.round((point.x * paperZoom + frame.x) - cropHalf)));
                    const cropY = Math.max(0, Math.min(canvas.height - 1, Math.round((point.y * paperZoom + frame.y) - cropHalf)));
                    const cropWidth = Math.max(1, Math.min(canvas.width - cropX, cropHalf * 2));
                    const cropHeight = Math.max(1, Math.min(canvas.height - cropY, cropHalf * 2));

                    eyedropperMagnifierCtx.clearRect(0, 0, magnifierSize, magnifierSize);
                    eyedropperMagnifierCtx.fillStyle = 'rgba(255,255,255,0.9)';
                    eyedropperMagnifierCtx.fillRect(0, 0, magnifierSize, magnifierSize);
                    eyedropperMagnifierCtx.drawImage(canvas, cropX, cropY, cropWidth, cropHeight, 0, 0, magnifierSize, magnifierSize);

                    eyedropperMagnifierCtx.strokeStyle = '#0f172a';
                    eyedropperMagnifierCtx.lineWidth = 1;
                    eyedropperMagnifierCtx.beginPath();
                    eyedropperMagnifierCtx.moveTo(magnifierSize / 2, 0);
                    eyedropperMagnifierCtx.lineTo(magnifierSize / 2, magnifierSize);
                    eyedropperMagnifierCtx.moveTo(0, magnifierSize / 2);
                    eyedropperMagnifierCtx.lineTo(magnifierSize, magnifierSize / 2);
                    eyedropperMagnifierCtx.stroke();

                    const pickedColor = resolveEyedropperColor(point);
                    eyedropperMagnifierCtx.fillStyle = pickedColor || '#ffffff';
                    eyedropperMagnifierCtx.fillRect(8, magnifierSize - 20, 30, 12);
                    eyedropperMagnifierCtx.strokeStyle = '#0f172a';
                    eyedropperMagnifierCtx.strokeRect(8, magnifierSize - 20, 30, 12);

                    eyedropperMagnifier.style.display = 'block';
                    eyedropperMagnifier.style.left = `${Math.min(Math.max(12, localX + 12), rect.width - 136)}px`;
                    eyedropperMagnifier.style.top = `${Math.min(Math.max(12, localY + 12), rect.height - 136)}px`;
                }

                function setActiveToolButton(toolName) {
                    document.querySelectorAll('.tool-btn').forEach((button) => {
                        const isActive = button.dataset.tool === toolName;
                        button.classList.toggle('is-active', isActive);
                    });
                    document.querySelectorAll('.color-sample-button').forEach((button) => {
                        const isActive = button.dataset.tool === toolName && toolName === 'eyedropper' && button.dataset.kind === currentEyedropperKind;
                        button.classList.toggle('is-active', isActive);
                    });
                    canvas.style.cursor = toolName === 'eyedropper' ? 'crosshair' : 'default';
                    if (toolName !== 'eyedropper' && eyedropperMagnifier) {
                        eyedropperMagnifier.style.display = 'none';
                    }
                }

                function getActiveColorKind() {
                    const strokeWrap = document.getElementById('strokeColorWrap');
                    const fillWrap = document.getElementById('fillColorWrap');
                    if (!strokeWrap || !fillWrap) return 'stroke';
                    return strokeWrap.classList.contains('is-active') ? 'stroke' : 'fill';
                }

                function sampleColorFromShape(shape) {
                    if (!shape) return null;
                    const activeKind = getActiveColorKind();
                    if (activeKind === 'fill') {
                        if (shapeIsClosed(shape) && shape.fill && shape.fill !== 'transparent') {
                            return shape.fill;
                        }
                        if (shape.stroke && shape.stroke !== 'transparent') {
                            return shape.stroke;
                        }
                        return defaultFillColor;
                    }
                    if (shape.stroke && shape.stroke !== 'transparent') {
                        return shape.stroke;
                    }
                    if (shapeIsClosed(shape) && shape.fill && shape.fill !== 'transparent') {
                        return shape.fill;
                    }
                    return defaultStrokeColor;
                }

                function getShapeSegments(shape) {
                    if (!shape) return [];

                    if (shape.type === 'freeform' && Array.isArray(shape.points) && shape.points.length > 1) {
                        return shape.points.slice(1).map((point, index) => ({
                            a: shape.points[index],
                            b: point
                        }));
                    }

                    if (shape.type === 'polygon' || shape.type === 'diamond') {
                        const vertices = getShapeVertices(shape);
                        return vertices.map((point, index) => ({
                            a: point,
                            b: vertices[(index + 1) % vertices.length]
                        }));
                    }

                    if (shape.type === 'circle' || shape.type === 'ellipse') {
                        const cx = shape.x + shape.width / 2;
                        const cy = shape.y + shape.height / 2;
                        const rx = Math.max(shape.width / 2, 1);
                        const ry = Math.max(shape.height / 2, 1);
                        const segments = [];
                        for (let i = 0; i < 48; i++) {
                            const a = (i / 48) * Math.PI * 2;
                            const b = ((i + 1) / 48) * Math.PI * 2;
                            segments.push({
                                a: { x: cx + Math.cos(a) * rx, y: cy + Math.sin(a) * ry },
                                b: { x: cx + Math.cos(b) * rx, y: cy + Math.sin(b) * ry }
                            });
                        }
                        return segments;
                    }

                    return [
                        { a: { x: shape.x, y: shape.y }, b: { x: shape.x + shape.width, y: shape.y } },
                        { a: { x: shape.x + shape.width, y: shape.y }, b: { x: shape.x + shape.width, y: shape.y + shape.height } },
                        { a: { x: shape.x + shape.width, y: shape.y + shape.height }, b: { x: shape.x, y: shape.y + shape.height } },
                        { a: { x: shape.x, y: shape.y + shape.height }, b: { x: shape.x, y: shape.y } }
                    ];
                }

                function segmentIntersection(a1, a2, b1, b2) {
                    const denominator = (a1.x - a2.x) * (b1.y - b2.y) - (a1.y - a2.y) * (b1.x - b2.x);
                    if (Math.abs(denominator) < 0.0001) {
                        return null;
                    }
                    const px = ((a1.x * a2.y - a1.y * a2.x) * (b1.x - b2.x) - (a1.x - a2.x) * (b1.x * b2.y - b1.y * b2.x)) / denominator;
                    const py = ((a1.x * a2.y - a1.y * a2.x) * (b1.y - b2.y) - (a1.y - a2.y) * (b1.x * b2.y - b1.y * b2.x)) / denominator;
                    const intersection = { x: px, y: py };
                    const onSegmentA = Math.min(a1.x, a2.x) - 1 <= intersection.x && intersection.x <= Math.max(a1.x, a2.x) + 1 &&
                        Math.min(a1.y, a2.y) - 1 <= intersection.y && intersection.y <= Math.max(a1.y, a2.y) + 1;
                    const onSegmentB = Math.min(b1.x, b2.x) - 1 <= intersection.x && intersection.x <= Math.max(b1.x, b2.x) + 1 &&
                        Math.min(b1.y, b2.y) - 1 <= intersection.y && intersection.y <= Math.max(b1.y, b2.y) + 1;
                    return onSegmentA && onSegmentB ? intersection : null;
                }

                const MAX_TRIM_NEIGHBOR_DISTANCE = 140;
                const MAX_TRIM_NEIGHBOR_SEGMENT_GAP = 14;

                function isTrimIntersectionBoundedSegment(shape, segment, point) {
                    if (!shape || !segment) return false;

                    const nearestEndpoint = Math.hypot(point.x - segment.a.x, point.y - segment.a.y) <= Math.hypot(point.x - segment.b.x, point.y - segment.b.y)
                        ? segment.a
                        : segment.b;
                    const endpointDistance = Math.hypot(point.x - nearestEndpoint.x, point.y - nearestEndpoint.y);
                    if (endpointDistance > 10) return false;

                    for (const other of shapes) {
                        if (other.id === shape.id) continue;
                        for (const otherSegment of getShapeSegments(other)) {
                            const hit = segmentIntersection(segment.a, segment.b, otherSegment.a, otherSegment.b);
                            if (!hit) continue;

                            const intersectionDistance = Math.hypot(hit.x - nearestEndpoint.x, hit.y - nearestEndpoint.y);
                            if (intersectionDistance > MAX_TRIM_NEIGHBOR_DISTANCE) continue;

                            const gapToOther = Math.min(
                                pointToSegmentDistance(hit, otherSegment.a, otherSegment.b),
                                pointToSegmentDistance(otherSegment.a, segment.a, segment.b),
                                pointToSegmentDistance(otherSegment.b, segment.a, segment.b),
                                Math.hypot(hit.x - otherSegment.a.x, hit.y - otherSegment.a.y),
                                Math.hypot(hit.x - otherSegment.b.x, hit.y - otherSegment.b.y)
                            );
                            if (gapToOther > MAX_TRIM_NEIGHBOR_SEGMENT_GAP) continue;

                            return true;
                        }
                    }

                    return false;
                }

                function findTrimTarget(point, trimShape) {
                    if (!trimShape) return null;

                    const candidates = [];
                    const segments = getShapeSegments(trimShape);

                    for (const segment of segments) {
                        if (!isTrimIntersectionBoundedSegment(trimShape, segment, point)) continue;

                        const nearestEndpoint = Math.hypot(point.x - segment.a.x, point.y - segment.a.y) <= Math.hypot(point.x - segment.b.x, point.y - segment.b.y)
                            ? segment.a
                            : segment.b;

                        const intersections = [];
                        for (const other of shapes) {
                            if (other.id === trimShape.id) continue;
                            for (const otherSegment of getShapeSegments(other)) {
                                const hit = segmentIntersection(segment.a, segment.b, otherSegment.a, otherSegment.b);
                                if (!hit) continue;

                                const endpointDistance = Math.hypot(hit.x - nearestEndpoint.x, hit.y - nearestEndpoint.y);
                                if (endpointDistance > MAX_TRIM_NEIGHBOR_DISTANCE) continue;

                                const gapToOther = Math.min(
                                    pointToSegmentDistance(hit, otherSegment.a, otherSegment.b),
                                    pointToSegmentDistance(otherSegment.a, segment.a, segment.b),
                                    pointToSegmentDistance(otherSegment.b, segment.a, segment.b),
                                    Math.hypot(hit.x - otherSegment.a.x, hit.y - otherSegment.a.y),
                                    Math.hypot(hit.x - otherSegment.b.x, hit.y - otherSegment.b.y)
                                );
                                if (gapToOther > MAX_TRIM_NEIGHBOR_SEGMENT_GAP) continue;

                                intersections.push({
                                    x: hit.x,
                                    y: hit.y,
                                    distance: endpointDistance
                                });
                            }
                        }

                        if (intersections.length === 0) continue;

                        const nearest = intersections
                            .sort((a, b) => a.distance - b.distance)[0];

                        if (nearest) {
                            candidates.push({ shape: trimShape, point: nearestEndpoint, intersection: nearest, segment });
                        }
                    }

                    if (!candidates.length) return null;
                    return candidates.sort((a, b) => {
                        const da = Math.hypot(a.intersection.x - a.point.x, a.intersection.y - a.point.y);
                        const db = Math.hypot(b.intersection.x - b.point.x, b.intersection.y - b.point.y);
                        return da - db;
                    })[0];
                }

                function getSelectedShapeTrimTarget(point) {
                    const selectedShape = selectedShapeId ? shapes.find(shape => shape.id === selectedShapeId) : null;
                    if (!selectedShape) return null;
                    if (!getShapeBorderHit(selectedShape, point)) return null;
                    return findTrimTarget(point, selectedShape);
                }

                function getTrimHoverTarget(point) {
                    const candidates = [];

                    for (const shape of shapes) {
                        for (const segment of getShapeSegments(shape)) {
                            if (!isTrimIntersectionBoundedSegment(shape, segment, point)) continue;

                            const nearestEndpoint = Math.hypot(point.x - segment.a.x, point.y - segment.a.y) <= Math.hypot(point.x - segment.b.x, point.y - segment.b.y)
                                ? segment.a
                                : segment.b;

                            const intersections = [];
                            for (const other of shapes) {
                                if (other.id === shape.id) continue;
                                for (const otherSegment of getShapeSegments(other)) {
                                    const hit = segmentIntersection(segment.a, segment.b, otherSegment.a, otherSegment.b);
                                    if (!hit) continue;

                                    const endpointDistance = Math.hypot(hit.x - nearestEndpoint.x, hit.y - nearestEndpoint.y);
                                    if (endpointDistance > MAX_TRIM_NEIGHBOR_DISTANCE) continue;

                                    const gapToOther = Math.min(
                                        pointToSegmentDistance(hit, otherSegment.a, otherSegment.b),
                                        pointToSegmentDistance(otherSegment.a, segment.a, segment.b),
                                        pointToSegmentDistance(otherSegment.b, segment.a, segment.b),
                                        Math.hypot(hit.x - otherSegment.a.x, hit.y - otherSegment.a.y),
                                        Math.hypot(hit.x - otherSegment.b.x, hit.y - otherSegment.b.y)
                                    );
                                    if (gapToOther > MAX_TRIM_NEIGHBOR_SEGMENT_GAP) continue;

                                    intersections.push({
                                        x: hit.x,
                                        y: hit.y,
                                        distance: endpointDistance
                                    });
                                }
                            }

                            if (!intersections.length) continue;

                            const firstIntersection = intersections
                                .sort((a, b) => a.distance - b.distance)[0];

                            if (!firstIntersection) continue;

                            const dist = pointToSegmentDistance(point, segment.a, segment.b);
                            candidates.push({
                                shape,
                                segment,
                                point: nearestEndpoint,
                                intersection: firstIntersection,
                                distance: dist
                            });
                        }
                    }

                    if (!candidates.length) return null;
                    return candidates.sort((a, b) => a.distance - b.distance)[0];
                }

                function lineSide(point, start, end) {
                    return (point.x - start.x) * (end.y - start.y) - (point.y - start.y) * (end.x - start.x);
                }

                function clipPolygonByCut(vertices, cutStart, cutEnd) {
                    if (!Array.isArray(vertices) || vertices.length < 3) {
                        return [];
                    }

                    const center = vertices.reduce((sum, vertex) => ({
                        x: sum.x + vertex.x,
                        y: sum.y + vertex.y
                    }), { x: 0, y: 0 });
                    const keepPositive = lineSide({
                        x: center.x / vertices.length,
                        y: center.y / vertices.length
                    }, cutStart, cutEnd) >= 0;

                    const result = [];
                    for (let index = 0; index < vertices.length; index++) {
                        const current = vertices[index];
                        const next = vertices[(index + 1) % vertices.length];
                        const currentSide = lineSide(current, cutStart, cutEnd) >= 0;
                        const nextSide = lineSide(next, cutStart, cutEnd) >= 0;

                        if (currentSide === keepPositive && nextSide === keepPositive) {
                            result.push({ ...next });
                        } else if (currentSide === keepPositive && nextSide !== keepPositive) {
                            const hit = segmentIntersection(current, next, cutStart, cutEnd);
                            if (hit) {
                                result.push({ ...hit });
                            }
                        } else if (currentSide !== keepPositive && nextSide === keepPositive) {
                            const hit = segmentIntersection(current, next, cutStart, cutEnd);
                            if (hit) {
                                result.push({ ...hit });
                            }
                            result.push({ ...next });
                        }
                    }

                    if (!result.length) {
                        return [];
                    }

                    return result.filter((point, index, arr) => {
                        const duplicateIndex = arr.findIndex(candidate =>
                            Math.abs(candidate.x - point.x) < 0.01 && Math.abs(candidate.y - point.y) < 0.01
                        );
                        return duplicateIndex === index;
                    });
                }

                function applyTrimToShape(shape, point, intersection) {
                    if (!shape || !intersection) return false;

                    const vertices = getShapeVertices(shape);
                    if (!vertices.length) return false;

                    const center = vertices.reduce((sum, vertex) => ({
                        x: sum.x + vertex.x,
                        y: sum.y + vertex.y
                    }), { x: 0, y: 0 });
                    const polygonCenter = {
                        x: center.x / vertices.length,
                        y: center.y / vertices.length
                    };

                    const dx = intersection.x - point.x;
                    const dy = intersection.y - point.y;
                    const length = Math.hypot(dx, dy) || 1;
                    const normalX = -dy / length;
                    const normalY = dx / length;
                    const offsetDirection = lineSide(polygonCenter, point, intersection) >= 0 ? -1 : 1;
                    const offsetAmount = 2;
                    const shiftedStart = {
                        x: point.x + normalX * offsetDirection * offsetAmount,
                        y: point.y + normalY * offsetDirection * offsetAmount
                    };
                    const shiftedEnd = {
                        x: intersection.x + normalX * offsetDirection * offsetAmount,
                        y: intersection.y + normalY * offsetDirection * offsetAmount
                    };

                    const clamped = clipPolygonByCut(vertices, shiftedStart, shiftedEnd);
                    if (!clamped.length || clamped.length < 3) {
                        const index = shapes.findIndex(item => item.id === shape.id);
                        if (index >= 0) {
                            shapes.splice(index, 1);
                            selectedShapeId = null;
                            document.getElementById('selectedShape').textContent = '없음';
                            const overlay = document.getElementById('textEditorOverlay');
                            if (overlay) overlay.style.display = 'none';
                            textEditorShapeId = null;
                        }
                        return true;
                    }

                    shape.type = 'freeform';
                    shape.closed = false;
                    shape.fill = 'transparent';
                    shape.points = clamped;
                    delete shape.width;
                    delete shape.height;
                    delete shape.x;
                    delete shape.y;
                    delete shape.sides;
                    delete shape.shapeType;
                    delete shape.centerX;
                    delete shape.centerY;
                    delete shape.radius;
                    return true;
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

                function toggleTrimTool() {
                    currentTool = currentTool === 'trim' ? null : 'trim';
                    trimHoverTarget = null;
                    setActiveToolButton(currentTool);
                }

                const shapeButtons = Array.from(document.querySelectorAll('.tool-shape'));
                shapeButtons[0].addEventListener('click', () => addShape('circle'));
                shapeButtons[1].addEventListener('click', () => addShape('freeform'));

                document.querySelector('[data-tool="trim"]').addEventListener('click', () => {
                    toggleTrimTool();
                });

                document.querySelectorAll('[data-tool="eyedropper"]').forEach((button) => {
                    button.addEventListener('click', () => {
                        const kind = button.dataset.kind || 'stroke';
                        if (currentTool === 'eyedropper' && currentEyedropperKind === kind) {
                            currentTool = null;
                            currentEyedropperKind = null;
                            setActiveToolButton(null);
                            return;
                        }
                        currentEyedropperKind = kind;
                        currentTool = 'eyedropper';
                        setActiveColorInput(kind);
                        setActiveToolButton(currentTool);
                    });
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

                    if (currentTool === 'trim') {
                        const trimCandidate = getTrimHoverTarget(point);

                        if (trimCandidate && trimCandidate.shape) {
                            const trimmed = applyTrimToShape(trimCandidate.shape, trimCandidate.point, trimCandidate.intersection);
                            if (trimmed) {
                                selectedShapeId = trimCandidate.shape.id;
                                document.getElementById('selectedShape').textContent = trimCandidate.shape.id;
                                trimHoverTarget = null;
                                drawPaper();
                                saveEditorState();
                            }
                            return;
                        }

                        if (point.x >= 0 && point.x <= currentPaper.width && point.y >= 0 && point.y <= currentPaper.height) {
                            trimHoverTarget = null;
                            drawPaper();
                            return;
                        }

                        return;
                    }

                    if (currentTool === 'eyedropper') {
                        const kind = currentEyedropperKind || getActiveColorKind();
                        const pickedColor = resolveEyedropperColor(point);
                        const normalizedColor = isHexColor(pickedColor) ? pickedColor : null;

                        if (normalizedColor) {
                            if (kind === 'stroke') {
                                document.getElementById('defaultStrokeColor').value = normalizedColor;
                                defaultStrokeColor = normalizedColor;
                                addRecentColor('stroke', normalizedColor);
                                updateRecentColorRow('stroke');
                                const selected = shapes.find(item => item.id === selectedShapeId);
                                if (selected) selected.stroke = normalizedColor;
                            } else {
                                document.getElementById('defaultFillColor').value = normalizedColor;
                                defaultFillColor = normalizedColor;
                                addRecentColor('fill', normalizedColor);
                                updateRecentColorRow('fill');
                                const selected = shapes.find(item => item.id === selectedShapeId);
                                if (selected && shapeIsClosed(selected)) selected.fill = normalizedColor;
                            }
                            setActiveColorInput(kind);
                            drawPaper();
                            saveEditorState();
                        }

                        currentEyedropperKind = null;
                        currentTool = null;
                        setActiveToolButton(null);
                        return;
                    }

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
                        const isAlreadySelected = selectedShapeId === borderShape.id;
                        selectedShapeId = borderShape.id;
                        if (isAlreadySelected) {
                            dragState = {
                                mode: 'move',
                                shapeId: borderShape.id,
                                startX: point.x,
                                startY: point.y,
                                original: { ...borderShape }
                            };
                        }
                        document.getElementById('selectedShape').textContent = borderShape.id;
                        syncSelectedShapeProperties();
                        document.getElementById('fontSize').value = '40';
                        drawPaper();
                        return;
                    }

                    const targetShape = getShapeAtPoint(point);
                    if (targetShape) {
                        const isAlreadySelected = selectedShapeId === targetShape.id;
                        selectedShapeId = targetShape.id;
                        if (isAlreadySelected) {
                            dragState = {
                                mode: 'move',
                                shapeId: targetShape.id,
                                startX: point.x,
                                startY: point.y,
                                original: { ...targetShape }
                            };
                        }
                        document.getElementById('selectedShape').textContent = targetShape.id;
                        syncSelectedShapeProperties();
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
                    if (trimHoverTarget) {
                        trimHoverTarget = null;
                        drawPaper();
                    }
                    if (eyedropperMagnifier) {
                        eyedropperMagnifier.style.display = 'none';
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

                    if (currentTool === 'eyedropper') {
                        updateEyedropperMagnifier(pointer);
                    } else if (eyedropperMagnifier) {
                        eyedropperMagnifier.style.display = 'none';
                    }

                    if (currentTool === 'trim') {
                        const nextTrimHoverTarget = getTrimHoverTarget(pointer);
                        if (nextTrimHoverTarget !== trimHoverTarget) {
                            trimHoverTarget = nextTrimHoverTarget;
                            drawPaper();
                        }
                    } else if (trimHoverTarget) {
                        trimHoverTarget = null;
                        drawPaper();
                    }

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
                        const shape = applyDefaultsToNewShape({
                            ...activeDraftShape,
                            id: `shape_${Date.now()}`,
                            fill: 'transparent'
                        });
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
                        const shape = applyDefaultsToNewShape({
                            ...activeDraftShape,
                            id: `shape_${Date.now()}`,
                            type: activeDraftShape.type || 'polygon',
                            x: activeDraftShape.x,
                            y: activeDraftShape.y,
                            width: activeDraftShape.width,
                            height: activeDraftShape.height,
                            sides: polygonSides,
                            shapeType: activeDraftShape.shapeType || 'polygon',
                            points: [],
                            fill: 'transparent'
                        });
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
                        const shape = applyDefaultsToNewShape({
                            id: `shape_${Date.now()}`,
                            type: 'freeform',
                            points: freeDrawingPoints,
                            fill: 'transparent',
                            stroke: defaultStrokeColor,
                            text: '',
                            closed: false
                        });
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
                        syncSelectedShapeProperties();
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
                            document.getElementById('fontSize').value = '40';
                            drawPaper();
                            return;
                        }
                    }
                    selectedShapeId = null;
                    document.getElementById('selectedShape').textContent = '없음';
                    drawPaper();
                });

                canvas.addEventListener('dblclick', (event) => {
                    const point = getCanvasPoint(event);
                    const targetShape = [...shapes].reverse().find(shape => {
                        if (!shapeIsClosed(shape)) return false;
                        if (shape.type === 'freeform' && Array.isArray(shape.points)) {
                            return point.x >= Math.min(...shape.points.map(item => item.x)) - 6 &&
                                point.x <= Math.max(...shape.points.map(item => item.x)) + 6 &&
                                point.y >= Math.min(...shape.points.map(item => item.y)) - 6 &&
                                point.y <= Math.max(...shape.points.map(item => item.y)) + 6;
                        }
                        return point.x >= shape.x && point.x <= shape.x + shape.width &&
                            point.y >= shape.y && point.y <= shape.y + shape.height;
                    });

                    if (!targetShape) return;
                    selectedShapeId = targetShape.id;
                    document.getElementById('selectedShape').textContent = targetShape.id;
                    textEditorShapeId = targetShape.id;
                    const overlay = document.getElementById('textEditorOverlay');
                    const editor = document.getElementById('shapeTextEditor');
                    editor.value = targetShape.text || '';
                    overlay.style.display = 'block';
                    overlay.style.left = `${Math.max(12, targetShape.x * 1.2)}px`;
                    overlay.style.top = `${Math.max(12, targetShape.y * 1.2)}px`;
                    editor.focus();
                    editor.select();
                    drawPaper();
                });

                document.getElementById('shapeTextEditor').addEventListener('input', () => {
                    if (!textEditorShapeId) return;
                    const shape = shapes.find(item => item.id === textEditorShapeId);
                    if (!shape || !shapeIsClosed(shape)) return;
                    const value = document.getElementById('shapeTextEditor').value;
                    distributeTextFlow(textEditorShapeId, value);
                    drawPaper();
                    saveEditorState();
                });

                document.addEventListener('click', (event) => {
                    const overlay = document.getElementById('textEditorOverlay');
                    const editor = document.getElementById('shapeTextEditor');
                    if (textEditorShapeId && overlay && !overlay.contains(event.target) && !event.target.closest('canvas')) {
                        overlay.style.display = 'none';
                        textEditorShapeId = null;
                    }
                    if (event.target === editor) {
                        return;
                    }
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

                function addRecentColor(kind, color) {
                    if (!isHexColor(color) && !isTransparentColor(color)) return;
                    const list = recentColorHistory[kind] || [];
                    const normalized = isTransparentColor(color) ? 'transparent' : color.toLowerCase();
                    const filtered = list.filter(entry => entry && entry.toLowerCase() !== normalized.toLowerCase());
                    filtered.unshift(normalized);
                    recentColorHistory[kind] = filtered.slice(0, 8);
                }

                function updateRecentColorRow(kind) {
                    const container = document.getElementById(kind === 'stroke' ? 'recentStrokeColors' : 'recentFillColors');
                    if (!container) return;
                    const colors = recentColorHistory[kind] || [];
                    container.innerHTML = '';
                    colors.forEach((color) => {
                        const swatch = document.createElement('button');
                        swatch.type = 'button';
                        swatch.className = `recent-color-swatch${isTransparentColor(color) ? ' is-transparent' : ''}`;
                        swatch.title = isTransparentColor(color) ? '투명 / 없음' : `최근 색상: ${color}`;
                        if (!isTransparentColor(color)) {
                            swatch.style.background = color;
                        }
                        swatch.addEventListener('click', () => {
                            const resolved = isTransparentColor(color) ? 'transparent' : color;
                            if (kind === 'stroke') {
                                document.getElementById('defaultStrokeColor').value = normalizeColorForPicker(resolved);
                                defaultStrokeColor = resolved;
                                const shape = shapes.find(s => s.id === selectedShapeId);
                                if (shape) shape.stroke = resolved;
                            } else {
                                document.getElementById('defaultFillColor').value = normalizeColorForPicker(resolved);
                                defaultFillColor = resolved;
                                const shape = shapes.find(s => s.id === selectedShapeId);
                                if (shape && shapeIsClosed(shape)) shape.fill = resolved;
                            }
                            addRecentColor(kind, resolved);
                            updateRecentColorRow(kind);
                            drawPaper();
                            saveEditorState();
                        });
                        container.appendChild(swatch);
                    });
                }

                function setActiveColorInput(kind) {
                    const strokeWrap = document.getElementById('strokeColorWrap');
                    const fillWrap = document.getElementById('fillColorWrap');
                    const isStroke = kind === 'stroke';
                    strokeWrap.classList.toggle('is-active', isStroke);
                    fillWrap.classList.toggle('is-active', !isStroke);
                }

                document.getElementById('defaultStrokeColor').addEventListener('input', () => {
                    defaultStrokeColor = document.getElementById('defaultStrokeColor').value;
                    addRecentColor('stroke', defaultStrokeColor);
                    updateRecentColorRow('stroke');
                    setActiveColorInput('stroke');
                    const shape = shapes.find(s => s.id === selectedShapeId);
                    if (shape) {
                        shape.stroke = defaultStrokeColor;
                    }
                    drawPaper();
                    saveEditorState();
                });

                document.getElementById('defaultFillColor').addEventListener('input', () => {
                    defaultFillColor = document.getElementById('defaultFillColor').value;
                    addRecentColor('fill', defaultFillColor);
                    updateRecentColorRow('fill');
                    setActiveColorInput('fill');
                    const shape = shapes.find(s => s.id === selectedShapeId);
                    if (shape && shapeIsClosed(shape)) {
                        shape.fill = defaultFillColor;
                    }
                    drawPaper();
                    saveEditorState();
                });

                function syncSelectedShapeProperties() {
                    const shape = shapes.find(s => s.id === selectedShapeId);
                    if (!shape) return;
                    document.getElementById('defaultStrokeColor').value = normalizeColorForPicker(defaultStrokeColor);
                    document.getElementById('defaultFillColor').value = normalizeColorForPicker(defaultFillColor);
                    if (selectedShapeId) {
                        const strokeValue = shape.stroke || defaultStrokeColor;
                        const fillValue = shapeIsClosed(shape) && shape.fill && shape.fill !== 'transparent'
                            ? shape.fill
                            : defaultFillColor;
                        document.getElementById('defaultStrokeColor').value = normalizeColorForPicker(strokeValue);
                        document.getElementById('defaultFillColor').value = normalizeColorForPicker(fillValue);
                        defaultStrokeColor = strokeValue;
                        defaultFillColor = fillValue;
                    }
                    updateRecentColorRow('stroke');
                    updateRecentColorRow('fill');
                    setActiveColorInput('stroke');
                }

                updateRecentColorRow('stroke');
                updateRecentColorRow('fill');
                setActiveColorInput('stroke');

                function applyDefaultsToNewShape(shape) {
                    if (!shape) return;
                    shape.stroke = shape.stroke || defaultStrokeColor;
                    if (typeof shape.fill === 'undefined' || shape.fill === null || shape.fill === '') {
                        shape.fill = 'transparent';
                    }
                    if (shape.type === 'freeform') {
                        if (typeof shape.closed === 'undefined') {
                            shape.closed = false;
                        }
                    } else if (typeof shape.closed === 'undefined') {
                        shape.closed = true;
                    }
                    if (shape.type !== 'freeform' && shape.fill && shape.fill !== 'transparent' && shape.fill === defaultFillColor && shape.closed === true) {
                        shape.fill = 'transparent';
                    }
                    return shape;
                }

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

                    if (event.ctrlKey && event.key && event.key.toLowerCase() === 't') {
                        event.preventDefault();
                        event.stopPropagation();
                        toggleTrimTool();
                        return;
                    }

                    if ((event.key === 'Delete' || event.key === 'Backspace') && selectedShapeId) {
                        const idx = shapes.findIndex(shape => shape.id === selectedShapeId);
                        if (idx >= 0) {
                            shapes.splice(idx, 1);
                            selectedShapeId = null;
                            document.getElementById('selectedShape').textContent = '없음';
                            const overlay = document.getElementById('textEditorOverlay');
                            if (overlay) overlay.style.display = 'none';
                            textEditorShapeId = null;
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
