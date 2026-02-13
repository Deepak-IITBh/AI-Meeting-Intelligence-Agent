
"""
Streamlit App - AI Meeting Intelligence Agent
Using Groq API + RAG
"""

import streamlit as st
from video_processor import process_video
from llm_utils import generate_meeting_insights
from rag_pipeline import build_vector_store, ask_question


# Session State Initialization
def initialize_session_state():
    if "video_processed" not in st.session_state:
        st.session_state.video_processed = False
    if "transcript" not in st.session_state:
        st.session_state.transcript = None
    if "meeting_summary" not in st.session_state:
        st.session_state.meeting_summary = None
    if "action_items" not in st.session_state:
        st.session_state.action_items = None
    if "vector_store_ready" not in st.session_state:
        st.session_state.vector_store_ready = False
# Header
def render_header():
    st.set_page_config(
        page_title="AI Meeting Intelligence",
        page_icon="🎥",
        layout="wide"
    )
    st.title("🎥 AI Meeting Intelligence Agent")
    st.markdown("Transform meeting videos into structured insights using AI")

# Sidebar
def render_sidebar():
    with st.sidebar:
        st.header("Configuration")
        st.text_input("Groq API Key", type="password", key="groq_key")

# Video Upload Section
def render_video_section():
    st.header("📹 Upload Meeting Video")

    uploaded_file = st.file_uploader(
        "Choose a video file",
        type=["mp4", "avi", "mov", "mkv"]
    )

    if uploaded_file:
        st.caption(f"📄 Selected: {uploaded_file.name}")

        if st.button("🚀 Process Video"):

            if not st.session_state.groq_key:
                st.error("Please enter Groq API key in Configuration.")
                return

            with st.spinner("Processing video..."):

                try:
                    # Step 1: Get Transcript
                    transcript = process_video(uploaded_file, "dummy")

                    if not transcript:
                        st.error(" Failed to extract transcript.")
                        return

                    # Step 2: Generate Summary + Actions
                    summary, actions = generate_meeting_insights(
                        transcript,
                        st.session_state.groq_key
                    )

                    # Step 3: Build RAG
                    build_vector_store(transcript)

                    # Save to session
                    st.session_state.transcript = transcript
                    st.session_state.meeting_summary = summary
                    st.session_state.action_items = actions
                    st.session_state.video_processed = True
                    st.session_state.vector_store_ready = True

                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    return

            st.success("Video processed successfully!")


# Summary Section
def render_summary_section():
    st.header("📋 Meeting Summary")

    if st.session_state.video_processed:
        if st.session_state.meeting_summary:
            st.write(st.session_state.meeting_summary)
        else:
            st.warning("Summary not available.")
    else:
        st.info("Process a video to see the summary.")

# Action Items Section
def render_action_section():
    st.header("Action Items")

    if st.session_state.video_processed:
        if st.session_state.action_items:
            for item in st.session_state.action_items:
                st.write(f"• {item}")
        else:
            st.warning("Action items not available.")
    else:
        st.info("Process a video to see action items.")


# Q&A Section (RAG)
def render_qa_section():
    st.header("💬 Ask Questions About the Meeting")

    if st.session_state.vector_store_ready:
        query = st.text_input(
            "Ask a question:",
            placeholder="What were the key decisions made?"
        )

        if st.button("🔍 Get Answer") and query:
            with st.spinner("Generating answer..."):
                answer = ask_question(query) 
                st.success(answer)
    else:
        st.info("Process a video to enable question answering.")


# Main
def main():
    initialize_session_state()
    render_header()
    render_sidebar()

    st.divider()
    render_video_section()

    st.divider()
    render_summary_section()

    st.divider()
    render_action_section()

    st.divider()
    render_qa_section()


if __name__ == "__main__":
    main()
