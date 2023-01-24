import pandas as pd

from application.config.paths import FILES_INPUT_PATH

df = pd.read_csv(f"{FILES_INPUT_PATH}/people_data(extended).csv")
pd.set_option("display.max_columns", None)

print(df["Index"].columns)
