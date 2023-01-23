import csv

from typing import Final
from application.config.paths import FILES_OUTPUT_PATH
from application.logging.loggers import get_core_logger
from application.files_example.generetors import generate_humans, Human

KEY__NAME: Final[str] = "name"
KEY__AGE: Final[int] = "age"


def files_example_csv():
    logger = get_core_logger()
    path_to_file = FILES_OUTPUT_PATH.joinpath("output.csv")

    amount: int = 10

    with open(path_to_file, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=[KEY__NAME, KEY__AGE])

        writer.writeheader()
        for human in generate_humans(amount=amount):
            writer.writerow({KEY__NAME: human.name, KEY__AGE: human.age})

    logger.info(f"Path to file: file://{path_to_file}\n")

    humans = []
    with open(path_to_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            human = Human(name=row[KEY__NAME], age=int(row[KEY__AGE]))
            humans.append(human)

    print(humans)
