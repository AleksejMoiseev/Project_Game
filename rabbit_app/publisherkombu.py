from kombu import Connection, Exchange, Queue
from message_bus.settings import settings
from message_bus import RabbitConfigKombu

media_exchange = Exchange(
    RabbitConfigKombu.exchange.value,
    RabbitConfigKombu.exchange_type.value,
    durable=True
)

video_queue = Queue(
    RabbitConfigKombu.queue.value,
    exchange=media_exchange,
    routing_key=RabbitConfigKombu.routing_key.value
)

connection = Connection(settings.BROKER_URL)


def process_media(body, message):
    print(body)
    message.ack()


with connection as conn:
    producer = conn.Producer(serializer='json')
    producer.publish(
        {'name': 'My_message', 'size': 2},
        exchange=media_exchange, routing_key='test',
        declare=[video_queue],
    )
