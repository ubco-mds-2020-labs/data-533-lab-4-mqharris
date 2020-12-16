import unittest
import pandas as pd
import numpy as np


from quickscreen.summary.summary_classes import Df_Info, Missing, Stats
from quickscreen.summary.summary_classes import PandasInputError, OptionInputError


class TestDfInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame(np.arange(100).reshape(20, 5))
        cls.df2 = cls.df.copy()
        cls.df2.iloc[0, 0] = np.nan
        cls.df3 = pd.DataFrame(np.full(shape=(20, 5), fill_value="a"))
        print("SetUpClass")

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass")

    def setUp(self):
        print("SetUp")
        self.i1 = Df_Info(self.df)
        self.i2 = Df_Info(self.df2)
        self.i3 = Df_Info(self.df3)

    def tearDown(self):
        print("TearDown")

    def test_Df_Info(self):
        self.assertIsInstance(self.i1, Df_Info)
        self.assertEqual(self.i1.type, "columns")
        self.assertEqual(self.i1.rows, 20)
        self.assertEqual(self.i1.columns, 5)
        self.assertEqual(self.i1.columns, 5)
        self.assertFalse(hasattr(Df_Info(123), "df"))
        self.assertFalse(hasattr(Df_Info(self.df, type="wrong"), "df"))

    def test_total_max(self):
        self.assertEqual(self.i1.total_max(), 99)
        self.assertEqual(self.i2.total_max(), 99)

    def test_total_min(self):
        self.assertEqual(self.i1.total_min(), 0)
        self.assertEqual(self.i2.total_min(), 1)

    def test_total_mean(self):
        self.assertEqual(self.i1.total_mean(), 49.5)
        self.assertEqual(self.i2.total_mean(), 50.0)
        self.assertIs(self.i3.total_mean(), np.nan)


class TestMissing(unittest.TestCase):
    def setUp(self):
        print("SetUp")
        self.df = pd.DataFrame(np.arange(100).reshape(20, 5))
        self.df2 = self.df.copy()
        self.df2.iloc[0, 0] = np.nan
        self.m1 = Missing(self.df)
        self.m2 = Missing(self.df2)

    def tearDown(self):
        print("TearDown")

    def test_Missing(self):
        self.assertIsInstance(self.m1, Df_Info)
        self.assertIsInstance(self.m1, Missing)
        self.assertEqual(self.m1.count_missing.sum(), 0)
        self.assertEqual(self.m2.count_missing.sum(), 1)
        self.assertEqual(self.m1.percent_missing.sum(), 0)
        self.assertFalse(hasattr(Missing(123), "df"))


class TestStats(unittest.TestCase):
    def setUp(self):
        print("SetUp")
        self.df = pd.DataFrame(np.arange(100).reshape(20, 5))
        self.df2 = self.df.copy()
        self.df2.iloc[0, 0] = np.nan
        self.s1 = Stats(self.df)
        self.s2 = Stats(self.df2)

    def tearDown(self):
        print("TearDown")

    def test_Stats(self):
        self.assertIsInstance(self.s1, Df_Info)
        self.assertIsInstance(self.s1, Stats)
        self.assertEqual(self.s1.sub_max.max(), 99)
        self.assertEqual(self.s1.sub_min.min(), 0)
        self.assertEqual(self.s1.sub_mean.mean(), 49.5)
        self.assertEqual(self.s2.sub_mean.mean(), 50.0)
        self.assertFalse(hasattr(Stats(123), "df"))


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)