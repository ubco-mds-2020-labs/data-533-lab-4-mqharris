# import datafill as dfl
import quickscreen.analysis.datafill as dfl
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


class Lm(dfl.DataEdit):
    """
    A class for easy linear regression functions on a pandas dataframe
    """

    def __init__(self, data):
        """
        description

        Parameters
        ----------
        name : type
            description

        Returns
        -------
        name : type
            description

        Examples
        --------
        >>> put examples here
        """
        dfl.DataEdit.__init__(self, data)

    def single_linear(self, predictor, estimator):
       """
        description

        Parameters
        ----------
        name : type
            description

        Returns
        -------
        name : type
            description

        Examples
        --------
        >>> put examples here
        """
        assert (isinstance(estimator, int) or estimator in self.data), "Please enter an integer or the name of a column for the estimator"
        assert (isinstance(predictor, int) or predictor in self.data), "Please enter an integer or the name of a column for the predictor" 
        x = self.data[estimator].to_numpy().reshape(-1,1)
        y = self.data[predictor].to_numpy().reshape(-1,1)
        l_regressor = LinearRegression()
        l_regressor.fit(x,y)
        prediction = l_regressor.predict(x)
        return prediction

    def single_linear_plot(self, predictor, estimator):
       """
        description

        Parameters
        ----------
        name : type
            description

        Returns
        -------
        name : type
            description

        Examples
        --------
        >>> put examples here
        """
        assert (isinstance(estimator, int) or estimator in self.data), "Please enter an integer or the name of a column for the estimator"
        assert (isinstance(predictor, int) or predictor in self.data), "Please enter an integer or the name of a column for the predictor" 
        x = self.data[estimator].to_numpy().reshape(-1,1)
        y = self.data[predictor].to_numpy().reshape(-1,1)
        prediction = self.single_linear(predictor, estimator)

        plt.scatter(x, y)
        plt.plot(x, prediction, color='red')
        plt.title("Linear Regression")
        plt.xlabel(estimator)
        plt.ylabel(predictor)

        return plt.show()

    def single_linear_eqn(self, predictor, estimator):
       """
        description

        Parameters
        ----------
        name : type
            description

        Returns
        -------
        name : type
            description

        Examples
        --------
        >>> put examples here
        """
        assert (isinstance(estimator, int) or estimator in self.data), "Please enter an integer or the name of a column for the estimator"
        assert (isinstance(predictor, int) or predictor in self.data), "Please enter an integer or the name of a column for the predictor" 
        x = self.data[estimator].to_numpy().reshape(-1,1)
        y = self.data[predictor].to_numpy().reshape(-1,1)
        l_regressor = LinearRegression()
        l_regressor.fit(x,y)

        coef = round(float(l_regressor.coef_),2)
        intercept = round(float(l_regressor.intercept_),2)
        print('y=' + str(coef) + 'x+' + str(intercept))
