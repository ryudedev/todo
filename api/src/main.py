from fastapi.middleware.cors import CORSMiddleware

from config import configs
from middleware import singleton
from middleware.create_app import create_app
from routes.v1 import v1_router


@singleton
class AppCreater:
    def __init__(self) -> None:
        self.app = create_app()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=configs.allow_origins,
            allow_methods=configs.allow_methods,
            allow_headers=configs.allow_headers,
            allow_credentials=configs.allow_credentials,
        )
        self.app.include_router(v1_router)


app = AppCreater().app
