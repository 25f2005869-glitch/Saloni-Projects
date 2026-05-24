# ============================================
# task_storage.py — Shared task storage module
# Format: title|status|category  (tasks.txt)
#
# Migration: lines without "|" (legacy format)
# are auto-converted to {title, status="Pending", category="Work"}.
# ============================================

def load_tasks(path="tasks.txt"):
    """
    Load tasks from *path* and return a list of dicts:
        {"title": str, "status": "Pending"|"Done", "category": str}

    Parsing rules (per line, after stripping whitespace):
      - Empty lines are skipped.
      - 3+ pipe-separated fields  → title | status | category
        (any extra fields are ignored).
      - Exactly 2 pipe-separated fields → title | status, category defaults to "Work".
      - No pipe (legacy line)    → entire line is title,
        status defaults to "Pending", category defaults to "Work".

    FileNotFoundError is handled gracefully (returns []).
    """
    tasks = []
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) >= 3:
                    tasks.append({
                        "title": parts[0].strip(),
                        "status": parts[1].strip(),
                        "category": parts[2].strip(),
                    })
                elif len(parts) == 2:
                    tasks.append({
                        "title": parts[0].strip(),
                        "status": parts[1].strip(),
                        "category": "Work",
                    })
                else:
                    # Legacy plain-text line → migrate with defaults
                    tasks.append({
                        "title": line,
                        "status": "Pending",
                        "category": "Work",
                    })
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks, path="tasks.txt"):
    """
    Write *tasks* to *path* in the unified format:
        title|status|category  (one task per line)
    """
    with open(path, "w") as f:
        for t in tasks:
            f.write(f"{t['title']}|{t['status']}|{t['category']}\n")
