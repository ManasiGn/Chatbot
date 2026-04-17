from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from google import genai

app = FastAPI()

# CORS (keep this)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NEW CLIENT
client = genai.Client(api_key="") #API key

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(data: Prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=data.prompt
        )
        return {"response": response.text}
    except Exception as e:
        print(e)
        return {"response": "Error: " + str(e)}