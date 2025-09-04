import time

import psutil
from fastapi import FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.database import engine
from src.handle_on_startup import handle_on_startup
from src.middlewares.cors import cors
from src.routes.private import private
from src.routes.public import public

app = FastAPI()

cors(app)


@app.on_event("startup")
async def on_startup():
    await handle_on_startup()


@app.get("/")
async def root_info():
    START_TIME = time.time()

    uptime_seconds = int(time.time() - START_TIME)

    cpu_percent = psutil.cpu_percent(interval=0.5)

    memory = psutil.virtual_memory()

    db_status = "ok"

    db_latency_ms = None

    try:
        async with AsyncSession(engine) as session:
            start_db = time.time()

            await session.execute(select(1))

            db_latency_ms = round((time.time() - start_db) * 1000, 2)

    except Exception as e:
        db_status = f"error: {str(e)}"

    return {
        "made_with": "FastAPI, SQLModel",
        "docs": "see /docs",
        "redoc": "see /redoc",
        "health": {
            "status": "ok",
            "uptime_seconds": uptime_seconds,
            "cpu_percent": cpu_percent,
            "memory": {
                "total_mb": round(memory.total / 1024 / 1024, 2),
                "available_mb": round(memory.available / 1024 / 1024, 2),
                "percent_used": memory.percent,
            },
            "database": {"status": db_status, "latency_ms": db_latency_ms},
        },
    }


for public_route in public:
    app.include_router(public_route)

for private_route in private:
    app.include_router(private_route)
