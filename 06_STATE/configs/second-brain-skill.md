# LifeOS SecondBrain Skill

## Purpose
Bridge Obsidian vault paths to LifeOS Memory v7.6 categories. Provides structured read/write operations between the vault and LifeOS Pulse daemon.

## Configuration

```yaml
skill:
  name: SecondBrain
  version: 1.0.0
  description: Unified knowledge graph integration between Obsidian vault and LifeOS Memory
  triggers:
    - "second brain"
    - "vault sync"
    - "memory sync"
    - "obsidian"
    - "knowledge graph"
  tools:
    - vault_read
    - vault_write
    - memory_sync
    - algorithm_trigger
```

## Vault ↔ Memory v7.6 Mapping

```python
MEMORY_BUCKET_MAP = {
    "WORK": "/home/x1/obsidianvault/WORK",
    "KNOWLEDGE": "/home/x1/obsidianvault/KNOWLEDGE",
    "LEARNING": "/home/x1/obsidianvault/LEARNING",
    "RELATIONSHIP": "/home/x1/obsidianvault/RELATIONSHIP",
    "OBSERVABILITY": "/home/x1/obsidianvault/OBSERVABILITY",
    "STATE": "/home/x1/obsidianvault/STATE",
}
```

## API Endpoints Used

```
# LifeOS Pulse at localhost:31337
GET  /api/memory/{bucket}      — list vault entries in bucket
POST /api/memory/{bucket}      — create entry (writes to vault + Memory)
GET  /api/memory/search?q=     — full-text search across buckets
POST /api/algorithm/step       — trigger OBSERVE→THINK→PLAN cycle
GET  /api/pulse/status         — daemon health check
```

## Skill Actions

### vault_read(bucket, query?)
Read entries from a vault bucket. If query provided, grep for matches.

### vault_write(bucket, title, content, tags)
Create a new markdown file in the correct bucket with proper frontmatter.

### memory_sync()
Bidirectional sync: push new vault files to LifeOS Memory, pull Memory entries to vault.

### algorithm_trigger(context)
Feed a vault entry into the LifeOS Algorithm loop starting at OBSERVE step.

## Hook Configuration

```json
{
  "hooks": {
    "on_capture": {
      "trigger": "new_file_in_raw",
      "action": "classify_and_route",
      "handler": "poznote_pipeline.py"
    },
    "on_vault_write": {
      "trigger": "file_written_to_vault",
      "action": "sync_to_memory",
      "handler": "memory_sync.py"
    },
    "on_algorithm_complete": {
      "trigger": "algorithm_step_complete",
      "action": "update_vault_entry",
      "handler": "algorithm_vault_bridge.py"
    }
  }
}
```
