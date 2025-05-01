import streamlit as st
from openai import OpenAI
import requests
from bs4 import BeautifulSoup

# --- PAGE CONFIGURATION ---
st.set_page_config(page_icon="🤖", page_title="GPT Chatbot", layout="wide")

# --- SETUP OPENAI API ---
api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual key or use environment variable
client = OpenAI(api_key=api_key)

# --- Optional: Web scraping example ---
@st.cache_data(show_spinner="Scraping example pages...")
def scrape_pages():
    urls = [
        "https://en.wikipedia.org/wiki/OpenAI",  # Example
        "https://en.wikipedia.org/wiki/ChatGPT"
    ]
    contents = []
    for url in urls:
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            main = soup.find("main") or soup.body
            if main:
                text = main.get_text(separator="\n").strip()
                contents.append(text)
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    return "\n\n".join(contents)

external_knowledge = scrape_pages()  # Optional knowledge base

# --- UI HEADER ---
st.image("Chatbot_Banner.jpg", use_column_width=True)  # Optional image (replace or remove)
st.title("💬 General GPT Chatbot")

with st.expander("ℹ️ How this works"):
    st.markdown("""
    - Ask any question and get responses from an AI chatbot
    - Powered by OpenAI’s GPT models
    - Includes optional scraped data to enhance context (edit the URLs in code)
    """)

# --- INITIALISE CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": f"""
            You are a helpful assistant. You can answer general questions and provide useful insights.
            Use the following (optional) external information if relevant:
            {external_knowledge}
            """
        }
    ]

# --- OPTIONAL: EXAMPLE PROMPTS ---
if len(st.session_state.messages) == 1:
    st.markdown("### 💡 Example prompts:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("What is ChatGPT?"):
            st.session_state.user_input = "What is ChatGPT?"
    with col2:
        if st.button("Explain how LLMs work"):
            st.session_state.user_input = "Explain how LLMs work"

# --- USER INPUT HANDLING ---
user_input = st.chat_input("Type your question here...", key="chat_input")

if "user_input" in st.session_state and st.session_state.user_input:
    if not user_input:
        user_input = st.session_state.user_input
    st.session_state.user_input = ""  # Clear after using

# --- DISPLAY CHAT HISTORY ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- PROCESS USER QUERY ---
if user_input:
    # Store user input
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display assistant reply with streaming
    with st.chat_message("assistant"):
        full_response = ""
        placeholder = st.empty()

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Change to "gpt-3.5-turbo" if needed
            messages=st.session_state.messages,
            temperature=0.7,
            stream=True
        )

        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                placeholder.markdown(full_response + "▌")

        placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
