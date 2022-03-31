from rabbit_app import message_bus
from kombu import Connection
from classic.messaging_kombu import KombuPublisher
from classic.messaging import Message
from message_bus.config import ExchangeFanout


class MessageBus:
    settings = message_bus.settings
    connection = Connection(settings.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )

    #publisher.plan(Message('OrderPlaced', {'order_number': 111111111111111}))
    publisher.plan(Message(ExchangeFanout.exchange.value, {'order_number': '1026658'}))
    publisher.flush()


def send_message(message):
    MessageBus.publisher.plan(
        Message('OrderPlaced', {'order_number': message})
    )
