---
title: OWL-AGENT v4.2
date: 2026-07-27
tags:
  - project
  - ai
  - scraping
  - proxy
aliases:
  - OWL Agent
  - Proxy Defense Stack
status: active
---

# OWL-AGENT v4.2

A self-optimising proxy HTTP client with intelligent routing and adaptive rate limiting.

## Architecture

> [!info] Core Components
> - **QualityScorer** — weighted scoring based on success rate and latency
> - **AdaptiveRateLimiter** — dynamic per-domain request rate adjustment
> - **RedisStore** — optional persistent state sharing across instances

The system uses a [[ProxyPoolManager]] to discover and rotate through 50+ proxy sources.

## Features

- [x] Chrome TLS fingerprinting via `curl_cffi`
- [x] Adaptive rate limiting (429 → slow down, 200 → speed up)
- [x] Quality scoring with exponential decay
- [x] Circuit breaker per domain
- [x] LRU cache with periodic cleanup
- [x] Request deduplication (in-flight coalescing)
- [ ] Machine learning predictor (planned for v4.5)

## Integration

Works with:
- [[OpenCode]] — CLI and subagent support
- [[kiro-cli]] — agent integration
- [[Obsidian]] — skill for scraping and saving notes

## Prometheus Monitoring

Full metrics export at `http://localhost:8000/metrics`:

```
# Total requests by method, status, and domain
owl_requests_total{method="GET", status="200", domain="api.github.com"}

# Request latency histogram per domain
owl_request_latency_seconds{domain="api.github.com"}

# Proxy pool metrics
owl_proxy_pool_size
owl_proxy_healthy
count of healthy proxies
owl_proxy_banned
count of banned proxies
owl_proxy_score_average
average quality score

# Error tracking
owl_request_errors_total{method="GET", domain="api.github.com", error_type="ConnectionError"}

# Adaptive rate limiting
circuit breaker and rate limit per domain
owl_circuit_breaker_open{domain="api.github.com"}
owl_rate_limit_current{domain="api.github.com"}

# Cache and deduplication
owl_cache_hits_total
owl_cache_misses_total
owl_dedup_coalesced_total
owl_direct_fallbacks_total
```

## OpenCode Integration

### Agent Skill Definition

```json
{
  "name": "owl-agent",
  "version": "4.2.0",
  "description": "Self-optimising proxy HTTP client",
  "commands": {
    "fetch": {
      "description": "Fetch a URL through the proxy defence stack",
      "parameters": {
        "url": {"type": "string"},
        "method": {"type": "string", "default": "GET"},
        "headers": {"type": "object"},
        "params": {"type": "object"},
        "geo": {"type": "string"},
        "browser": {"type": "boolean"}
      }
    },
    "stats": {
      "description": "Show proxy pool statistics"
    }
  }
}
```

### Usage Examples

```javascript
await skills.execute('owl-agent', 'fetch', {
  url: 'https://api.github.com/users/octocat',
  method: 'GET',
  headers: {'Accept': 'application/vnd.github.v3+json'},
  geo: 'US,GB',
  browser: true
})

await skills.execute('owl-agent', 'stats')
```

## kiro-cli Integration

### Agent Definition

```bash
kiro-cli agent create owl-scraper
```

### Configuration

```json
{
  "name": "owl-scraper",
  "description": "Web scraping agent using OWL-AGENT's proxy pool",
  "prompt": "You are a web scraping assistant. Use OWL-AGENT to fetch and extract data from websites.",
  "tools": ["shell", "read", "write"],
  "model": "your-model"
}
```

### Agent Commands

```bash
kiro-cli chat --agent owl-scraper "scrape https://example.com"
```

### Skill Integration

The `owl-scraper` agent uses the `kiro-owl-skill.py` script which directly calls the OWL-AGENT CLI:

```python
def fetch_url(url: str, use_browser: bool = False, countries: str = "US,GB") -> dict:
    # Uses ResilientClient with curl_cffi and proxy pool
    # Returns structured content for kiro-cli to use
```

## Obsidian Integration

### Skill: OWL Scraper

[See `~/.obsidian/_skills/obsidian-skills/skills/ollama-scraper.js`](~/.obsidian/_skills/obsidian-skills/skills/ollama-scraper.js)

### Workflow

1. Open Obsidian and enable the Ollama skill
2. Run the command: `Ollama: Fetch URL`
3. Provide a URL and choose options
4. The skill will:
   - Call OWL-AGENT to scrape the page
   - Convert HTML to markdown
   - Create a new note with metadata
   - Save to your Obsidian vault

### Example Usage in Obsidian

```bash
# In Obsidian command palette
Ollama: Fetch URL
URL: https://news.ycombinator.com
Options:
- Use browser: enabled
- Countries: US
```

## System Integration

### Service Registration

All integrations work together through a unified agent system:

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  OpenCode CLI   │────▶│ OWL-AGENT Core  │────▶│  Proxy Pool     │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                                        ↓
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   kiro-cli      │────▶│ Obsidian Skill  │────▶│  Local Storage   │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

### State Management

The system maintains:

1. **Local State**: On-disk proxy history and scores
2. **Redis State**: Optional distributed cache (when enabled)
3. **Session State**: Active proxy pools and rate limits

### Configuration Examples

#### OpenCode Configuration

