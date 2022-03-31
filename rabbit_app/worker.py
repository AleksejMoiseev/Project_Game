import logging

from kombu import Connection
from rabbit_app import message_bus

logging.basicConfig(level=logging.INFO)


class MessageBus:
    settings = message_bus.Settings()
    connection = Connection(settings.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    consumer = message_bus.create_consumer(
        connection
    )


MessageBus.consumer.run()
