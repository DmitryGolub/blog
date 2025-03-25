from fastapi import FastAPI

from src.posts.router import router as posts_router
from src.users.router import router as users_router
from src.posts.comments.router import router as comments_router


app = FastAPI()

app.include_router(posts_router)
app.include_router(users_router)
app.include_router(comments_router)

