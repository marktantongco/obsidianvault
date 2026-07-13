---
title: API Key Guide
type: reference
created: 2026-07-09
updated: 2026-07-09
tags: [api, keys, configuration]
---

# API Key Guide

**Last Updated**: 2026-07-09

---

## Current Status

| Provider | Status | Key Location |
|----------|--------|--------------|
| OpenAI | ✅ Configured | `~/.opencode/.env` |
| Anthropic | ⏳ Pending | — |
| Google Gemini | ⏳ Pending | — |
| Xiaomi MiMo | ⏳ Pending | — |

---

## 1. OpenAI — CONFIGURED ✅

### Status
Already configured during setup.

### Location
```bash
~/.opencode/.env
~/.claude/.env
~/.hermes/hermes-agent/.env
~/.codex/.env
```

### Verify
```bash
cat ~/.opencode/.env | head -1
# Should show: OPENAI_API_KEY=sk-proj-...
```

### Usage
- OpenCode: Default provider
- Codex: Primary provider
- Claude Code: Fallback provider
- Hermes: Fallback provider

---

## 2. Anthropic (Claude) — PENDING ⏳

### Why Needed
- Claude Code uses Anthropic API directly
- Better performance for code review
- Access to Claude 3.5/4 models

### How to Get

#### Step 1: Create Account
1. Go to: https://console.anthropic.com/
2. Click "Sign Up"
3. Create account with email
4. Verify email

#### Step 2: Add Credits
1. Go to "Billing"
2. Add payment method
3. Add credits ($5 minimum recommended)

#### Step 3: Create API Key
1. Go to "API Keys"
2. Click "Create Key"
3. Name it: "claude-code"
4. Copy the key (starts with `sk-ant-`)

#### Step 4: Configure
```bash
# Add to Claude Code
echo "ANTHROPIC_API_KEY=sk-ant-..." >> ~/.claude/.env

# Add to OpenCode (optional)
echo "ANTHROPIC_API_KEY=sk-ant-..." >> ~/.opencode/.env
```

### Pricing
- Claude 3.5 Sonnet: $3/1M input, $15/1M output
- Claude 3 Opus: $15/1M input, $75/1M output
- Claude 3 Haiku: $0.25/1M input, $1.25/1M output

---

## 3. Google Gemini — PENDING ⏳

### Why Needed
- Free tier available
- Good for testing
- Fast response times

### How to Get

#### Step 1: Go to AI Studio
1. Go to: https://aistudio.google.com/apikey
2. Sign in with Google account

#### Step 2: Create API Key
1. Click "Create API key"
2. Select project (or create new)
3. Copy the key

#### Step 3: Configure
```bash
# Add to agents
echo "GEMINI_API_KEY=..." >> ~/.opencode/.env
echo "GEMINI_API_KEY=..." >> ~/.hermes/hermes-agent/.env
```

### Pricing (Free Tier)
- 60 requests/minute
- 32K tokens/request
- No credit card required

---

## 4. Xiaomi MiMo — PENDING ⏳

### Why Needed
- Access to MiMo models
- 1000 free web searches/day
- Good for Chinese language tasks

### How to Get

#### Step 1: Create Account
1. Go to: https://mimo.mi.com
2. Sign up with email/phone
3. Verify account

#### Step 2: Get API Key
1. Go to Console
2. Navigate to API Keys
3. Create new key
4. Copy the key

#### Step 3: Configure
```bash
# Add to MiMo Code
mimo auth login
# Follow prompts to authenticate
```

### Pricing
- Pay-as-you-go available
- Token Plan subscriptions
- 1000 free web searches/day

---

## 5. Configuration Files

### Location Summary
```bash
~/.opencode/.env      # OpenCode
~/.claude/.env        # Claude Code
~/.hermes/hermes-agent/.env  # Hermes
~/.codex/.env         # Codex
```

### Format
```bash
# Each file contains:
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...  # optional
GEMINI_API_KEY=...            # optional
```

### Permissions
```bash
# Set secure permissions
chmod 600 ~/.opencode/.env ~/.claude/.env ~/.hermes/hermes-agent/.env ~/.codex/.env
```

---

## 6. Testing API Keys

### Test OpenAI
```bash
export OPENAI_API_KEY=$(grep OPENAI_API_KEY ~/.opencode/.env | cut -d= -f2)
curl -s https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY" | head -20
```

### Test Anthropic
```bash
export ANTHROPIC_API_KEY=$(grep ANTHROPIC_API_KEY ~/.claude/.env | cut -d= -f2)
curl -s https://api.anthropic.com/v1/models \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" | head -20
```

### Test Gemini
```bash
export GEMINI_API_KEY=$(grep GEMINI_API_KEY ~/.opencode/.env | cut -d= -f2)
curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY" | head -20
```

---

## 7. Security Best Practices

1. **Never commit keys to git**
2. **Use .env files** (already done)
3. **Set file permissions** to 600
4. **Rotate keys** periodically
5. **Monitor usage** in provider dashboards
6. **Use separate keys** for different environments

---

## 8. Troubleshooting

### Key Not Found
```bash
# Check if key is set
cat ~/.opencode/.env | grep API_KEY

# Check if file exists
ls -la ~/.opencode/.env
```

### Permission Denied
```bash
# Fix permissions
chmod 600 ~/.opencode/.env
```

### Invalid Key
1. Verify key is copied correctly
2. Check for extra spaces/newlines
3. Regenerate key in provider dashboard
4. Update .env file

---

## Next Steps

1. [ ] Get Anthropic API key
2. [ ] Get Gemini API key
3. [ ] Get MiMo API key
4. [ ] Configure all keys
5. [ ] Test each provider
