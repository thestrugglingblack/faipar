import pandas as pd
import numpy as np
import nfl_data_py as nfl

seasons = range(2016, 2022+1)
pbp_py = nfl.import_pbp_data(seasons)

pbp_py_p = pbp_py.query("play_type == 'pass' & air_yards.notnull()").reset_index()

pbp_py_p["pass_length_air_yards"] = np.where(pbp_py_p["air_yards"] >= 20, "long", "short")

pbp_py_p["passing_yards"] = np.where(pbp_py_p["passing_yards"].isnull(), 0, pbp_py_p["passing_yards"])

# Showw both long and short passes results
pbp_py_p["passing_yards"].describe()

# Filter out based on short passes
pbp_py_p.query('pass_length_air_yards == "short"')["passing_yards"].describe()

# Filter out based on long passes
pbp_py_p.query('pass_length_air_yards == "long"')["passing_yards"].describe()

# EPA aka Expected Points Added is a more continuous measure of play success that uses situational factors to assign a point value to each play.
pbp_py_p.query('pass_length_air_yards == "short"')["epa"].describe()
pbp_py_p.query('pass_length_air_yards == "long"')["epa"].describe()

# Histograms are plots that allow you to see data by summing the counts of data points into bars. Those are called "bins"
import seaborn as sns
import matplotlib.pyplot as plt

sns.displot(data=pbp_py, x="passing_yards")
plt.show()
