# from fastapi import FastAPI, Request
# from app_logger import logger
# from trace_middleware import trace_id_middleware
# from exception import AppException

# app = FastAPI()
# app.middleware("http")(trace_id_middleware)

# @app.get("/test-logs")
# def test_logs(request: Request):
#     trace_id = request.state.trace_id  # Get from request.state
#     logger.info("This is an INFO log message", extra={"trace_id": trace_id, "PatientId": "Patient1"})
#     logger.error("This is an ERROR log message", extra={"trace_id": trace_id, "PatientId": "Patient1"})
#     return {"message": "Logs have been emitted"}

# main.py

from fastapi import FastAPI
from middleware import logging_middleware
from exceptions import AppException, SecurityException
from exception_handler import (
    app_exception_handler,
    global_exception_handler
)

app = FastAPI()

# Register middleware
app.middleware("http")(logging_middleware)

# Register exception handlers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)


@app.get("/success")
async def success():
    return {"message": "Success"}


@app.get("/custom-error")
async def custom_error():
    raise SecurityException("Invalid token")


@app.get("/global-error")
async def global_error():
    return 1 / 0