from quickscreen.plot.plotter import Plotter
from quickscreen.plot.grapher import Histogram, ScatterPlot
import pandas as pd

if __name__ == "__main__":
    

    def test_histogram():
        df = pd.read_csv("./data/CarPrice.csv")
        d = Histogram(data=df)

        d.add_title("this is the title")
        d.add_label_names("x axis", "y axis")

        d.histrogram_on_column("curbweight")
        d.show_plot()

    def test_scatterplot():
        df = pd.read_csv("./data/CarPrice.csv")
        d = ScatterPlot(data=df)

        d.add_title("this is the title")
        d.add_label_names("x axis", "y axis")

        d.scatter_on_columns("curbweight", "horsepower")
        d.show_plot()


    # test_scatterplot()
    test_histogram()