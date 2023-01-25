import pandas as pd
from application.config.paths import FILES_INPUT_PATH


def calculate_data():

    path_to_file = FILES_INPUT_PATH.joinpath("download_file.csv")
    df = pd.read_csv(path_to_file)

    height_count: int = df["Height(Inches)"].count()
    height_sum: int = df["Height(Inches)"].sum()
    average_height = height_sum / height_count

    weight_count: int = df["Weight(Pounds)"].count()
    weight_sum: int = df["Weight(Pounds)"].sum()
    average_weight = weight_sum / weight_count

    return f"Average HEIGHT is: {average_height}\nAverage WEIGHT is: {average_weight}"
