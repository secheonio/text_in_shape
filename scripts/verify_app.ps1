# Text in Shape 검증용 실행 스크립트
# 사용법:
#   powershell -ExecutionPolicy Bypass -File .\scripts\verify_app.ps1

$ErrorActionPreference = "Stop"

$repoRoot = "d:\VSCode\text_in_shape"
$serverUrl = "http://127.0.0.1:5000/"

Set-Location $repoRoot

Write-Host "[1/6] 저장소 상태 확인"
Get-ChildItem
Write-Host "---"

Write-Host "[2/6] git 상태 확인"
git status --short --branch
Write-Host "---"

Write-Host "[3/6] 테스트 실행"
pytest -q
Write-Host "---"

Write-Host "[4/6] 서버 실행"
$server = Start-Process -FilePath "python" -ArgumentList "main.py" -PassThru -WindowStyle Minimized
Start-Sleep -Seconds 2

Write-Host "[5/6] 브라우저 접속 확인"
Start-Process $serverUrl

Write-Host "[6/6] 브라우저 검증 체크리스트 확인"
Write-Host "- http://127.0.0.1:5000 에서 UI 로딩 확인"
Write-Host "- 도형 생성 확인"
Write-Host "- 선택/이동 확인"
Write-Host "- 회전 입력 확인"
Write-Host "- trim 확인"
Write-Host "- 저장/불러오기 확인"
Write-Host "---"

Write-Host "검증 절차가 시작되었습니다. 브라우저에서 체크리스트를 따라 확인해 주세요."
