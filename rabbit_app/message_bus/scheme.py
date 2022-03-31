from classic.messaging_kombu import BrokerScheme
from kombu import Exchange, Queue
from .config import ExchangeFanout

exchange = Exchange(
    ExchangeFanout.exchange.value,
    ExchangeFanout.exchange_type.value,
)

queue1 = Queue(ExchangeFanout.queue.value, exchange)

broker_scheme = BrokerScheme(Queue(ExchangeFanout.queue.value, exchange))


# broker_scheme = BrokerScheme(
#     Queue('PrintOrderPlaced', Exchange('OrderPlaced'))
# )
