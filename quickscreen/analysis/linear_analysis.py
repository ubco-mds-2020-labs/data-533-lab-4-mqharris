import column_analysis as ca
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class lm(ca.Placeholder):
    def __init__(self, data):
        ca.Placeholder.__init__(self, data)

    def singlelinear(self, predictor, estimator):
        assert (isinstance(estimator, int) or estimator in self.data), "Please enter an integer or the name of a column for the estimator"
        assert (isinstance(predictor, int) or predictor in self.data), "Please enter an integer or the name of a column for the predictor" 
        x = self.data[estimator].to_numpy().reshape(-1,1)
        y = self.data[predictor].to_numpy().reshape(-1,1)
        l_regressor = LinearRegression()
        l_regressor.fit(x,y)
        prediction = l_regressor.predict(x)
        return prediction

    