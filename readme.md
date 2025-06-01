# Knowledge-base AI

**Knowledge-base AI** is a FastAPI-based project designed to build an AI agent using **LangGraph** and **PydanticAI**. The application scrapes web URIs for information, answers queries based on the gathered data, and creates knowledge bases.

---

## 🚀 Project Description

This project leverages FastAPI to provide a RESTful API for interacting with an AI agent. The agent is capable of:

- Scraping web pages for content.
- Summarizing the content and generating insights.
- Answering user queries based on the scraped data.

The application uses **LangGraph** and **PydanticAI** to structure and process data, making it a robust solution for building knowledge bases.

---

> 📌 **Like this project? [Give it a ⭐ on GitHub](https://github.com/lakshyakumar/Knowledge-Base-AI)!**
---

## 🛠 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/knowledge-base-ai.git
cd knowledge-base-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Copy the sample environment file and edit it:
```bash
cp .env.sample .env
```
Update the `.env` file with your API keys and configurations.

---

## ▶️ Running the Application

### Development Mode
To run the application with auto-reload:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The app will be available at: [http://0.0.0.0:8000](http://0.0.0.0:8000)

---

## 📡 API Routes

### ✅ Health Check
- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Returns the health status of the application.

---

### ℹ️ Project Details
- **Endpoint**: `/`
- **Method**: `GET`
- **Description**: Provides metadata about the project (name, version, description).

---

### 🔍 Query Scraping
- **Endpoint**: `/query`
- **Method**: `GET`
- **Description**: Accepts a query string and invokes the AI agent to scrape and process data.
- **Query Parameter**:
  - `query` (required): The query string describing what to scrape.

---

## 🔐 Environment Variables

The application uses the following environment variables (see `.env.sample`):

- `OPENAI_API_KEY`: The API key for accessing OpenAI services.
- `MODEL`: The AI model to use (default: `gpt-4o-mini`).
- `TAVILY_API_KEY`: The API key for accessing Tavily services.

Ensure these variables are set correctly in your `.env` file.

---

## Future Enhancements

- Improved scraping for js based websites.
- scraping all links of a website.
- Chunked summarization.
- introduction of semantic search and creation of knowledge bases.
- Enhanced error handling and logging.

## 🤝 Contributing

We welcome contributions from everyone! Please read our [**Contributing Guide**](CONTRIBUTING.md) to get started. ✨

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
