from classic.messaging_kombu import KombuConsumer
from kombu import Connection

from rabbit_app.message_bus.scheme import broker_scheme
from rabbit_app.message_bus.config import ExchangeFanout


def send_message_to_manager(order_number):
    print(order_number)


def create_consumer(connection: Connection) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection,
                             scheme=broker_scheme)

    consumer.register_function(
        send_message_to_manager, ExchangeFanout.queue.value,
    )

    return consumer
