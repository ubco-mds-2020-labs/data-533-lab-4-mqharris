# summary_classes.py
import pandas as pd
import numpy as np


class Df_Info:
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
        try:
            return self.df.max().max()
        except:
            return np.nan

    def total_min(self):
        try:
            return self.df.max().max()
        except:
            return np.nan

    def total_mean(self):
        try:
            return self.df.mean(numeric_only=True).mean(numeric_only=True)
        except:
            return np.nan

    def total_missing(self):
        return self.df.isnull().sum().sum()


class Missing(Df_Info):
    def __init__(self, df, type="columns"):
        df_info.__init__(self, df, type)
        if self.type == "columns":
            self.count_missing = df.isnull().sum()
            self.percent_missing = self.count_missing / self.columns
        else:
            self.count_missing = df.isnull().sum(axis=1)
            self.percent_missing = self.count_missing / self.rows


class Stats(Df_Info):
    def __init__(self, df, type="columns"):
        Df_Info.__init__(self, df, type)
        if self.type == "columns":
            self.sub_max = df.max(numeric_only=True)
            self.sub_min = df.min(numeric_only=True)
            self.sub_mean = df.mean(numeric_only=True)
        else:
            self.sub_max = df.max(axis=1, numeric_only=True)
            self.sub_min = df.min(axis=1, numeric_only=True)
            self.sub_mean = df.mean(axis=1, numeric_only=True)
