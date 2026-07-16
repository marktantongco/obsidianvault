import os
import re
import sys
import subprocess
import json
from datetime import datetime, timezone
import urllib.request

VAULT_DIR = os.getcwd()
FOLDERS = ["concepts", "entities", "journal", "skills", "references", "synthesis", "projects", "config"]

def get_git_mtime(filepath):
    try:
        res = subprocess.run(["git", "log", "-n", "1", "--pretty=format:%cI", "--", filepath], capture_output=True, text=True, check=True)
        date_str = res.stdout.strip()
        if date_str:
            return datetime.fromisoformat(date_str)
    except Exception:
        pass
    # Fallback to file system mtime
    try:
        return datetime.fromtimestamp(os.path.getmtime(filepath), tz=timezone.utc)
    except Exception:
        return datetime.min.replace(tzinfo=timezone.utc)

def parse_frontmatter(content):
    frontmatter = {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        # Simple YAML parsing (only key-value strings)
        for line in yaml_text.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'").strip(">").strip("-").strip()
                frontmatter[key] = val
    return frontmatter

def build_index():
    index_data = {}
    for folder in FOLDERS:
        index_data[folder] = []
        path = os.path.join(VAULT_DIR, folder)
        if not os.path.exists(path):
            continue
        
        for filename in os.listdir(path):
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(path, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue
            
            fm = parse_frontmatter(content)
            title = fm.get("title") or filename[:-3]
            summary = fm.get("summary") or ""
            link_name = filename[:-3]
            index_data[folder].append((link_name, title, summary))
            
        index_data[folder].sort(key=lambda x: x[0].lower())
    
    # Generate index.md content
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "---",
        "title: Wiki Index",
        f"updated: {now_iso}",
        "---",
        "",
        "# Wiki Index",
        "",
        f"*Last updated: {now_iso}*",
        ""
    ]
    
    for folder in FOLDERS:
        if not index_data[folder]:
            continue
        lines.append(f"## {folder.capitalize()}")
        for link_name, title, summary in index_data[folder]:
            desc = f" — {summary}" if summary else ""
            lines.append(f"- [[{folder}/{link_name}|{title}]]{desc}")
        lines.append("")
        
    # Write special index entries
    lines.extend([
        "## Special",
        "- [[hot]] · [[log]] · [[AGENTS]]",
        ""
    ])
    
    with open(os.path.join(VAULT_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("index.md compiled successfully.")

def build_hot():
    all_files = []
    for root, dirs, files in os.walk(VAULT_DIR):
        # Exclude hidden directories and special files
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for file in files:
            if not file.endswith(".md") or file in ["index.md", "hot.md", "log.md"]:
                continue
            filepath = os.path.join(root, file)
            mtime = get_git_mtime(filepath)
            all_files.append((filepath, mtime))
            
    # Get 10 most recently updated
    all_files.sort(key=lambda x: x[1], reverse=True)
    recent = all_files[:10]
    
    # Fallback/Default Content
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    hot_content = [
        "---",
        "title: Hot Cache",
        f"updated: {now_iso}",
        "---",
        "",
        "# Hot Cache",
        "",
        "## Recent Activity"
    ]
    
    llm_summaries = []
    for path, mtime in recent:
        rel_path = os.path.relpath(path, VAULT_DIR)
        name = os.path.basename(path)[:-3]
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            content = ""
        fm = parse_frontmatter(content)
        title = fm.get("title") or name
        summary = fm.get("summary") or "Updated note."
        llm_summaries.append(f"- {rel_path} ({title}): {summary}")
        hot_content.append(f"- {mtime.strftime('%Y-%m-%d')} [[{rel_path[:-3]}|{title}]] — {summary}")
        
    api_key = os.environ.get("GROQ_API_KEY")
    if api_key:
        print("Groq API Key found. Generating semantic summary...")
        prompt = (
            "You are an AI second brain summarizer. Summarize the following recent activity logs in a premium, "
            "concise bullet list detailing what was accomplished or learned recently in our wiki. Focus on "
            "connections and key insights. Do not include introductory or concluding conversational filler.\n\n"
            + "\n".join(llm_summaries)
        )
        
        req_data = json.dumps({
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are a professional technical writer and summarizer. Be direct, direct, and zero fluff."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2
        }).encode("utf-8")
        
        req = urllib.request.Request(
            "https://api.groq.com/openai/v1/chat/completions",
            data=req_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            method="POST"
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                resp_data = json.loads(response.read().decode("utf-8"))
                llm_response = resp_data["choices"][0]["message"]["content"]
                
                # Replace the simple list with the LLM response
                hot_content = [
                    "---",
                    "title: Hot Cache",
                    f"updated: {now_iso}",
                    "---",
                    "",
                    "# Hot Cache",
                    "",
                    "## Recent Activity",
                    llm_response.strip(),
                    "",
                    "## Key Takeaways",
                    "- Knowledge is compiled dynamically on Cloudflare edge.",
                    "- Vault references are maintained via git webhook cron trigger."
                ]
        except Exception as e:
            print(f"Error calling Groq API: {e}. Falling back to standard list.")
            
    with open(os.path.join(VAULT_DIR, "hot.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(hot_content))
    print("hot.md compiled successfully.")

def write_log():
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    log_entry = f"- [{now_str}] DAILY-UPDATE (Cloudflare Edge Sync trigger completed index & hot.md update)\n"
    log_path = os.path.join(VAULT_DIR, "log.md")
    
    # Read existing log or start new
    content = ""
    if os.path.exists(log_path):
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            pass
            
    # Prepend log entry
    if content.startswith("---"):
        # has frontmatter, insert after frontmatter
        parts = content.split("---", 2)
        if len(parts) >= 3:
            new_content = "---" + parts[1] + "---" + "\n" + log_entry + parts[2].strip() + "\n"
        else:
            new_content = log_entry + content
    else:
        new_content = log_entry + content
        
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("log.md updated successfully.")

if __name__ == "__main__":
    build_index()
    build_hot()
    write_log()
