from fastapi import FastAPI
from app.agents.writer import generate_section

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI report generator is running."}

@app.post("/generate")
def generate():
    return generate_section()
