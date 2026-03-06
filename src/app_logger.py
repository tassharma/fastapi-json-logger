import logging
import json
import sys

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            'level': record.levelname,
            'message': record.getMessage(),
            'timestamp': self.formatTime(record),
            'service': record.name,
        }
        # Only include explicitly passed extra attributes
        # Standard LogRecord attributes to exclude
        standard_attrs = set([
            'name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename', 'module',
            'exc_info', 'exc_text', 'stack_info', 'lineno', 'funcName', 'created', 'msecs',
            'relativeCreated', 'thread', 'threadName', 'processName', 'process', 'message'
        ])
        for key, value in record.__dict__.items():
            if key not in standard_attrs and not key.startswith('_'):
                log_obj[key] = value
        return json.dumps(log_obj)

def setup_logger():
    logger = logging.getLogger("fastapi_json_logger")
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    
    logger.addHandler(handler)

setup_logger()

logger = logging.getLogger("fastapi_json_logger")