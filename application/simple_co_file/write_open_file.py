from application.config.paths import FILES_SPECIAL_FOLDER
from application.logging.loggers import get_core_logger


def create_read_file():
    logger = get_core_logger()
    path_to_file = FILES_SPECIAL_FOLDER.joinpath("simple_file.txt")

    content = input("Enter some content for file: ")

    text_file = open(path_to_file, mode="w")
    text_file.writelines(content)
    text_file.close()

    text_file = open(path_to_file)
    text = text_file.read()

    logger.info(f"\nPath to file: file://{path_to_file}\nDONE.\n\nFile content:\n{text}\n\n")
    text_file.close()
