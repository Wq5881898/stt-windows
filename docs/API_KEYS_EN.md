# API key setup

[简体中文](API_KEYS_ZH.md) | **English** | [Back to README](../README_EN.md)

## Gladia: required

1. Register and sign in at the [Gladia dashboard](https://app.gladia.io/).
2. Create or copy a key in **API keys**. See the [official instructions](https://support.gladia.io/article/how-to-get-the-api-key-from-my-account).
3. Open **API Key Management** → Gladia → **Add Key**, paste, then **Save**.
4. Click **Test All Keys**, then transcribe a short recording.

Multiple keys are supported. Rotation follows actual provider rejection or limit responses. `Free limit reached (estimated)` is estimated from visible jobs, not an authoritative balance or guarantee that requests will stop. Check current billing and quota in the provider dashboard; no fixed free allowance or reset schedule is promised.

## MiniMax: default translation provider

1. Use the platform for your account region: [China](https://platform.minimax.cn/) or [International](https://platform.minimax.io/). The previous China hostname may redirect to the new platform.
2. Create a key under **API Keys** and activate API access or fund the account if required. See [official prerequisites](https://platform.minimax.io/docs/guides/quickstart-preparation).
3. In the **MiniMax M3** tab, enter the key, Base URL, and model.

| Account | Base URL | Model |
| --- | --- | --- |
| China general API | `https://api.minimax.cn/v1` | `MiniMax-M3` |
| International general API | `https://api.minimax.io/v1` | `MiniMax-M3` |
| Previously tested China endpoint | `https://api.minimaxi.com/v1` | `MiniMax-M3` |

Follow the [OpenAI compatibility documentation](https://platform.minimax.cn/docs/api-reference/text-openai-api) and your account's permissions. Match the key's region. The app uses Chat Completions, so the Base URL must not end in `/anthropic` or `/chat/completions`.

Click **Test All Keys**, then **Save**. Enable translation and select MiniMax in the main window. A connectivity test sends a tiny request that may incur a small charge; it does not query an official balance.

## GLM

1. Sign in at [Z.AI](https://z.ai/) and create an [API key](https://z.ai/manage-apikey/apikey-list).
2. Check model access and API balance using the [general API quick start](https://docs.z.ai/guides/overview/quick-start).
3. In the GLM tab, use **`https://api.z.ai/api/paas/v4`** for the general API and an accessible model such as **`glm-5.3-flash`** or **`glm-5.3`**.

Older configurations may use `https://api.z.ai/api/coding/paas/v4`, which is the dedicated Coding Plan endpoint. Use general API access for ordinary translation and check the provider's rules before using a Coding Plan. A model access error does not necessarily mean the key is invalid.

## Self-hosted Qwen

Ask your administrator for these values, enter them in the Qwen tab, test, and save:

```text
Base URL: https://your-qwen-host.example.com/v1
API Key: supplied by your administrator
Model: exact name exposed by the server
```

The server must support OpenAI-compatible Chat Completions and SSE streaming. Its proxy must also allow sustained streams. Translation batches run serially with checkpoints.

## Files and migration

All connection fields are editable in the key dialog. Alternatively, close the app and edit `config/minimax.json`, `glm.json`, or `qwen.json` beside it:

```json
{
  "base_url": "https://api.minimax.io/v1",
  "api_key": "your-api-key",
  "model": "MiniMax-M3"
}
```

Gladia keys live in `config/gladia_keys.txt`, one per line. Provider `*_API_KEY`, `*_BASE_URL`, and `*_MODEL` environment variables override files; prefixes are `MINIMAX`, `GLM`, and `QWEN`. Copy your configuration privately when migrating. Never commit real keys.
