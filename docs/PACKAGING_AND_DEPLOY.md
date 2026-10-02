# Windows Packaging And Release

## Source Run

```powershell
git clone https://github.com/Wq5881898/stt-windows.git
cd stt-windows
run_gui.bat
```

## Build

Use the project Python environment that contains PyQt6 and PyInstaller:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\desktop\build_release.ps1
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

Never upload `release\video2text\` directly. Publish only the sanitized artifacts to [stt-windows Releases](https://github.com/Wq5881898/stt-windows/releases).

## Verification

`build_release.ps1` invokes `scripts\desktop\smoke_test_release.ps1`. The checks cover imports, Qt DLL loading, configuration paths, deduplication, long-audio splitting and merge timestamps, and GUI initialization. Paid Gladia or LLM calls are intentionally excluded.
