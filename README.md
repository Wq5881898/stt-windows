# stt-windows

**简体中文** | [English](README_EN.md)

把音频、视频转换为 TXT 文稿或 SRT 字幕的 Windows 客户端。支持队列、中文原文转写、英文转中文，以及长录音自动切分后合并。

[下载 Windows 版](https://github.com/Wq5881898/stt-windows/releases/latest) · [申请与配置 Key](docs/API_KEYS_ZH.md) · [问题反馈](https://github.com/Wq5881898/stt-windows/issues) · [网页版](https://github.com/Wq5881898/stt-web)

## 五分钟开始使用

1. 打开 [Releases](https://github.com/Wq5881898/stt-windows/releases/latest)，下载 **`stt-windows-x64-v版本号.zip`**，不要下载 GitHub 的 `Source code`。
2. 右键 ZIP，选择“全部解压缩”，放到可写的目录，例如 `D:\Apps\stt-windows`。
3. 打开解压后的 `video2text` 文件夹，双击 **`video2text.exe`**。保留整个文件夹；`_internal`、`config`、`outputs` 都是程序的一部分。
4. 进入顶部 **API Key Management**，在 Gladia 区点击 **Add Key**，粘贴自己的 Key，点击 **Save**。
5. 拖入录音或视频，选择 `txt` / `srt` 和 **Output Folder**，点击 **Start Processing**。完成后点击 **Open Result File**。

EXE 已包含 Python、Qt、ffmpeg 和 ffprobe，不需要另外安装。支持 Windows 10/11 64 位；转写与翻译需要联网和自己的 API Key。Windows 可能提示未签名应用，请先核对下载来源与 SHA256。

## Key 从哪里申请

| 用途 | 申请入口 | 是否必需 |
| --- | --- | --- |
| Gladia 音频转文字 | [Gladia 控制台](https://app.gladia.io/) → API keys | 必需 |
| MiniMax 翻译 | [中国区平台](https://platform.minimax.cn/) / [国际平台](https://platform.minimax.io/) → API Keys | 翻译时三选一 |
| GLM 翻译 | [Z.AI API Keys](https://z.ai/manage-apikey/apikey-list) | 翻译时三选一 |
| Qwen 翻译 | 自己部署的服务管理员提供 Base URL、Key、模型名 | 翻译时三选一 |

只转写不翻译，只需 Gladia。开启 **Translate English to Chinese** 后，在 **Translation Model** 选择配置好的模型。Key 管理窗口可以填写 **Key、Base URL、Model**，点击 **Test All Keys** 检查连通性，再点击 **Save**。

MiniMax 中国区与国际区使用不同地址，GLM 普通 API 与 Coding Plan 也不同。详细地址、注册步骤、用量说明见 [Key 教程](docs/API_KEYS_ZH.md)。供应商可能收费，请以各自控制台的额度与账单为准。

## 常用设置

| 设置 | 建议 |
| --- | --- |
| Source Language | 默认 Auto Detect；中文录音可选 Chinese，保持中文原文 |
| Output | `txt` 阅读文稿；`srt` 带时间轴的字幕 |
| Output Folder | 最终结果保存到这个目录；输出文件名沿用源文件名 |
| Translate English to Chinese | 给英文片段添加中文译文，保留英文；中文片段不强制翻成英文 |

录音超过 8,000 秒会自动分段转写，再合并为一个结果；SRT 时间轴按原录音连续排列。任务失败时保留检查点和中间音频，便于重试；成功后清理生成的中间音频，源文件和最终结果保留。

## Key 和缓存保存在哪里

| 运行方式 | 配置 | 任务缓存 |
| --- | --- | --- |
| EXE | `video2text.exe` 同级 `config\` | 同级 `outputs\work\jobs\` |
| Python 源码 | 仓库根目录 `config\` | 根目录 `outputs\work\jobs\` |

`config/gladia_keys.txt` 每行一个 Key；翻译配置为 `minimax.json`、`glm.json`、`qwen.json`。设置了供应商环境变量或 `VIDEO2TEXT_CONFIG_DIR` 时，环境变量优先。公开 Release 不带 Key。

## 从源码运行

普通用户直接使用 EXE。开发者安装 [Python 3.11+](https://www.python.org/downloads/windows/) 和 [Git](https://git-scm.com/downloads/win)，Python 安装时勾选 Add Python to PATH，然后在 PowerShell 执行：

```powershell
git clone https://github.com/Wq5881898/stt-windows.git
cd stt-windows
powershell -ExecutionPolicy Bypass -File scripts\desktop\setup.ps1
.\run_gui.bat
```

源码处理视频或长音频还需要 [FFmpeg](https://ffmpeg.org/download.html#build-windows)，把包含 `ffmpeg.exe` 和 `ffprobe.exe` 的 `bin` 目录加入 PATH。`run_gui.bat` 优先使用本仓库 `.venv`；从其他目录双击也可启动。

## 常见问题

| 问题 | 怎么处理 |
| --- | --- |
| 提示缺少 Gladia Key | 在 API Key Management 保存，确认使用当前程序同级 `config`，并检查过期环境变量覆盖 |
| QtCore / DLL 加载失败 | 重新完整解压 Release；不要单独复制 EXE；检查杀毒软件是否隔离 `_internal` 文件 |
| 中文录音变英文 | Source Language 选 Chinese / Auto Detect；不需要翻译时取消翻译选项 |
| 401 / 403 | 检查 Key、Base URL 所属地区和服务权限 |
| 402 / 429 | 查看供应商余额、额度和频率限制；有效 Key 不等于还有免费额度 |
| 长时间无结果 | 查看 Runtime Log 和 Task Details，保留失败任务，恢复网络后重试 |
| 视频没有声音 | 文件必须包含可解码音轨 |

反馈问题时附上程序版本和脱敏日志，不要贴 Key。

## 开发与打包

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
powershell -ExecutionPolicy Bypass -File scripts\desktop\build_release.ps1
powershell -ExecutionPolicy Bypass -File scripts\desktop\package_public_release.ps1
```

构建脚本支持 `-PythonExe`、`-FfmpegPath`、`-FfprobePath`；优先使用 `.venv`、`tools/ffmpeg/bin` 或 PATH。只发布 `release/artifacts` 中脱敏后的 ZIP 与 SHA256，详见 [打包说明](docs/PACKAGING_AND_DEPLOY.md)。

本项目从 `video2text` 拆分并保留相关历史；Web 与 Docker 在独立的 `stt-web` 仓库。`outputs/work` 下保留历史 DeepL 批处理脚本，桌面产品当前使用 MiniMax / GLM / Qwen。安装说明组织参考 [Buzz](https://github.com/chidiwilliams/buzz) 的下载入口与快速入门结构。
