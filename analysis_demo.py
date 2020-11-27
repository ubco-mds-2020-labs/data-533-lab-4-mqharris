import pandas as pd

from quickscreen.analysis.linear_analysis import *
from quickscreen.analysis.datafill import *

if __name__ == "__main__":

    df = pd.read_csv("./data/CarPrice.csv")
    print(df.head())
