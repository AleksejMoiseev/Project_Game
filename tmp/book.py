from dataclasses import dataclass
from dataclasses import field

def foo(price: str):
    price.replace('$', '')



@dataclass
class Book:
    price: str = field(default_factory=)

    def save_price(self):
        return self.price.replace('$', '')


# @dataclass
# class Book(BaseModel):
#     author: str
#     title: str
#     publisher: str
#     subtitle: str
#     language: str
#     isbn10: str
#     isbn13: str
#     pages: int
#     year: int
#     rating: int
#     desc: Text
#     price: str
#     image: str
#     url: str
#     pdf: dict
#     created: datetime = field(default_factory=datetime.now)

if __name__ == '__main__':
    b = Book(price='$46.73')
    print(b.price)