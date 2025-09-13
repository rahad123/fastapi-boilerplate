from src.app.modules.users import users_repo
from fastapi import Response, Request


async def get_user(req):
    user_id = int(req.path_params.get("user_id"))

    # Call the repository function to retrieve the user
    return await users_repo.get_user(user_id)


async def create_user(req):
    payload = await req.json()

    # Call the repository function to create the user
    return await users_repo.create_user(payload)
