# Windows Packaging And Release

## Source Run

```powershell
git clone https://github.com/Wq5881898/stt-windows.git
cd stt-windows
powershell -ExecutionPolicy Bypass -File scripts\desktop\setup.ps1
.\run_gui.bat
```

## Build

Use the local `.venv` created by setup, or pass `-PythonExe`. Put ffmpeg and ffprobe on PATH or in `tools/ffmpeg/bin`, or supply explicit paths:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\desktop\build_release.ps1
# Explicit overrides when tools are not on PATH:
# powershell -ExecutionPolicy Bypass -File scripts\desktop\build_release.ps1 -PythonExe C:\Python312\python.exe -FfmpegPath C:\ffmpeg\bin\ffmpeg.exe -FfprobePath C:\ffmpeg\bin\ffprobe.exe
```

The runnable one-folder build is written under:

```text
release\video2text\video2text\
```

Keep `video2text.exe`, `_internal/`, `config/`, and `outputs/` together. Moving only the EXE breaks Qt, ffmpeg, configuration, and cache paths.

## Public Artifact

```powershell
powershell -ExecutionPolicy Bypass -File scripts\desktop\package_public_release.ps1
```

The script:

- copies the verified one-folder build into a clean staging directory;
- replaces all local API keys with safe empty templates;
- removes runtime jobs and logs;
- scans staged files for credentials;
- creates a versioned ZIP and SHA256 file under `release\artifacts\`.

The public ZIP is named `stt-windows-x64-vVERSION.zip`, contains `video2text/video2text.exe`, and includes Chinese/English README and key guides. The EXE stays in its complete folder. A tag must point at the commit used to build its release.

Never upload `release\video2text\` directly. Publish only the sanitized artifacts to [stt-windows Releases](https://github.com/Wq5881898/stt-windows/releases).

## Verification

`build_release.ps1` invokes `scripts\desktop\smoke_test_release.ps1`. The checks cover imports, Qt DLL loading, configuration paths, deduplication, long-audio splitting and merge timestamps, and GUI initialization. Paid Gladia or LLM calls are intentionally excluded.
