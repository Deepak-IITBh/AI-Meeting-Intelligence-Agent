AI Powered Meeting Intelligence Agent

This project is a simple but practical meeting analysis tool built using Streamlit. The idea is to take a meeting video, extract useful information from it, and allow users to interact with the meeting content through summaries and Q&A.

Instead of just storing the video, the system processes it and provides structured insights like summaries and action items. It also allows users to ask questions about the meeting using a basic RAG (Retrieval-Augmented Generation) pipeline.

What This Project Can Do
Upload meeting videos (MP4, AVI, MOV, MKV)
Generate a short summary of the meeting
Extract action items from the discussion
Ask questions about the meeting content
Retrieve relevant answers using vector search
The UI is clean and simple so the focus stays on functionality.

Project Structure

```
AI-Meeting-Intelligence-Agent/
│
├── app.py                    # Streamlit UI and main application workflow
├── video_processor.py        # Video file handling and audio extraction
├── rag_pipeline.py           # FAISS vector store and Q&A retrieval
├── llm_utils.py              # LLM integration for summaries and action items
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (API keys)
└── README.md                 # Project documentation
```

**File Descriptions**

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application - handles UI, video upload, and workflow orchestration |
| `video_processor.py` | Processes video files, extracts audio, and generates transcripts |
| `rag_pipeline.py` | Creates FAISS vector embeddings and performs semantic search for Q&A |
| `llm_utils.py` | Integrates Groq API to generate summaries and extract action items |
| `requirements.txt` | Lists all Python package dependencies |
| `.env` | Stores sensitive API keys (GROQ_API_KEY) - not committed to git |

Setup Instructions
Requirements
Python 3.8 or above
Groq API key (get it from https://console.groq.com)

Steps to Run
1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate it:

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root and add:
```
GROQ_API_KEY=your_api_key_here
```

5. Run the app:
```bash
streamlit run app.py
```


The application will open at:

http://localhost:8501

How to Use the App

Upload a meeting video.

Click on “Process Video”.
Once processed, you’ll see:
A short summary of the meeting
Extracted action items

You can then type a question about the meeting and get answers based on the transcript.

Tech Stack Used

Streamlit – For the web interface
Groq API – For LLM-powered summaries and Q&A
sentence-transformers – To generate embeddings
FAISS – For similarity search
Python – Backend logic