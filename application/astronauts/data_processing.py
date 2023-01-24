from application.astronauts.astronauts_request import request_astronauts
from application.config.paths import FILES_OUTPUT_PATH
from application.logging.loggers import get_core_logger


def astronauts_names(content=request_astronauts()):
    logger = get_core_logger()
    path_to_file = FILES_OUTPUT_PATH.joinpath("output_astronauts.txt")

    with open(path_to_file, mode="w") as file:
        file.write(f"Total astronauts is: {content['number']}\n\n")
        for full_name in content["people"]:
            file.write(f"{full_name['name']}\n")

    logger.info(f"\nPath to file: file://{path_to_file}\nDONE.\n")
