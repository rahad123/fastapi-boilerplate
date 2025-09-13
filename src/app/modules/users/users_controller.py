from src.app.modules.users import users_service
from src.utils.response_formatter import format_response, format_error
from fastapi import Request, Response
from http import HTTPStatus


async def get_user(req, res):
    try:
        user = await users_service.get_user(req)

        return format_response(res, HTTPStatus.OK.value, user,
                               "User retrieved successfully")
    except Exception as e:
        return format_error(
            HTTPStatus.INTERNAL_SERVER_ERROR.value,
            f"An error occurred while retrieving user: {str(e)}",
            res)


async def create_user(req, res):
    try:
        user = await users_service.create_user(req)

        return format_response(res, HTTPStatus.CREATED.value,
                               user, "User created successfully")
    except Exception as e:
        return format_error(
            HTTPStatus.INTERNAL_SERVER_ERROR.value,
            f"An error occurred while creating user: {str(e)}",
            res)
