# stt-windows

Windows desktop client for converting local audio and video files into TXT or SRT transcripts.

This repository is intentionally independent from the web product. The companion web repository is [stt-web](https://github.com/Wq5881898/stt-web).

## Capabilities

- drag files or folders into a local processing queue;
- Auto, English, Chinese, and English + Chinese source-language modes;
- TXT and SRT output;
- optional English-to-Chinese translation using MiniMax M3, GLM, or Qwen;
- streaming, serial translation batches with checkpoints;
- automatic splitting and merging for recordings longer than 8,000 seconds;
- resumable Gladia jobs and retained failed-job media;
- local API key management, environment checks, logs, presets, and recent outputs.

## Start From Source

From the repository root:

```powershell
run_gui.bat
```

Or run the entry point directly:

```powershell
python apps\desktop\main.py
```

`run_gui.bat` sets the repository root and `PYTHONPATH`, preventing `ModuleNotFoundError: packages` when launched from another directory.

## Local Configuration

The source version reads credentials from `config/`:

- `config/gladia_keys.txt`: one Gladia key per line;
- `config/minimax.json`;
- `config/glm.json`;
- `config/qwen.json`.

The packaged EXE reads the same file names from `<exe-folder>\config\`. Real credentials are ignored by Git and must never be committed.

## Repository Layout

```text
apps/desktop/          PyQt6 desktop application
packages/shared_core/  transcription, translation, and media pipeline
outputs/work/          runtime helper modules and historical batch tools
scripts/desktop/       build, smoke-test, and public packaging scripts
config/                safe examples; local secrets are ignored
tests/                 desktop and long-audio tests
```

## Tests

```powershell
python -m unittest tests.test_bilingual_rendering tests.test_desktop_long_audio
```

## Build And Public Package

```powershell
powershell -ExecutionPolicy Bypass -File scripts\desktop\build_release.ps1
powershell -ExecutionPolicy Bypass -File scripts\desktop\package_public_release.ps1
```

The public packaging step replaces local keys with empty templates and scans the package for credential leakage. Upload only artifacts from `release\artifacts\`; never publish the private test build under `release\video2text\`.

See [Packaging and deployment](docs/PACKAGING_AND_DEPLOY.md) and [current status](docs/CURRENT_STATE_ZH.md) for operational details.

## Repository Split

This project was split from `Wq5881898/video2text` on 2026-10-02 with its relevant Git history preserved. Web, Vercel, NAS Worker, and Docker deployment code now live only in `stt-web`.
