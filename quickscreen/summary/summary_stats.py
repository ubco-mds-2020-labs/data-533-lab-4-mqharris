# summary_stats.py
import pandas as pd

from quickscreen.summary.summary_classes import *


def missing_summary(df, type="columns"):
    data = missing(df, type)
    df_out = {
        "count_missing": data.count_missing,
        "percent_missing": data.percent_missing,
    }

    return pd.concat(df_out, axis=1)


def stats_summary(df, type="columns"):
    data = stats(df, type)
    df_out = {"max": data.sub_max, "min": data.sub_min, "mean": data.sub_mean}

    return pd.concat(df_out, axis=1)


def all_summary(df, type="columns"):
    return pd.concat([stats_summary(df, type), missing_summary(df, type)], axis=1)


def simple_summary(df):
    data = df_info(df)
    output_labels = [
        "df_max",
        "df_min",
        "df_mean",
        "row_count",
        "column_count",
        "total_missing",
    ]
    output_values = [
        data.total_max(),
        data.total_min(),
        data.total_mean(),
        data.rows,
        data.columns,
        data.total_missing(),
    ]
    return pd.DataFrame({"values": output_values}, index=output_labels)
