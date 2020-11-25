from quickscreen.plot.plotter import Plotter
from quickscreen.plot.grapher import Histogram
import pandas as pd

if __name__ == "__main__":
    
    df = pd.read_csv("./data/CarPrice.csv")
    d = Histogram(data=df)
    d.data.info()

    d.add_title("this is the title")
    d.add_label_names("x axis", "y axis")

    print(d.plot_title)
    print(d.label_names[0])