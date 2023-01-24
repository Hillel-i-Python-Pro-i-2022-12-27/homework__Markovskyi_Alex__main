# from application import greetings
# from application.files_example.files_example_csv import files_example_csv
# from application.files_example.files_example_txt import files_example_txt
# from application.requests_example.requests_example import requests_example

from application.logging.init_logging import init_logging
from application.users_generator.users_file_example_txt import users_file_example_txt


def main() -> None:
    # ---------------------------------------
    # print(f"REALIZATION MULTIPLE TASKS:\n")
    # print(f"Greetings:\n{greetings()}\n")
    # files_example_txt()
    # files_example_csv()
    # requests_example()
    # ---------------------------------------

    users_file_example_txt()


if __name__ == "__main__":
    init_logging()
    main()
