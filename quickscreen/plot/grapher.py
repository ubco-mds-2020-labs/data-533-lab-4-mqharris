import matplotlib.pyplot as plt
import seaborn as sns

from .plotter import Plotter

class HistogramPlot(Plotter):
    def __init__(self, data):
        super().__init__(data)

    def histogram(self, col_name, bins=10):
        c1 = self.data[col_name]
        plt.hist(c1, bins=bins)

class ScatterPlot(Plotter):
    def __init__(self, data):
        super().__init__(data)
    
    def scatter(self, col1, col2):
        c1 = self.data[col1]
        c2 = self.data[col2]
        plt.plot(c1, c2, "o")

class ConfusionPlot(Plotter):
    def __init__(self, data):
        super().__init__(data)

    def confusion(self):
        sns.pairplot(self.data, diag_kws={'bins': 10})
