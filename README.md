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
.
├── app.py
├── video_processor.py
├── rag_pipeline.py
├── llm_utils.py
├── requirements.txt
└── README.md

What Each File Does

app.py – Handles the Streamlit UI and overall workflow.
video_processor.py – Manages video file handling and transcript simulation.
rag_pipeline.py – Builds the FAISS vector store and handles question answering.
llm_utils.py – Generates the meeting summary and action items.
requirements.txt – Contains the required Python dependencies.

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