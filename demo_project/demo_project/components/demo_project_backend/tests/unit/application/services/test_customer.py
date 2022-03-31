import pytest
from pydantic import ValidationError

from simple_shop.application import errors
from simple_shop.application.services import Customers


@pytest.fixture(scope='function')
def service(customers_repo):
    return Customers(customers_repo=customers_repo)


def test__get_info(service, customers_repo):
    customer_id = 1

    service.get_info(customer_id=customer_id)

    call_args, _ = customers_repo.get_by_id.call_args
    assert call_args == (customer_id, )


def test__get_info__missing_customer_id_arg(service, customers_repo):
    with pytest.raises(ValidationError):
        service.get_info()


def test__get_info__no_customer(service, customers_repo):
    customers_repo.get_by_id.return_value = None

    customer_id = 1
    with pytest.raises(errors.NoCustomer):
        service.get_info(customer_id=customer_id)
