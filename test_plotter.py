import unittest
import pandas as pd
import numpy as np

from quickscreen.plot.plotter import Plotter, PlatformError

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
        self.i1.add_title(5)
        self.assertEqual(self.i1.plot_title, title)

    def test_add_axis_label(self):
        x_label = "this is x"
        y_label = "this is y"
        self.i1.add_label_names(x_label, y_label)
        self.assertEqual(self.i1.label_names, (x_label, y_label))
        self.i1.add_label_names(5, y_label)
        self.assertEqual(self.i1.label_names, (x_label, y_label))
        self.i1.add_label_names(x_label, 3)
        self.assertEqual(self.i1.label_names, (x_label, y_label))
        self.i1.add_label_names(5, 3)
        self.assertEqual(self.i1.label_names, (x_label, y_label))

    def test_save_plot(self):
        self.i1.save_plot(test_flag=1)
        x_label = "this is x"
        y_label = "this is y"
        title = "Test Title"
        self.i1.add_label_names(x_label, y_label)
        self.i1.add_title(title)
        test = self.i1.save_plot(test_flag=1)
        self.assertEqual(test, "test")


    def test_show_plot(self):
        self.i1.show_plot(test_flag=1)
        x_label = "this is x"
        y_label = "this is y"
        title = "Test Title"
        self.i1.add_label_names(x_label, y_label)
        self.i1.add_title(title)
        test = self.i1.show_plot(test_flag=1)
        self.assertEqual(test, "test")

    def test_custom_exceptions(self):
        try:
            raise PlatformError("test")
        except PlatformError as ex:
            self.assertEqual(ex.message, "test")
