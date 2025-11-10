# File name: main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Create the main application
app = FastAPI()

# --- Add CORS Middleware ---
# This allows your websites to talk to this server
origins = [
    "https://primingparagon.org",
    "https://www.primingparagon.org",
    "http://palegoldenrid-nightinggale-250665.hostingersite.com",
    "https://palegoldenrid-nightinggale-250665.hostingersite.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Define the data model for our chat ---
class ChatRequest(BaseModel):
    prompt: str

# --- Your Root Endpoint ---
@app.get("/")
def read_root():
    return {"message": "Paragon AI backend is live."}

# --- Your Chat Endpoint ---
@app.post("/chat")
def handle_chat(request: ChatRequest):
    user_message = request.prompt

    # --- TODO: AI Logic Goes Here ---
    # For now, we'll just send a simple response back

    ai_response = f"Backend received your message: '{user_message}'. Paragon AI is not yet connected to an LLM."

    # Send the response back as JSON
    return {"reply": ai_response}}
