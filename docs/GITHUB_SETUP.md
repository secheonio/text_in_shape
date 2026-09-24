# GitHub 연동 가이드

## 1. 저장소 초기화

```bash
git init
git branch -M main
git add .
git commit -m "Initial project setup"
```

## 2. 원격 저장소 연결

```bash
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
```

## 3. 브랜치 전략

- `main`: 안정 버전
- `feature/*`: 기능 단위 개발
- `hotfix/*`: 긴급 수정

## 4. 협업 규칙

- 기능별 커밋 메시지 작성
- 테스트 실행 후 푸시
- PR을 통해 기능 검토

## 5. 향후 업그레이드 방향

- 텍스트 포맷 개선
- 도형 생성/수정 기능 고도화
- 템플릿 관리 시스템 개선
- CI 자동 테스트 구성
