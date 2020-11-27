from quickscreen.plot.plotter import Plotter
from quickscreen.plot.grapher import *
from quickscreen.analysis.datafill import *
from quickscreen.analysis.linear_analysis import *
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
        d = ScatterMatrix(data=df)
        d.scatter_matrix()
        d.save_plot()

    def test_datafill():
        df = pd.read_csv("./data/CarPrice.csv")
        df1 = pd.read_csv("./data/CarPrice.csv")
        de = Data_edit(df)
        de1 = Data_edit(df1)

        # de3 = de1 + de.data.curbweight
        # print(de1.data.shape)
        # print(de3.data.shape)
        # print(de3.data.head())

        isinstance(de.data, pd.core.frame.DataFrame)
        print(isinstance(de.data.curbweight, pd.core.frame.DataFrame))

    def test_Lm():
        df = pd.read_csv("./data/CarPrice.csv")
        de = Data_edit(df)
        print(de.data)
        l = lm(df)
        sr = l.singlelineareqn("enginesize", "horsepower")
        print(sr)




    # test_datafill()
    # test_scatterplot()
    # test_histogram()
    # test_confusion()
    test_Lm()
