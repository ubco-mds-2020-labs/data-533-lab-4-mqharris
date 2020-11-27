#linear.py
import pandas as pd


class Placeholder:

    def __init__(self, data):
        self.data = data
        assert isinstance(self.data, pd.core.frame.DataFrame), "Not a Pandas data frame."

    def display(self):
        return self.data

    def columntype(self, column):
        assert (isinstance(column, int) or column in self.data), "Please enter an integer or the name of a column"
        return self.data.dtypes[column]

    def sum_column(self, column):
        assert (isinstance(column, int) or column in self.data), "Please enter an integer or the name of a column"
        return self.data[column].sum()

    def avg_column(self, column):
        assert (isinstance(column, int) or column in self.data), "Please enter an integer or the name of a column"
        assert self.columntype(column)==('int64' or 'float64'), "This column is not numeric"
        return self.data[column].mean()

    def sd_column(self, column):
        assert (isinstance(column, int) or column in self.data), "Please enter an integer or the name of a column"
        assert self.columntype(column)==('int64' or 'float64'), "This column is not numeric"
        return (sum((self.data[column]-self.avg_column(column))**2)/len(self.data[column]))**(1/2)

    
    def column_stats(self, column):
        assert (isinstance(column, int) or column in self.data), "Please enter an integer or the name of a column"
        if column is int:
            column_name=str(self.data.columns[column])
        else:
            column_name=column
        out = {"Sum of "+ column_name:self.sum_column(column), "Average of "+ column_name:self.avg_column(column), "Standard deviation of "+ column_name:self.sd_column(column)}
        return out

    def __add__(self, other):
        return self.data.append(other)


        





