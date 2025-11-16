# Translation-AI-FastAPI-OpenAI

<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/8aa024a4-051d-4c7f-bba1-5f3609deb82a" />
<img width="1906" height="908" alt="image" src="https://github.com/user-attachments/assets/fea1d23b-1679-4e93-b119-a315ea9754a6" />
<img width="1906" height="909" alt="image" src="https://github.com/user-attachments/assets/ba9d5fef-2525-4d77-85b9-a02fc985fcfe" />

A simple **multilingual translation API** built with **FastAPI** and **OpenAI GPT** models.  
This project allows you to translate text between languages using a REST API and test it via **Swagger UI**.

---

## Features

- Translate text to multiple languages using OpenAI GPT.
- Simple REST API built with FastAPI.
- Swagger UI integration for easy testing.
- Environment variables managed with `.env`.

---

## Project Structure
```bash
translation_ai/
│
├── main.py # FastAPI entry point
├── requirements.txt # Python dependencies
├── .gitignore # Ignore .env, .venv, etc.
├── .env.example # Example environment variables
├── config/
│ └── settings.py # Configuration and environment loader
├── routers/
│ └── translate.py # Translation API router
├── services/
│ └── openai_translator.py # OpenAI translation service
└── static/
└── index.html # Optional UI / static page

```

---

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/riponalmamun/Translation-AI-FastAPI-OpenAI.git
cd Translation-AI-FastAPI-OpenAI
```



2. **Create a virtual environment**
```bash
python -m venv .venv
# Activate on Windows
.venv\Scripts\Activate.ps1
# or on Linux/macOS
source .venv/bin/activate

```
3.  **Install dependencies **


Install dependencies

```bash
pip install -r requirements.txt


```

4.  **Create a .env file **


5. **copy .env.example .env **

6.  Then open .env and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here

```
Run the Server
```bash
uvicorn main:app --reload
```
The API will be available at:
```bash
http://127.0.0.1:8000
```
Swagger UI for testing:
```bash
http://127.0.0.1:8000/docs
```

API Usage
```bash
Endpoint: /translation/translation/
```

Method: POST

```bash
Body Example:
{
  "text": "I am Ripon",
  "target_lang": "Bangla"
}

Response Example:
{
  "translated_text": "আমি রিপন"
}
```

Contributing


Fork the repo
```bash

Create your branch (git checkout -b feature/new-feature)


Commit your changes (git commit -m 'Add new feature')


Push to the branch (git push origin feature/new-feature)
```

Open a Pull Request



License
This project is licensed under the MIT License.

Acknowledgements

```bash
FastAPI

```
OpenAI GPT Models


```bash


If you want, I can also **write a `.env.example` file** so your repo is fully ready to share without exposing your real API key.  

Do you want me to do that?

```
