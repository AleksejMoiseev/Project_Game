from kombu import Connection
from sqlalchemy import create_engine

from evraz.classic.sql_storage import TransactionContext

from simple_shop.adapters import database, log, mail_sending, message_bus
from simple_shop.application import services


class Settings:
    db = database.Settings()
    message_bus = message_bus.Settings()


class Logger:
    log.configure(
        Settings.db.LOGGING_CONFIG,
        Settings.message_bus.LOGGING_CONFIG,
    )


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine, expire_on_commit=False)

    orders_repo = database.repositories.OrdersRepo(context=context)


class MailSending:
    sender = mail_sending.FileMailSender()


class Application:
    orders = services.Orders(
        orders_repo=DB.orders_repo,
        mail_sender=MailSending.sender,
    )


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    consumer = message_bus.create_consumer(connection, Application.orders)

    @staticmethod
    def declare_scheme():
        message_bus.broker_scheme.declare(MessageBus.connection)


if __name__ == '__main__':
    MessageBus.declare_scheme()
    MessageBus.consumer.run()
