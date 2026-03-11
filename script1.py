# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:34:48 2025

@author: rhyme
"""

import streamlit as st
import requests
import random

# DIRECT API KEY (no dotenv)
API_KEY = "ENTER YOUR KEY"

API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

def ask_gemini(prompt_list):
    payload = {"contents": [{"parts": [{"text": p} for p in prompt_list]}]}
    response = requests.post(f"{API_URL}?key={API_KEY}", json=payload)
    data = response.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return f"Error: {data}"

# ---------------------------
# Chat & Game States
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "game_active" not in st.session_state:
    st.session_state.game_active = False

if "game_items" not in st.session_state:
    st.session_state.game_items = []

# ---------------------------
# Memory Game Logic
# ---------------------------
def start_memory_game():
    lists = [
        ["apple", "key", "cup"],
        ["pencil", "wallet", "comb", "spoon"],
        ["book", "glasses", "phone", "coin"],
        ["chair", "mirror", "towel"],
        ["bread", "bottle", "ring", "pen", "card"]
    ]
    chosen = random.choice(lists)
    st.session_state.game_items = chosen
    st.session_state.game_active = True

    return (
        "Let's try a small memory game.\n\n"
        f"Remember these items:\n➡ **{', '.join(chosen)}**\n\n"
        "Tell me once you're ready 😊"
    )

def check_memory_answer(answer):
    correct = st.session_state.game_items
    user = [w.strip().lower() for w in answer.split(",")]

    score = sum(1 for w in user if w in correct)
    st.session_state.game_active = False

    return (
        f"You remembered **{score}/{len(correct)}** items.\n\n"
        f"The correct list was: **{', '.join(correct)}**.\n"
        "Good job! Want to play again? Say *start game*."
    )

# ---------------------------
# Streamlit UI
# ---------------------------

#st.image("elder.jpeg", width=250)
with st.chat_message("system"):
    st.write("Hello 😊 I'm here to keep you company.")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

prompt = st.chat_input("Type your message here")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    if "start game" in prompt.lower():
        reply = start_memory_game()

    elif st.session_state.game_active:
        reply = check_memory_answer(prompt)

    else:
        history = "\n".join([f"[{m['role']}]: {m['content']}" for m in st.session_state.messages])
        system_prompt = """
You are a warm, friendly AI companion for older adults.
Keep answers short (1–2 lines), simple, and encouraging.
"""

        reply = ask_gemini([
            system_prompt,
            f"Conversation:\n{history}",
            f"User: {prompt}"
        ])

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:34:48 2025

@author: rhyme
"""

import streamlit as st
import requests
import random

# DIRECT API KEY (no dotenv)
API_KEY = "ENTER YOUR KEY"

API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

def ask_gemini(prompt_list):
    payload = {"contents": [{"parts": [{"text": p} for p in prompt_list]}]}
    response = requests.post(f"{API_URL}?key={API_KEY}", json=payload)
    data = response.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return f"Error: {data}"

# ---------------------------
# Chat & Game States
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "game_active" not in st.session_state:
    st.session_state.game_active = False

if "game_items" not in st.session_state:
    st.session_state.game_items = []

# ---------------------------
# Memory Game Logic
# ---------------------------
def start_memory_game():
    lists = [
        ["apple", "key", "cup"],
        ["pencil", "wallet", "comb", "spoon"],
        ["book", "glasses", "phone", "coin"],
        ["chair", "mirror", "towel"],
        ["bread", "bottle", "ring", "pen", "card"]
    ]
    chosen = random.choice(lists)
    st.session_state.game_items = chosen
    st.session_state.game_active = True

    return (
        "Let's try a small memory game.\n\n"
        f"Remember these items:\n➡ **{', '.join(chosen)}**\n\n"
        "Tell me once you're ready 😊"
    )

def check_memory_answer(answer):
    correct = st.session_state.game_items
    user = [w.strip().lower() for w in answer.split(",")]

    score = sum(1 for w in user if w in correct)
    st.session_state.game_active = False

    return (
        f"You remembered **{score}/{len(correct)}** items.\n\n"
        f"The correct list was: **{', '.join(correct)}**.\n"
        "Good job! Want to play again? Say *start game*."
    )

# ---------------------------
# Streamlit UI
# ---------------------------

#st.image("elder.jpeg", width=250)
with st.chat_message("system"):
    st.write("Hello 😊 I'm here to keep you company.")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

prompt = st.chat_input("Type your message here")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    if "start game" in prompt.lower():
        reply = start_memory_game()

    elif st.session_state.game_active:
        reply = check_memory_answer(prompt)

    else:
        history = "\n".join([f"[{m['role']}]: {m['content']}" for m in st.session_state.messages])
        system_prompt = """
You are a warm, friendly AI companion for older adults.
Keep answers short (1–2 lines), simple, and encouraging.
"""

        reply = ask_gemini([
            system_prompt,
            f"Conversation:\n{history}",
            f"User: {prompt}"
        ])

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)