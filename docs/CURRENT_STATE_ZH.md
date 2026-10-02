# stt-windows 当前状态

> 基线日期：2026-10-02

安装与使用以 [中文 README](../README.md) / [English README](../README_EN.md) 为准。`v0.1.1` 是拆分后首个公开 EXE Release；新增中英 Key 教程、可编辑的翻译 Base URL/Model、本地 `.venv` 安装脚本与可移植构建工具路径。

## 已实现

- Windows PyQt6 多文件和文件夹队列，支持拖拽、失败重试和任务恢复。
- TXT/SRT 输出；源语言支持 Auto、English、Chinese、English + Chinese。
- Gladia 转写；英文转中文可选 MiniMax M3、GLM 或 Qwen。
- LLM 翻译采用流式响应、严格串行批次和逐批缓存。
- 超过 8,000 秒的媒体自动均衡切分，逐段转写后合并为单一结果。
- 成功后删除提取音轨和切分文件；失败任务保留中间文件和 checkpoint。
- 客户端可维护和检测 Gladia、MiniMax、GLM、Qwen 配置。
- PyInstaller one-folder 打包，内置 ffmpeg/ffprobe，并执行构建后 smoke tests。

## 路径

| 运行方式 | Key 配置 | Job 缓存 |
|---|---|---|
| Python | 仓库 `config/` | 仓库 `outputs/work/jobs/` |
| EXE | `<exe-folder>/config/` | `<exe-folder>/outputs/work/jobs/` |

真实 Key 不进入 Git。公开 ZIP 只能由 `scripts/desktop/package_public_release.ps1` 生成。

## 项目边界

本仓库不包含网页前端、Vercel API、NAS Worker 或 Docker 部署。网页产品独立位于 [stt-web](https://github.com/Wq5881898/stt-web)。两个仓库运行时互不依赖。
