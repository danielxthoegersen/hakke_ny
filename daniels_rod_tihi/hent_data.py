import pandas as pd


df = pd.read_csv("database_dummy.csv")

line_number = 1
specific_column = 0

film_1_titel = df.iloc[line_number][specific_column]

print(film_1_titel.removeprefix("["))