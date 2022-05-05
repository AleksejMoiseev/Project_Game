from rabbit_app import message_bus
from kombu import Connection
from classic.messaging_kombu import KombuPublisher
from classic.messaging import Message
from message_bus.config import ExchangeFanout, RabbitConfigKombu


class MessageBus:
    settings = message_bus.settings
    connection = Connection(settings.BROKER_URL)
    #message_bus.broker_scheme.declare(connection)
    message_bus.broker_scheme_with_routing_key.declare(connection)

    # publisher = KombuPublisher(
    #     connection=connection,
    #     scheme=message_bus.broker_scheme,
    # )

    publisher_with_routing_key = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme_with_routing_key,
    )

    # #publisher.plan(Message('OrderPlaced', {'order_number': 111111111111111}))
    # publisher.plan(
    #     Message(ExchangeFanout.exchange.value, {'order_number': 333333}), Message(ExchangeFanout.exchange.value, {'order_number': 44444})
    # )

    # publisher.flush()

    publisher_with_routing_key.plan(Message(RabbitConfigKombu.exchange.value, {'message': 777777}))
    publisher_with_routing_key.flush()


# def send_message(message):
#     MessageBus.publisher.plan(
#         Message('OrderPlaced', {'order_number': message})
#     )
