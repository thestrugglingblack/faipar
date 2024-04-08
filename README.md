```

 __                         _                                            _                                _ 
|_  _  _ _|_|_  _  |  |    |_|__  _  |  \/_|_ o  _  _        o _|_|_    |_) \/_|_|_  _ __     _ __  _|   |_)
|  (_)(_) |_|_)(_| |  |    | || |(_| |  /  |_ | (_ _>    \^/ |  |_| |   |   /  |_| |(_)| |   (_|| |(_|   | \

```

## Table of Contents
* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
    * [Setup Python in Rstudio](#setup-python-in-rstudio)
    * [Run the Scripts](#run-the-scripts)
* [Lessons Learned](#lessons-learned)

## Overview
Baseball is not the only sport to use "moneyball." American football fans, teams, and gamblers are increasingly using data to gain an edge against the competition. Professional and college teams use data to help select players and identify team needs. Fans use data to guide fantasy team picks and strategies. Sports bettors and fantasy football players are using data to help inform decision making. This concise book provides a clear introduction to using statistical models to analyze football data.

## Prerequisites
* Python v3.10
* R
* R Studio

## Getting Started
### Setup in Python in RStudio
Through the console run the following:
> Note: Make sure to exit out of the python repl if activated.
1. `reticulate::virtualenv_create('r-reticulate')`
2. `reticulate::use_virtualenv('r-reticulate', required = TRUE)`
3. `reticulate::source_python('PATH_TO_SCRIPT')`
4. `reticulate::py_install("PACKAGE_NAME")`

### Run the Scripts
Coming Soon.

## Lessons Learned
* _Histograms_ are plots that allow you to see data by summing the counts of data points into bars. Those are called "_bins_"