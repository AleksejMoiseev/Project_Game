from typing import List, Optional

from sqlalchemy import select

from evraz.classic.components import component
from evraz.classic.sql_storage import BaseRepository

from simple_shop.application import interfaces
from simple_shop.application.dataclasses import Cart, Customer, Order, Product

# yapf: disable


@component
class CustomersRepo(BaseRepository, interfaces.CustomersRepo):
    def get_by_id(self, id_: int) -> Optional[Customer]:
        query = select(Customer).where(Customer.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, customer: Customer):
        self.session.add(customer)
        self.session.flush()

    def get_or_create(self, id_: Optional[int]) -> Customer:
        if id_ is None:
            customer = Customer()
            self.add(customer)
        else:
            customer = self.get_by_id(id_)
            if customer is None:
                customer = Customer()
                self.add(customer)

        return customer


@component
class ProductsRepo(BaseRepository, interfaces.ProductsRepo):
    def find_by_keywords(
        self,
        search: str = '',
        limit: int = 10,
        offset: int = 0
    ) -> List[Product]:

        query = (
            select(Product).order_by(Product.sku).limit(limit).offset(offset)
        )

        if search is not None:
            query = query.where(
                Product.title.ilike(f'%{search}%')
                | Product.description.ilike(f'%{search}%')
            )

        return self.session.execute(query).scalars().all()

    def get_by_sku(self, sku: str) -> Optional[Product]:
        query = select(Product).where(Product.sku == sku)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, product: Product):
        self.session.add(product)
        self.session.flush()


@component
class CartsRepo(BaseRepository, interfaces.CartsRepo):
    def get_for_customer(self, customer_id: int) -> Optional[Cart]:
        query = select(Cart).where(Cart.customer_id == customer_id)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, cart: Cart):
        self.session.add(cart)
        self.session.flush()

    def remove(self, cart: Cart):
        self.session.delete(cart)

    def get_or_create(self, customer_id: int) -> Cart:
        cart = self.get_for_customer(customer_id)
        if cart is None:
            cart = Cart(customer_id)
            self.add(cart)

        return cart


@component
class OrdersRepo(BaseRepository, interfaces.OrdersRepo):
    def get_by_number(self, number: int) -> Optional[Order]:
        query = select(Order).where(Order.number == number)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, order: Order):
        self.session.add(order)
        self.session.flush()

# yapf: enable