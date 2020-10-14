import uvicorn
from fastapi import FastAPI

from {{ cookiecutter.app_name }} import config
from {{ cookiecutter.app_name }}.routes import init_routes


def app_builder():
    application = FastAPI(version=config.API_VERSION, debug=config.APP_DEBUG)
    init_routes(application)
    return application


app = app_builder()

if __name__ == "__main__":
    uvicorn.run("{{ cookiecutter.app_name }}.main:app", port=8000, reload=config.APP_DEBUG, debug=config.APP_DEBUG)
