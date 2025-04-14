import time
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from src.posts.router import router as posts_router
from src.users.router import router as users_router
from src.posts.comments.router import router as comments_router
from src.images.router import router as router_images
from src.config import settings
from src.logger import logger


app = FastAPI()


app.mount("/static", StaticFiles(directory="src/static"), "static")


app.include_router(posts_router)
app.include_router(users_router)
app.include_router(comments_router)
app.include_router(router_images)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    logger.info("Request handling time", extra={
        "process_time": round(process_time, 4)
    })

    return response
