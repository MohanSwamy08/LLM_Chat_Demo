import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


st.title("LLM Chat Demo")


if "chat" not in st.session_state:
    st.session_state.chat = []


for m in st.session_state.chat:
    st.chat_message(m["role"]).write(m["content"])


prompt = st.chat_input("Ask something")


if prompt:
    st.session_state.chat.append({"role":"user","content":prompt})


    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.chat
    )


    reply = res.choices[0].message.content
    st.session_state.chat.append({"role":"assistant","content":reply})
    st.rerun()


