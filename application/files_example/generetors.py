import random
from typing import NamedTuple
from collections.abc import Iterator

from faker import Faker

faker = Faker()


class Human(NamedTuple):
    name: str
    age: int

    def __str__(self):
        return f"{self.name} {self.age}"

    __repr__ = __str__


def generate_human():
    return Human(name=faker.first_name(), age=random.randint(10, 90))


def generate_humans(amount: int = 10) -> Iterator[Human]:
    for _ in range(amount):
        yield generate_human()
