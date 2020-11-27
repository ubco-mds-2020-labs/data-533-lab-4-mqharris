#linear.py
import pandas as pd


class DataEdit:

    def __init__(self, data):
        self.data = data
        assert isinstance(self.data, pd.core.frame.DataFrame), "Not a Pandas data frame."

    def display(self):
        return self.data

    def columntype(self, column):
        assert (isinstance(column, int) or column in self.data), "Please enter an integer or the name of a column"
        return self.data.dtypes[column]

    def __add__(self, other):
        assert isinstance(self.data, pd.core.frame.DataFrame), "Not a Pandas data frame."
        return DataEdit(self.data.append(other, ignore_index=True))
    
    def __sub__(self, other):
        assert isinstance(self.data, pd.core.frame.DataFrame), "Not a Pandas data frame."
        temp = pd.concat([self.data, other], axis=0, join='outer')
        common = pd.concat([self.data, temp],axis=0, join='inner', ignore_index=True).dropna(axis=0)
        return DataEdit(common)

    def rm_duplicates(self):
        return DataEdit(self.data.drop_duplicates())

    def rm_nan(self):
        return DataEdit(self.data.dropna(axis=0))
    
    def quick_clean(self):
        return DataEdit(self.data.drop_duplicates().dropna(axis=0))




        





