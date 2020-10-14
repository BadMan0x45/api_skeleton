from {{ cookiecutter.app_name }}.api import internal_

from fastapi import FastAPI


def init_routes(app: FastAPI):
    app.include_router(internal_.router)
