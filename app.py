import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate,
)

# Custom CSS styling
st.markdown(
    """
    <style>
        .main {
            background-color: #1a1a1a;
            color: #ffffff;
            text-align: center;
        }
        .stTextInput textarea, .stMarkdown, .stChatMessage {
            color: #ffffff !important;
            font-weight: bold !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title and caption
st.title("💬 DeepSeek Chat")
st.caption("Your AI Assistant for Code and Debugging")

# Initialize the chat engine
llm_engine = ChatOllama(
    model="deepseek-r1:1.5b",
    base_url="http://localhost:11434",
    temperature=0.3,
)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an AI assistant. Provide helpful, concise, and accurate responses to any query. "
    "If the question is about coding, provide code examples and debugging tips. Always respond in English."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you today? 💻"}]

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input and processing
user_query = st.chat_input("Type your question here...")

def generate_ai_response(user_input):
    try:
        prompt_chain = build_prompt_chain()
        processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
        response = processing_pipeline.invoke({"query": user_input})  # Ensure user query is passed
        return response
    except Exception as e:
        return f"Error: {e}"

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})

    # Generate AI response
    with st.spinner("🧠 Processing..."):
        ai_response = generate_ai_response(user_query)  # Pass user input correctly
    
    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})

    # Rerun to update chat display
    st.experimental_rerun()
