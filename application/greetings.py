from faker import Faker


def greetings():
    return f"Hello {Faker().first_name()}"
