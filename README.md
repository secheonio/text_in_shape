# Text in Shape

Text in Shape은 용지 크기를 선택하고, 도형 안에 텍스트를 넣어 템플릿을 제작하고 저장하는 웹 기반 편집 도구입니다.

## 주요 기능

- 용지 크기 선택: A4, A5, Letter, 사용자 지정 크기
- 도형 생성: 원, 자유형, 다각형, 텍스트 기반 구성 요소
- 텍스트 입력: 선택한 도형에 텍스트를 직접 배치
- 템플릿 저장/불러오기: 사용자 정의 `.sit` 포맷 활용
- 웹 UI 기반 편집: 브라우저에서 바로 실행 가능
- 패키지 호환성 정리: `text_in_shape` / `sgape_in_text` 경로 혼선을 제거

## 최근 변경 사항

- 웹 앱 진입점 정리 및 실행 경로 안정화
- Flask 기반 루트 페이지의 정상 응답 확인
- 패키지 import 경로 혼재 해결
- 테스트 보강: 엔트리포인트 import 회귀 검증 추가
- 전체 테스트 통과 확인 (`7 passed`)

## 실행 방법

1. Python 3.10 이상 설치
2. 의존성 설치

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. 실행

```bash
python main.py
```

4. 브라우저에서 확인

```text
http://127.0.0.1:5000/
```

> 현재 실행 환경은 프로젝트 로컬 `.venv`를 사용하도록 설정되어 있으며, Flask와 Pillow 등 의존성이 설치된 상태를 기준으로 동작합니다.

## 사용 흐름

1. 프로그램 실행
2. 용지 크기 선택
3. 도형 생성 또는 이미지 영역 선택
4. 도형 선택 후 텍스트 입력
5. 템플릿 저장 (`.sit`)
6. 이후 다시 불러와서 수정/재사용

## .sit 파일 형식

`.sit`는 ZIP 기반의 사용자 정의 템플릿 파일입니다.

- `document.json`: 용지 정보, 도형 정보, 텍스트 내용
- `background.png`: 선택된 이미지 배경

이 형식은 프로그램 전용 포맷으로, 템플릿을 안전하게 보관하고 확장하기 좋습니다.

## 프로젝트 구조

```text
.
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   └── sgape_in_text/
│       ├── __init__.py
│       ├── editor.py
│       ├── models.py
│       └── template_manager.py
├── tests/
│   └── test_template_manager.py
├── docs/
│   ├── ARCHITECTURE.md
│   └── GITHUB_SETUP.md
├── .github/
│   └── workflows/
│       └── python-tests.yml
└── .sit
```

## GitHub 연동 절차

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<your-user>/<your-repo>.git
git push -u origin main
```

## 향후 업그레이드 아이디어

- 텍스트 스타일 관리: 글꼴, 색상, 정렬, 줄 간격
- 다중 페이지 템플릿 지원
- 도형 크기 조절 및 드래그 이동
- 고급 이미지 마스킹 기능
- 자동 텍스트 배치 로직
- JSON 내보내기/가져오기
- 플러그인 구조로 모듈 확장

## 문서

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/GITHUB_SETUP.md](docs/GITHUB_SETUP.md)

## 라이선스

본 예제는 학습용 데모 프로젝트이며, 필요에 따라 자유롭게 수정하여 사용하실 수 있습니다.
