from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.posts.router import router as posts_router
from src.users.router import router as users_router
from src.posts.comments.router import router as comments_router

from src.images.router import router as router_images


app = FastAPI()


app.mount("/static", StaticFiles(directory="src/static"), "static")


app.include_router(posts_router)
app.include_router(users_router)
app.include_router(comments_router)
app.include_router(router_images)