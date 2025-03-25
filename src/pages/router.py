from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from src.posts.router import get_posts


router = APIRouter(
    prefix="/pages",
    tags=["Frontend"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/posts")
async def get_posts_page(
    request: Request,
    posts = Depends(get_posts)
):
    context = {
        "request": request,
        "posts": posts,
    }
    
    return templates.TemplateResponse(name="index.html", context=context)
