from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str
    TITLE: str
    DESCRIPTION: str
    VERSION: str

    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///demo.sqlite'

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
