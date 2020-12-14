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
        try:
            self.data = data
            assert isinstance(self.data, pd.core.frame.DataFrame)
        except:
            print("Not a Pandas data frame.")
            return

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
        try:
            return self.data
        except:
            print('Can not display data')
            return

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
        try:
            assert (isinstance(column, int) or column in self.data)
            return self.data.dtypes[column]
        except:
            print("Please enter an integer or the name of a column")
            return

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
        >>> DataEdit(df1) + df2
        """
        try:
            assert isinstance(other, pd.core.frame.DataFrame)
            return DataEdit(self.data.append(other, ignore_index=True))
        except:
            print("Not a Pandas data frame.")
            return
            
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
        try:
            assert isinstance(other, pd.core.frame.DataFrame)
        except:
            print("Not a Pandas data frame.")
            return
        try:
            common = self.data.merge(other, indicator='i', how='outer').query('i=="left_only"').drop('i',1)
        except:
            common = self.data
        return DataEdit(common)

    def rm_duplicates(self):
        """
        removes duplicate rows from DataEdit object's data

        Parameters
        ----------
        None

        Returns
        -------
        DataEdit instance
            with the same data as the original object, but with duplicate rows removed
        
        Examples
        --------
        >>> DataEdit(df).rm_duplicates()
        """
        
        return DataEdit(self.data.drop_duplicates())

        
    def rm_nan(self):
        """
        Removes rows that have na for values

        Parameters
        ----------
        None

        Returns
        -------
        DataEdit instance
            with the same data as the original object,
            but with rows comintaining na removed
        
        Examples
        --------
        >>> DataEdit(df1).rm_nan()
        """

        return DataEdit(self.data.dropna(axis=0))  


    def quick_clean(self):
        """
        Removes rows that have na for values and rows that are duplicates

        Parameters
        ----------
        None

        Returns
        -------
        DataEdit instance
            with the same data as the original object,
            but with rows comintaining na removed,
            and duplicate rows removed
        
        Examples
        --------
        >>> DataEdit(df1).quick_clean()
        """

        return DataEdit(self.data.drop_duplicates().dropna(axis=0))
