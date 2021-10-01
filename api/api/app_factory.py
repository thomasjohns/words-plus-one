from fastapi import FastAPI as FastAPIApp

from api.routers import demo_router


# TODO: add middleware/etc. registration


def register_routers(app: FastAPIApp) -> None:
    app.include_router(demo_router)


# TODO: add config param
def create_app() -> FastAPIApp:
    app = FastAPIApp()
    register_routers(app)
    return app
