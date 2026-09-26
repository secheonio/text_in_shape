# Render 배포용 최종 문서

## 1. 프로젝트 상태 요약

이 프로젝트는 Flask 기반 웹 애플리케이션입니다. 따라서 GitHub Pages 같은 정적 호스팅이 아니라 Render의 Python Web Service로 배포하는 것이 맞습니다.

핵심 확인 사항:
- 실행 진입점: `main.py`
- Flask 앱 생성: `create_app()`
- 시작 명령: `gunicorn main:app`
- 의존성 파일: `requirements.txt`
- 배포 설정 파일: `render.yaml`

## 2. 이미 준비된 설정

### `render.yaml`

```yaml
services:
  - type: web
    name: text-in-shape
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn main:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.12.7
```

### `main.py`

```python
import os

from src.text_in_shape.web_app import create_app

app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
```

## 3. GitHub에 최신 코드 반영

복붙용 명령:

```bash
git add .
git commit -m "Prepare Render deployment"
git branch -M main
git push origin main
```

브랜치가 `master`라면 아래처럼 사용합니다.

```bash
git add .
git commit -m "Prepare Render deployment"
git push origin master
```

## 4. Render에서 서비스 생성

1. https://render.com 에 로그인
2. Dashboard에서 `New` → `Web Service` 선택
3. GitHub 저장소 연결
4. 이 프로젝트 repo 선택
5. 아래 값을 입력

### Render 설정값

- Name: `text-in-shape`
- Region: 가장 가까운 지역
- Runtime: `Python`
- Branch: `main` 또는 기본 브랜치
- Root Directory: 비움
- Build Command:

```bash
pip install -r requirements.txt
```

- Start Command:

```bash
gunicorn main:app
```

- Python Version: `3.12.7`
- Plan: `Free`

6. `Create Web Service` 클릭

## 5. 배포 확인

배포가 완료되면 Render에서 서비스 URL이 생성됩니다. 보통 아래와 같은 형태입니다.

```text
https://text-in-shape.onrender.com
```

브라우저에서 해당 URL을 열어 다음을 확인합니다.
- 페이지가 정상적으로 로드됨
- 캔버스가 보임
- 도형을 생성할 수 있음
- 선택/이동/회전/trim 동작이 동작함
- 서버 로그에 오류가 없음

## 6. 문제 해결

### Gunicorn 실행 오류

로그에 `gunicorn: command not found` 또는 `ModuleNotFoundError`가 나오면 아래를 확인합니다.

```bash
pip install -r requirements.txt
```

그리고 Start Command가 다음인지 확인합니다.

```bash
gunicorn main:app
```

### 앱 import 오류

`ImportError` 또는 `No module named ...`가 나오면 다음 import가 올바른지 확인합니다.

```python
from src.text_in_shape.web_app import create_app
```

### 정적 호스팅 실수 방지

이 프로젝트는 정적인 웹 페이지가 아니므로 GitHub Pages로는 배포하지 않습니다.
Render를 사용해야 합니다.

## 7. 최종 체크리스트

- [ ] GitHub repo 연결됨
- [ ] `pip install -r requirements.txt` 설정됨
- [ ] `gunicorn main:app` 설정됨
- [ ] Python 버전 3.12.7 설정됨
- [ ] 서비스가 `Live` 상태
- [ ] 브라우저에서 앱이 정상 로드됨
- [ ] 주요 기능 확인 완료

## 8. 최종 복붙용 요약

```bash
git add .
git commit -m "Prepare Render deployment"
git push origin main
```

```bash
pip install -r requirements.txt
```

```bash
gunicorn main:app
```

Render 설정값:
- Python
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn main:app`
- Python Version: `3.12.7`
- Plan: `Free`
