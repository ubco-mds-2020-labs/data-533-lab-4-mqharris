import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        plt.clf()

    def test_initialization(self):
        self.assertIsInstance(self.histogram, HistogramPlot)
        self.assertIsInstance(self.scattermatrix, ScatterMatrix)
        self.assertIsInstance(self.scatterplot, ScatterPlot)

    def test_grapher_data(self):
        # histogram
        data_hist = self.histogram.histogram("B")
        data_per_bin = [10.0] * 10
        bin_data = [0.,19.8,39.6,59.4,79.2,99.,118.8,138.6,158.4,178.2,198.]
        self.assertListEqual(list(data_hist[0]), data_per_bin)
        self.assertEqual(len(list(data_hist[1])), len(bin_data))
        for i in range(0, len(bin_data)):
            self.assertAlmostEqual(bin_data[i], data_hist[1][i])
        
        # scatter plot
        data_sp = self.scatterplot.scatter("A", "B")[0]
        returned_x = list(data_sp.get_xdata())
        returned_y = list(data_sp.get_ydata())
        expected_x = [x for x in range(0, 100)]
        expected_y = [x*2 for x in range(0, 100)]
        self.assertListEqual(returned_x, expected_x)
        self.assertListEqual(returned_y, expected_y)

        # scatter matrix
        expected_axis_0 = (-4.95, 103.95, -4.95, 103.95)
        expected_axis_1 = (-9.9, 207.9, -4.95, 103.95)
        data_sm = self.scattermatrix.scatter_matrix()
        data_sm = (data_sm.axes[0])
        self.assertEqual(expected_axis_0, data_sm[0].axis())
        self.assertEqual(expected_axis_1, data_sm[1].axis())
