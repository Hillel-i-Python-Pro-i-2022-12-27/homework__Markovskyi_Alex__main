from application.config.paths import FILES_OUTPUT_PATH
from application.logging.loggers import get_core_logger
from application.users_generator.users_generator import generate_users


def users_file_example_txt():
    logger = get_core_logger()
    path_to_file = FILES_OUTPUT_PATH.joinpath("users_with_emails.txt")

    # amount: int = int(input("Enter the number of user for generation: "))
    amount: int = 25

    with open(path_to_file, mode="w") as file:
        for user in generate_users(amount=amount):
            file.write(f"{user.full_name} | {user.email};\n")

    logger.info(f"\nPath to file: file://{path_to_file}\nDONE.\n")
