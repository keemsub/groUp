from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api import pages, posts, chat

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# 라우터 등록
app.include_router(pages.router)
app.include_router(posts.router)
app.include_router(chat.router)