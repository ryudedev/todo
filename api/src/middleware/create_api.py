from fastapi import APIRouter

from middleware.tags import Tags


def create_api(prefix: str, tags: list[Tags], api_routes: list[APIRouter]) -> APIRouter:
    if not prefix:
        raise ValueError("prefix is required")
    if not tags:
        raise ValueError("tags is required")
    if not api_routes:
        raise ValueError("api_routes is required")

    app = APIRouter(prefix=prefix, tags=[tag.value for tag in tags])
    for api_route in api_routes:
        app.include_router(api_route)

    return app
