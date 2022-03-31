from kombu import Connection, Exchange, Queue

media_exchange = Exchange('amq.direct', 'direct', durable=True)
video_queue = Queue('My_Queu', exchange=media_exchange, routing_key='test')

connection = Connection('amqp://user:password@localhost:5672//')


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
