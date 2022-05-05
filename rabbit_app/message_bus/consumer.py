from classic.messaging_kombu import KombuConsumer
from kombu import Connection

from rabbit_app.message_bus.scheme import broker_scheme, broker_scheme_with_routing_key
from rabbit_app.message_bus.config import ExchangeFanout, RabbitConfigKombu


def send_message_to_manager(order_number):
    print(order_number)


def send_message_with_routing_key(message):
    print(message)


def create_consumer(connection: Connection) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection,
                             scheme=broker_scheme)

    consumer.register_function(
        send_message_to_manager, ExchangeFanout.queue.value,
    )

    return consumer


def create_consumer_with_routing_key(connection: Connection) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection,
                             scheme=broker_scheme_with_routing_key)

    consumer.register_function(
        send_message_with_routing_key, RabbitConfigKombu.queue.value,
    )

    return consumer
