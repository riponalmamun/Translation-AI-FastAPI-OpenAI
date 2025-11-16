from fastapi import APIRouter
from pydantic import BaseModel
from services.openai_translator import translate_text

router = APIRouter(prefix="/translation", tags=["Translation"])

class TranslationRequest(BaseModel):
    text: str
    target_lang: str = "Bangla"

@router.post("/")
def translate_api(request: TranslationRequest):
    translated = translate_text(request.text, request.target_lang)
    return {"translated_text": translated}
