import unittest
import pandas as pd
import numpy as np

from quickscreen.plot.plotter import Plotter

class TestPlotter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame(np.arange(100).reshape(20, 5))
        print("set up TestPlotter class")
    
    @classmethod
    def tearDownClass(cls):
        print("tear down TestPlotter class")
    
    def setUp(self):
        print("setUp plotter instance")
        self.i1 = Plotter(self.df)

    def tearDown(self):
        print("tearDown TestPlotter instance")
    
    def test_Plotter(self):
        self.assertIsInstance(self.i1, Plotter)
        self.assertIsNone(self.i1.label_names)
        self.assertIsNone(self.i1.plot_title)

    def test_add_title(self):
        title = "Test Title"
        self.i1.add_title(title)
        self.assertEqual(self.i1.plot_title, title)

    def test_add_axis_label(self):
        x_label = "this is x"
        y_label = "this is y"
        self.i1.add_label_names(x_label, y_label)
        self.assertEqual(self.i1.label_names, (x_label, y_label))
