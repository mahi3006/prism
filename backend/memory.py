import json
from pathlib import Path

MEMORY_FILE = Path("rejected_ideas.json")

def load_rejected_ideas():
    if MEMORY_FILE.exists():
        return json.loads(MEMORY_FILE.read_text())
    return []

def save_rejected_ideas(ideas):
    MEMORY_FILE.write_text(json.dumps(ideas, indent=2))
#