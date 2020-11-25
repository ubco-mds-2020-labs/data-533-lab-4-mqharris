import matplotlib.pyplot as plt
from .plotter import Plotter

class Histogram(Plotter):
    def __init__(self, data):
        super().__init__(data)