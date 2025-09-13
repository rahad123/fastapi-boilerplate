from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define configurations for different environments
configurations = {
    "development": {
        "SERVICE_NAME": os.getenv("SERVICE_NAME", "DESIGN_PATTERN"),
        "PORT": int(os.getenv("PORT", "8080")),
        "HOST": os.getenv("HOST", "127.0.0.1"),
    },
    "production": {
        "SERVICE_NAME": os.getenv("SERVICE_NAME"),
        "PORT": os.getenv("PORT"),
        "HOST": os.getenv("HOST"),
    }
}

# Get configuration variables based on the environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
config = configurations.get(ENVIRONMENT, configurations["development"])
