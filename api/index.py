from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import json
import random

app = FastAPI()

# Dicionário de personagens com roteiros visuais
CHARACTERS = {
    "goku": {
        "stages": [
            {"time": 0, "desc": "Dois circulos sobrepostos + linha curva", "illusion": "Oculos ou sorriso"},
            {"time": 2, "desc": "Linhas verticais + curvas laterais", "illusion": "Rosto humano generico"},
            {"time": 4, "desc": "Cabelo espetado + sobrancelhas grossas", "illusion": "Cabelo baguncado"},
            {"time": 6, "desc": "Olhos determinados + detalhes finais", "illusion": "Revelacao: GOKU"}
        ],
        "features": ["cabelo espetado dourado", "olhos verdes", "uniforme laranja", "expressao determinada"]
    },
    "naruto": {
        "stages": [
            {"time": 0, "desc": "Dois circulos + linha central", "illusion": "Olhos e nariz"},
            {"time": 2, "desc": "Linhas diagonais acima", "illusion": "Cabelo baguncado"},
            {"time": 4, "desc": "Bandana com simbolo da Folha", "illusion": "Revelacao parcial"},
            {"time": 6, "desc": "Bigodes + olhos azuis + detalhes", "illusion": "Revelacao: NARUTO"}
        ],
        "features": ["cabelo loiro espetado", "bandana preta", "bigodes no rosto", "jaqueta laranja"]
    },
    "vegeta": {
        "stages": [
            {"time": 0, "desc": "Forma oval + linhas internas", "illusion": "Rosto serio"},
            {"time": 2, "desc": "Linhas duras + sobrancelhas", "illusion": "Expressao severa"},
            {"time": 4, "desc": "Cabelo preto espetado para cima", "illusion": "Silhueta familiar"},
            {"time": 6, "desc": "Armadura saiyajin + olhos frios", "illusion": "Revelacao: VEGETA"}
        ],
        "features": ["cabelo preto espetado", "armadura saiyajin azul", "olhos frios", "expressao arrogante"]
    },
    "luffy": {
        "stages": [
            {"time": 0, "desc": "Circulo + linha curva", "illusion": "Sorriso largo"},
            {"time": 2, "desc": "Olhos redondos + cabelo curto", "illusion": "Rosto jovem"},
            {"time": 4, "desc": "Chapeu de palha aparecendo", "illusion": "Revelacao parcial"},
            {"time": 6, "desc": "Corpo elastico + sorriso caracteristico", "illusion": "Revelacao: LUFFY"}
        ],
        "features": ["chapeu de palha", "camisa vermelha", "bracos elasticos", "sorriso largo"]
    },
    "gojo": {
        "stages": [
            {"time": 0, "desc": "Dois circulos brancos", "illusion": "Olhos vendados?"},
            {"time": 2, "desc": "Linhas de cabelo branco", "illusion": "Cabelo prateado"},
            {"time": 4, "desc": "Venda preta nos olhos", "illusion": "Revelacao parcial"},
            {"time": 6, "desc": "Uniforme escuro + sorriso misterioso", "illusion": "Revelacao: GOJO"}
        ],
        "features": ["cabelo branco prateado", "venda preta nos olhos", "uniforme escuro", "sorriso misterioso"]
    }
}

@app.get("/", response_class=HTMLResponse)
async def root():
    html_path = os.path.join(os.path.dirname(__file__), "..", "public", "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r") as f:
            return f.read()
    return "<h1>AI Drawing Video Generator</h1><p>Em construcao...</p>"

@app.post("/api/generate")
async def generate_video(character: str = Form(...)):
    char_lower = character.lower().strip()
    
    if char_lower not in CHARACTERS:
        return JSONResponse({
            "error": "Personagem nao encontrado",
            "available": list(CHARACTERS.keys())
        }, status_code=404)
    
    char_data = CHARACTERS[char_lower]
    
    return {
        "character": character,
        "stages": char_data["stages"],
        "features": char_data["features"],
        "message": f"Roteiro visual gerado para {character}",
        "status": "success"
    }

@app.get("/api/characters")
async def list_characters():
    return {
        "characters": list(CHARACTERS.keys()),
        "count": len(CHARACTERS)
    }

@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "AI Drawing Video Generator"}
