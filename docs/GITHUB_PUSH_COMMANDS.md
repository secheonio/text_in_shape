# GitHub push용 명령 정리

## 1. 원격 저장소 확인

```bash
git remote -v
```

원하는 저장소가 `origin`에 연결되어 있는지 확인합니다.

```bash
git remote set-url origin https://github.com/secheonio/shape-in-text.git
```

오타 원격 저장소가 남아 있으면 제거합니다.

```bash
git remote remove origine
```

## 2. 현재 상태 확인

```bash
git status
```

## 3. 변경 사항 추가

```bash
git add .
```

## 4. 커밋

```bash
git commit -m "Prepare Render deployment"
```

## 5. 브랜치 확인

```bash
git branch
```

기본 브랜치가 `main`이라면:

```bash
git branch -M main
git push -u origin main
```

기본 브랜치가 `master`라면:

```bash
git push -u origin master
```

## 6. 이후 반복 푸시

```bash
git add .
git commit -m "Update app"
git push origin main
```

## 7. 전체 복붙용 명령

```bash
git remote -v
git remote set-url origin https://github.com/secheonio/shape-in-text.git
git remote remove origine
git status
git add .
git commit -m "Prepare Render deployment"
git branch -M main
git push -u origin main
```

## 8. 참고

- 이 프로젝트는 Flask 웹앱이므로 GitHub Pages가 아니라 Render로 배포합니다.
- 원격 저장소는 의도한 GitHub repo 하나만 남기는 것이 안전합니다.
