from fastapi import FastAPI

from api import router


# TODO: add middleware/etc. registration


# TODO: add config param
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router.router)
    return app
