from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from app.services.chat_service import get_chat_response
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/resume_chat", response_class=HTMLResponse)
async def resume_chat_ui(request: Request):
    return templates.TemplateResponse("resume_chat.html", {"request": request})

class ChatRequest(BaseModel):
    question: str

@router.post("/api/chat")
async def chat(request: ChatRequest):
    answer = get_chat_response(request.question)
    return JSONResponse(content={"answer": answer})
