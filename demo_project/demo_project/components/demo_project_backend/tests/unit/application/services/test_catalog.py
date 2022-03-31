import pytest
from pydantic import ValidationError

from simple_shop.application import errors
from simple_shop.application.services import Catalog


@pytest.fixture(scope='function')
def service(products_repo):
    return Catalog(products_repo=products_repo)


def test__search_products(service, products_repo):
    search_str = 'U'
    limit = 10
    offset = 0

    service.search_products(search=search_str, limit=limit, offset=offset)

    call_args, _ = products_repo.find_by_keywords.call_args
    assert call_args == (search_str, limit, offset)


def test__search_products__default_input_args(service, products_repo):
    service.search_products()

    call_args, _ = products_repo.find_by_keywords.call_args
    assert call_args == (None, 10, 0)


def test__get_product(service, products_repo):
    sku = 'U-001'

    service.get_product(sku=sku)

    call_args, _ = products_repo.get_by_sku.call_args
    assert call_args == (sku, )


def test__get_product__missing_sku_arg(service, products_repo):
    with pytest.raises(ValidationError):
        service.get_product()


def test__get_product__no_product(service, products_repo):
    products_repo.get_by_sku.return_value = None

    sku = 'U-001'

    with pytest.raises(errors.NoProduct):
        service.get_product(sku=sku)
