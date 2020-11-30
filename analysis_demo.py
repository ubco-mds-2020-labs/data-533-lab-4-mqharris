import pandas as pd

from quickscreen.analysis.linear_analysis import *
from quickscreen.analysis.datafill import *

if __name__ == "__main__":
    

    # sub example

    df = pd.read_csv("./data/CarPrice.csv")
    # print(df.head())

    de = DataEdit(df)
    de1 = DataEdit(df)

    two_row = (df.iloc[0:2])
    print(type(two_row.iloc[0:1]))
    print(two_row)

    d = de - two_row
    print(df.shape)
    print(d.data.shape)