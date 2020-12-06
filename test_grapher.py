import unittest
import pandas as pd
import numpy as np

from quickscreen.plot.grapher import HistogramPlot
from quickscreen.plot.grapher import ScatterPlot
from quickscreen.plot.grapher import ScatterMatrix

class TestGrapher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame(
            data={
                "A":[x for x in range(0, 100)],
                "B":[x*2 for x in range(0, 100)],
                "C":[x*3 for x in range(0, 100)],
                "D":[x*4 for x in range(0, 100)]
            }
        )
    
    @classmethod
    def tearDownClass(cls):
        print("TearDownClass")
    
    def setUp(self):
        print("SetUp")
        self.histogram = HistogramPlot(self.df)
        self.scatterplot = ScatterPlot(self.df)
        self.scattermatrix = ScatterMatrix(self.df)
    
    def tearDown(self):
        print("TearDown")

    def test_initialization(self):
        self.assertIsInstance(self.histogram, HistogramPlot)
        self.assertIsInstance(self.scattermatrix, ScatterMatrix)
        self.assertIsInstance(self.scatterplot, ScatterPlot)

    def test_grapher_data(self):
        shit = self.histogram.histogram("B")
        print(dir(shit))
        shit.xkcd()
        