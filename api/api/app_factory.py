from fastapi import FastAPI as FastAPIApp

from api.routers import demo_router


# TODO: add middleware/etc. registration


def register_routers(app: FastAPIApp) -> None:
    app.include_router(demo_router)


def register_startup_events(app: FastAPIApp) -> None:
    # TODO: will this work?
    @app.on_event('startup')
    def temp_startup() -> None:
        print('temp startup event printing')


def register_shutdown_events(app: FastAPIApp) -> None:
    # TODO: will this work?
    @app.on_event('shutdown')
    def temp_shutdown() -> None:
        print('temp shutdown event printing')


# TODO: add config param
def create_app() -> FastAPIApp:
    app = FastAPIApp()
    register_routers(app)
    register_startup_events(app)
    register_shutdown_events(app)
    return app
