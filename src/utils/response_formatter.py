from fastapi import Response
from fastapi.responses import JSONResponse


def format_response(
        response: Response,
        status_code: int,
        data=None,
        message="",
        success=True) -> JSONResponse:
    """
    Format a JSON response with the given status code, data, message, and success status.
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "status_code": status_code,
            "success": success,
            "data": data,
            "error": not success,
            "message": message
        }
    )


def format_error(status_code: int, message: str, response: Response) -> dict:
    """
    Format an error response with the given status code and message.
    """
    response.status_code = status_code
    return format_response(response, status_code, message=message, success=False)
