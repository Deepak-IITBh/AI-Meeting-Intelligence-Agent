"""
RAG Pipeline for Meeting Intelligence Agent
Uses sentence-transformers for embeddings and FAISS for vector storage
"""

import logging
from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

logger = logging.getLogger(__name__)

# Global variables
vector_store = None
chunks = None
embedder = None

# Initialize Embedder
def initialize_embedder(model_name: str = "all-MiniLM-L6-v2") -> None:
    global embedder
    if embedder is None:
        logger.info(f"Loading embedder model: {model_name}")
        embedder = SentenceTransformer(model_name)
        logger.info("Embedder initialized successfully")

# Split Transcript into Chunks
def split_transcript_into_chunks(transcript: str, chunk_size: int = 3) -> List[str]:
    lines = transcript.strip().split("\n")
    chunks_list = []

    for i in range(0, len(lines), chunk_size):
        chunk = "\n".join(lines[i:i + chunk_size])
        if chunk.strip():
            chunks_list.append(chunk)

    logger.info(f"Split transcript into {len(chunks_list)} chunks")
    return chunks_list

# Build FAISS Vector Store
def build_vector_store(transcript: str) -> bool:
    global vector_store, chunks, embedder

    if not transcript or not transcript.strip():
        logger.error("Empty transcript provided")
        return False

    try:
        initialize_embedder()

        chunks = split_transcript_into_chunks(transcript)

        if not chunks:
            logger.error("No valid chunks created")
            return False

        embeddings = embedder.encode(chunks, convert_to_numpy=True)

        dimension = embeddings.shape[1]
        vector_store = faiss.IndexFlatL2(dimension)
        vector_store.add(embeddings.astype(np.float32))

        logger.info("Vector store created successfully")
        return True

    except Exception as e:
        logger.error(f"Error building vector store: {str(e)}")
        return False
# Ask Question (RAG Retrieval)
def ask_question(query: str, top_k: int = 3) -> str:
    global vector_store, chunks, embedder

    # Safety checks
    if vector_store is None or chunks is None:
        return "Please upload and process a video first to ask questions."

    if not query or not query.strip():
        return "Please enter a valid question."

    try:
        initialize_embedder()
        top_k = int(top_k)

        query_embedding = embedder.encode([query], convert_to_numpy=True)

        distances, indices = vector_store.search(
            query_embedding.astype(np.float32),
            top_k
        )

        relevant_chunks = [
            chunks[i] for i in indices[0] if i < len(chunks)
        ]

        if not relevant_chunks:
            return "No relevant information found in the transcript."

        answer = "Based on the meeting discussion:\n\n"
        answer += "\n\n".join(relevant_chunks)

        return answer

    except Exception as e:
        logger.error(f"Error answering question: {str(e)}")
        return "Error retrieving answer. Please try again."
