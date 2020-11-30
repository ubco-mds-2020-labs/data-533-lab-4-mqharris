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
        numpy.dtype
            dtype of column
        """
        assert (isinstance(column, int) or column in self.data), "Please enter an integer or the name of a column"
        return self.data.dtypes[column]

    def __add__(self, other):
        """
        appends one dataframe to another

        Parameters
        ----------
        other : pandas.Dataframe
            the dataframe to add to the original

        Returns
        -------
        pandas.Dataframe
            the two dataframes appended

        Examples
        --------
        >>> TODO
        """
        assert isinstance(other, pd.core.frame.DataFrame), "Not a Pandas data frame."
        return DataEdit(self.data.append(other, ignore_index=True))
    
    def __sub__(self, other):
        """
        removes the insersection of the two dataframes

        Parameters
        ----------
        other : pandas.Dataframe
            the dataframe to intersect with the original

        Returns
        -------
        pandas.Dataframe
            original dataframe with interseciton with other removed
        
        Examples
        --------
        >>> difference = DataEdit(df1) - df2
        """
        assert isinstance(other, pd.core.frame.DataFrame), "Not a Pandas data frame."
        # temp = pd.concat([self.data, other], axis=0, join='outer')
        # # t = pd.concat([df, df], axis=0, join='outer', ignore_index=True)
        # common = pd.concat([self.data, temp],axis=0, join='inner', ignore_index=True).dropna(axis=0)
        # # common = pd.concat([df, t],axis=0, join='inner', ignore_index=True).dropna(axis=0)
        try:
            common = self.data.merge(other, indicator='i', how='outer').query('i=="left_only"').drop('i',1)
        except:
            common=self.data
        return DataEdit(common)

    def rm_duplicates(self):
        return DataEdit(self.data.drop_duplicates())

    def rm_nan(self):
        return DataEdit(self.data.dropna(axis=0))
    
    def quick_clean(self):
        return DataEdit(self.data.drop_duplicates().dropna(axis=0))




        





