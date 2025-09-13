from fastapi import FastAPI
from src.routers.v1 import users_route
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # You can specify origins here, e.g., ["http://localhost", "http://example.com"]
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def init_func():
    return {"message": "FastAPI template Server is running."}


def create_app():
    app.include_router(users_route.UserRouter, prefix="/api/v1")
    return app
