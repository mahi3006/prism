from fastapi import FastAPI
from prompt_generator import generate_prompts

app = FastAPI()

@app.get("/generate-prompts")
def generate(topic: str):
    prompts = generate_prompts(topic)
    return {
        "topic": topic,
        "prompts": prompts
    }
