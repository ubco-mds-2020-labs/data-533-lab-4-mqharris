import matplotlib.pyplot as plt
from .plotter import Plotter

class Histogram(Plotter):
    def __init__(self, data):
        super().__init__(data)

    def histrogram_on_column(self, col_name):
        plt.hist(self.data[col_name], bins=10)
        if self.label_names:
                plt.xlabel(self.label_names[0])
                plt.ylabel(self.label_names[1])
        if self.plot_title:
                plt.title(self.plot_title)


class ScatterPlot(Plotter):
    def __init__(self, data):
        super().__init__(data)
    
    def scatter_on_columns(self, col1, col2):
        c1 = self.data[col1]
        c2 = self.data[col2]
        plt.plot(c1, c2, "o")
        if self.label_names:
            plt.xlabel(self.label_names[0])
            plt.ylabel(self.label_names[1])
        if self.plot_title:
            plt.title(self.plot_title)
