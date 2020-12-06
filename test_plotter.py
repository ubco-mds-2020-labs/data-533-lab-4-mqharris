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
        self.i1 = Plotter(self.df)

    def tearDown(self):
        print("tearDown TestPlotter instance")
    
    