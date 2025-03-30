from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

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


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
