# exceptions.py

class AppException(Exception):
    """
    Base application exception
    """
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class SecurityException(AppException):
    def __init__(self, message="Unauthorized"):
        super().__init__(message, 401)


class ValidationException(AppException):
    def __init__(self, message="Bad Request"):
        super().__init__(message, 400)


class NotFoundException(AppException):
    def __init__(self, message="Not Found"):
        super().__init__(message, 404)