from quickscreen.plot.plotter import Plotter
from quickscreen.plot.grapher import *
import pandas as pd

if __name__ == "__main__":
    

    def test_histogram():
        df = pd.read_csv("./data/CarPrice.csv")
        d = HistogramPlot(data=df)

        d.add_title("this is the title")
        d.add_label_names("x axis", "y axis")

        d.histogram("curbweight")
        d.show_plot()

    def test_scatterplot():
        df = pd.read_csv("./data/CarPrice.csv")
        d = ScatterPlot(data=df)

        d.add_title("this is the title")
        d.add_label_names("x axis", "y axis")

        d.scatter("curbweight", "horsepower")
        d.show_plot()

    def test_confusion():
        # this doesn't display nicely on my machine
        df = pd.read_csv("./data/CarPrice.csv")
        d = ConfusionPlot(data=df)
        d.confusion()
        d.save_plot()


    # test_scatterplot()
    # test_histogram()
    test_confusion()
    