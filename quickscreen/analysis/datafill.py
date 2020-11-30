#linear.py
import pandas as pd


class DataEdit:
    """
    A class for easy dataframe manipulation
    """

    def __init__(self, data):
        """
        Initializes data edit class

        Parameters
        ----------
        data : pandas.Dataframe
            the pandas dataframe to be manipulated

        Returns
        -------
        None

        Examples
        --------
        >>> DataEdit(pd.Dataframe(data))
        """
        self.data = data
        assert isinstance(self.data, pd.core.frame.DataFrame), "Not a Pandas data frame."

    def display(self):
        """
        Getter function for data

        Parameters
        ----------
        None

        Returns
        -------
        pandas.Dataframe
            class's data
        """
        return self.data

    def columntype(self, column):
        """
        Gets the data type for the column specified by index or by nane

        Parameters
        ----------
        column : int or string
            int - column index, string - column name

        Returns
        -------
        pandas.Dataframe
            class's data
        """
        assert (isinstance(column, int) or column in self.data), "Please enter an integer or the name of a column"
        return self.data.dtypes[column]

    def __add__(self, other):
        assert isinstance(other, pd.core.frame.DataFrame), "Not a Pandas data frame."
        return DataEdit(self.data.append(other, ignore_index=True))
    
    def __sub__(self, other):
        assert isinstance(other, pd.core.frame.DataFrame), "Not a Pandas data frame."
        temp = pd.concat([self.data, other], axis=0, join='outer')
        common = pd.concat([self.data, temp],axis=0, join='inner', ignore_index=True).dropna(axis=0)
        return DataEdit(common)

    def rm_duplicates(self):
        return DataEdit(self.data.drop_duplicates())

    def rm_nan(self):
        return DataEdit(self.data.dropna(axis=0))
    
    def quick_clean(self):
        return DataEdit(self.data.drop_duplicates().dropna(axis=0))




        





