from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    html_path = os.path.join(os.path.dirname(__file__), "..", "public", "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r") as f:
            return f.read()
    return "<h1>AI Drawing Video Generator</h1><p>Em construcao...</p>"

@app.get("/api/health")
async def health():
    return {"status": "ok"}
