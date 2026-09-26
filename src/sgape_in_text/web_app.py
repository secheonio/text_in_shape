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
                    gap: 6px;
                    flex-wrap: wrap;
                    padding: 8px 10px;
                    background: linear-gradient(180deg, #e5ebf2 0%, #dfe7ee 100%);
                    border-bottom: 1px solid #bac6d3;
                    align-items: center;
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.8);
                }
                .toolbar > * {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0;
                }
                .toolbar label {
                    margin: 0;
                    padding: 0 4px 0 2px;
                    min-height: 30px;
                    line-height: 1.1;
                    font-size: 11px;
                    letter-spacing: 0.01em;
                    font-weight: 700;
                    color: #394a5d;
                    text-transform: none;
                    white-space: nowrap;
                    max-width: 72px;
                    overflow: hidden;
                    text-overflow: ellipsis;
                }
                .paper-compact-group {
                    display: inline-flex;
                    align-items: center;
                    gap: 4px;
                    padding: 4px 5px 4px 4px;
                    border: 1px solid #c1ceda;
                    border-radius: 8px;
                    background: linear-gradient(180deg, #f6faff 0%, #ebf1f7 100%);
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), 0 1px 0 rgba(15, 23, 42, 0.04);
                }
                .paper-compact-icon {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    width: 18px;
                    height: 18px;
                    border-radius: 5px;
                    background: linear-gradient(180deg, #e0ebff 0%, #d4e2ff 100%);
                    border: 1px solid #a8c4f8;
                    color: #1d4ed8;
                    font-size: 11px;
                    font-weight: 700;
                    line-height: 1;
                    padding: 0;
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.7);
                }
                .paper-compact-group .toolbar-select,
                .paper-compact-group .toolbar-input,
                .paper-compact-group .toolbar-button {
                    border: 1px solid #c5d3df;
                    background: linear-gradient(180deg, #fdfefe 0%, #edf3f9 100%);
                    border-radius: 6px;
                    min-height: 26px;
                    height: 26px;
                    line-height: 1.1;
                    padding: 0 7px;
                    font-size: 11px;
                    color: #1f2937;
                }
                .paper-compact-group .toolbar-select {
                    width: 90px;
                    min-width: 90px;
                    padding-right: 18px;
                    appearance: none;
                    background-image: linear-gradient(45deg, transparent 50%, #475569 50%), linear-gradient(135deg, #475569 50%, transparent 50%);
                    background-position: calc(100% - 12px) calc(50% - 2px), calc(100% - 8px) calc(50% - 2px);
                    background-size: 4px 4px, 4px 4px;
                    background-repeat: no-repeat;
                }
                .paper-dimensions {
                    display: inline-flex;
                    align-items: center;
                    gap: 3px;
                }
                .paper-compact-group .toolbar-input {
                    width: 50px;
                    min-width: 50px;
                    padding: 0 5px;
                    text-align: center;
                    font-variant-numeric: tabular-nums;
                }
                .paper-dims-separator {
                    font-size: 10px;
                    color: #64748b;
                    line-height: 1;
                    padding: 0 1px;
                }
                .paper-compact-group .toolbar-button {
                    width: 26px;
                    min-width: 26px;
                    padding: 0;
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 11px;
                    font-weight: 700;
                    color: #1d4ed8;
                }
                .toolbar button,
                .toolbar select,
                .toolbar input {
                    border: 1px solid #b5c2cf;
                    background: linear-gradient(180deg, #f9fbfd 0%, #edf3f8 100%);
                    padding: 5px 10px;
                    border-radius: 6px;
                    cursor: pointer;
                    font-size: 12px;
                    transition: all 0.15s ease;
                    color: #1f2937;
                    min-height: 30px;
                    height: 30px;
                    line-height: 1.1;
                    vertical-align: middle;
                }
                .toolbar button.tool-btn {
                    font-weight: 600;
                    background: linear-gradient(180deg, #f9fbfd 0%, #edf3f8 100%);
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    padding: 0 10px;
                }
                .toolbar button.tool-shape { background: linear-gradient(180deg, #e8f4ff 0%, #d9ecff 100%); border-color: #8fb8e7; }
                .shape-mode-group {
                    display: inline-flex;
                    align-items: center;
                    gap: 3px;
                    padding: 4px 5px;
                    border: 1px solid #c1ceda;
                    border-radius: 8px;
                    background: linear-gradient(180deg, #f3f7fb 0%, #e8edf3 100%);
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), 0 1px 0 rgba(15, 23, 42, 0.04);
                }
                .shape-mode-button,
                .shape-side-btn {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    min-width: 30px;
                    height: 28px;
                    border-radius: 6px;
                    border: 1px solid #c8d3de;
                    background: linear-gradient(180deg, #fdfefe 0%, #edf3f8 100%);
                    color: #1f2937;
                    font-size: 13px;
                    font-weight: 700;
                    cursor: pointer;
                    transition: transform 0.12s ease, box-shadow 0.12s ease, border-color 0.12s ease, background 0.12s ease, filter 0.12s ease;
                    padding: 0 7px;
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), inset 0 -1px 0 rgba(148,163,184,0.14), 0 1px 0 rgba(15,23,42,0.04);
                }
                .shape-mode-button:hover,
                .shape-side-btn:hover {
                    background: linear-gradient(180deg, #ffffff 0%, #f0f6ff 100%);
                    border-color: #9bb8dd;
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.95), 0 1px 2px rgba(59,130,246,0.08), 0 0 0 1px rgba(96,165,250,0.08);
                    transform: translateY(-1px);
                }
                .shape-mode-button[data-shape-kind="arc"]:hover .cad-icon,
                .shape-mode-button[data-shape-kind="line"]:hover .cad-icon,
                .shape-mode-button[data-shape-kind="freeform"]:hover .cad-icon,
                .shape-mode-button[data-shape-kind="polygon"]:hover .cad-icon {
                    transform: scale(1.18);
                }
                .shape-mode-button[data-shape-kind="arc"]:hover .cad-icon { color: #0f766e; }
                .shape-mode-button[data-shape-kind="line"]:hover .cad-icon { color: #2563eb; }
                .shape-mode-button[data-shape-kind="freeform"]:hover .cad-icon { color: #b45309; }
                .shape-mode-button[data-shape-kind="polygon"]:hover .cad-icon { color: #7c3aed; }
                .shape-mode-button[data-shape-kind="arc"].is-active .cad-icon { color: #0f766e; }
                .shape-mode-button[data-shape-kind="line"].is-active .cad-icon { color: #1d4ed8; }
                .shape-mode-button[data-shape-kind="freeform"].is-active .cad-icon { color: #b45309; }
                .shape-mode-button[data-shape-kind="polygon"].is-active .cad-icon { color: #6d28d9; }
                .cad-icon {
                    position: relative;
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    width: 15px;
                    height: 15px;
                    vertical-align: middle;
                    flex-shrink: 0;
                    color: #334155;
                    transition: color 0.12s ease, transform 0.14s ease, filter 0.14s ease;
                }
                .cad-icon svg {
                    display: block;
                    width: 100%;
                    height: 100%;
                    overflow: visible;
                }
                .polygon-pill {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    min-width: 18px;
                    height: 17px;
                    padding: 0 2px;
                    border-radius: 4px;
                    background: linear-gradient(180deg, rgba(59,130,246,0.08), rgba(59,130,246,0.02));
                    border: 1px solid rgba(71,85,105,0.2);
                    color: #24364c;
                    font-size: 10px;
                    line-height: 1;
                    font-weight: 800;
                    letter-spacing: 0.02em;
                    font-variant-numeric: tabular-nums;
                }
                .shape-mode-button.is-active,
                .shape-side-btn.is-active {
                    background: linear-gradient(180deg, #dfeefc 0%, #c9dffb 100%);
                    border-color: #5d9cf7;
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.86), inset 0 -1px 0 rgba(59,130,246,0.1), 0 0 0 1px rgba(59,130,246,0.12), 0 2px 6px rgba(59,130,246,0.16);
                    color: #0f172a;
                    transform: translateY(0);
                }
                .shape-mode-button.is-active .cad-icon,
                .shape-side-btn.is-active .cad-icon,
                .shape-side-btn.is-active .polygon-pill {
                    color: #123a7a;
                    transform: scale(1.04);
                }
                .shape-mode-button:active,
                .shape-side-btn:active {
                    background: linear-gradient(180deg, #d7ebff 0%, #bfd8fb 100%);
                    box-shadow: inset 0 2px 5px rgba(37,99,235,0.14), inset 0 1px 0 rgba(255,255,255,0.75);
                    transform: translateY(1px) scale(0.995);
                }
                .shape-mode-button:focus-visible,
                .shape-side-btn:focus-visible {
                    outline: 2px solid rgba(37,99,235,0.7);
                    outline-offset: 2px;
                }
                .shape-side-picker {
                    display: grid;
                    grid-template-columns: repeat(7, minmax(16px, 1fr));
                    align-items: center;
                    gap: 2px;
                    padding: 4px 5px;
                    border: 1px solid #c1ceda;
                    border-radius: 8px;
                    background: linear-gradient(180deg, #f5f9fc 0%, #e8edf3 100%);
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.9), 0 1px 0 rgba(15, 23, 42, 0.04);
                    max-width: 200px;
                    min-width: 176px;
                }
                .shape-side-btn {
                    width: 100%;
                    min-width: 0;
                    height: 23px;
                    font-size: 10.5px;
                    padding: 0 2px;
                    border-radius: 5px;
                    font-weight: 700;
                    letter-spacing: 0.03em;
                    font-variant-numeric: tabular-nums;
                    background: linear-gradient(180deg, #ffffff 0%, #edf3f8 100%);
                }
                .toolbar button.tool-trim { background: #dcfce7; border-color: #22c55e; font-size: 20px; padding: 7px 12px; min-width: 42px; }
                .toolbar button.tool-object-select {
                    background: linear-gradient(180deg, #eef6ff 0%, #dfeeff 100%);
                    border-color: #7ab0ff;
                    padding: 7px 11px;
                    min-width: 42px;
                }
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
                    width: 100%;
                    height: calc(100vh - 72px);
                    overflow: hidden;
                }
                .canvas-panel {
                    flex: 1 1 auto;
                    width: 100%;
                    min-width: 0;
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
                    position: absolute;
                    right: 18px;
                    top: 18px;
                    width: min(320px, 32vw);
                    min-width: 220px;
                    min-height: 260px;
                    height: 420px;
                    max-width: calc(100% - 32px);
                    max-height: calc(100% - 32px);
                    background: rgba(255,255,255,0.94);
                    border: 1px solid rgba(148, 163, 184, 0.7);
                    border-radius: 12px;
                    padding: 0;
                    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.15);
                    backdrop-filter: blur(8px);
                    z-index: 20;
                    resize: both;
                    overflow: auto;
                    transition: opacity 0.15s ease, transform 0.15s ease;
                }
                .sidebar.is-hidden {
                    display: none;
                }
                .sidebar.is-dragging {
                    user-select: none;
                    cursor: grabbing;
                }
                .property-window-toggle {
                    position: absolute;
                    right: 18px;
                    top: 18px;
                    z-index: 21;
                    display: none;
                    padding: 8px 12px;
                    border-radius: 999px;
                    background: rgba(15, 23, 42, 0.8);
                    color: #fff;
                    border: 1px solid rgba(255,255,255,0.2);
                    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.18);
                    cursor: pointer;
                }
                .property-window-toggle.is-visible {
                    display: inline-flex;
                }
                .sidebar-header {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 12px;
                    padding: 12px 14px 10px;
                    border-bottom: 1px solid rgba(148, 163, 184, 0.55);
                    background: rgba(248, 250, 252, 0.9);
                    cursor: grab;
                    user-select: none;
                }
                .sidebar-header:active {
                    cursor: grabbing;
                }
                .sidebar h3 {
                    margin: 0;
                    font-size: 18px;
                }
                .sidebar-inner {
                    padding: 16px;
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
                <div class="paper-compact-group" aria-label="용지 선택 및 치수">
                    <span class="paper-compact-icon" aria-hidden="true">▣</span>
                    <select id="paperSelect" class="toolbar-select" aria-label="용지 선택">
                        <option value="A4">A4</option>
                        <option value="A5">A5</option>
                        <option value="Letter">Letter</option>
                        <option value="BusinessCard">명함</option>
                        <option value="Custom">사용자 지정</option>
                    </select>
                    <div class="paper-dimensions" aria-label="용지 크기">
                        <input id="customPaperWidth" class="toolbar-input" type="number" min="50" value="210" step="1" placeholder="W" aria-label="가로" />
                        <span class="paper-dims-separator">×</span>
                        <input id="customPaperHeight" class="toolbar-input" type="number" min="50" value="297" step="1" placeholder="H" aria-label="세로" />
                    </div>
                    <button type="button" id="swapPaperOrientation" class="tool-btn tool-apply toolbar-button" title="가로/세로 전환" aria-label="가로 세로 전환">↔</button>
                </div>
                <div class="shape-mode-group" aria-label="도형 선택">
                    <button type="button" class="tool-btn shape-mode-button is-active" data-shape-kind="line" title="직선" aria-label="직선">
                        <span class="cad-icon" aria-hidden="true">
                            <svg viewBox="0 0 16 16" role="img" aria-hidden="true">
                                <path d="M2.5 12.5L12.5 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
                                <path d="M10.5 3.5h2v2" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </span>
                    </button>
                    <button type="button" class="tool-btn shape-mode-button" data-shape-kind="arc" title="원/호" aria-label="원/호">
                        <span class="cad-icon" aria-hidden="true">
                            <svg viewBox="0 0 16 16" role="img" aria-hidden="true">
                                <circle cx="8" cy="8" r="5" fill="none" stroke="currentColor" stroke-width="1.5"/>
                                <path d="M4 11.5A4.5 4.5 0 0 1 11.5 4" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
                                <path d="M8 2v12M2 8h12" fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" opacity="0.75"/>
                            </svg>
                        </span>
                    </button>
                    <button type="button" class="tool-btn shape-mode-button" data-shape-kind="polygon" title="다각형" aria-label="다각형">
                        <span class="cad-icon" aria-hidden="true">
                            <svg viewBox="0 0 16 16" role="img" aria-hidden="true">
                                <path d="M8 2.3L12.8 5.1V10.9L8 13.7L3.2 10.9V5.1L8 2.3Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>
                                <path d="M8 2.3v11.4M3.2 5.1l9.6 5.8M12.8 5.1L3.2 10.9" fill="none" stroke="currentColor" stroke-width="0.9" stroke-linecap="round" opacity="0.6"/>
                            </svg>
                        </span>
                    </button>
                    <button type="button" class="tool-btn shape-mode-button" data-shape-kind="freeform" title="자유형" aria-label="자유형">
                        <span class="cad-icon" aria-hidden="true">
                            <svg viewBox="0 0 16 16" role="img" aria-hidden="true">
                                <path d="M2 10.5C3.1 8.5 4.3 7 5.5 7c1.6 0 2 2.2 3.2 2.2 1.1 0 1.8-1.7 2.9-2.1 1.1-.4 2.4.8 2.4 1.8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M3 12.5H13" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" opacity="0.7"/>
                            </svg>
                        </span>
                    </button>
                </div>
                <div class="shape-side-picker" aria-label="다각형 수 선택">
                    <button type="button" class="shape-side-btn is-active" data-sides="3" title="3각">
                        <span class="polygon-pill">3</span>
                    </button>
                    <button type="button" class="shape-side-btn" data-sides="4" title="4각">
                        <span class="polygon-pill">4</span>
                    </button>
                    <button type="button" class="shape-side-btn" data-sides="5" title="5각">
                        <span class="polygon-pill">5</span>
                    </button>
                    <button type="button" class="shape-side-btn" data-sides="6" title="6각">
                        <span class="polygon-pill">6</span>
                    </button>
                    <button type="button" class="shape-side-btn" data-sides="8" title="8각">
                        <span class="polygon-pill">8</span>
                    </button>
                    <button type="button" class="shape-side-btn" data-sides="12" title="12각">
                        <span class="polygon-pill">12</span>
                    </button>
                    <button type="button" class="shape-side-btn" data-sides="24" title="24각">
                        <span class="polygon-pill">24</span>
                    </button>
                </div>
                <select id="shapeTypeSelect" title="도형 종류" style="display:none;">
                    <option value="line" selected>직선</option>
                    <option value="arc">원/호</option>
                    <option value="freeform">자유형</option>
                    <option value="3">3각</option>
                    <option value="4">4각</option>
                    <option value="5">5각</option>
                    <option value="6">6각</option>
                    <option value="8">8각</option>
                    <option value="12">12각</option>
                    <option value="24">24각</option>
                </select>
                <button type="button" class="tool-btn tool-object-select" data-tool="object-select" title="개체 선택" aria-label="개체 선택">
                    <svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true" style="display:block;">
                        <rect x="2.5" y="2.5" width="11" height="11" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.5"/>
                        <path d="M5.5 2.5v2M10.5 2.5v2M5.5 11.5v2M10.5 11.5v2M2.5 5.5h2M11.5 5.5h2M2.5 10.5h2M11.5 10.5h2" fill="none" stroke="currentColor" stroke-width="0.9" stroke-linecap="round" opacity="0.8"/>
                    </svg>
                </button>
                <button type="button" class="tool-btn tool-trim" data-tool="trim" title="트림" aria-label="트림">✂</button>
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

                    <aside id="propertyWindow" class="sidebar" style="width: 320px; height: 420px; right: 18px; top: 18px; left: auto;">
                        <div class="sidebar-header" aria-label="속성 창 이동">
                            <h3>도형 속성</h3>
                            <button type="button" id="propertyWindowClose" class="tool-btn" style="padding:4px 8px; font-size:12px; min-width:auto;" aria-label="속성 창 닫기">⤢</button>
                        </div>
                        <div class="sidebar-inner">
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
                            <div class="field">
                                <label>회전 (° / +시계, -반시계)</label>
                                <input id="rotationDegrees" type="number" value="0" min="-360" max="360" step="1" aria-label="도형 회전 각도" />
                            </div>
                        </div>
                    </aside>
                </div>
            <script>
                const canvas = document.getElementById('editorCanvas');
                const customPaperWidthInput = document.getElementById('customPaperWidth');
                const customPaperHeightInput = document.getElementById('customPaperHeight');
                const rotationDegreesInput = document.getElementById('rotationDegrees');
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
                const documentModel = {
                    version: 1,
                    id: 'doc-default',
                    paper: { ...currentPaper },
                    view: { zoom: 1, panX: 0, panY: 0 },
                    styles: {
                        stroke: '#222222',
                        fill: '#ffffff',
                        strokeWidth: 1.2,
                        fontFamily: 'Arial',
                        fontSize: 40
                    },
                    layers: [{ id: 'layer-default', name: '기본', visible: true, locked: false, order: 1 }],
                    selections: { selectedIds: [], primaryId: null, bounds: null },
                    shapes: []
                };
                const shapes = [
                    { id: 'shape_1', type: 'polygon', x: 120, y: 140, width: 260, height: 180, sides: 6, text: 'shape in text', fill: 'transparent', stroke: '#222222', closed: true, rotation: 0 }
                ];
                documentModel.shapes = shapes;
                let selectedShapeId = 'shape_1';
                let selectedShapeIds = new Set([selectedShapeId]);
                let currentTool = null;
                let currentEyedropperKind = null;
                let freeDrawingPoints = [];
                let isDrawingFreeform = false;
                let hoverHandleName = null;
                let trimHoverTarget = null;
                let trimDragState = null;
                let dragState = null;
                let objectSelectDragState = null;
                let activeDraftShape = null;
                let paperDragState = null;
                let textEditorShapeId = null;
                const shapeTypeSelect = document.getElementById('shapeTypeSelect');
                const polygonSidesSelect = shapeTypeSelect;
                let polygonSides = Number(shapeTypeSelect.value) || 6;

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

                function getShapeBounds(shape) {
                    if (!shape) return null;
                    if (shape.type === 'freeform' && Array.isArray(shape.points) && shape.points.length) {
                        const xs = shape.points.map(point => point.x);
                        const ys = shape.points.map(point => point.y);
                        return {
                            minX: Math.min(...xs),
                            minY: Math.min(...ys),
                            maxX: Math.max(...xs),
                            maxY: Math.max(...ys)
                        };
                    }
                    if (shape.type === 'line') {
                        const x1 = Number(shape.x) || 0;
                        const y1 = Number(shape.y) || 0;
                        const x2 = Number.isFinite(shape.endX) ? shape.endX : (Number(shape.x) || 0) + (Number(shape.width) || 0);
                        const y2 = Number.isFinite(shape.endY) ? shape.endY : (Number(shape.y) || 0) + (Number(shape.height) || 0);
                        return {
                            minX: Math.min(x1, x2),
                            minY: Math.min(y1, y2),
                            maxX: Math.max(x1, x2),
                            maxY: Math.max(y1, y2)
                        };
                    }
                    const x = Number(shape.x) || 0;
                    const y = Number(shape.y) || 0;
                    const width = Number(shape.width) || 0;
                    const height = Number(shape.height) || 0;
                    return {
                        minX: x,
                        minY: y,
                        maxX: x + width,
                        maxY: y + height
                    };
                }

                function setSelectedShapes(ids) {
                    const nextIds = Array.from(new Set((ids || []).filter(Boolean))).filter(id => shapes.some(shape => shape.id === id));
                    selectedShapeIds = new Set(nextIds);
                    selectedShapeId = nextIds[0] || null;
                    const selectedLabelEl = document.getElementById('selectedShape');
                    if (selectedLabelEl) {
                        selectedLabelEl.textContent = nextIds.length > 1 ? `${nextIds.length}개 선택` : (selectedShapeId || '없음');
                    }
                    if (selectedShapeId) {
                        syncSelectedShapeProperties();
                    }
                }

                function isShapeFullyContainedInRect(shape, rect) {
                    const bounds = getShapeBounds(shape);
                    if (!bounds) return false;
                    const left = Math.min(rect.x1, rect.x2);
                    const right = Math.max(rect.x1, rect.x2);
                    const top = Math.min(rect.y1, rect.y2);
                    const bottom = Math.max(rect.y1, rect.y2);
                    return bounds.minX >= left && bounds.maxX <= right && bounds.minY >= top && bounds.maxY <= bottom;
                }

                function isShapeIntersectsRect(shape, rect) {
                    const bounds = getShapeBounds(shape);
                    if (!bounds) return false;
                    const left = Math.min(rect.x1, rect.x2);
                    const right = Math.max(rect.x1, rect.x2);
                    const top = Math.min(rect.y1, rect.y2);
                    const bottom = Math.max(rect.y1, rect.y2);
                    return !(bounds.maxX < left || bounds.minX > right || bounds.maxY < top || bounds.minY > bottom);
                }

                function getObjectSelectRectFromDrag(startX, startY, endX, endY) {
                    return {
                        x1: startX,
                        y1: startY,
                        x2: endX,
                        y2: endY
                    };
                }

                function normalizeSelectionRect(rect) {
                    const x1 = Math.min(rect.x1, rect.x2);
                    const x2 = Math.max(rect.x1, rect.x2);
                    const y1 = Math.min(rect.y1, rect.y2);
                    const y2 = Math.max(rect.y1, rect.y2);
                    return { x1, y1, x2, y2 };
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
                    const panel = canvas.parentElement;
                    const panelRect = panel ? panel.getBoundingClientRect() : null;
                    const width = Math.max(600, Math.round((panelRect && panelRect.width > 0 ? panelRect.width : window.innerWidth * 0.72)));
                    const height = Math.max(400, Math.round((panelRect && panelRect.height > 0 ? panelRect.height : window.innerHeight * 0.68)));
                    const ratio = Math.min(window.devicePixelRatio || 1, 2);
                    canvas.width = Math.max(1, Math.round(width * ratio));
                    canvas.height = Math.max(1, Math.round(height * ratio));
                    canvas.style.width = `${width}px`;
                    canvas.style.height = `${height}px`;
                    canvas.style.maxHeight = 'none';
                    canvas.style.objectFit = 'fill';
                    if (panel) {
                        panel.style.width = `${width}px`;
                    }
                    if (ctx) {
                        ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
                    }
                }

                function updateCanvasSize() {
                    resizeCanvasToPaper();
                    drawPaper();
                }

                const propertyWindow = document.getElementById('propertyWindow');
                const propertyWindowHeader = propertyWindow ? propertyWindow.querySelector('.sidebar-header') : null;
                const propertyWindowCloseButton = document.getElementById('propertyWindowClose');
                const propertyWindowToggleButton = document.createElement('button');
                propertyWindowToggleButton.type = 'button';
                propertyWindowToggleButton.className = 'property-window-toggle';
                propertyWindowToggleButton.textContent = '속성창 열기';
                propertyWindowToggleButton.setAttribute('aria-label', '속성창 열기');
                propertyWindowToggleButton.setAttribute('aria-expanded', 'true');
                propertyWindowToggleButton.addEventListener('click', () => {
                    if (!propertyWindow) return;
                    const shouldShow = propertyWindow.classList.contains('is-hidden');
                    setPropertyWindowVisible(shouldShow);
                });
                const canvasPanel = document.querySelector('.canvas-panel');
                if (canvasPanel) {
                    canvasPanel.appendChild(propertyWindowToggleButton);
                }

                function setPropertyWindowVisible(visible) {
                    if (!propertyWindow) return;
                    const isVisible = Boolean(visible);
                    propertyWindow.classList.toggle('is-hidden', !isVisible);
                    propertyWindowToggleButton.classList.toggle('is-visible', !isVisible);
                    propertyWindowToggleButton.setAttribute('aria-expanded', String(isVisible));
                    propertyWindowToggleButton.textContent = isVisible ? '속성창 닫기' : '속성창 열기';
                    propertyWindowToggleButton.title = isVisible ? '속성창 닫기' : '속성창 열기';
                }

                if (propertyWindowCloseButton) {
                    propertyWindowCloseButton.addEventListener('click', () => setPropertyWindowVisible(false));
                }

                let propertyWindowDragState = null;

                if (propertyWindowHeader) {
                    propertyWindowHeader.addEventListener('mousedown', (event) => {
                        if (event.target.closest('button')) {
                            return;
                        }
                        const rect = propertyWindow.getBoundingClientRect();
                        propertyWindowDragState = {
                            offsetX: event.clientX - rect.left,
                            offsetY: event.clientY - rect.top,
                        };
                        propertyWindow.classList.add('is-dragging');
                    });
                }

                document.addEventListener('mousemove', (event) => {
                    if (!propertyWindowDragState || !propertyWindow) return;
                    const hostRect = propertyWindow.parentElement.getBoundingClientRect();
                    const left = Math.min(Math.max(event.clientX - hostRect.left - propertyWindowDragState.offsetX, 10), hostRect.width - propertyWindow.offsetWidth - 10);
                    const top = Math.min(Math.max(event.clientY - hostRect.top - propertyWindowDragState.offsetY, 10), hostRect.height - propertyWindow.offsetHeight - 10);
                    propertyWindow.style.left = `${left}px`;
                    propertyWindow.style.top = `${top}px`;
                    propertyWindow.style.right = 'auto';
                });

                document.addEventListener('mouseup', () => {
                    if (propertyWindowDragState) {
                        propertyWindowDragState = null;
                        propertyWindow.classList.remove('is-dragging');
                    }
                });

                function applyPropertyWindowDefaults() {
                    if (!propertyWindow) return;
                    const preferredWidth = Math.min(340, Math.max(260, Math.round((canvasPanel ? canvasPanel.clientWidth : 980) * 0.27)));
                    const preferredHeight = Math.min(460, Math.max(320, Math.round((canvasPanel ? canvasPanel.clientHeight : 720) * 0.62)));
                    propertyWindow.style.width = `${preferredWidth}px`;
                    propertyWindow.style.height = `${preferredHeight}px`;
                    propertyWindow.style.right = '18px';
                    propertyWindow.style.top = '18px';
                    propertyWindow.style.left = 'auto';
                    propertyWindow.classList.remove('is-hidden');
                    propertyWindowToggleButton.classList.remove('is-visible');
                    propertyWindowToggleButton.textContent = '속성창 닫기';
                    propertyWindowToggleButton.title = '속성창 닫기';
                    propertyWindowToggleButton.setAttribute('aria-expanded', 'true');
                }

                const ensurePropertyWindowDefaults = applyPropertyWindowDefaults;

                window.addEventListener('resize', () => {
                    if (!propertyWindow || propertyWindow.classList.contains('is-hidden')) {
                        return;
                    }
                    applyPropertyWindowDefaults();
                    updateCanvasSize();
                });
                ensurePropertyWindowDefaults();

                function shapeIsClosed(shape) {
                    if (!shape || typeof shape !== 'object') return true;
                    if (shape.closed === false) return false;
                    if (shape.type === 'line') return false;
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

                function drawRotationHandle(handle, isActive, isHovered) {
                    const radius = 13;
                    const stroke = isActive ? '#4c1d95' : isHovered ? '#a78bfa' : '#7c3aed';
                    const fill = isActive ? '#7c3aed' : isHovered ? '#ede9fe' : '#ffffff';
                    const baseRing = isActive ? 2.8 : 2.2;

                    ctx.save();
                    ctx.translate(handle.x, handle.y);
                    ctx.strokeStyle = stroke;
                    ctx.fillStyle = fill;
                    ctx.lineWidth = baseRing;

                    ctx.beginPath();
                    ctx.arc(0, 0, radius, -Math.PI * 0.9, Math.PI * 0.9);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.arc(0, 0, radius - 3, -Math.PI * 0.8, Math.PI * 0.8);
                    ctx.stroke();

                    const arrowInfo = [
                        { angle: -Math.PI * 0.5, size: 10, turn: -1 },
                        { angle: Math.PI * 0.5, size: 10, turn: 1 }
                    ];

                    arrowInfo.forEach(({ angle, size, turn }) => {
                        const tipX = Math.cos(angle) * (radius + 6);
                        const tipY = Math.sin(angle) * (radius + 6);
                        const baseX = Math.cos(angle) * radius;
                        const baseY = Math.sin(angle) * radius;
                        const flankX = Math.cos(angle + turn * 0.42) * (radius + 3);
                        const flankY = Math.sin(angle + turn * 0.42) * (radius + 3);

                        ctx.beginPath();
                        ctx.moveTo(baseX, baseY);
                        ctx.lineTo(tipX, tipY);
                        ctx.lineTo(flankX, flankY);
                        ctx.closePath();
                        ctx.fill();
                        ctx.stroke();

                        ctx.beginPath();
                        ctx.moveTo(Math.cos(angle) * (radius - 2), Math.sin(angle) * (radius - 2));
                        ctx.lineTo(Math.cos(angle) * (radius + size), Math.sin(angle) * (radius + size));
                        ctx.stroke();
                    });

                    ctx.beginPath();
                    ctx.arc(0, 0, 3.5, 0, Math.PI * 2);
                    ctx.fillStyle = stroke;
                    ctx.fill();
                    ctx.restore();
                }

                function drawShape(shape) {
                    ctx.strokeStyle = shape.stroke || '#222222';
                    ctx.lineWidth = selectedShapeId === shape.id ? 4 : 2;
                    const center = getShapeCenter(shape);
                    const rotationRadians = ((Number(shape.rotation) || 0) * Math.PI) / 180;

                    ctx.save();
                    ctx.translate(center.x, center.y);
                    ctx.rotate(rotationRadians);
                    ctx.translate(-center.x, -center.y);

                    if (shape.type === 'line') {
                        const x1 = shape.x;
                        const y1 = shape.y;
                        const x2 = Number.isFinite(shape.endX) ? shape.endX : shape.x + shape.width;
                        const y2 = Number.isFinite(shape.endY) ? shape.endY : shape.y + shape.height;
                        ctx.beginPath();
                        ctx.moveTo(x1, y1);
                        ctx.lineTo(x2, y2);
                        ctx.stroke();
                        ctx.restore();
                        return;
                    }

                    if (shape.type === 'arc') {
                        const cx = Number(shape.cx) || (Number(shape.x) || 0) + (Number(shape.width) || 0) / 2;
                        const cy = Number(shape.cy) || (Number(shape.y) || 0) + (Number(shape.height) || 0) / 2;
                        const radius = Number(shape.radius) || Math.max((Number(shape.width) || 0) / 2, 1);
                        const start = Number.isFinite(Number(shape.startAngle)) ? Number(shape.startAngle) : 0;
                        const end = Number.isFinite(Number(shape.endAngle)) ? Number(shape.endAngle) : Math.PI * 2;
                        const sweep = ((end - start + Math.PI * 2) % (Math.PI * 2));
                        ctx.beginPath();
                        ctx.arc(cx, cy, radius, start, start + sweep, false);
                        ctx.stroke();
                        ctx.restore();
                        return;
                    }

                    if (shape.type === 'freeform') {
                        if (shape.points && shape.points.length > 1) {
                            ctx.beginPath();
                            ctx.moveTo(shape.points[0].x, shape.points[0].y);
                            for (let i = 1; i < shape.points.length; i++) {
                                ctx.lineTo(shape.points[i].x, shape.points[i].y);
                            }
                            if (shapeIsClosed(shape) && shape.points.length > 2) {
                                ctx.closePath();
                                const fillColor = shape.fill && shape.fill !== 'transparent' ? shape.fill : 'rgba(34, 197, 94, 0.14)';
                                ctx.fillStyle = fillColor;
                                ctx.fill();
                                ctx.strokeStyle = selectedShapeId === shape.id ? '#15803d' : '#16a34a';
                                ctx.lineWidth = selectedShapeId === shape.id ? 3.6 : 2.8;
                                ctx.stroke();
                            } else {
                                ctx.fillStyle = 'transparent';
                                ctx.stroke();
                            }
                        }
                        ctx.restore();
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

                    ctx.restore();

                    const isSelected = selectedShapeIds.has(shape.id) || selectedShapeId === shape.id;
                    if (isSelected) {
                        const ids = getSelectedShapeIds();
                        const selectionHandles = ids.length > 1 ? getSelectionHandlesForSelection(ids) : getSelectionHandles(shape);
                        const activeHandleName = dragState && dragState.mode !== 'move' && ((dragState.shapeIds && dragState.shapeIds.includes(shape.id)) || dragState.shapeId === shape.id) ? dragState.handle : null;
                        const rotationLineStart = ids.length > 1 ? getSelectionBounds(ids) : getShapeCenter(shape);
                        const rotationLineEnd = selectionHandles.find(handle => handle.name === 'rotation') || rotationLineStart;
                        ctx.beginPath();
                        ctx.moveTo(rotationLineStart.centerX || rotationLineStart.x || 0, rotationLineStart.centerY || rotationLineStart.y || 0);
                        ctx.lineTo(rotationLineEnd.x, rotationLineEnd.y);
                        ctx.strokeStyle = '#0f172a';
                        ctx.lineWidth = 1.4;
                        ctx.setLineDash([5, 5]);
                        ctx.stroke();
                        ctx.setLineDash([]);

                        selectionHandles.forEach(handle => {
                            if (handle.name === 'rotation') {
                                const isHovered = handle.name === hoverHandleName && !activeHandleName;
                                const isActive = handle.name === activeHandleName;
                                drawRotationHandle(handle, isActive, isHovered);
                                return;
                            }

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
                }

                function clampZoom(value) {
                    return Number.isFinite(value) && value > 0 ? value : 0.05;
                }

                function getPaperCenter() {
                    const viewportWidth = canvas.clientWidth || canvas.width;
                    const viewportHeight = canvas.clientHeight || canvas.height;
                    return {
                        x: viewportWidth / 2 + (Number(paperPan.x) || 0),
                        y: viewportHeight / 2 + (Number(paperPan.y) || 0)
                    };
                }

                function getPaperFrame() {
                    const width = currentPaper.width * paperZoom;
                    const height = currentPaper.height * paperZoom;
                    const { x: centerX, y: centerY } = getPaperCenter();
                    return {
                        x: centerX - width / 2,
                        y: centerY - height / 2,
                        width,
                        height,
                        centerX,
                        centerY
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
                    const x = event.clientX - rect.left;
                    const y = event.clientY - rect.top;
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
                        if (shape.type === 'freeform' && shape.points) {
                            const hit = shape.points.some(vertex => Math.abs(vertex.x - point.x) <= 6 && Math.abs(vertex.y - point.y) <= 6);
                            if (hit) {
                                return shape;
                            }
                            continue;
                        }

                        const minX = shape.type === 'line'
                            ? Math.min(shape.x, Number.isFinite(shape.endX) ? shape.endX : shape.x + shape.width)
                            : shape.x;
                        const maxX = shape.type === 'line'
                            ? Math.max(shape.x, Number.isFinite(shape.endX) ? shape.endX : shape.x + shape.width)
                            : shape.x + shape.width;
                        const minY = shape.type === 'line'
                            ? Math.min(shape.y, Number.isFinite(shape.endY) ? shape.endY : shape.y + shape.height)
                            : shape.y;
                        const maxY = shape.type === 'line'
                            ? Math.max(shape.y, Number.isFinite(shape.endY) ? shape.endY : shape.y + shape.height)
                            : shape.y + shape.height;
                        const withinBounds = point.x >= minX && point.x <= maxX && point.y >= minY && point.y <= maxY;
                        if (withinBounds) {
                            return shape;
                        }
                    }
                    return null;
                }

                function isPointInShape(shape, point) {
                    if (!shape || !point) return false;

                    if (shape.type === 'freeform' && Array.isArray(shape.points) && shape.points.length > 1) {
                        return shape.points.some(vertex => Math.abs(vertex.x - point.x) <= 6 && Math.abs(vertex.y - point.y) <= 6);
                    }

                    if (shape.type === 'line') {
                        const x2 = Number.isFinite(shape.endX) ? shape.endX : shape.x + shape.width;
                        const y2 = Number.isFinite(shape.endY) ? shape.endY : shape.y + shape.height;
                        const a = { x: shape.x, y: shape.y };
                        const b = { x: x2, y: y2 };
                        return pointToSegmentDistance(point, a, b) <= 8;
                    }

                    if (shape.type === 'circle' || shape.type === 'ellipse') {
                        const cx = shape.x + shape.width / 2;
                        const cy = shape.y + shape.height / 2;
                        const rx = Math.max(shape.width / 2, 1);
                        const ry = Math.max(shape.height / 2, 1);
                        const dx = point.x - cx;
                        const dy = point.y - cy;
                        return (dx * dx) / (rx * rx) + (dy * dy) / (ry * ry) <= 1;
                    }

                    const vertices = getShapeVertices(shape);
                    let inside = false;
                    for (let i = 0, j = vertices.length - 1; i < vertices.length; j = i++) {
                        const vi = vertices[i];
                        const vj = vertices[j];
                        const intersect = ((vi.y > point.y) !== (vj.y > point.y)) &&
                            (point.x < (vj.x - vi.x) * (point.y - vi.y) / (vj.y - vi.y + Number.EPSILON) + vi.x);
                        if (intersect) inside = !inside;
                    }
                    return inside;
                }

                function getObjectSelectTarget(point) {
                    const borderCandidate = [...shapes].reverse().find(shape => getShapeBorderHit(shape, point));
                    if (borderCandidate) return borderCandidate;
                    return [...shapes].reverse().find(shape => isPointInShape(shape, point)) || null;
                }

                function toggleObjectSelectionAtPoint(point, event) {
                    if (!point || typeof point.x !== 'number' || typeof point.y !== 'number') {
                        return false;
                    }

                    const target = getObjectSelectTarget(point);
                    if (!target) {
                        if (!(event && event.shiftKey)) {
                            setSelectedShapes([]);
                        }
                        return false;
                    }

                    const nextIds = new Set(selectedShapeIds);
                    if (event && event.shiftKey) {
                        if (nextIds.has(target.id)) {
                            nextIds.delete(target.id);
                        } else {
                            nextIds.add(target.id);
                        }
                        setSelectedShapes(Array.from(nextIds));
                        return true;
                    }

                    setSelectedShapes([target.id]);
                    return true;
                }

                function selectObjectAtPoint(point, event) {
                    return toggleObjectSelectionAtPoint(point, event || null);
                }

                function getShapeCenter(shape) {
                    if (!shape) return { x: 0, y: 0 };
                    if (Number.isFinite(Number(shape.cx)) && Number.isFinite(Number(shape.cy))) {
                        return { x: Number(shape.cx), y: Number(shape.cy) };
                    }
                    const x = Number(shape.x) || 0;
                    const y = Number(shape.y) || 0;
                    const width = Number(shape.width) || 0;
                    const height = Number(shape.height) || 0;
                    return { x: x + width / 2, y: y + height / 2 };
                }

                function createLineShape(startPoint, endPoint, overrides = {}) {
                    const sx = Number(startPoint.x) || 0;
                    const sy = Number(startPoint.y) || 0;
                    const ex = Number(endPoint.x) || 0;
                    const ey = Number(endPoint.y) || 0;
                    return applyDefaultsToNewShape({
                        id: `shape_${Date.now()}_${Math.random().toString(16).slice(2, 7)}`,
                        type: 'line',
                        x: sx,
                        y: sy,
                        width: ex - sx,
                        height: ey - sy,
                        endX: ex,
                        endY: ey,
                        fill: 'transparent',
                        stroke: defaultStrokeColor,
                        closed: false,
                        rotation: 0,
                        ...overrides
                    });
                }

                function createCircleShape(center, radius, overrides = {}) {
                    const cx = Number(center.x) || 0;
                    const cy = Number(center.y) || 0;
                    const r = Math.max(2, Number(radius) || 0);
                    return applyDefaultsToNewShape({
                        id: `shape_${Date.now()}_${Math.random().toString(16).slice(2, 7)}`,
                        type: 'circle',
                        x: cx - r,
                        y: cy - r,
                        width: r * 2,
                        height: r * 2,
                        fill: 'transparent',
                        stroke: defaultStrokeColor,
                        closed: true,
                        rotation: 0,
                        cx,
                        cy,
                        radius: r,
                        ...overrides
                    });
                }

                function createArcShape(center, radius, startAngle, endAngle, overrides = {}) {
                    const cx = Number(center.x) || 0;
                    const cy = Number(center.y) || 0;
                    const r = Math.max(2, Number(radius) || 0);
                    const start = Number(startAngle) || 0;
                    const end = Number(endAngle) || 0;
                    return applyDefaultsToNewShape({
                        id: `shape_${Date.now()}_${Math.random().toString(16).slice(2, 7)}`,
                        type: 'arc',
                        cx,
                        cy,
                        radius: r,
                        startAngle: start,
                        endAngle: end,
                        x: cx - r,
                        y: cy - r,
                        width: r * 2,
                        height: r * 2,
                        fill: 'transparent',
                        stroke: defaultStrokeColor,
                        closed: false,
                        rotation: 0,
                        ...overrides
                    });
                }

                function createPolylineShape(points, overrides = {}) {
                    const validPoints = (Array.isArray(points) ? points : []).filter(point => point && Number.isFinite(point.x) && Number.isFinite(point.y));
                    if (!validPoints.length) return null;
                    return applyDefaultsToNewShape({
                        id: `shape_${Date.now()}_${Math.random().toString(16).slice(2, 7)}`,
                        type: 'freeform',
                        points: validPoints,
                        closed: false,
                        fill: 'transparent',
                        stroke: defaultStrokeColor,
                        rotation: 0,
                        ...overrides
                    });
                }

                function rotatePoint(point, center, angleRadians) {
                    const dx = point.x - center.x;
                    const dy = point.y - center.y;
                    const cos = Math.cos(angleRadians);
                    const sin = Math.sin(angleRadians);
                    return {
                        x: center.x + dx * cos - dy * sin,
                        y: center.y + dx * sin + dy * cos
                    };
                }

                function getShapeVertices(shape) {
                    if (shape.type === 'line') {
                        const x2 = Number.isFinite(shape.endX) ? shape.endX : shape.x + shape.width;
                        const y2 = Number.isFinite(shape.endY) ? shape.endY : shape.y + shape.height;
                        return [
                            { x: shape.x, y: shape.y },
                            { x: x2, y: y2 }
                        ];
                    }

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

                const TRIM_EDGE_SNAP_DISTANCE = 12;

                function pointOnSegment(point, a, b, tolerance = TRIM_EDGE_SNAP_DISTANCE) {
                    const dist = pointToSegmentDistance(point, a, b);
                    return dist <= tolerance;
                }

                function nearestPointOnSegment(point, a, b) {
                    const dx = b.x - a.x;
                    const dy = b.y - a.y;
                    if (dx === 0 && dy === 0) {
                        return { x: a.x, y: a.y };
                    }
                    const t = Math.max(0, Math.min(1, ((point.x - a.x) * dx + (point.y - a.y) * dy) / (dx * dx + dy * dy)));
                    return {
                        x: a.x + t * dx,
                        y: a.y + t * dy
                    };
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

                function getSelectedShapeIds() {
                    const ids = selectedShapeIds.size > 0
                        ? Array.from(selectedShapeIds)
                        : selectedShapeId
                            ? [selectedShapeId]
                            : [];
                    return ids.filter(id => shapes.some(shape => shape.id === id));
                }

                function getSelectionBounds(ids) {
                    const validIds = Array.from(new Set((ids || []).filter(Boolean))).filter(id => shapes.some(shape => shape.id === id));
                    if (!validIds.length) {
                        return null;
                    }

                    const bounds = validIds
                        .map(id => shapes.find(shape => shape.id === id))
                        .filter(Boolean)
                        .map(shape => getShapeBounds(shape))
                        .filter(Boolean)
                        .reduce((acc, current) => ({
                            minX: Math.min(acc.minX, current.minX),
                            minY: Math.min(acc.minY, current.minY),
                            maxX: Math.max(acc.maxX, current.maxX),
                            maxY: Math.max(acc.maxY, current.maxY)
                        }), { minX: Infinity, minY: Infinity, maxX: -Infinity, maxY: -Infinity });

                    if (!Number.isFinite(bounds.minX) || !Number.isFinite(bounds.minY)) {
                        return null;
                    }

                    const width = bounds.maxX - bounds.minX;
                    const height = bounds.maxY - bounds.minY;
                    return {
                        minX: bounds.minX,
                        minY: bounds.minY,
                        maxX: bounds.maxX,
                        maxY: bounds.maxY,
                        width,
                        height,
                        centerX: bounds.minX + width / 2,
                        centerY: bounds.minY + height / 2
                    };
                }

                function getSelectionHandles(shape) {
                    const handleSize = 12;
                    const hitRadius = 18;
                    const center = getShapeCenter(shape);
                    const rotationRadians = ((Number(shape.rotation) || 0) * Math.PI) / 180;
                    const baseHandles = [
                        { name: 'nw', x: shape.x, y: shape.y },
                        { name: 'n', x: shape.x + shape.width / 2, y: shape.y },
                        { name: 'ne', x: shape.x + shape.width, y: shape.y },
                        { name: 'w', x: shape.x, y: shape.y + shape.height / 2 },
                        { name: 'e', x: shape.x + shape.width, y: shape.y + shape.height / 2 },
                        { name: 'sw', x: shape.x, y: shape.y + shape.height },
                        { name: 's', x: shape.x + shape.width / 2, y: shape.y + shape.height },
                        { name: 'se', x: shape.x + shape.width, y: shape.y + shape.height }
                    ].map(point => ({
                        ...rotatePoint(point, center, rotationRadians),
                        name: point.name,
                        size: handleSize,
                        hitRadius
                    }));

                    const rotationOffsetY = -Math.max(shape.width, shape.height) * 0.65 - 24;
                    const rotationHandle = rotatePoint({
                        x: center.x,
                        y: center.y + rotationOffsetY
                    }, center, rotationRadians);

                    return [
                        ...baseHandles,
                        { name: 'rotation', x: rotationHandle.x, y: rotationHandle.y, size: handleSize, hitRadius }
                    ];
                }

                function getSelectionHandlesForSelection(ids) {
                    const bounds = getSelectionBounds(ids);
                    if (!bounds) {
                        return [];
                    }

                    const handleSize = 12;
                    const hitRadius = 18;
                    const baseHandles = [
                        { name: 'nw', x: bounds.minX, y: bounds.minY },
                        { name: 'n', x: bounds.centerX, y: bounds.minY },
                        { name: 'ne', x: bounds.maxX, y: bounds.minY },
                        { name: 'w', x: bounds.minX, y: bounds.centerY },
                        { name: 'e', x: bounds.maxX, y: bounds.centerY },
                        { name: 'sw', x: bounds.minX, y: bounds.maxY },
                        { name: 's', x: bounds.centerX, y: bounds.maxY },
                        { name: 'se', x: bounds.maxX, y: bounds.maxY }
                    ].map(point => ({ ...point, size: handleSize, hitRadius }));

                    const rotationHandleY = bounds.minY - Math.max(bounds.width, bounds.height) * 0.65 - 24;
                    return [
                        ...baseHandles,
                        { name: 'rotation', x: bounds.centerX, y: rotationHandleY, size: handleSize, hitRadius }
                    ];
                }

                function getResizeHandles(shape) {
                    return getSelectionHandles(shape);
                }

                function isResizeHandleHit(shape, point) {
                    const handles = getSelectionHandles(shape);
                    const hit = handles.find(handle =>
                        Math.abs(point.x - handle.x) <= handle.hitRadius &&
                        Math.abs(point.y - handle.y) <= handle.hitRadius
                    );
                    return hit ? hit.name : null;
                }

                function getGroupResizeHandleHit(ids, point) {
                    const handles = getSelectionHandlesForSelection(ids);
                    const hit = handles.find(handle =>
                        Math.abs(point.x - handle.x) <= handle.hitRadius &&
                        Math.abs(point.y - handle.y) <= handle.hitRadius
                    );
                    return hit ? hit.name : null;
                }

                function getEffectiveSelectionHandles() {
                    const ids = getSelectedShapeIds();
                    if (ids.length > 1) {
                        return getSelectionHandlesForSelection(ids);
                    }
                    const primary = ids[0] ? shapes.find(shape => shape.id === ids[0]) : null;
                    return primary ? getSelectionHandles(primary) : [];
                }

                function getEffectiveHandleHit(point) {
                    const ids = getSelectedShapeIds();
                    if (ids.length > 1) {
                        return getGroupResizeHandleHit(ids, point);
                    }
                    const primary = ids[0] ? shapes.find(shape => shape.id === ids[0]) : null;
                    return primary ? isResizeHandleHit(primary, point) : null;
                }

                function resizeSelectionGroupFromHandle(selectionIds, handleName, dx, dy, originalBounds) {
                    const bounds = originalBounds || getSelectionBounds(selectionIds);
                    if (!bounds) {
                        return {};
                    }

                    const nextBounds = { ...bounds };
                    const minSize = 10;
                    switch (handleName) {
                        case 'nw':
                            nextBounds.minX = Math.min(bounds.minX + dx, bounds.maxX - minSize);
                            nextBounds.minY = Math.min(bounds.minY + dy, bounds.maxY - minSize);
                            break;
                        case 'n':
                            nextBounds.minY = Math.min(bounds.minY + dy, bounds.maxY - minSize);
                            break;
                        case 'ne':
                            nextBounds.minY = Math.min(bounds.minY + dy, bounds.maxY - minSize);
                            nextBounds.maxX = Math.max(bounds.minX + minSize, bounds.maxX + dx);
                            break;
                        case 'w':
                            nextBounds.minX = Math.min(bounds.minX + dx, bounds.maxX - minSize);
                            break;
                        case 'e':
                            nextBounds.maxX = Math.max(bounds.minX + minSize, bounds.maxX + dx);
                            break;
                        case 'sw':
                            nextBounds.minX = Math.min(bounds.minX + dx, bounds.maxX - minSize);
                            nextBounds.maxY = Math.max(bounds.minY + minSize, bounds.maxY + dy);
                            break;
                        case 's':
                            nextBounds.maxY = Math.max(bounds.minY + minSize, bounds.maxY + dy);
                            break;
                        case 'se':
                            nextBounds.maxX = Math.max(bounds.minX + minSize, bounds.maxX + dx);
                            nextBounds.maxY = Math.max(bounds.minY + minSize, bounds.maxY + dy);
                            break;
                        default:
                            return {};
                    }

                    const nextWidth = Math.max(1, nextBounds.maxX - nextBounds.minX);
                    const nextHeight = Math.max(1, nextBounds.maxY - nextBounds.minY);
                    const oldWidth = Math.max(1, bounds.width);
                    const oldHeight = Math.max(1, bounds.height);

                    const edited = {};
                    for (const id of selectionIds) {
                        const shape = shapes.find(item => item.id === id);
                        if (!shape) continue;
                        const original = shape;
                        const originalBoundsForShape = getShapeBounds(original);
                        const relX = oldWidth > 0 ? (originalBoundsForShape.minX - bounds.minX) / oldWidth : 0;
                        const relY = oldHeight > 0 ? (originalBoundsForShape.minY - bounds.minY) / oldHeight : 0;
                        const relRight = oldWidth > 0 ? (originalBoundsForShape.maxX - bounds.minX) / oldWidth : 1;
                        const relBottom = oldHeight > 0 ? (originalBoundsForShape.maxY - bounds.minY) / oldHeight : 1;
                        const scaledMinX = nextBounds.minX + relX * nextWidth;
                        const scaledMinY = nextBounds.minY + relY * nextHeight;
                        const scaledMaxX = nextBounds.minX + relRight * nextWidth;
                        const scaledMaxY = nextBounds.minY + relBottom * nextHeight;
                        const targetWidth = Math.max(1, scaledMaxX - scaledMinX);
                        const targetHeight = Math.max(1, scaledMaxY - scaledMinY);

                        if (original.type === 'line') {
                            const x2 = Number.isFinite(original.endX) ? original.endX : original.x + original.width;
                            const y2 = Number.isFinite(original.endY) ? original.endY : original.y + original.height;
                            const lineBounds = getShapeBounds(original);
                            const lineRelX1 = oldWidth > 0 ? (original.x - bounds.minX) / oldWidth : 0;
                            const lineRelY1 = oldHeight > 0 ? (original.y - bounds.minY) / oldHeight : 0;
                            const lineRelX2 = oldWidth > 0 ? (x2 - bounds.minX) / oldWidth : 1;
                            const lineRelY2 = oldHeight > 0 ? (y2 - bounds.minY) / oldHeight : 1;
                            const targetX1 = nextBounds.minX + lineRelX1 * nextWidth;
                            const targetY1 = nextBounds.minY + lineRelY1 * nextHeight;
                            const targetX2 = nextBounds.minX + lineRelX2 * nextWidth;
                            const targetY2 = nextBounds.minY + lineRelY2 * nextHeight;
                            original.x = targetX1;
                            original.y = targetY1;
                            original.width = Math.max(1, targetX2 - targetX1);
                            original.height = Math.max(1, targetY2 - targetY1);
                            original.endX = targetX2;
                            original.endY = targetY2;
                        } else {
                            original.x = scaledMinX;
                            original.y = scaledMinY;
                            original.width = targetWidth;
                            original.height = targetHeight;
                        }

                        edited[id] = original;
                    }

                    return edited;
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

                function drawTrimCutGuide(ctx2d, target, offsetX, offsetY, zoom) {
                    if (!target || !target.segment || !target.point || !target.intersection) return;

                    const segmentA = {
                        x: target.segment.a.x * zoom + offsetX,
                        y: target.segment.a.y * zoom + offsetY
                    };
                    const segmentB = {
                        x: target.segment.b.x * zoom + offsetX,
                        y: target.segment.b.y * zoom + offsetY
                    };
                    const cutStart = {
                        x: target.point.x * zoom + offsetX,
                        y: target.point.y * zoom + offsetY
                    };
                    const cutEnd = {
                        x: target.intersection.x * zoom + offsetX,
                        y: target.intersection.y * zoom + offsetY
                    };

                    const vertices = Array.isArray(target.shape && target.shape.points)
                        ? target.shape.points
                        : getShapeVertices(target.shape);
                    const referenceCenter = vertices.length
                        ? vertices.reduce((sum, vertex) => ({ x: sum.x + vertex.x, y: sum.y + vertex.y }), { x: 0, y: 0 })
                        : { x: 0, y: 0 };
                    const polygonCenter = vertices.length
                        ? { x: referenceCenter.x / vertices.length, y: referenceCenter.y / vertices.length }
                        : { x: (cutStart.x + cutEnd.x) / 2, y: (cutStart.y + cutEnd.y) / 2 };

                    const dirX = cutEnd.x - cutStart.x;
                    const dirY = cutEnd.y - cutStart.y;
                    const dirLength = Math.hypot(dirX, dirY) || 1;
                    const normalX = -dirY / dirLength;
                    const normalY = dirX / dirLength;
                    const stripWidth = 18;
                    const keepSide = lineSide(polygonCenter, { x: cutStart.x, y: cutStart.y }, { x: cutEnd.x, y: cutEnd.y }) >= 0 ? 1 : -1;
                    const keepOffset = { x: normalX * keepSide * stripWidth, y: normalY * keepSide * stripWidth };
                    const cutOffset = { x: normalX * -keepSide * stripWidth, y: normalY * -keepSide * stripWidth };
                    const keepStart = { x: cutStart.x + keepOffset.x, y: cutStart.y + keepOffset.y };
                    const keepEnd = { x: cutEnd.x + keepOffset.x, y: cutEnd.y + keepOffset.y };
                    const cutStartOffset = { x: cutStart.x + cutOffset.x, y: cutStart.y + cutOffset.y };
                    const cutEndOffset = { x: cutEnd.x + cutOffset.x, y: cutEnd.y + cutOffset.y };
                    const angle = Math.atan2(dirY, dirX);
                    const arrowSize = 10;

                    ctx2d.save();
                    ctx2d.lineCap = 'round';
                    ctx2d.lineJoin = 'round';

                    ctx2d.fillStyle = keepSide >= 0 ? 'rgba(34, 197, 94, 0.18)' : 'rgba(239, 68, 68, 0.18)';
                    ctx2d.strokeStyle = keepSide >= 0 ? '#16a34a' : '#dc2626';
                    ctx2d.lineWidth = 1.5;
                    ctx2d.beginPath();
                    ctx2d.moveTo(cutStart.x, cutStart.y);
                    ctx2d.lineTo(cutEnd.x, cutEnd.y);
                    ctx2d.lineTo(keepEnd.x, keepEnd.y);
                    ctx2d.lineTo(keepStart.x, keepStart.y);
                    ctx2d.closePath();
                    ctx2d.fill();
                    ctx2d.stroke();

                    ctx2d.fillStyle = keepSide >= 0 ? 'rgba(239, 68, 68, 0.1)' : 'rgba(34, 197, 94, 0.1)';
                    ctx2d.strokeStyle = keepSide >= 0 ? '#dc2626' : '#16a34a';
                    ctx2d.beginPath();
                    ctx2d.moveTo(cutStart.x, cutStart.y);
                    ctx2d.lineTo(cutEnd.x, cutEnd.y);
                    ctx2d.lineTo(cutEndOffset.x, cutEndOffset.y);
                    ctx2d.lineTo(cutStartOffset.x, cutStartOffset.y);
                    ctx2d.closePath();
                    ctx2d.fill();
                    ctx2d.stroke();

                    ctx2d.shadowColor = keepSide >= 0 ? 'rgba(34, 197, 94, 0.6)' : 'rgba(239, 68, 68, 0.6)';
                    ctx2d.shadowBlur = 14;
                    ctx2d.strokeStyle = keepSide >= 0 ? '#22c55e' : '#ef4444';
                    ctx2d.lineWidth = 6;
                    ctx2d.beginPath();
                    ctx2d.moveTo(segmentA.x, segmentA.y);
                    ctx2d.lineTo(segmentB.x, segmentB.y);
                    ctx2d.stroke();

                    ctx2d.shadowBlur = 0;
                    ctx2d.strokeStyle = '#0f172a';
                    ctx2d.lineWidth = 1.1;
                    ctx2d.setLineDash([6, 5]);
                    ctx2d.beginPath();
                    ctx2d.moveTo(cutStart.x, cutStart.y);
                    ctx2d.lineTo(cutEnd.x, cutEnd.y);
                    ctx2d.stroke();
                    ctx2d.setLineDash([]);

                    ctx2d.fillStyle = '#0f172a';
                    ctx2d.beginPath();
                    ctx2d.moveTo(cutEnd.x, cutEnd.y);
                    ctx2d.lineTo(
                        cutEnd.x - arrowSize * Math.cos(angle - Math.PI / 6),
                        cutEnd.y - arrowSize * Math.sin(angle - Math.PI / 6)
                    );
                    ctx2d.lineTo(
                        cutEnd.x - arrowSize * Math.cos(angle + Math.PI / 6),
                        cutEnd.y - arrowSize * Math.sin(angle + Math.PI / 6)
                    );
                    ctx2d.closePath();
                    ctx2d.fill();

                    ctx2d.strokeStyle = keepSide >= 0 ? '#22c55e' : '#ef4444';
                    ctx2d.lineWidth = 2.2;
                    ctx2d.beginPath();
                    ctx2d.moveTo(cutStart.x, cutStart.y);
                    ctx2d.lineTo(cutEnd.x, cutEnd.y);
                    ctx2d.stroke();

                    const keepLabelX = cutStart.x + dirX * 0.5 + normalX * (keepSide >= 0 ? 16 : -16);
                    const keepLabelY = cutStart.y + dirY * 0.5 + normalY * (keepSide >= 0 ? 16 : -16);
                    const cutLabelX = cutStart.x + dirX * 0.5 + normalX * (keepSide >= 0 ? -16 : 16);
                    const cutLabelY = cutStart.y + dirY * 0.5 + normalY * (keepSide >= 0 ? -16 : 16);

                    ctx2d.font = 'bold 11px sans-serif';
                    ctx2d.fillStyle = keepSide >= 0 ? '#15803d' : '#b91c1c';
                    ctx2d.fillText('KEEP', keepLabelX, keepLabelY);
                    ctx2d.fillStyle = keepSide >= 0 ? '#b91c1c' : '#15803d';
                    ctx2d.fillText('CUT', cutLabelX, cutLabelY);

                    ctx2d.restore();
                }

                function drawPaper() {
                    normalizePaperState();
                    const viewportWidth = canvas.clientWidth || canvas.width;
                    const viewportHeight = canvas.clientHeight || canvas.height;
                    ctx.setTransform(window.devicePixelRatio || 1, 0, 0, window.devicePixelRatio || 1, 0, 0);
                    ctx.clearRect(0, 0, viewportWidth, viewportHeight);
                    ctx.fillStyle = '#e5e7eb';
                    ctx.fillRect(0, 0, viewportWidth, viewportHeight);

                    const gridSize = 24 * paperZoom;
                    const { x: originX, y: originY } = getPaperCenter();
                    ctx.strokeStyle = 'rgba(148, 163, 184, 0.42)';
                    ctx.lineWidth = 1;
                    for (let x = Math.floor((originX % gridSize) - gridSize); x <= viewportWidth + gridSize; x += gridSize) {
                        ctx.beginPath();
                        ctx.moveTo(x, 0);
                        ctx.lineTo(x, viewportHeight);
                        ctx.stroke();
                    }
                    for (let y = Math.floor((originY % gridSize) - gridSize); y <= viewportHeight + gridSize; y += gridSize) {
                        ctx.beginPath();
                        ctx.moveTo(0, y);
                        ctx.lineTo(viewportWidth, y);
                        ctx.stroke();
                    }

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
                        drawTrimCutGuide(ctx, trimHoverTarget, paperX, paperY, paperZoom);
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
                    const selectedPaperName = (currentPaper && currentPaper.label && currentPaper.label !== 'Custom')
                        ? currentPaper.label
                        : paperSelect.value;
                    const currentWidth = Number(customPaperWidthInput.value || 210);
                    const currentHeight = Number(customPaperHeightInput.value || 297);
                    const swappedWidth = currentHeight;
                    const swappedHeight = currentWidth;

                    customPaperWidthInput.value = swappedWidth;
                    customPaperHeightInput.value = swappedHeight;
                    isLandscapeMode = swappedWidth >= swappedHeight;

                    if (selectedPaperName && selectedPaperName !== 'Custom') {
                        const preset = PAPER_MM[selectedPaperName] || paperSizes[selectedPaperName];
                        if (preset) {
                            paperSelect.value = selectedPaperName;
                            currentPaper = {
                                width: mmToPixel(swappedWidth),
                                height: mmToPixel(swappedHeight),
                                label: selectedPaperName
                            };
                            clampPaperPan();
                            resizeCanvasToPaper();
                            drawPaper();
                            updateOrientationButton();
                            saveEditorState();
                            return;
                        }
                    }

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
                    const effectiveToolName = toolName === 'shape' && ['circle', 'line', 'freeform', 'polygon'].includes(currentTool)
                        ? 'shape'
                        : toolName;
                    document.querySelectorAll('.tool-btn').forEach((button) => {
                        const isActive = button.dataset.tool === effectiveToolName;
                        button.classList.toggle('is-active', isActive);
                    });
                    document.querySelectorAll('.shape-mode-button').forEach((button) => {
                        const isActive = currentTool && button.dataset.shapeKind === currentTool;
                        button.classList.toggle('is-active', isActive);
                    });
                    document.querySelectorAll('.shape-side-btn').forEach((button) => {
                        const isActive = currentTool === 'polygon' && Number(button.dataset.sides) === Number(polygonSides);
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

                    if (shape.type === 'line') {
                        const x2 = Number.isFinite(shape.endX) ? shape.endX : shape.x + shape.width;
                        const y2 = Number.isFinite(shape.endY) ? shape.endY : shape.y + shape.height;
                        return [{
                            a: { x: shape.x, y: shape.y },
                            b: { x: x2, y: y2 }
                        }];
                    }

                    if (shape.type === 'freeform' && Array.isArray(shape.points) && shape.points.length > 1) {
                        return shape.points.slice(1).map((point, index) => ({
                            a: shape.points[index],
                            b: point
                        }));
                    }

                    if (shape.type === 'arc') {
                        const cx = Number(shape.cx) || (Number(shape.x) || 0) + (Number(shape.width) || 0) / 2;
                        const cy = Number(shape.cy) || (Number(shape.y) || 0) + (Number(shape.height) || 0) / 2;
                        const radius = Number(shape.radius) || Math.max((Number(shape.width) || 0) / 2, 2);
                        const start = Number.isFinite(Number(shape.startAngle)) ? Number(shape.startAngle) : 0;
                        const end = Number.isFinite(Number(shape.endAngle)) ? Number(shape.endAngle) : Math.PI * 2;
                        const span = ((end - start + Math.PI * 2) % (Math.PI * 2));
                        const segments = [];
                        const sampleCount = Math.max(12, Math.ceil(span / (Math.PI / 18)));
                        for (let index = 0; index < sampleCount; index++) {
                            const a = start + (span * index) / sampleCount;
                            const b = start + (span * (index + 1)) / sampleCount;
                            segments.push({
                                a: { x: cx + Math.cos(a) * radius, y: cy + Math.sin(a) * radius },
                                b: { x: cx + Math.cos(b) * radius, y: cy + Math.sin(b) * radius }
                            });
                        }
                        return segments;
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

                    const projected = nearestPointOnSegment(point, segment.a, segment.b);
                    const distToSegment = Math.hypot(point.x - projected.x, point.y - projected.y);
                    if (distToSegment > TRIM_EDGE_SNAP_DISTANCE * 2) return false;

                    for (const other of shapes) {
                        if (other.id === shape.id) continue;
                        for (const otherSegment of getShapeSegments(other)) {
                            const hit = segmentIntersection(segment.a, segment.b, otherSegment.a, otherSegment.b);
                            if (!hit) continue;

                            const hitDistanceToProjected = Math.hypot(hit.x - projected.x, hit.y - projected.y);
                            if (hitDistanceToProjected > MAX_TRIM_NEIGHBOR_DISTANCE) continue;

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

                        const projected = nearestPointOnSegment(point, segment.a, segment.b);
                        const intersections = [];
                        for (const other of shapes) {
                            if (other.id === trimShape.id) continue;
                            for (const otherSegment of getShapeSegments(other)) {
                                const hit = segmentIntersection(segment.a, segment.b, otherSegment.a, otherSegment.b);
                                if (!hit) continue;

                                const hitDistanceToProjected = Math.hypot(hit.x - projected.x, hit.y - projected.y);
                                if (hitDistanceToProjected > MAX_TRIM_NEIGHBOR_DISTANCE) continue;

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
                                    distance: hitDistanceToProjected
                                });
                            }
                        }

                        if (intersections.length === 0) continue;

                        const nearest = intersections.sort((a, b) => a.distance - b.distance)[0];
                        if (nearest) {
                            candidates.push({ shape: trimShape, point: projected, intersection: nearest, segment });
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

                function collectTrimTargetCandidates(shape, point) {
                    if (!shape || !point) return [];

                    const candidates = [];
                    const segments = getShapeSegments(shape);

                    for (const segment of segments) {
                        if (!isTrimIntersectionBoundedSegment(shape, segment, point)) continue;

                        const projected = nearestPointOnSegment(point, segment.a, segment.b);
                        const intersections = [];
                        for (const other of shapes) {
                            if (other.id === shape.id) continue;
                            for (const otherSegment of getShapeSegments(other)) {
                                const hit = segmentIntersection(segment.a, segment.b, otherSegment.a, otherSegment.b);
                                if (!hit) continue;

                                const hitDistanceToProjected = Math.hypot(hit.x - projected.x, hit.y - projected.y);
                                if (hitDistanceToProjected > MAX_TRIM_NEIGHBOR_DISTANCE) continue;

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
                                    distance: hitDistanceToProjected
                                });
                            }
                        }

                        if (!intersections.length) continue;

                        const nearest = intersections.sort((a, b) => a.distance - b.distance)[0];
                        if (!nearest) continue;

                        candidates.push({
                            shape,
                            segment,
                            point: projected,
                            intersection: nearest,
                            distance: Math.hypot(point.x - projected.x, point.y - projected.y)
                        });
                    }

                    return candidates.sort((a, b) => a.distance - b.distance);
                }

                function getTrimHoverTarget(point) {
                    if (!point) return null;
                    const candidates = [];
                    for (const shape of shapes) {
                        const shapeCandidates = collectTrimTargetCandidates(shape, point);
                        candidates.push(...shapeCandidates);
                    }
                    return candidates.length ? candidates[0] : null;
                }

                function getTrimNodeCandidates(shape, segment) {
                    if (!shape || !segment) return [];
                    const nodes = [];
                    const addNode = (node) => {
                        if (!node || !Number.isFinite(node.x) || !Number.isFinite(node.y)) return;
                        const existing = nodes.find(candidate =>
                            Math.abs(candidate.x - node.x) < 0.2 && Math.abs(candidate.y - node.y) < 0.2
                        );
                        if (!existing) {
                            nodes.push({ x: node.x, y: node.y });
                        }
                    };

                    addNode(segment.a);
                    addNode(segment.b);
                    for (const vertex of getShapeVertices(shape)) {
                        addNode(vertex);
                    }

                    for (const other of shapes) {
                        if (other.id === shape.id) continue;
                        for (const otherSegment of getShapeSegments(other)) {
                            const hit = segmentIntersection(segment.a, segment.b, otherSegment.a, otherSegment.b);
                            if (hit) {
                                addNode(hit);
                            }
                        }
                    }

                    const segmentVecX = segment.b.x - segment.a.x;
                    const segmentVecY = segment.b.y - segment.a.y;
                    const segmentLength = Math.hypot(segmentVecX, segmentVecY) || 1;

                    return nodes
                        .filter(node => pointOnSegment(node, segment.a, segment.b, 1.5))
                        .map(node => ({
                            x: node.x,
                            y: node.y,
                            distance: ((node.x - segment.a.x) * segmentVecX + (node.y - segment.a.y) * segmentVecY) / segmentLength
                        }))
                        .sort((a, b) => a.distance - b.distance);
                }

                function resolveTrimCutBoundary(shape, segment, point) {
                    if (!shape || !segment) {
                        return { start: point, end: point };
                    }

                    const projected = nearestPointOnSegment(point, segment.a, segment.b);
                    const nodes = getTrimNodeCandidates(shape, segment);
                    const segmentVecX = segment.b.x - segment.a.x;
                    const segmentVecY = segment.b.y - segment.a.y;
                    const segmentLength = Math.hypot(segmentVecX, segmentVecY) || 1;
                    const currentDistance = ((projected.x - segment.a.x) * segmentVecX + (projected.y - segment.a.y) * segmentVecY) / segmentLength;

                    const prevNode = nodes
                        .filter(node => node.distance <= currentDistance)
                        .sort((a, b) => b.distance - a.distance)[0] || {
                            x: projected.x,
                            y: projected.y,
                            distance: currentDistance
                        };
                    const nextNode = nodes
                        .filter(node => node.distance >= currentDistance)
                        .sort((a, b) => a.distance - b.distance)[0] || {
                            x: projected.x,
                            y: projected.y,
                            distance: currentDistance
                        };

                    if (Math.abs(prevNode.distance - nextNode.distance) < 0.001) {
                        return {
                            start: projected,
                            end: projected
                        };
                    }

                    return {
                        start: {
                            x: prevNode.x,
                            y: prevNode.y
                        },
                        end: {
                            x: nextNode.x,
                            y: nextNode.y
                        }
                    };
                }

                function lineSide(point, start, end) {
                    return (point.x - start.x) * (end.y - start.y) - (point.y - start.y) * (end.x - start.x);
                }

                function classifyTrimSide(point, cutStart, cutEnd, referencePoint = null) {
                    if (!point || !cutStart || !cutEnd) return 'keep';
                    const reference = referencePoint || {
                        x: (cutStart.x + cutEnd.x) / 2,
                        y: (cutStart.y + cutEnd.y) / 2
                    };
                    const pointSide = lineSide(point, cutStart, cutEnd);
                    const referenceSide = lineSide(reference, cutStart, cutEnd);
                    if (Math.abs(pointSide) < 0.0001 && Math.abs(referenceSide) < 0.0001) return 'keep';
                    return pointSide * referenceSide >= 0 ? 'keep' : 'cut';
                }

                function reconstructTrimmedShape(shape, cutStart, cutEnd) {
                    if (!shape || !cutStart || !cutEnd) return [];

                    const vertices = getShapeVertices(shape);
                    if (vertices.length < 3) return [];

                    const center = vertices.reduce((sum, vertex) => ({
                        x: sum.x + vertex.x,
                        y: sum.y + vertex.y
                    }), { x: 0, y: 0 });
                    const polygonCenter = {
                        x: center.x / vertices.length,
                        y: center.y / vertices.length
                    };

                    const keepVertices = [];
                    for (let index = 0; index < vertices.length; index++) {
                        const current = vertices[index];
                        const next = vertices[(index + 1) % vertices.length];
                        const currentKind = classifyTrimSide(current, cutStart, cutEnd, polygonCenter);
                        const nextKind = classifyTrimSide(next, cutStart, cutEnd, polygonCenter);

                        if (currentKind === 'keep' && nextKind === 'keep') {
                            keepVertices.push({ ...next });
                            continue;
                        }

                        if (currentKind === 'keep' && nextKind === 'cut') {
                            const hit = segmentIntersection(current, next, cutStart, cutEnd);
                            if (hit) keepVertices.push({ ...hit });
                            continue;
                        }

                        if (currentKind === 'cut' && nextKind === 'keep') {
                            const hit = segmentIntersection(current, next, cutStart, cutEnd);
                            if (hit) keepVertices.push({ ...hit }, { ...next });
                        }
                    }

                    const deduped = [];
                    for (const point of keepVertices) {
                        const seen = deduped.some(candidate =>
                            Math.abs(candidate.x - point.x) < 0.01 && Math.abs(candidate.y - point.y) < 0.01
                        );
                        if (!seen) deduped.push(point);
                    }

                    return deduped.length >= 3 ? deduped : [];
                }

                function clipPolygonByCut(vertices, cutStart, cutEnd) {
                    if (!Array.isArray(vertices) || vertices.length < 3) {
                        return [];
                    }

                    const center = vertices.reduce((sum, vertex) => ({
                        x: sum.x + vertex.x,
                        y: sum.y + vertex.y
                    }), { x: 0, y: 0 });
                    const polygonCenter = {
                        x: center.x / vertices.length,
                        y: center.y / vertices.length
                    };
                    const keepPositive = classifyTrimSide(polygonCenter, cutStart, cutEnd, polygonCenter) === 'keep';

                    const result = [];
                    for (let index = 0; index < vertices.length; index++) {
                        const current = vertices[index];
                        const next = vertices[(index + 1) % vertices.length];
                        const currentSide = classifyTrimSide(current, cutStart, cutEnd, polygonCenter) === 'keep';
                        const nextSide = classifyTrimSide(next, cutStart, cutEnd, polygonCenter) === 'keep';

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

                    const targetSegment = getShapeSegments(shape).find(segment =>
                        pointOnSegment(point, segment.a, segment.b, TRIM_EDGE_SNAP_DISTANCE) ||
                        pointOnSegment(intersection, segment.a, segment.b, TRIM_EDGE_SNAP_DISTANCE)
                    ) || getShapeSegments(shape)[0];

                    const trimBoundary = resolveTrimCutBoundary(shape, targetSegment, point);
                    const cutStart = trimBoundary.start || point;
                    const cutEnd = trimBoundary.end || intersection;

                    let edgeTrimIndex = -1;
                    for (let index = 0; index < vertices.length; index++) {
                        const current = vertices[index];
                        const next = vertices[(index + 1) % vertices.length];
                        if (pointOnSegment(cutStart, current, next, TRIM_EDGE_SNAP_DISTANCE) && pointOnSegment(cutEnd, current, next, TRIM_EDGE_SNAP_DISTANCE)) {
                            edgeTrimIndex = index;
                            break;
                        }
                    }

                    if (edgeTrimIndex >= 0) {
                        const current = vertices[edgeTrimIndex];
                        const next = vertices[(edgeTrimIndex + 1) % vertices.length];
                        const distanceToCurrent = Math.hypot(cutStart.x - current.x, cutStart.y - current.y);
                        const distanceToNext = Math.hypot(cutStart.x - next.x, cutStart.y - next.y);
                        const keepIndex = distanceToCurrent >= distanceToNext ? edgeTrimIndex : (edgeTrimIndex + 1) % vertices.length;
                        vertices[keepIndex] = { x: cutEnd.x, y: cutEnd.y };

                        const cleaned = vertices.filter((vertex, index, arr) => {
                            const previous = arr[(index - 1 + arr.length) % arr.length];
                            const duplicate = Math.abs(vertex.x - previous.x) < 0.01 && Math.abs(vertex.y - previous.y) < 0.01;
                            return !duplicate;
                        });

                        if (cleaned.length < 3) {
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
                        shape.closed = true;
                        shape.fill = 'rgba(34, 197, 94, 0.14)';
                        shape.points = cleaned;
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

                    const reconstructed = reconstructTrimmedShape(shape, cutStart, cutEnd);
                    if (reconstructed.length >= 3) {
                        shape.type = 'freeform';
                        shape.closed = true;
                        shape.fill = 'rgba(34, 197, 94, 0.14)';
                        shape.points = reconstructed;
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

                    const center = vertices.reduce((sum, vertex) => ({
                        x: sum.x + vertex.x,
                        y: sum.y + vertex.y
                    }), { x: 0, y: 0 });
                    const polygonCenter = {
                        x: center.x / vertices.length,
                        y: center.y / vertices.length
                    };

                    const dx = cutEnd.x - cutStart.x;
                    const dy = cutEnd.y - cutStart.y;
                    const length = Math.hypot(dx, dy) || 1;
                    const normalX = -dy / length;
                    const normalY = dx / length;
                    const offsetDirection = lineSide(polygonCenter, cutStart, cutEnd) >= 0 ? -1 : 1;
                    const offsetAmount = 2;
                    const shiftedStart = {
                        x: cutStart.x + normalX * offsetDirection * offsetAmount,
                        y: cutStart.y + normalY * offsetDirection * offsetAmount
                    };
                    const shiftedEnd = {
                        x: cutEnd.x + normalX * offsetDirection * offsetAmount,
                        y: cutEnd.y + normalY * offsetDirection * offsetAmount
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
                    shape.closed = true;
                    shape.fill = 'rgba(34, 197, 94, 0.14)';
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
                    const selectedShapeType = shapeTypeSelect.value;
                    const normalized = type || selectedShapeType;
                    currentTool = normalized === 'line' || normalized === 'arc' || normalized === 'freeform' || normalized === 'polygon' || normalized === 'circle'
                        ? (normalized === 'circle' ? 'arc' : normalized)
                        : 'polygon';
                    if (normalized === 'freeform') {
                        isDrawingFreeform = false;
                        freeDrawingPoints = [];
                    }
                    if (normalized === 'arc' || normalized === 'line') {
                        activeDraftShape = null;
                    }
                    if (normalized === 'polygon') {
                        const config = getSelectedPolygonConfig();
                        polygonSides = config.sides;
                        polygonSidesSelect.dataset.shapeType = config.shapeType;
                    }
                    setActiveToolButton('shape');
                }

                function getSelectedPolygonConfig() {
                    const value = polygonSidesSelect.value;
                    const sides = Number(value) || 6;
                    return { sides, shapeType: 'polygon' };
                }

                function syncShapeSelection(kind) {
                    const nextKind = kind || 'line';
                    const shapeModeButtons = document.querySelectorAll('.shape-mode-button');
                    shapeModeButtons.forEach((button) => {
                        button.classList.toggle('is-active', button.dataset.shapeKind === nextKind);
                    });
                    const shapeSideButtons = document.querySelectorAll('.shape-side-btn');
                    const isPolygon = nextKind === 'polygon';
                    shapeSideButtons.forEach((button) => {
                        button.classList.toggle('is-active', isPolygon && Number(button.dataset.sides) === Number(polygonSides));
                    });
                    shapeTypeSelect.value = nextKind === 'polygon' ? String(polygonSides) : nextKind === 'arc' ? 'arc' : nextKind;
                    currentTool = nextKind === 'arc' ? 'arc' : nextKind;
                    activeDraftShape = null;
                    setActiveToolButton('shape');
                }

                document.querySelectorAll('.shape-mode-button').forEach((button) => {
                    button.addEventListener('click', () => {
                        const kind = button.dataset.shapeKind || 'line';
                        if (kind === 'polygon') {
                            polygonSides = Number(polygonSidesSelect.value) || 6;
                            syncShapeSelection('polygon');
                            return;
                        }
                        syncShapeSelection(kind);
                    });
                });

                document.querySelectorAll('.shape-side-btn').forEach((button) => {
                    button.addEventListener('click', () => {
                        const value = Number(button.dataset.sides) || 6;
                        polygonSides = value;
                        polygonSidesSelect.value = String(value);
                        document.querySelectorAll('.shape-side-btn').forEach((sideButton) => {
                            sideButton.classList.toggle('is-active', Number(sideButton.dataset.sides) === value);
                        });
                        currentTool = 'polygon';
                        syncShapeSelection('polygon');
                    });
                });

                polygonSidesSelect.addEventListener('change', (event) => {
                    const config = getSelectedPolygonConfig();
                    polygonSides = config.sides;
                    currentTool = 'polygon';
                    activeDraftShape = null;
                    setActiveToolButton('shape');
                    polygonSidesSelect.dataset.shapeType = config.shapeType;
                    const sideButtons = document.querySelectorAll('.shape-side-btn');
                    sideButtons.forEach((button) => {
                        button.classList.toggle('is-active', Number(button.dataset.sides) === polygonSides);
                    });
                });

                function toggleTrimTool() {
                    currentTool = currentTool === 'trim' ? null : 'trim';
                    trimHoverTarget = null;
                    setActiveToolButton(currentTool);
                }

                document.querySelector('[data-tool="trim"]').addEventListener('click', () => {
                    toggleTrimTool();
                });

                document.querySelector('[data-tool="object-select"]').addEventListener('click', () => {
                    currentTool = currentTool === 'object-select' ? null : 'object-select';
                    if (currentTool === 'object-select') {
                        objectSelectDragState = null;
                    }
                    setActiveToolButton(currentTool);
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

                    if (currentTool === 'object-select') {
                        objectSelectDragState = {
                            startX: point.x,
                            startY: point.y,
                            endX: point.x,
                            endY: point.y,
                            moved: false
                        };
                        drawPaper();
                        return;
                    }

                    if (currentTool === 'trim') {
                        const trimCandidate = getTrimHoverTarget(point);
                        trimDragState = trimCandidate ? {
                            start: point,
                            current: point,
                            candidate: trimCandidate
                        } : null;

                        if (trimCandidate && trimCandidate.shape) {
                            const trimmed = applyTrimToShape(trimCandidate.shape, trimCandidate.point, trimCandidate.intersection);
                            if (trimmed) {
                                selectedShapeId = null;
                                document.getElementById('selectedShape').textContent = '없음';
                                trimHoverTarget = null;
                                trimDragState = null;
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
                        if (!activeDraftShape || activeDraftShape.type !== 'polygon') {
                            activeDraftShape = {
                                id: `shape_${Date.now()}`,
                                type: 'polygon',
                                points: [{ x: point.x, y: point.y }],
                                x: point.x,
                                y: point.y,
                                width: 0,
                                height: 0,
                                sides: polygonSides,
                                text: '',
                                fill: 'transparent',
                                stroke: defaultStrokeColor,
                                closed: false,
                                cadMode: true
                            };
                        } else {
                            const draftPoints = Array.isArray(activeDraftShape.points) ? activeDraftShape.points : [{ x: activeDraftShape.x, y: activeDraftShape.y }];
                            if (draftPoints.length > 2 && Math.hypot(point.x - draftPoints[0].x, point.y - draftPoints[0].y) < 10) {
                                const shape = applyDefaultsToNewShape({
                                    ...activeDraftShape,
                                    id: `shape_${Date.now()}`,
                                    type: 'polygon',
                                    x: Math.min(...draftPoints.map(p => p.x)),
                                    y: Math.min(...draftPoints.map(p => p.y)),
                                    width: Math.max(12, Math.max(...draftPoints.map(p => p.x)) - Math.min(...draftPoints.map(p => p.x))),
                                    height: Math.max(12, Math.max(...draftPoints.map(p => p.y)) - Math.min(...draftPoints.map(p => p.y))),
                                    points: draftPoints,
                                    closed: true,
                                    fill: 'transparent'
                                });
                                shapes.push(shape);
                                selectedShapeId = shape.id;
                                document.getElementById('selectedShape').textContent = shape.id;
                                activeDraftShape = null;
                                currentTool = null;
                                setActiveToolButton(null);
                                drawPaper();
                                saveEditorState();
                                return;
                            }
                            activeDraftShape.points.push({ x: point.x, y: point.y });
                        }
                        drawPaper();
                        return;
                    }

                    if (currentTool === 'line') {
                        if (!activeDraftShape || activeDraftShape.type !== 'line') {
                            activeDraftShape = createLineShape(point, point, {
                                id: `draft_${Date.now()}`,
                                cadMode: true,
                                text: ''
                            });
                            drawPaper();
                            return;
                        }

                        const shape = createLineShape(
                            { x: activeDraftShape.x, y: activeDraftShape.y },
                            { x: point.x, y: point.y }
                        );
                        shapes.push(shape);
                        selectedShapeId = shape.id;
                        document.getElementById('selectedShape').textContent = shape.id;
                        activeDraftShape = null;
                        currentTool = null;
                        setActiveToolButton(null);
                        drawPaper();
                        saveEditorState();
                        return;
                    }

                    if (currentTool === 'arc') {
                        if (!activeDraftShape || activeDraftShape.type !== 'arc') {
                            activeDraftShape = createArcShape(point, 0, 0, 0, {
                                id: `draft_${Date.now()}`,
                                cadMode: true,
                                startPoint: { x: point.x, y: point.y },
                                endPoint: { x: point.x, y: point.y },
                                text: ''
                            });
                            drawPaper();
                            return;
                        }

                        const center = { x: activeDraftShape.cx, y: activeDraftShape.cy };
                        const startPoint = activeDraftShape.startPoint || center;
                        const endPoint = { x: point.x, y: point.y };
                        const radius = Math.max(4, Math.hypot(endPoint.x - center.x, endPoint.y - center.y));
                        const startAngle = Math.atan2(startPoint.y - center.y, startPoint.x - center.x);
                        const endAngle = Math.atan2(endPoint.y - center.y, endPoint.x - center.x);
                        const shape = createArcShape(center, radius, startAngle, endAngle, {
                            stroke: defaultStrokeColor,
                            fill: 'transparent'
                        });
                        shapes.push(shape);
                        selectedShapeId = shape.id;
                        document.getElementById('selectedShape').textContent = shape.id;
                        activeDraftShape = null;
                        currentTool = null;
                        setActiveToolButton(null);
                        drawPaper();
                        saveEditorState();
                        return;
                    }

                    const selectedIds = getSelectedShapeIds();
                    const primaryShape = selectedIds.length > 0 ? shapes.find(shape => shape.id === selectedIds[0]) : null;
                    const groupHandleName = selectedIds.length > 1 ? getGroupResizeHandleHit(selectedIds, point) : null;
                    const singleHandleName = primaryShape ? isResizeHandleHit(primaryShape, point) : null;
                    const activeHandle = groupHandleName || singleHandleName;

                    if (activeHandle) {
                        const selected = selectedIds.length > 1 ? selectedIds : [primaryShape ? primaryShape.id : null].filter(Boolean);
                        const bounds = getSelectionBounds(selected);
                        const shapeForTarget = primaryShape || shapes.find(shape => shape.id === selected[0]);
                        if (!shapeForTarget && selected.length === 0) {
                            return;
                        }

                        selectedShapeId = selected[0] || null;
                        hoverHandleName = activeHandle;
                        if (activeHandle === 'rotation') {
                            const groupedCenter = bounds ? { x: bounds.centerX, y: bounds.centerY } : getShapeCenter(shapeForTarget);
                            dragState = {
                                mode: 'rotate',
                                shapeId: selected[0],
                                shapeIds: selected,
                                handle: activeHandle,
                                startX: point.x,
                                startY: point.y,
                                original: Object.fromEntries(selected.map(id => [id, { ...shapes.find(shape => shape.id === id) }])),
                                startAngle: Math.atan2(point.y - groupedCenter.y, point.x - groupedCenter.x),
                                groupCenter: groupedCenter,
                                originalBounds: bounds
                            };
                        } else {
                            dragState = {
                                mode: 'resize',
                                shapeId: selected[0],
                                shapeIds: selected,
                                handle: activeHandle,
                                startX: point.x,
                                startY: point.y,
                                original: Object.fromEntries(selected.map(id => [id, { ...shapes.find(shape => shape.id === id) }])),
                                originalBounds: bounds
                            };
                        }
                        document.getElementById('selectedShape').textContent = selected.length > 1 ? `${selected.length}개 선택` : (selected[0] || '없음');
                        drawPaper();
                        return;
                    }

                    const borderShape = [...shapes].reverse().find(shape => getShapeBorderHit(shape, point));
                    if (borderShape) {
                        const shapesInSelection = selectedShapeIds.size > 0 ? Array.from(selectedShapeIds) : [selectedShapeId].filter(Boolean);
                        const isAlreadySelected = shapesInSelection.includes(borderShape.id);
                        const nextSelected = isAlreadySelected ? shapesInSelection : [borderShape.id];
                        setSelectedShapes(nextSelected);
                        if (isAlreadySelected) {
                            const allSelected = nextSelected
                                .map(id => shapes.find(shape => shape.id === id))
                                .filter(Boolean);
                            const originalMap = Object.fromEntries(allSelected.map(shape => [shape.id, { ...shape }]));
                            dragState = {
                                mode: 'move',
                                shapeId: borderShape.id,
                                shapeIds: nextSelected,
                                startX: point.x,
                                startY: point.y,
                                original: originalMap
                            };
                        }
                        document.getElementById('fontSize').value = '40';
                        drawPaper();
                        return;
                    }

                    const targetShape = getShapeAtPoint(point);
                    if (targetShape) {
                        const shapesInSelection = selectedShapeIds.size > 0 ? Array.from(selectedShapeIds) : [selectedShapeId].filter(Boolean);
                        const isAlreadySelected = shapesInSelection.includes(targetShape.id);
                        const nextSelected = isAlreadySelected ? shapesInSelection : [targetShape.id];
                        setSelectedShapes(nextSelected);
                        if (isAlreadySelected) {
                            const allSelected = nextSelected
                                .map(id => shapes.find(shape => shape.id === id))
                                .filter(Boolean);
                            const originalMap = Object.fromEntries(allSelected.map(shape => [shape.id, { ...shape }]));
                            dragState = {
                                mode: 'move',
                                shapeId: targetShape.id,
                                shapeIds: nextSelected,
                                startX: point.x,
                                startY: point.y,
                                original: originalMap
                            };
                        }
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

                    if (objectSelectDragState) {
                        objectSelectDragState.endX = pointer.x;
                        objectSelectDragState.endY = pointer.y;
                        objectSelectDragState.moved = true;
                        drawPaper();
                        return;
                    }

                    if (currentTool === 'trim') {
                        if (trimDragState) {
                            trimDragState.current = pointer;
                            const dragCandidate = getTrimHoverTarget(pointer) || trimDragState.candidate;
                            if (dragCandidate && dragCandidate.shape) {
                                trimHoverTarget = dragCandidate;
                            } else {
                                trimHoverTarget = null;
                            }
                            drawPaper();
                            return;
                        }

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
                        const dragPoint = getCanvasPoint(event);
                        const dx = dragPoint.x - dragState.startX;
                        const dy = dragPoint.y - dragState.startY;

                        if (dragState.mode === 'move') {
                            const selectedIds = dragState.shapeIds && dragState.shapeIds.length ? dragState.shapeIds : [dragState.shapeId];
                            for (const selectedId of selectedIds) {
                                const target = shapes.find(item => item.id === selectedId);
                                if (!target) continue;
                                const original = dragState.original[selectedId] || dragState.original;
                                const snapped = applySnapToShape(target.id, original.x + dx, original.y + dy, target.width, target.height);
                                target.x = snapped.x;
                                target.y = snapped.y;
                            }
                        } else if (dragState.mode === 'rotate') {
                            const selectedIds = dragState.shapeIds && dragState.shapeIds.length ? dragState.shapeIds : [dragState.shapeId].filter(Boolean);
                            const center = dragState.groupCenter || getSelectionBounds(selectedIds)?.center || { x: 0, y: 0 };
                            const currentAngle = Math.atan2(dragPoint.y - center.y, dragPoint.x - center.x);
                            const deltaDegrees = ((currentAngle - dragState.startAngle) * 180) / Math.PI;
                            const originalMap = dragState.original || {};
                            for (const selectedId of selectedIds) {
                                const target = shapes.find(item => item.id === selectedId);
                                if (!target) continue;
                                const original = originalMap[selectedId] || originalMap;
                                const originalRotation = Number(original.rotation) || 0;
                                target.rotation = originalRotation + deltaDegrees;
                            }
                            if (rotationDegreesInput && selectedShapeId && selectedIds.includes(selectedShapeId)) {
                                const current = shapes.find(shape => shape.id === selectedShapeId);
                                if (current) {
                                    rotationDegreesInput.value = String(Number.isFinite(Number(current.rotation)) ? Number(current.rotation) : 0);
                                }
                            }
                        } else {
                            const selectedIds = dragState.shapeIds && dragState.shapeIds.length ? dragState.shapeIds : [dragState.shapeId].filter(Boolean);
                            if (selectedIds.length > 1) {
                                const originalBounds = dragState.originalBounds || getSelectionBounds(selectedIds);
                                if (originalBounds) {
                                    const resizeMap = resizeSelectionGroupFromHandle(selectedIds, dragState.handle, dx, dy, originalBounds);
                                    Object.entries(resizeMap).forEach(([id, updated]) => {
                                        const shape = shapes.find(item => item.id === id);
                                        if (!shape) return;
                                        Object.assign(shape, updated);
                                    });
                                }
                            } else {
                                const shape = shapes.find(item => item.id === dragState.shapeId);
                                if (!shape) return;
                                const original = dragState.original[dragState.shapeId] || dragState.original;
                                const resized = resizeShapeFromHandle(original, dragState.handle, dx, dy);
                                shape.x = resized.x;
                                shape.y = resized.y;
                                shape.width = resized.width;
                                shape.height = resized.height;
                            }
                        }

                        drawPaper();
                        saveEditorState();
                        return;
                    }

                    if (activeDraftShape && currentTool === 'arc') {
                        const draft = activeDraftShape;
                        const center = { x: draft.cx, y: draft.cy };
                        const endPoint = getCanvasPoint(event);
                        const radius = Math.hypot(endPoint.x - center.x, endPoint.y - center.y);
                        draft.radius = radius;
                        draft.endPoint = { x: endPoint.x, y: endPoint.y };
                        draft.startAngle = Math.atan2((draft.startPoint || center).y - center.y, (draft.startPoint || center).x - center.x);
                        draft.endAngle = Math.atan2(endPoint.y - center.y, endPoint.x - center.x);
                        draft.x = center.x - radius;
                        draft.y = center.y - radius;
                        draft.width = radius * 2;
                        draft.height = radius * 2;
                        drawPaper();
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

                    if (activeDraftShape && currentTool === 'line') {
                        activeDraftShape.width = pointer.x - activeDraftShape.x;
                        activeDraftShape.height = pointer.y - activeDraftShape.y;
                        activeDraftShape.endX = pointer.x;
                        activeDraftShape.endY = pointer.y;
                        drawPaper();
                        return;
                    }

                    if (!isDrawingFreeform || currentTool !== 'freeform') return;
                    freeDrawingPoints.push({ x: pointer.x, y: pointer.y });
                    drawPaper();
                });

                canvas.addEventListener('mouseup', (event) => {
                    if (currentTool === 'trim' && trimDragState) {
                        const point = getCanvasPoint(event);
                        const finalTarget = getTrimHoverTarget(point) || trimDragState.candidate;
                        if (finalTarget && finalTarget.shape) {
                            const trimmed = applyTrimToShape(finalTarget.shape, finalTarget.point, finalTarget.intersection);
                            if (trimmed) {
                                selectedShapeId = null;
                                document.getElementById('selectedShape').textContent = '없음';
                                trimHoverTarget = null;
                                trimDragState = null;
                                drawPaper();
                                saveEditorState();
                            }
                        }
                        trimDragState = null;
                        trimHoverTarget = null;
                        drawPaper();
                        return;
                    }

                    if (objectSelectDragState) {
                        const clickPoint = { x: objectSelectDragState.startX, y: objectSelectDragState.startY };
                        const dragSize = Math.hypot(
                            objectSelectDragState.endX - objectSelectDragState.startX,
                            objectSelectDragState.endY - objectSelectDragState.startY
                        );
                        const shiftPressed = !!(event && event.shiftKey);

                        if (dragSize <= 3) {
                            selectObjectAtPoint(clickPoint, event);
                        } else {
                            const selectionRect = normalizeSelectionRect(getObjectSelectRectFromDrag(
                                objectSelectDragState.startX,
                                objectSelectDragState.startY,
                                objectSelectDragState.endX,
                                objectSelectDragState.endY
                            ));
                            const selectedIds = shapes
                                .filter(shape => isShapeFullyContainedInRect(shape, selectionRect) || isShapeIntersectsRect(shape, selectionRect))
                                .map(shape => shape.id);

                            if (selectedIds.length > 0) {
                                if (shiftPressed) {
                                    const merged = new Set(selectedShapeIds);
                                    selectedIds.forEach(id => merged.add(id));
                                    setSelectedShapes(Array.from(merged));
                                } else {
                                    setSelectedShapes(selectedIds);
                                }
                            } else if (!shiftPressed) {
                                selectObjectAtPoint(clickPoint, event);
                            }
                        }

                        objectSelectDragState = null;
                        if (!shiftPressed) {
                            currentTool = null;
                            setActiveToolButton(null);
                        }
                        drawPaper();
                        saveEditorState();
                        return;
                    }

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

                    if (activeDraftShape && currentTool === 'line') {
                        const shape = applyDefaultsToNewShape({
                            ...activeDraftShape,
                            id: `shape_${Date.now()}`,
                            type: 'line',
                            x: activeDraftShape.x,
                            y: activeDraftShape.y,
                            width: activeDraftShape.width,
                            height: activeDraftShape.height,
                            endX: activeDraftShape.endX || activeDraftShape.x + activeDraftShape.width,
                            endY: activeDraftShape.endY || activeDraftShape.y + activeDraftShape.height,
                            fill: 'transparent',
                            stroke: defaultStrokeColor,
                            closed: false
                        });
                        const lineLength = Math.hypot(shape.width, shape.height);
                        if (lineLength > 4) {
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

                    if (currentTool === 'object-select') {
                        const selected = selectObjectAtPoint(point, event);
                        if (!event.shiftKey) {
                            currentTool = null;
                            setActiveToolButton(null);
                        }
                        drawPaper();
                        return;
                    }

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
                    const pointerX = event.clientX - rect.left;
                    const pointerY = event.clientY - rect.top;
                    const viewportWidth = canvas.clientWidth || canvas.width;
                    const viewportHeight = canvas.clientHeight || canvas.height;
                    const frame = getPaperFrame();
                    const insidePaper = pointerX >= frame.x && pointerX <= frame.x + frame.width &&
                        pointerY >= frame.y && pointerY <= frame.y + frame.height;

                    if (!insidePaper && !event.shiftKey) {
                        return;
                    }

                    event.preventDefault();
                    const delta = event.deltaY || event.wheelDelta || 0;
                    const nextZoom = clampZoom(paperZoom * (delta > 0 ? 0.9 : 1.1));
                    const worldX = (pointerX - frame.x) / paperZoom;
                    const worldY = (pointerY - frame.y) / paperZoom;

                    const nextWidth = currentPaper.width * nextZoom;
                    const nextHeight = currentPaper.height * nextZoom;
                    const viewportCenterX = viewportWidth / 2;
                    const viewportCenterY = viewportHeight / 2;

                    paperZoom = nextZoom;
                    const nextPaperX = pointerX - worldX * paperZoom;
                    const nextPaperY = pointerY - worldY * paperZoom;
                    paperPan.x = nextPaperX - viewportCenterX + nextWidth / 2;
                    paperPan.y = nextPaperY - viewportCenterY + nextHeight / 2;
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
                    if (rotationDegreesInput) {
                        rotationDegreesInput.value = String(Number.isFinite(Number(shape.rotation)) ? Number(shape.rotation) : 0);
                    }
                    updateRecentColorRow('stroke');
                    updateRecentColorRow('fill');
                    setActiveColorInput('stroke');
                }

                function commitRotationFromInput() {
                    const shape = shapes.find(s => s.id === selectedShapeId);
                    if (!shape || !rotationDegreesInput) return;

                    const sanitized = rotationDegreesInput.value;
                    const nextValue = Number(sanitized);
                    if (!Number.isFinite(nextValue)) {
                        rotationDegreesInput.value = String(Number.isFinite(Number(shape.rotation)) ? Number(shape.rotation) : 0);
                        return;
                    }

                    shape.rotation = nextValue;
                    rotationDegreesInput.value = String(nextValue);
                    dragState = null;
                    hoverHandleName = null;
                    drawPaper();
                    saveEditorState();
                }

                if (rotationDegreesInput) {
                    rotationDegreesInput.addEventListener('focus', () => {
                        rotationDegreesInput.select();
                    });

                    rotationDegreesInput.addEventListener('input', () => {
                        const shape = shapes.find(s => s.id === selectedShapeId);
                        if (!shape) return;
                        const nextValue = Number(rotationDegreesInput.value);
                        shape.rotation = Number.isFinite(nextValue) ? nextValue : 0;
                        drawPaper();
                        saveEditorState();
                    });

                    rotationDegreesInput.addEventListener('keydown', (event) => {
                        if (event.key === 'Enter' && event.target && event.target.id === 'rotationDegrees') {
                            event.preventDefault();
                            event.stopPropagation();
                            commitRotationFromInput();
                            rotationDegreesInput.blur();
                        }
                    });
                }

                updateRecentColorRow('stroke');
                updateRecentColorRow('fill');
                setActiveColorInput('stroke');

                function applyDefaultsToNewShape(shape) {
                    if (!shape) return;
                    shape.stroke = shape.stroke || defaultStrokeColor;
                    shape.rotation = Number(shape.rotation) || 0;
                    if (typeof shape.fill === 'undefined' || shape.fill === null || shape.fill === '') {
                        shape.fill = 'transparent';
                    }
                    if (shape.type === 'line') {
                        shape.closed = false;
                    } else if (shape.type === 'freeform') {
                        if (typeof shape.closed === 'undefined') {
                            shape.closed = false;
                        }
                    } else if (typeof shape.closed === 'undefined') {
                        shape.closed = true;
                    }
                    if (shape.type !== 'freeform' && shape.type !== 'line' && shape.fill && shape.fill !== 'transparent' && shape.fill === defaultFillColor && shape.closed === true) {
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
                    const target = event.target;
                    if (target && target.matches('input, textarea, select')) {
                        if (event.key === 'Enter' && target.id === 'rotationDegrees') {
                            event.preventDefault();
                            event.stopPropagation();
                            commitRotationFromInput();
                            target.blur();
                        }
                        return;
                    }

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

                    if ((event.key === 'Delete' || event.key === 'Backspace')) {
                        const idsToDelete = selectedShapeIds.size > 0
                            ? Array.from(selectedShapeIds)
                            : selectedShapeId
                                ? [selectedShapeId]
                                : [];

                        if (idsToDelete.length > 0) {
                            for (const id of idsToDelete) {
                                const idx = shapes.findIndex(shape => shape.id === id);
                                if (idx >= 0) {
                                    shapes.splice(idx, 1);
                                }
                            }
                            selectedShapeIds.clear();
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
                    const restoredPaperName = currentPaper && currentPaper.label && currentPaper.label !== 'Custom'
                        ? currentPaper.label
                        : 'Custom';
                    paperSelect.value = restoredPaperName;
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
