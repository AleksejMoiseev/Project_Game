from rabbit_app import message_bus
from kombu import Connection
from classic.messaging_kombu import KombuPublisher
from classic.messaging import Message


class MessageBus:
    settings = message_bus.Settings()
    connection = Connection(settings.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )


def send_message(message):
    MessageBus.publisher.plan(
        Message('OrderPlaced', {'order_number': message})
    )
