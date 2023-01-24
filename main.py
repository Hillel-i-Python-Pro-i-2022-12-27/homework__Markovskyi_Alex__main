from application import greetings
from application.files_example.files_example_csv import files_example_csv
from application.files_example.files_example_txt import files_example_txt
from application.logging.init_logging import init_logging
from application.requests_example.requests_example import requests_example


def main() -> None:
    print(greetings())
    files_example_txt()
    files_example_csv()
    requests_example()


if __name__ == "__main__":
    init_logging()
    main()
