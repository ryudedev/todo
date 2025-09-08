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

    log_level: str = Field(..., validation_alias="LOG_LEVEL")


configs = Configs()
