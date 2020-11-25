import pandas as pd
import matplotlib.pyplot as plt

class plotter():

    def __init__(self, data):
        self.data = data
        self.plot_title = None
        self.label_names = None

    def add_title(self, title):
        self.plot_title = title

    def add_label_names(self, x_label, y_label):
        self.label_names = (x_label, y_label)
    
