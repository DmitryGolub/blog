from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from src.posts.router import get_posts, get_post
from src.posts.comments.router import get_comments


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
    
    return templates.TemplateResponse(name="posts.html", context=context)



@router.get("/posts/{post_id}")
async def get_post_by_id_page(
    request: Request,
    post = Depends(get_post),
    comments = Depends(get_comments)
):
    context = {
        "request": request,
        "post": post,
        "comments": comments,
    }

    return templates.TemplateResponse(name="post.html", context=context)