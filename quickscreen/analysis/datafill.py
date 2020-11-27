#linear.py
import pandas as pd


class Data_edit:

    def __init__(self, data):
        self.data = data
        assert isinstance(self.data, pd.core.frame.DataFrame), "Not a Pandas data frame."

    def display(self):
        return self.data

    def columntype(self, column):
        assert (isinstance(column, int) or column in self.data), "Please enter an integer or the name of a column"
        return self.data.dtypes[column]

    def __add__(self, other):
        return self.data.append(other)


        





