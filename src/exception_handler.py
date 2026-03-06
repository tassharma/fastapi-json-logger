# exception_handler.py

from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions import AppException
import logging

logger = logging.getLogger("app")
logging.basicConfig(level=logging.INFO)


async def app_exception_handler(request: Request, exc: AppException):
    """
    Handles all known/custom exceptions
    """
    logger.error(
        f"Application error: {exc.message} | Path: {request.url.path}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.message,
            "type": exc.__class__.__name__
        }
    )


async def global_exception_handler(request: Request, exc: Exception):
    """
    Handles unexpected exceptions
    """
    logger.exception(
        f"Unhandled error at {request.url.path}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "type": "UnexpectedError"
        }
    )