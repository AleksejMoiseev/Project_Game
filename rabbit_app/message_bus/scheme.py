from classic.messaging_kombu import BrokerScheme
from kombu import Exchange, Queue
from .config import ExchangeFanout, RabbitConfigKombu

exchange = Exchange(
    ExchangeFanout.exchange.value,
    ExchangeFanout.exchange_type.value,
)

queue1 = Queue(ExchangeFanout.queue.value, exchange)

broker_scheme = BrokerScheme(Queue(ExchangeFanout.queue.value, exchange))


# broker_scheme = BrokerScheme(
#     Queue('PrintOrderPlaced', Exchange('OrderPlaced'))
# )

routing_key = 'routing_key'

exchange_with_routing_key = Exchange(
    RabbitConfigKombu.exchange.value,
    RabbitConfigKombu.exchange_type.value,
)

broker_scheme_with_routing_key = BrokerScheme(
    Queue(RabbitConfigKombu.queue.value, exchange_with_routing_key, routing_key=routing_key)
)
