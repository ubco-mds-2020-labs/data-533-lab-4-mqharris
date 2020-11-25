# missing.py
import pandas as pd

# helper function
def check_df(df):
    if not isinstance(df, pd.DataFrame):
        raise Exception("Input must be a pandas DataFrame")


class missing_summary_c:
    def __init__(self, df):
        self.df = df

    def total_missing(self):
        return self.df.isnull().sum()

    def percent_missing(self):
        return missing_summary_c.total_missing(self) / self.df.shape[0]


def missing_summary(df):
    check_df(df)
    data = missing_summary_c(df)
    df_out = {
        "count_missing": data.total_missing(),
        "percent_missing": data.percent_missing(),
    }

    return pd.concat(df_out, axis=1)
