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
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPEN_API_KEY")
client = OpenAI(api_key=api_key)
```

### 🌐 Web Scraping for External Knowledge
This block of code provides the opportunity for the chatbot to enhances its knowledge and answers using webscraped content: 
``` python
def scrape_pages():
    urls = [ "List of URLs", 
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
```

### 🎨 Streamlit Front-End
Streamlit handles all UI rendering:

`st.chat_input()` collects user input.
`st.chat_message()` displays user and assistant messages.
Buttons and layout are defined using `st.columns()` and `st.button()`.

Example: 
``` python
st.chat_input("Ask your question...")
st.chat_message("user").markdown(user_input)
```

### 🧾 Prompt Engineering & Chat History
The assistant is initialised with a system message that defines its behaviour and inserts optional scraped content.

Example: 
``` python
st.session_state.messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant... {external_knowledge}"
    }
]
```
When the user asks a question, it's appended to this message history and sent to the OpenAI API for streaming response generation:
``` python
response = client.chat.completions.create(
    model="gpt-4o-mini", # OpenAI model 
    messages=st.session_state.messages, # Sends the entire chat history (system instructions + user/assistant messages) to the model.
    temperature=0.7,  # Controls the randomness of the model's output, ranging between 0-1 
    stream=True # Tells OpenAI to stream the response back in chunks (tokens), instead of waiting for the full answer.
)

```


### How to run it locally

Using your local Anaconda prompt, in the terminal type: 

```
FILE_PATH
streamlit run '{filename}.py'
```


