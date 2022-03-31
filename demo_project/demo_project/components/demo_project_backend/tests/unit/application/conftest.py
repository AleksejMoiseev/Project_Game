from unittest.mock import Mock

import pytest

from simple_shop.application import interfaces


@pytest.fixture(scope='function')
def products_repo(product_1, product_2):
    products_repo = Mock(interfaces.ProductsRepo)
    products_repo.find_by_keywords = Mock(return_value=[product_1, product_2])
    products_repo.get_by_sku = Mock(return_value=[product_1])

    return products_repo


@pytest.fixture(scope='function')
def customers_repo(customer):
    customers_repo = Mock(interfaces.CustomersRepo)
    customers_repo.get_by_id = Mock(return_value=customer)

    return customers_repo
