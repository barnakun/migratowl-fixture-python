from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "fixture"
    debug: bool = False
