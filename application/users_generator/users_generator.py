from typing import NamedTuple
from collections.abc import Iterator
from faker import Faker

faker = Faker()


class User(NamedTuple):
    full_name: str
    email: str

    def __str__(self):
        return f"{self.full_name} {self.email}"

    __repr__ = __str__


def generate_user():
    return User(full_name=faker.name(), email=faker.email())


def generate_users(amount) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
