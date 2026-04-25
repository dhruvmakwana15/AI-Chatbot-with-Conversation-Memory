import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

path = r"C:\Users\dhruv\OneDrive\Desktop\Langchain_model\Chatmodel\.env"
load_dotenv(path)
# Model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=200
)

model = ChatHuggingFace(llm=llm)

# UI
st.title("💬 Smart Chatbot")

# Initialize chat history with system message
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(
            content="""
            You are a helpful, accurate, and concise AI assistant.
            - Answer clearly and simply
            - If you don't know something, say so honestly
            - Avoid unnecessary long explanations"""
        )
    ]

# Display messages 
for msg in st.session_state.chat_history:
    if isinstance(msg, SystemMessage):
        continue
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    st.chat_message(role).write(msg.content)

# Input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    try:
        # Send full conversation to model  
        result = model.invoke(st.session_state.chat_history)
        reply = result.content
    except Exception as e:
        reply = f"Error: {str(e)}"

    # Add AI response
    st.session_state.chat_history.append(AIMessage(content=reply))

    # Show latest messages
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(reply)