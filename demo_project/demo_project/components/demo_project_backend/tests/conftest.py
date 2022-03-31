import pytest

from simple_shop.application import dataclasses


@pytest.fixture(scope='function')
def product_1():
    return dataclasses.Product(
        sku='U-001',
        title='Отвертка',
        description='Отвертка крестовая',
        price=234.1,
    )


@pytest.fixture(scope='function')
def product_2():
    return dataclasses.Product(
        sku='U-002',
        title='Дрель',
        description='Дрель-перфоратор',
        price=2341.1,
    )


@pytest.fixture(scope='function')
def cart_position_1(product_1):
    return dataclasses.CartPosition(
        id=1,
        product=product_1,
        quantity=1,
    )


@pytest.fixture(scope='function')
def cart_position_2(product_2):
    return dataclasses.CartPosition(
        id=2,
        product=product_2,
        quantity=2,
    )


@pytest.fixture(scope='function')
def cart(cart_position_1, cart_position_2):
    return dataclasses.Cart(
        id=1,
        customer_id=1,
        positions=[cart_position_1, cart_position_2],
    )


@pytest.fixture(scope='function')
def customer():
    return dataclasses.Customer(
        id=1,
        email='foo@example.com',
    )
