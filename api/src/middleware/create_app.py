from fastapi import APIRouter, FastAPI

from config import configs


def create_app(extra_routes: list[APIRouter] = []) -> FastAPI:
    app = FastAPI(
        title=configs.todo_api_name,
        version=configs.version,
    )

    @app.get("/")
    def health():
        return {"message": "Hello, World!"}

    if extra_routes:
        for route in extra_routes:
            app.include_router(route)

    return app
