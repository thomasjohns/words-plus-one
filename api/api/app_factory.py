from fastapi import FastAPI as FastAPIApp

from api import router


# TODO: add middleware/etc. registration


def register_routers(app: FastAPIApp) -> None:
    app.include_router(router.router)


# TODO: add config param
def create_app() -> FastAPIApp:
    app = FastAPIApp()
    register_routers(app)
    return app
