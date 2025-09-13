from fastapi import APIRouter, Request, Response
from src.app.modules.users import users_controller

UserRouter = APIRouter(prefix="/users")


@UserRouter.get("/{user_id}")
async def read_user(req: Request, res: Response):
    return await users_controller.get_user(req, res)


@UserRouter.post("/")
async def create_user(req: Request, res: Response):
    return await users_controller.create_user(req, res)
