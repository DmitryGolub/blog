from fastapi import FastAPI

from src.posts.router import router as posts_router


app = FastAPI()

app.include_router(posts_router)

@app.get("/")
async def home_page():
    return {"Hello": "World"}
