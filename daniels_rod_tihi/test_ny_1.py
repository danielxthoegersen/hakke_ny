import pandas as pd

colnames=["film_titel", "fede_skurke", "bar_hud", "vilde_våben", "one_liners", "episk_action", "total_score"]

# Hent data
df = pd.read_csv("database_dummy.csv", names=colnames, header=None)

sorted_database = df.sort_values("total_score", ascending=False)

print(sorted_database)


