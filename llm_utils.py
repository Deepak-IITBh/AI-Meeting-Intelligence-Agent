
"""
LLM Utilities for Meeting Intelligence Agent
Uses Groq API for meeting insights generation
"""

from typing import Tuple, List
from groq import Groq


def generate_meeting_insights(transcript: str, groq_api_key: str) -> Tuple[str, List[str]]:
    """
    Generate meeting summary and action items using Groq
    """

    if not transcript.strip():
        raise ValueError("Empty transcript")

    if not groq_api_key:
        raise ValueError("Groq API key not provided")

    # Initialize Groq client properly
    client = Groq(api_key=groq_api_key)

    model = "llama-3.1-8b-instant"

    # SUMMARY
    summary_response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"""
Provide a concise 5-7 line professional meeting summary.

Transcript:
{transcript}
"""
            }
        ],
        temperature=0.3,
        max_tokens=400,
    )

    summary = summary_response.choices[0].message.content.strip()
#ACTION ITEMS
    action_response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"""
Extract clear action items from this transcript.
Return only bullet points.

Transcript:
{transcript}
"""
            }
        ],
        temperature=0.3,
        max_tokens=400,
    )

    raw_actions = action_response.choices[0].message.content.strip()

    action_items = []
    for line in raw_actions.split("\n"):
        line = line.strip()
        if line.startswith("-"):
            action_items.append(line[1:].strip())
        elif line:
            action_items.append(line)

    return summary, action_items[:5]
