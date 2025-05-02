# 🤖 Generalised GPT Chatbot with Streamlit

This is a simple yet powerful AI chatbot built using Python and Streamlit that leverages OpenAI’s GPT models to answer general queries. It includes optional web scraping for enhanced context and demonstrates best practices in prompt engineering and interactive web app development.

---

## 💡 Purpose

The goal of this chatbot is to provide a **generalised, customisable framework** that can be deployed as a personal or business assistant. You can easily modify the input context, extend it to include file/document parsing, or fine-tune its personality and use-case through prompt engineering.

---

## 🧰 Tools & Technologies Used

- **Python** – Core programming language
- **Streamlit** – To create a lightweight, reactive web interface
- **OpenAI API** – To interact with GPT models (`gpt-4o-mini`, `gpt-3.5-turbo`, etc.)
- **BeautifulSoup** – For optional web scraping functionality
- **Requests** – To fetch content from web pages

---

## 🧠 Prompt Engineering Concepts Applied

- **System Role Definition**: The chatbot is primed with a clear identity and boundaries to ensure consistent behaviour and tone.
- **Context Injection**: Optional scraped or preloaded content is passed into the system prompt to simulate retrieval-augmented generation (RAG) on a lightweight scale.
- **Few-shot Prompting**: Example prompts are displayed at the start to guide user interactions.

---

## 🧩 Code Overview

### 🔐 OpenAI API Setup
The app connects to OpenAI using the `openai` Python SDK. You’ll need to provide your API key:
```python
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")  
