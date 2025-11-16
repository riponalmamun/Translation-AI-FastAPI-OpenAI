from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers.translate import router as translate_router
import os

app = FastAPI(
    title="Multilingual Translation AI",
    description="Translation API using FastAPI + OpenAI GPT models",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(translate_router, prefix="/translation", tags=["Translation"])

if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
def home():
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    return {"message": "Translation API is running!", "docs": "/docs"}

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "healthy", "model": "gpt-4o-mini"}