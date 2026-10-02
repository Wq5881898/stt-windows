# v0.1.1

## 简体中文

拆分后的独立 Windows 客户端公开版。

- EXE、Qt、Python、ffmpeg/ffprobe 同包提供；完整解压即可启动。
- 附带可切换的中英文 README、Gladia 和翻译 Key 申请/配置教程。
- Key 管理窗口可填写翻译 Base URL 与模型名，测试当前未保存的连接配置。
- 源码安装优先使用本仓库 `.venv`；构建不再依赖开发者的硬编码路径。
- 公开包清除真实 Key、任务缓存与日志，再执行配置、Qt、去重、长音频、拖拽目标冒烟测试。

请在 API Key Management 添加自己的 Gladia Key；翻译按需配置。公开包不包含任何 Key。应用未签名，下载后可核对 SHA256。

## English

The first public release of the standalone Windows repository.

- Complete portable folder with EXE, Qt, Python, and ffmpeg/ffprobe.
- Chinese/English installation and API key documentation.
- Editable translation Base URL and model; connectivity checks use current form values.
- Local `.venv` launcher and portable build-tool discovery.
- Sanitized credentials/cache/logs, followed by packaged configuration, Qt, deduplication, long-audio and drag/drop smoke checks.

Supply your own Gladia key and optional translation credentials. The release contains no API keys and is unsigned. A SHA256 checksum accompanies the archive.
