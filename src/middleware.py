# middleware.py

from fastapi import Request
import logging
import time

logger = logging.getLogger("app")


async def logging_middleware(request: Request, call_next):
    start_time = time.time()

    logger.info(f"➡ Incoming: {request.method} {request.url.path}")

    response = await call_next(request)

    duration = round(time.time() - start_time, 4)
    logger.info(f"⬅ Response: {response.status_code} | {duration}s")

    return response