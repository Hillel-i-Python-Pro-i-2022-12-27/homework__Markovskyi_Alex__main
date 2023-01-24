from faker import Faker


def greetings():
    return f"Hello {Faker().first_name()} {Faker().last_name()} from {Faker().country()}"
