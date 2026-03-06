from fastapi import Request, Response
from app_logger import logger
import uuid

async def trace_id_middleware(request: Request, call_next):
    trace_id = request.headers.get("x-trace-id")
    if not trace_id:
        trace_id = str(uuid.uuid4())
    request.state.trace_id = trace_id  # Store in request.state
    logger.info(
        "Request received",
        extra={
            "trace_id": trace_id,
            "method": request.method,
            "url": str(request.url)
        }
    )
    response: Response = await call_next(request)
    response.headers["x-trace-id"] = trace_id
    logger.info(
        "Response finished",
        extra={
            "trace_id": trace_id,
            "status_code": response.status_code,
            "url": str(request.url)
        }
    )
    return response