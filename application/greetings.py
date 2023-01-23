from faker import Faker


def greetings():
    return f"Hello\n" f"{Faker().first_name()} {Faker().last_name()}\n" f"from {Faker().country()}"
