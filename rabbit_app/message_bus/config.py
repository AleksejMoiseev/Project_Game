from enum import Enum
from pydantic import BaseSettings


class Settings(BaseSettings):
    BROKER_URL: str


settings = Settings(BROKER_URL='amqp://user:password@localhost:5672//')


class RabbitConfigKombu(Enum):

    exchange = 'amq.direct'
    exchange_type = 'direct'
    routing_key = 'test'
    queue = 'My_Queu'


class ExchangeFanout(Enum):
    exchange = 'amq.fanout'
    exchange_type = 'fanout'
    queue = 'fan-1'