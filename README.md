# 🔍 Semantic Search & Real-Time Agent Chatbot

An interactive web application combining a semantic search engine with a LangGraph-powered chatbot agent. Designed to deliver intelligent search, natural language interaction, and real-time tool invocation—all under one roof.

## ✨ Key Features

- 🧠 **Semantic Search Engine** using SentenceTransformers and cosine similarity
- 📡 **Real-Time Chatbot Agent** powered by LangGraph + LangChain + Groq
- 🔎 **Live Data Access** via TavilySearch integrated as a custom tool
- 💬 **Streamlit-based Chat UI** with persistent chat history
- 🧪 **Dual Applications**: `search_app.py` for query similarity, `app.py` for agent interaction

## 📁 Project Structure


├── agent.py              # LangGraph agent with Groq + TavilySearch integration
├── app.py                # Streamlit UI for chatbot agent
├── search_app.py         # Streamlit UI for semantic search
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (Groq API key, model config)

## 🔧 Setup Instructions

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**
   Create a `.env` file with your model and keys:
   ```env
   MODEL_NAME=llama-3-8b
   GROQ_API_KEY=your_groq_key_here
   ```

3. **Run the Semantic Search App**
   ```bash
   streamlit run search_app.py
   ```

4. **Run the Chatbot Agent App**
   ```bash
   streamlit run app.py
   ```

## 🧠 Semantic Search Overview

- Uses `sentence-transformers` to embed corpus of sentences
- Computes similarity with user query
- Ranks and displays top matching results along with scores
- Visual similarity breakdown included

## 🤖 Agent Chatbot Overview

- Uses LangGraph’s `create_react_agent()` with Groq LLM
- Dynamic prompt injection via `RunnableConfig`
- Invokes `TavilySearch` for fetching current data (e.g. weather)
- Handles multiple roles, streaming responses via Streamlit

## 📓 Example Prompt

> `"How is the weather in Denton, Texas today?"`  
Response pulled via TavilySearch and streamed into the assistant response.

## 🧰 Future Enhancements

- Extend `my_tool()` to accept dynamic queries
- Add memory or long-term context to `AgentState`
- Visualize query history and agent decisions
- Add summarization layer to semantic search results

## 🙏 Acknowledgments

Powered by:
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Groq](https://groq.com/)
- [Tavily Search API](https://www.tavily.com/)
- [Streamlit](https://streamlit.io/)
- [Sentence Transformers](https://www.sbert.net/)
