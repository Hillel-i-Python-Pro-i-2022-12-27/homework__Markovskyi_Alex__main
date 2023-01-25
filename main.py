# from application import greetings
# from application.files_example.files_example_csv import files_example_csv
# from application.files_example.files_example_txt import files_example_txt
# from application.requests_example.requests_example import requests_example

from application.astronauts.data_processing import astronauts_names
from application.get_csv_from_googledrive.request import requests__file_from_googledrive
from application.logging.init_logging import init_logging
from application.simple_co_file.write_open_file import create_read_file
from application.users_generator.users_file_example_txt import users_file_example_txt


def main() -> None:
    # ---------------------------------------
    # print(f"REALIZATION MULTIPLE TASKS:\n")
    # print(f"Greetings:\n{greetings()}\n")
    # files_example_txt()
    # files_example_csv()
    # requests_example()
    # ---------------------------------------

    # Simple create file in folder "special_folder" and open file with some text
    create_read_file()

    # Generate users
    users_file_example_txt()

    # Astronauts names and quality
    astronauts_names()

    # Download *.csv file from Google Drive and processing data
    requests__file_from_googledrive()


if __name__ == "__main__":
    init_logging()
    main()
