from sqlalchemy import create_engine

from evraz.classic.sql_storage import TransactionContext

from simple_shop.adapters import database, log, mail_sending, shop_api
from simple_shop.application import services


class Settings:
    db = database.Settings()
    shop_api = shop_api.Settings()


class Logger:
    log.configure(
        Settings.db.LOGGING_CONFIG,
        Settings.shop_api.LOGGING_CONFIG,
    )


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    customers_repo = database.repositories.CustomersRepo(context=context)
    products_repo = database.repositories.ProductsRepo(context=context)
    carts_repo = database.repositories.CartsRepo(context=context)
    orders_repo = database.repositories.OrdersRepo(context=context)


class MailSending:
    sender = mail_sending.FileMailSender()


class Application:
    catalog = services.Catalog(products_repo=DB.products_repo)
    checkout = services.Checkout(
        customers_repo=DB.customers_repo,
        products_repo=DB.products_repo,
        carts_repo=DB.carts_repo,
        orders_repo=DB.orders_repo,
    )
    orders = services.Orders(
        orders_repo=DB.orders_repo,
        mail_sender=MailSending.sender,
    )
    customers = services.Customers(customers_repo=DB.customers_repo)

    is_dev_mode = Settings.shop_api.IS_DEV_MODE
    allow_origins = Settings.shop_api.ALLOW_ORIGINS


class Aspects:
    services.join_points.join(DB.context)
    shop_api.join_points.join(DB.context)


app = shop_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    allow_origins=Application.allow_origins,
    catalog=Application.catalog,
    checkout=Application.checkout,
    orders=Application.orders,
    customers=Application.customers,
)
