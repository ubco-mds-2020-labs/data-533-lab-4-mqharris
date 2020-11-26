import datetime

import pandas as pd
from pandas.api.types import is_numeric_dtype
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

        if self.label_names:
                plt.xlabel(self.label_names[0])
                plt.ylabel(self.label_names[1])
        if self.plot_title:
                plt.title(self.plot_title)
        plt.show()

    def save_plot(self, save_loc=".", file_name=None):
        # currently hard coded to save only as jpg
        # currently only hard coded save in the root dir
        if self.label_names:
                plt.xlabel(self.label_names[0])
                plt.ylabel(self.label_names[1])
        if self.plot_title:
                plt.title(self.plot_title)
        if file_name is None:
            x = datetime.datetime.now()
            str_date = str(x.date())+str(x.time())
            file_name = type(self).__name__ +"_"+ str_date
        plt.savefig(save_loc+file_name+".jpg")

    def get_numeric_columns(self):
        # Not currently used
        numeric_columns = []
        for col in self.data.columns:
            if is_numeric_dtype(self.data[col]):
                numeric_columns.append(col)
        return numeric_columns

