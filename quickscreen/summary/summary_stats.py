import pandas as pd

from summary_classes import *


def missing_summary(df, assess="columns"):
    data = missing(df, assess)
    df_out = {
        "count_missing": data.count_missing,
        "percent_missing": data.percent_missing,
    }

    return pd.concat(df_out, axis=1)


def stats_summary(df, assess="columns"):
    data = stats(df, assess)
    df_out = {"max": data.sub_max, "min": data.sub_min}

    return pd.concat(df_out, axis=1)


def all_summary(df, assess="columns"):
    return pd.concat([stats_summary(df, assess), missing_summary(df, assess)], axis=1)


def simple_summary(df):
    data = df_info(df)
    output_labels = ["df_max", "df_min", "row_count", "column_count", "total_missing"]
    output_values = [
        data.total_max,
        data.total_min,
        data.rows,
        data.columns,
        data.total_missing,
    ]
    return pd.DataFrame({"values": output_values}, index=output_labels)
