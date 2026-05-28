"""
Pydantic схемы для валидации различных форматов ошибок API.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, StrictInt, StrictStr, StrictBool


class StandardErrorResponse(BaseModel):
    """
    Стандартный формат ошибки API.
    Используется для ошибок авторизации и других стандартных ошибок.

    Пример:
    {
        "status": 401,
        "title": "Wrong authentification.",
        "detail": "Неправильный логин или пароль."
    }
    """
    status: StrictInt
    title: StrictStr
    detail: StrictStr


class ErrorData(BaseModel):
    """Данные ошибки в формате API"""
    errorCode: Optional[StrictInt] = None
    id: Optional[StrictStr] = None


class ApiErrorResponse(BaseModel):
    """
    Формат ошибки API с полем success.
    Используется для ошибок операций (удаление, обновление и т.д.).

    Пример:
    {
        "success": False,
        "message": "Bad request, id required",
        "data": {"errorCode": 404}
    }
    """
    success: StrictBool
    message: StrictStr
    data: ErrorData


class ValidationErrorResponse(BaseModel):
    """
    Формат ошибки валидации.
    Используется для ошибок валидации входных данных.

    Пример:
    {
        "success": False,
        "message": "Validation failed",
        "errors": {
            "field1": ["Error message 1", "Error message 2"],
            "field2": ["Error message 3"]
        }
    }
    """
    success: StrictBool
    message: StrictStr
    errors: Optional[Dict[str, Any]] = None
