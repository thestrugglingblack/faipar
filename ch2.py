import pandas as pd
import numpy as np
import nfl_data_py as nfl

seasons = range(2016, 2022+1)
pbp_py = nfl.import_pbp_data(seasons)

pbp_py_p = pbp_py.query("play_type == 'pass' & air_yards.notnull()").reset_index()

pbp_py_p["pass_length_air_yards"] = np.where(pbp_py_p["air_yards"] >= 20, "long", "short")

pbp_py_p["passing_yards"] = np.where(pbp_py_p["passing_yards"].isnull(), 0, pbp_py_p["passing_yards"])
s
pbp_py_p["passing_yards"].describe()

