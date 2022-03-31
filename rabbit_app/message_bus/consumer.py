from classic.messaging_kombu import KombuConsumer
from kombu import Connection


from .scheme import broker_scheme


def create_consumer(connection: Connection,
                    orders) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection,
                             scheme=broker_scheme)

    consumer.register_function(
        orders.send_message_to_manager, 'PrintOrderPlaced',
    )

    return consumer
