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

pbp_r_p |>
  pull(passing_yards)
  summary()
  
  