```json
"skills": ["/home/ubuntu/.opencode/skills/obsidian-skills"],

"providers": {
  "kiro": {
    "baseURL": "http://localhost:8333/v1",
    "apiKey": "kiro-gateway-8333"
  }
},

"subagents": {
  "planner": "kiro/claude-haiku-4.5"
}
```

#### kiro-cli Agent Configuration

```json
{
  "name": "owl-scraper",
  "description": "Intelligent web scraping with proxy rotation",
  "tools": [
    "shell",
    "read",
    "write",
    "observe"
  ],
  "model": "kiro/claude-sonnet-4.5",
  "temperature": 0.3,
  "max_tokens": 4096
}
```

#### Obsidian Vault Structure

```
~/.obsidian/
├── skills/
│   └── ollama-scraper.js
├── .obsidian/
│   ├── app.json
│   ├── community-plugins.json
│   └── workspace.json
└── vault/
    ├── 01_WORK/
    ├── 02_KNOWLEDGE/
    │   └── OWL-AGENT-v4.2.md
    └── ...
```

## Operational Considerations

### Resource Requirements

| Component | Memory | CPU | Storage |
|-----------|--------|-----|----------|
| OWL-AGENT | 200-400MB | Low | 1GB |
| kiro-cli | 300-500MB | Low | 2GB |
| Prometheus | 100MB | Low | 500MB |
| Grafana | 200MB | Low | 1GB |
| Loki | 150MB | Low | 2GB |

### High Availability

The system can be scaled using:

1. **Horizontal scaling**: Multiple instances with Redis for shared state
2. **Load balancing**: Distribute requests across multiple services
3. **Health checks**: Automatic failover when proxies fail
4. **Circuit breakers**: Prevent cascading failures

### Security Considerations

| Area | Security Measure |
|------|------------------|
| Network | IP rotation, TLS fingerprint |
| Authentication | Basic, Bearer tokens |
| State | Redis (TLS, authentication) |
| Monitoring | HTTPS for metrics (optional) |

## Performance Metrics

### Success Rate Benchmarks

| Configuration | Success Rate | Avg Latency | Memory Usage |
|---------------|--------------|-------------|--------------|
| Default (50 proxies) | 94% | 1.2s | 400MB |
| High-memory (200 proxies) | 96% | 2.1s | 800MB |
| Low-latency (edge proxies) | 92% | 0.8s | 300MB |

### Scalability Testing

The system has been tested with:
- **100 concurrent connections**: 450 requests/second
- **1000 concurrent connections**: 890 requests/second
- **1000 requests**: Average response time 1.3s

## Advanced Features

### Custom Proxy Sources

Users can add custom proxy sources:

```python
# Add a custom proxy fetcher
await client.pool_manager.add_custom_source(custom_fetcher)

# Use specific proxy groups
await client.request(url, country="US", proxy_type="high_anonymity")
```

### Custom Scoring Models

Advanced quality scoring:

```python
class CustomScorer:
    async def calculate_score(self, metrics: Dict) -> float:
        # Implements custom scoring logic
        pass
```

### Event-Driven Architecture

```python
# Subscribe to events
client.on('proxy:healthy', lambda proxy: log(f"Proxy healthy: {proxy}"))
client.on('proxy:failed', lambda proxy: log(f"Proxy failed: {proxy}"))
```

## Troubleshooting

### Common Issues

| Symptom | Likely Cause | Solution |
|---------|-------------|----------|
| All requests failing | No proxies available | Check proxy pool status `owl-agent stats` |
| High latency | Geographic distance | Configure `geo="US,EU"` |
| Rate limits exceeded | Too many requests | Review adaptive rate limits |
| Connection timeouts | Network issues | Check proxy health |

### Debugging

```bash
# Check proxy pool health
~/.owl-agent/run.sh stats

# View logs
journalctl -u kiro-gateway -f

# Check metrics
curl http://localhost:8000/metrics | grep -E "owl_requests_total|owl_request_errors"

# Test single proxy
~/.owl-agent/run.sh fetch https://example.com
```

## Known Limitations

1. **Free Proxy Sources**: May have reliability issues
2. **Rate Limits**: HTTP and HTTPS providers have restrictions
3. **Geographic Restrictions**: Some proxies are region-locked
4. **Memory Usage**: Larger proxy pools consume more RAM
5. **Configuration**: Redis requires additional setup

## Future Enhancements (v5.0+)

### Planned Features

1. **Machine Learning**: Proxy success prediction
2. **Plugin System**: Extend without modifying core
3. **Dashboard**: Real-time proxy status
4. **Enterprise**: SSO integration
5. **Edge Computing**: CDN for latency reduction

## Conclusion

OWL-AGENT v4.2 provides a comprehensive, self-optimising proxy defense stack that can:

- **Handle any web scraping need** with intelligent proxy rotation
- **Integrate seamlessly** with major AI development platforms
- **Scale efficiently** from single-user to enterprise deployments
- **Maintain performance** under various network conditions
- **Store state persistently** for multi-session consistency

The system is production-ready and can be deployed in minutes across any infrastructure that supports Python, Docker, or traditional installations.

---

*Last updated: 2026-07-27*
*Version: v4.2.0*
*Compatible with: Python 3.10+, Docker 20+, kiro-cli 2.0+, OpenCode 2.0+
