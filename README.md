# Week 3 – Day 10: Public Deployment (Render)

This final day wraps up our GPT-based agent backend by making it accessible to the public.

## Live API Features

- `/chat` – Conversational GPT with memory + tools
- `/chat/stream` – Stream GPT-4o token-by-token responses
- `/upload/{user_id}` – Upload + embed your own PDF
- Persona-prompt + memory summarization
- Deployed with Docker on Render (free tier)

## Tech Stack

- LangGraph
- Langchain + Langchain OpenAI
- GPT-4o
- FastAPI
- Docker
- Render (free web hosting)

## Test with:

```bash
curl -X POST https://gpt-copilot.onrender.com/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id": "dinesh", "query": "What is our onboarding policy?"}'
