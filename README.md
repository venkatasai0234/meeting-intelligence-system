# 🧠 Meeting Intelligence System

An end-to-end NLP + ML Engineering project that transforms raw meeting transcripts into structured insights including action items, decisions, topics, semantic search, and summaries.

---

## 🚀 Features

* 📄 Transcript preprocessing and cleaning
* ✅ Action item extraction
* 📌 Decision detection
* 🧩 Topic segmentation
* 🔍 Semantic search (Sentence Transformers + reranking)
* 📝 Automated meeting summary generation
* ⚡ FastAPI backend (production-style API)
* 🌐 Streamlit frontend (interactive UI)
* 🧪 Unit + API testing with pytest

---

## 🏗️ System Architecture

```
Transcript Input
      ↓
Preprocessing (cleaning, parsing)
      ↓
Structured Records (speaker + text)
      ↓
-----------------------------------
| Action Items | Decisions | Topics |
-----------------------------------
      ↓
Semantic Search (Sentence Transformers)
      ↓
Summary Generation
      ↓
Final Structured JSON Output
```

---

## 📂 Project Structure

```
meeting-intelligence-system/
│
├── app/
│   ├── api.py              # FastAPI backend
│   ├── streamlit_app.py   # Streamlit UI
│   ├── schemas.py         # Pydantic models
│   └── __init__.py
│
├── src/
│   ├── preprocess.py
│   ├── search.py
│   ├── topics.py
│   ├── summary.py
│   ├── action_items.py
│   ├── decisions.py
│   └── output_formatter.py
│
├── tests/
│   ├── test_preprocess.py
│   ├── test_api.py
│   └── conftest.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── requirements.txt
├── main.py
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/venkatasai0234/meeting-intelligence-system.git
cd meeting-intelligence-system
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Run main pipeline

```
python main.py
```

---

### Run FastAPI server

```
uvicorn app.api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### Run Streamlit UI

```
streamlit run app/streamlit_app.py
```

---

## 📡 API Usage

### POST `/analyze`

Request:

```
{
  "transcript": "John: We should send the proposal...",
  "query": "What was decided?"
}
```

---

### POST `/analyze-file`

* Upload a `.txt` transcript file
* Optional query parameter

---

## 🧪 Run Tests

```
pytest
```

---

## Example Output

```
{
  "summary": {
    "overview": "The meeting focused on proposal, client review, and demo.",
    "key_decisions": [
      "The team agreed to delay the product demo until Thursday."
    ],
    "key_action_items": [
      "John: We should send the updated proposal by Friday."
    ]
  },
  "action_items": [...],
  "decisions": [...],
  "topics": [...],
  "search_results": [...]
}
```

---

## 🔥 Key ML Concepts Used

* NLP preprocessing (text cleaning, parsing)
* Rule-based baseline systems
* Sentence embeddings (Sentence-BERT)
* Semantic similarity (cosine similarity)
* Retrieval + reranking strategy
* Structured information extraction
* API design with Pydantic models
* End-to-end ML pipeline design

---

## 🎯 Future Improvements

* Replace rule-based extraction with ML models
* Add real-time audio transcription (speech-to-text)
* Use FAISS for scalable vector search
* Add user feedback loop for model improvement
* Dockerize and deploy to cloud (AWS/GCP/Azure)

---

## 💼 Why this project is strong

This project demonstrates:

* End-to-end ML system design
* NLP + retrieval + API integration
* Production-style architecture
* Real-world use case (meeting intelligence systems like Otter.ai)

## 👨‍💻 Author

**Venkata Siva Sai Krishna Prasad Yedupati**
Master’s in Computer Science — San Jose State University
