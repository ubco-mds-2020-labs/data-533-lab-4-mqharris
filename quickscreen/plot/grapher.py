import matplotlib.pyplot as plt
import seaborn as sns

from .plotter import Plotter


class HistogramPlot(Plotter):
    """
    Historgram plot subclass of Plotter class
    """

    def __init__(self, data, plot_title=None, label_names=None):
        """
        Initialize class using the Plotter class

        Parameters
        ----------
        data : pandas.DataFrame
            the Pandas Dataframe to be plotted
        plot_title : str, optional (default = None)
            the plot title
        label_names : str tuple, optional (default = None)
            the x-axis and y-axis titles (x-axis is position [0], y-axis is position [1])

        Returns
        -------
        None

        Examples
        --------
        >>> HistogramPlot(pd.DataFrame(data), "Name of Plot", ("Name of X-axis", "Name of Y-axis"))
        """
        Plotter.__init__(self, data, plot_title=None, label_names=None)

    def histogram(self, col_name, bins=10):
        """
        Simple histogram plot

        Parameters:
        -----------
        col_name = "str"
            column name to be used for plotting
        bins = int, optional (default = 10)
            number of bins to use in histogram

        Returns:
        --------
        None

        Examples:
        ---------
        >>> working_hist = HistogramPlot(pd.DataFrame(data, columns = ['col1', 'col2']))
        >>> working_hist.histogram('col1', bins=20)
        """
        c1 = self.data[col_name]
        plt.hist(c1, bins=bins)


class ScatterPlot(Plotter):
    """
    Scatter plot subclass of Plotter class
    """

    def __init__(self, data, plot_title=None, label_names=None):
        """
        Initialize class using the Plotter class

        Parameters
        ----------
        data : pandas.DataFrame
            the Pandas Dataframe to be plotted
        plot_title : str, optional (default = None)
            the plot title
        label_names : str tuple, optional (default = None)
            the x-axis and y-axis titles (x-axis is position [0], y-axis is position [1])

        Returns
        -------
        None

        Examples
        --------
        >>> ScatterPlot(pd.DataFrame(data), "Name of Plot", ("Name of X-axis", "Name of Y-axis"))
        """
        Plotter.__init__(self, data, plot_title=None, label_names=None)

    def scatter(self, col1, col2):
        """
        Simple histogram plot

        Parameters:
        -----------
        col1 = "str"
            column name to be used for x-axis values
        col1 = "str"
            column name to be used for y-axis values

        Returns:
        --------
        None

        Examples:
        ---------
        >>> working_scatter = HistogramPlot(pd.DataFrame(data, columns = ['col1', 'col2']))
        >>> working_scatter.ScatterPlot('col1', 'col2')
        """
        c1 = self.data[col1]
        c2 = self.data[col2]
        plt.plot(c1, c2, "o")


class ScatterMatrix(Plotter):
    """
    ScatterMatrix plot subclass of Plotter class
    """

    def __init__(self, data, plot_title=None, label_names=None):
        """
        Initialize class using the Plotter class

        Parameters
        ----------
        data : pandas.DataFrame
            the Pandas Dataframe to be plotted
        plot_title : str, optional (default = None)
            the plot title
        label_names : str tuple, optional (default = None)
            the x-axis and y-axis titles (x-axis is position [0], y-axis is position [1])

        Returns
        -------
        None

        Examples
        --------
        >>> ScatterMatrix(pd.DataFrame(data), "Name of Plot", ("Name of X-axis", "Name of Y-axis"))
        """
        Plotter.__init__(self, data, plot_title=None, label_names=None)

    def scatter_matrix(self):
        """
        Seaborn Scatter Matrix plot

        Parameters:
        -----------
        col1 = "str"
            column name to be used for x-axis values
        col1 = "str"
            column name to be used for y-axis values

        Returns:
        --------
        None

        Examples:
        ---------
        >>> working_scatter = HistogramPlot(pd.DataFrame(data, columns = ['col1', 'col2']))
        >>> working_scatter.ScatterPlot('col1', 'col2')
        """
        sns.pairplot(self.data, diag_kws={"bins": 10})
