library("tidyverse")
library("nflfastR")
library("ggthemes")

pbp_r <- load_pbp(2016:2022)

pbp_r_p <- 
  pbp_r |>
  filter(play_type == "pass" & !is.na(air_yards))

pbp_r_p <-
  pbp_r_p |>
  mutate(
    pass_length_air_yards = ifelse(air_yards >= 20, 'long', 'short'),
    passing_yards = ifelse(is.na(passing_yards), 0, passing_yards)
  )

# Filter on both Long and Short Passes
pbp_r_p |>
  pull(passing_yards) |>
  summary()

# Filter on short passes
pbp_r_p |>
  filter(pass_length_air_yards == "short") |>
  pull(passing_yards) |>
  summary()

# Filter on long passes
pbp_r_p |>
  filter(pass_length_air_yards == "long") |>
  pull(passing_yards) |>
  summary()

# Pull Results based on EPA
pbp_r_p |>
  filter(pass_length_air_yards == "short") |>
  pull(epa) |>
  summary()
pbp_r_p |>
  filter(pass_length_air_yards == "long") |>
  pull(epa) |>
  summary()

# Histograms are plots that allow you to see data by summing the counts of data points into bars. Those are called "bins"
library(ggplot2)
# Wraps charts in print to show in RStudio
print(ggplot(pbp_r, aes(x = passing_yards)) +
  geom_histogram())
  