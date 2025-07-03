"""AI orchestration service using FastAPI."""
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from shared import phi_utils

app = FastAPI()
MCP_URL = os.getenv("MCP_URL", "http://mcp-service:5008")


class AskRequest(BaseModel):
    """Incoming question format."""
    user_id: str
    message: str


@app.post("/ask")
async def ask(req: AskRequest):
    """Handle an incoming question and orchestrate AI models."""
    # TODO: intent classification
    if "patient" in req.message:
        mcp_resp = requests.get(f"{MCP_URL}/mcp/{req.user_id}")
        mcp_context = mcp_resp.json()
    else:
        mcp_context = {}
    prompt = f"Answer with empathy using context: { {{} if not mcp_context else mcp_context} } \n {req.message}"
    rewritten = phi_utils.rewrite_tone(prompt)
    # TODO: call LLM like GPT-4 or Perplexity
    return {"reply": f"AI response to: {rewritten}"}
