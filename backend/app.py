from fastapi import FastAPI, Request
from pydantic import BaseModel
from time import time
import openai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from filters import filter_response
from topic_validator import is_valid_topic
from hint_levels import detect_hint_levels
import json
from datetime import datetime
import logging
from pathlib import Path
import csv
import sqlite3


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_user_interaction(ip, user_input, ai_response):
    logging.info(f"IP: {ip} - User Input: {user_input} - AI Response: {ai_response}")
    timestamp = datetime.now().isoformat()

    conn = sqlite3.connect("chat_logs.db")
    cursor = conn.cursor()

    # Create the logs table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            ip TEXT,
            user_input TEXT,
            ai_response TEXT
        )
    """)

    # Insert the chat record
    cursor.execute("""
        INSERT INTO chat_logs (timestamp, ip, user_input, ai_response)
        VALUES (?, ?, ?, ?)
    """, (timestamp, ip, user_input, ai_response))

    conn.commit()
    conn.close()


# Session memory to store chat history per IP
session_memory = {}
SESSION_LIMIT = 15

# Variable set-up to stop spam
last_request_time = {}
THROTTLE_TIME = 8

app = FastAPI()

# Allow all origins for testing (you can restrict later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

BASE_SYSTEM_PROMPT = """
You are a patient and friendly coding/math tutor. 
Never give direct answers. Instead, ask guiding questions, offer hints, and encourage step-by-step thinking.
Politely refuse if the user asks for the full answer directly.
Ask the user to provide what they have already done/tried to offer more helpful feedback.
Constantly be providing the user helpful, constructive criticism, while remaining friendly and encouraging.
Always keep explanations short and simple unless the user asks for deep detail.
Prefer to give a simple idea first and offer to expand if the user wants more.
Avoid listing too many definitions or going into every detail unless requested.
"""

class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
async def chat(req: ChatRequest, request: Request):
    # checks for garbage or whitespace, preventing wasting tokens
    user_input = req.user_input.strip()

    allowed_low_confidence = ["idk", "i don't know", "i'm stuck", "i'm lost", "confused", "no idea", "help", "what", "how", "why", "huh"]

    # Step 1 → check garbage/empty input first
    if not user_input or (len(user_input) < 3 and user_input not in allowed_low_confidence):
        return {"response": "Please enter a valid math or coding question so I can help you."}

    # Step 2 → check allowed topics with seperate AI interpreter
    if not is_valid_topic(user_input):
        return {"response": "This tutor is designed to help with coding and math questions. Please ask something related to those topics."}
    
    # checks for spam
    ip = request.client.host
    now = time()

    log_user_interaction(ip, user_input)

    if ip in last_request_time and now - last_request_time[ip] < THROTTLE_TIME:
        return {"response": "Please slow down and wait a few seconds before asking another question."}

    last_request_time[ip] = now

    # detects the hint level from user input
    hint_level = detect_hint_levels(req.user_input)

    # modify system prompt based on the hint level
    system_prompt = BASE_SYSTEM_PROMPT

    if hint_level == 3:
        system_prompt += "\nThe user seems very confused or discouraged. Provide very clear and supportive hints, and be especially encouraging. Break down the problem step-by-step gently. Still do NOT just give away the answer."
    elif hint_level == 2:
        system_prompt += "\nThe user seems stuck. Provide detailed and explicit hints to guide them, but do not give the answer."
    else:
        system_prompt += "\nThe user is making progress. Offer only light hints or ask guiding questions."

    # Prepare or update session memory
    if ip not in session_memory:
        session_memory[ip] = []

    # Add user input to session history
    session_memory[ip].append({"role": "user", "content": req.user_input})

    # Build messages with system + memory
    messages = [{"role": "system", "content": system_prompt}] + session_memory[ip]

    # Limit memory length
    if len(session_memory[ip]) > SESSION_LIMIT:
        session_memory[ip] = session_memory[ip][-SESSION_LIMIT:]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    except Exception as e:
        return {"response": "Sorry, I'm having trouble reaching the AI right now. Please try again shortly."}

    if not response.choices or not response.choices[0].message or not response.choices[0].message.content.strip():
      return {"response": "Sorry, I couldn't generate a response. Please try again."}

    raw_response = response.choices[0].message.content

    # Add assistant response to session memory
    session_memory[ip].append({"role": "assistant", "content": raw_response})

    safe_response = filter_response(raw_response)

    return {"response": safe_response}