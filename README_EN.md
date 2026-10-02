# stt-windows

[简体中文](README.md) | **English**

A Windows desktop app that turns audio and video into TXT transcripts or SRT subtitles. Queue local files, preserve the original language, optionally translate English into Chinese, and split long recordings automatically.

[Download for Windows](https://github.com/Wq5881898/stt-windows/releases/latest) · [API key setup](docs/API_KEYS_EN.md) · [Report an issue](https://github.com/Wq5881898/stt-windows/issues) · [Web edition](https://github.com/Wq5881898/stt-web)

## Get started in five minutes

1. Open [Releases](https://github.com/Wq5881898/stt-windows/releases/latest). Download **`stt-windows-x64-vVERSION.zip`**, rather than GitHub's `Source code` archive.
2. Extract the entire ZIP into a writable directory, such as `D:\Apps\stt-windows`.
3. Open the extracted `video2text` folder and double-click **`video2text.exe`**. Keep `_internal`, `config`, and `outputs` beside the EXE.
4. Open **API Key Management**. Under Gladia, click **Add Key**, paste your key, and click **Save**.
5. Drop a recording or video, choose `txt` / `srt` and an **Output Folder**, then click **Start Processing**. Use **Open Result File** when it finishes.

The release includes Python, Qt, ffmpeg, and ffprobe. No separate runtime installation is needed. Use 64-bit Windows 10/11; transcription and translation require internet access and your own API keys. The application is unsigned, so Windows may display a warning. Check the source and the published SHA256.

## Get API keys

| Service | Registration / key management | Required? |
| --- | --- | --- |
| Gladia transcription | [Gladia dashboard](https://app.gladia.io/) → API keys | Yes |
| MiniMax translation | [China platform](https://platform.minimax.cn/) / [International platform](https://platform.minimax.io/) → API Keys | Choose one translation provider |
| GLM translation | [Z.AI API Keys](https://z.ai/manage-apikey/apikey-list) | Choose one translation provider |
| Qwen translation | Obtain the Base URL, API key, and model name from your server administrator | Choose one translation provider |

For transcription alone, only Gladia is needed. To translate, enable **Translate English to Chinese** and choose a configured **Translation Model**. The key dialog lets you enter **Key, Base URL, and Model**. Click **Test All Keys** to check connectivity, then **Save**.

MiniMax China and international accounts use different endpoints. GLM's general API and Coding Plan also differ. See the [key guide](docs/API_KEYS_EN.md) for exact addresses and quota caveats. Provider usage may be billed separately.

## Choose output

| Setting | What to choose |
| --- | --- |
| Source Language | Auto Detect by default; Chinese for Chinese recordings |
| Output | `txt` for reading; `srt` for timed subtitles |
| Output Folder | Final files go here and keep the source filename stem |
| Translate English to Chinese | Add Chinese to English segments while keeping the English text |

Recordings longer than 8,000 seconds are split and merged into one result, with continuous SRT timestamps. Failed tasks keep checkpoints and intermediate audio for retry. Success removes generated intermediate audio; your original file and final output remain.

## Configuration and cache

| Run mode | Credentials | Job cache |
| --- | --- | --- |
| EXE | `config\` beside `video2text.exe` | `outputs\work\jobs\` beside the EXE |
| Python source | `config\` at the repository root | Root `outputs\work\jobs\` |

`gladia_keys.txt` holds one key per line. Translation settings use `minimax.json`, `glm.json`, and `qwen.json`. Provider environment variables and `VIDEO2TEXT_CONFIG_DIR` take precedence when set. Public releases contain no credentials.

## Run from source

Install [Python 3.11+](https://www.python.org/downloads/windows/) with Add Python to PATH enabled and [Git](https://git-scm.com/downloads/win), then run in PowerShell:

```powershell
git clone https://github.com/Wq5881898/stt-windows.git
cd stt-windows
powershell -ExecutionPolicy Bypass -File scripts\desktop\setup.ps1
.\run_gui.bat
```

Source users need [FFmpeg](https://ffmpeg.org/download.html#build-windows) for video and long recordings. Add its `bin` directory containing both `ffmpeg.exe` and `ffprobe.exe` to PATH. The launcher prefers the repository's `.venv`.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Missing Gladia key | Save it in API Key Management; check this installation's `config` and environment overrides |
| QtCore / DLL import failure | Extract the complete ZIP again; check whether antivirus quarantined `_internal` files |
| Chinese becomes English | Select Chinese / Auto Detect and disable translation if unnecessary |
| 401 / 403 | Check key, region, endpoint, and permissions |
| 402 / 429 | Check provider balance, quota, and rate limits; valid authentication does not guarantee free capacity |
| Processing takes too long | Read Runtime Log and Task Details; keep the failed job and retry after restoring connectivity |
| Video has no audio | A decodable audio track is required |

Include the application version and redacted logs in bug reports. Never post API keys.

## Development and releases

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
powershell -ExecutionPolicy Bypass -File scripts\desktop\build_release.ps1
powershell -ExecutionPolicy Bypass -File scripts\desktop\package_public_release.ps1
```

Build overrides: `-PythonExe`, `-FfmpegPath`, and `-FfprobePath`. The build discovers local `.venv`, `tools/ffmpeg/bin`, or PATH. Publish only sanitized ZIP and SHA256 files from `release/artifacts`. See [packaging details](docs/PACKAGING_AND_DEPLOY.md).

Relevant history was preserved when splitting from `video2text`. Web and Docker are maintained in `stt-web`. Historical DeepL batch tools under `outputs/work` are separate from the current MiniMax / GLM / Qwen desktop workflow. The download-first structure follows the example of [Buzz](https://github.com/chidiwilliams/buzz).
