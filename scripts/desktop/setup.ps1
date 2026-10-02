param([string]$PythonExe = 'python')
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $root
$venvPython = Join-Path $root '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $venvPython)) {
  & $PythonExe -m venv (Join-Path $root '.venv')
  if ($LASTEXITCODE -ne 0) { throw 'Install Python 3.11 or newer with Add Python to PATH enabled.' }
}
& $venvPython -m pip install -r (Join-Path $root 'requirements.txt')
if ($LASTEXITCODE -ne 0) { throw 'Dependency installation failed. Check the preceding pip error.' }
Write-Host 'Setup complete. Run .\run_gui.bat and open API Key Management.'
Write-Host 'Source users need ffmpeg and ffprobe on PATH for video and long recordings.'
