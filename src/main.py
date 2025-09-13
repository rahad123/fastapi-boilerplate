import uvicorn
from src import create_app
from src.config.config_service import config

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host=config["HOST"], port=config["PORT"])
