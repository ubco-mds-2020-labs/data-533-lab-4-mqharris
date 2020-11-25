import pandas as pd
import matplotlib.pyplot as plt

class Plotter():

    def __init__(self, data, plot_title=None, label_names=None):
        self.data = data
        self.plot_title = plot_title
        self.label_names = label_names

    def add_title(self, title):
        self.plot_title = title

    def add_label_names(self, x_label, y_label):
        self.label_names = (x_label, y_label)

    def show_plot(self):
        plt.show()
    
