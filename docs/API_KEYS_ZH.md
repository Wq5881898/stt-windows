# API Key 申请与配置

**简体中文** | [English](API_KEYS_EN.md) | [返回 README](../README.md)

## Gladia：必需

1. 打开 [Gladia](https://app.gladia.io/)，注册并登录。
2. 在控制台 **API keys** 中创建或复制 Key；[官方说明](https://support.gladia.io/article/how-to-get-the-api-key-from-my-account)。
3. 客户端 → **API Key Management** → Gladia → **Add Key** → 粘贴 → **Save**。
4. 点击 **Test All Keys**，再用一个短录音验证转写。

支持保存多个 Key。程序按供应商返回的拒绝/限额错误切换 Key，控制台中的 `Free limit reached (estimated)` 是根据可见任务估算的提示，不代表账单或远端必定停止服务。真实额度、套餐与余额请查 Gladia 控制台，不保证固定免费额度或重置周期。

## MiniMax：翻译的默认选择

1. 选择与账户地区一致的平台：[中国区](https://platform.minimax.cn/) 或 [国际区](https://platform.minimax.io/)。旧中国区入口 `platform.minimaxi.com` 可能跳转到新平台。
2. 登录，进入 **API Keys** 创建 Key；根据账户情况开通 API 或充值。参考 [官方准备说明](https://platform.minimax.io/docs/guides/quickstart-preparation)。
3. Key 管理窗口 → **MiniMax M3** 页，填写 Key、Base URL 和 Model。

| 账户 | Base URL | Model |
| --- | --- | --- |
| 中国区普通 API | `https://api.minimax.cn/v1` | `MiniMax-M3` |
| 国际区普通 API | `https://api.minimax.io/v1` | `MiniMax-M3` |
| 已验证可用的旧中国区地址 | `https://api.minimaxi.com/v1` | `MiniMax-M3` |

请以 [中国区 OpenAI 兼容文档](https://platform.minimax.cn/docs/api-reference/text-openai-api) 和账户权限为准。Key 与地区不能随意混用。程序调用 OpenAI 兼容的 `chat/completions`，因此不要填写 `/anthropic` 或完整的 `/chat/completions` 地址。

点击 **Test All Keys** → **Save**，主界面开启 **Translate English to Chinese** 并选择 MiniMax。测试会发送一条很短的请求，可能产生少量计费；不提供官方余额查询。

## GLM

1. 登录 [Z.AI](https://z.ai/)，打开 [API Keys](https://z.ai/manage-apikey/apikey-list) 创建 Key。
2. 参考 [普通 API 快速入门](https://docs.z.ai/guides/overview/quick-start)，确认模型权限和 API 余额。
3. GLM 页填 Key，普通 API 的 Base URL 为 **`https://api.z.ai/api/paas/v4`**，Model 可填有权限的 **`glm-5.3-flash`** / **`glm-5.3`**。

旧配置可能保留 `https://api.z.ai/api/coding/paas/v4`；这是 Coding Plan 专用地址。普通翻译使用普通 API 地址，Coding Plan 是否允许此用途请查看供应商规则。`404` / 模型无权限不等于 Key 本身一定失效。

## 自部署 Qwen

向服务管理员确认这三项，在 Qwen 页填写后测试、保存：

```text
Base URL: https://your-qwen-host.example.com/v1
API Key: 由管理员提供
Model: 服务实际暴露的模型名称
```

服务必须支持 OpenAI 兼容 Chat Completions 与 SSE 流式返回，服务端和代理也必须允许持续流式连接。程序按批次串行翻译，保存检查点，不会把一个文件的所有分段同时压到服务器。

## 手工配置与迁移

Key 管理窗口已支持填写上述全部字段。也可在程序关闭后编辑同级 `config/minimax.json`、`glm.json`、`qwen.json`：

```json
{
  "base_url": "https://api.minimax.io/v1",
  "api_key": "your-api-key",
  "model": "MiniMax-M3"
}
```

转写 Key 在 `config/gladia_keys.txt`，每行一个。`*_API_KEY`、`*_BASE_URL`、`*_MODEL` 环境变量优先于文件，三个前缀分别为 `MINIMAX`、`GLM`、`QWEN`。迁移配置只需私下复制 `config`；不要提交真实文件到 GitHub。
