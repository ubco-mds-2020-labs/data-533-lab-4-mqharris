from quickscreen.plot.plotter import Plotter
from quickscreen.plot.grapher import *
import quickscreen.summary.summary_stats as summary
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

    def test_simple_summary():
        df = pd.read_csv("./data/CarPrice.csv")
        print(summary.simple_summary(df))

    def test_missing_summary():
        df = pd.read_csv("./data/CarPrice.csv")
        print(summary.missing_summary(df))
        print(summary.missing_summary(df, type="rows"))

    def test_stats_summary():
        df = pd.read_csv("./data/CarPrice.csv")
        print(summary.stats_summary(df))
        print(summary.stats_summary(df, type="rows"))

    def test_all_summary():
        df = pd.read_csv("./data/CarPrice.csv")
        print(summary.all_summary(df))
        print(summary.all_summary(df, type="rows"))

    # test_scatterplot()
    # test_histogram()
    # test_confusion()

    # test_simple_summary()
    # test_missing_summary()
    # test_stats_summary()
    # test_all_summary()
