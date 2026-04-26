💬 Smart AI Chatbot (LangChain + HuggingFace + Streamlit)

An interactive AI-powered chatbot built using LangChain, HuggingFace LLaMA-3, and Streamlit.
The application supports real-time conversations with memory, enabling context-aware responses.
Built by Dhruv Makwana

🚀 Features

🧠 Context-aware conversation using chat history
🤖 Powered by LLaMA-3 via HuggingFace Endpoint
💬 Structured messaging with SystemMessage, HumanMessage, and AIMessage
⚡ Real-time chat interface using Streamlit
🛡️ Exception handling for stable user experience

🛠️ Tech Stack
python
langchain
LangChain
HuggingFace
Streamlit
dotenv

⚙️ Setup Instructions
🔹 1. Clone the repository
git clone https://github.com/username/repo-name.git
cd your-repo-name
🔹 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
🔹 3. Install dependencies
pip install -r requirements.txt
🔹 4. Add API key
Create a .env file and add:
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
🔹 5. Run the app
streamlit run app.py

💡 How it works
Uses LangChain message objects to maintain conversation flow
Stores chat history in Streamlit session state
Sends full conversation to LLM for context-aware responses
Applies system prompt to control AI behavior

Screenshot
<img width="1354" height="979" alt="image" src="https://github.com/user-attachments/assets/24e9f226-1882-4ced-a800-99bab2cea998" />
