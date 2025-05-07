from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

posts = []

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "posts": posts})

@router.get("/write", response_class=HTMLResponse)
async def write_form(request: Request):
    return templates.TemplateResponse("write.html", {"request": request})

@router.post("/write", response_class=HTMLResponse)
async def submit_post(request: Request, title: str = Form(...), content: str = Form(...)):
    posts.append({"title": title, "content": content})
    return templates.TemplateResponse("dashboard.html", {"request": request, "posts": posts})
