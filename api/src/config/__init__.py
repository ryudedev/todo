import os
from pydantic import Field
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Configs(BaseSettings):
    def __init__(self) -> None:
        env = os.environ.get("ENV", "local").lower()
        dotenv_path = os.path.join(os.path.dirname(__file__), f".env_{env}")
        load_dotenv(dotenv_path=dotenv_path)
        super().__init__()

    version: str = Field(..., validation_alias="VERSION")
    log_level: str = Field(..., validation_alias="LOG_LEVEL")
    todo_api_name: str = Field(..., validation_alias="TODO_API_NAME")

    # CORS
    allow_origins: list[str] = Field(..., validation_alias="ALLOW_ORIGINS")
    allow_methods: list[str] = Field(..., validation_alias="ALLOW_METHODS")
    allow_headers: list[str] = Field(..., validation_alias="ALLOW_HEADERS")
    allow_credentials: bool = Field(..., validation_alias="ALLOW_CREDENTIALS")


configs = Configs()
