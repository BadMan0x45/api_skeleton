import os

# APP settings
APP_DEBUG = os.getenv("APP_DEBUG", False)
APP_ENV = os.getenv("APP_ENV", "prod")


# API settings
API_PREFIX = os.getenv("API_PREFIX", "")
API_VERSION = os.getenv("API_VERSION", "v1")
