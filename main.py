from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent_graph import run_agent, run_agent_stream
from file_upload import router as upload_router
from fastapi.responses import StreamingResponse

# Create app BEFORE including routers
app = FastAPI()

# Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# Register routers
app.include_router(upload_router)

# Chat route
class ChatRequest(BaseModel):
    user_id: str
    query: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = run_agent(request.user_id, request.query)
    return {"response": response}

"""@app.post("/chat/stream")
async def stream_chat(req: ChatRequest):
    response = StreamingResponse(
        run_agent_stream(req.user_id, req.query),
        media_type="text/event-stream"
    )
    return  response"""

@app.post("/chat/stream")
async def stream_chat(req: ChatRequest):
    def event_stream():
        for chunk in run_agent_stream(req.user_id, req.query):
            yield chunk + "\n"
    return StreamingResponse(event_stream(), media_type="text/plain")