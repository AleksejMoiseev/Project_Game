from pydantic import BaseSettings


class Settings(BaseSettings):
    BROKER_URL: str


settings = Settings(BROKER_URL='amqp://user:password@localhost:5672//')