import subprocess
import re
from memory import load_rejected_ideas


def generate_prompts(topic: str, n_prompts=8):
    rejected = load_rejected_ideas()

    system_prompt = f"""
You are a defense-intelligence search query generator.

Task:
Generate {n_prompts} short, technical search queries about the given topic.

Rules:
- Must include 2024 or 2025
- Must contain at least one military/technical term
  (radar, RF, EO/IR, DEW, sensor fusion, swarm, electronic warfare)
- Use Boolean operators (AND, OR)
- Keep queries concise and specific for web crawling
- Avoid previously rejected ideas:
{rejected}
- Output only the numbered list

Topic:
{topic}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3.1:8b"],
        input=system_prompt,
        text=True,
        capture_output=True
    )

    prompts = []
    for line in result.stdout.split("\n"):
        line = line.strip()
        if not line:
            continue

        # Remove numbering like "1. ", "2) "
        cleaned = re.sub(r"^\d+[\.\)]\s*", "", line)

        if cleaned:
            prompts.append(cleaned)

    return prompts
