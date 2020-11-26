# summary_classes.py
import pandas as pd


class df_info:
    def __init__(self, df, type="columns"):
        if not isinstance(df, pd.DataFrame):
            raise Exception("Input must be a pandas DataFrame")
        if not (type in ("columns", "rows")):
            raise Exception("choose another type option either: rows or columns")
        self.df = df
        self.type = type
        self.rows = self.df.shape[0]
        self.columns = self.df.shape[0]

    def total_max(self):
        return self.df.max().max()

    def total_min(self):
        return self.df.min().min()

    def total_missing(self):
        return self.df.isnull().sum().sum()


class missing(df_info):
    def __init__(self, df, type="columns"):
        df_info.__init__(self, df, type)
        if self.type == "columns":
            self.count_missing = df.isnull().sum()
            self.percent_missing = self.count_missing / self.columns
        else:
            self.count_missing = df.isnull().sum(axis=1)
            self.percent_missing = self.count_missing / self.rows


class stats(df_info):
    def __init__(self, df, type="columns"):
        df_info.__init__(self, df, type)
        if self.type == "columns":
            self.sub_max = df.max()
            self.sub_min = df.min()
        else:
            self.sub_max = df.max(axis=1)
            self.sub_min = df.min(axis=1)
