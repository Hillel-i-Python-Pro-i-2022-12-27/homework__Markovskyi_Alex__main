import math

import pandas as pd
from application.config.paths import FILES_OUTPUT_PATH


def calculate_data():
    inches_to_cm: float = 2.54
    pounds_to_kg: float = 0.45359237

    path_to_file = FILES_OUTPUT_PATH.joinpath("download_file.csv")
    df = pd.read_csv(path_to_file)

    height_count: int = df["Height(Inches)"].count()
    height_sum: int = df["Height(Inches)"].sum()
    average_height = (height_sum * inches_to_cm) / height_count
    average_height = math.ceil(average_height)

    weight_count: int = df["Weight(Pounds)"].count()
    weight_sum: int = df["Weight(Pounds)"].sum()
    average_weight = (weight_sum * pounds_to_kg) / weight_count
    average_weight = math.ceil(average_weight)

    return f"Average HEIGHT is: {average_height} cm.\nAverage WEIGHT is: {average_weight} kg."
