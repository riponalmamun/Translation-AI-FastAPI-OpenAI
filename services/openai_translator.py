from openai import OpenAI
from config.settings import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def translate_text(text: str, target_lang: str):
    prompt = f"Translate the following text into {target_lang}:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a multilingual translation assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # NEW SDK FORMAT:
    return response.choices[0].message.content
