import unittest
import pandas as pd
import numpy as np


from quickscreen.summary.summary_stats import missing_summary
from quickscreen.summary.summary_stats import stats_summary
from quickscreen.summary.summary_stats import all_summary
from quickscreen.summary.summary_stats import simple_summary


class TestSummaryStats(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(np.arange(100).reshape(20, 5))
        self.df2 = self.df.copy()
        self.df2.iloc[0, 0] = np.nan
        self.test_array1 = np.arange(5)
        self.test_array2 = np.arange(95, 100)

    def tearDown(self):
        pass

    def test_missing_summary(self):
        self.assertIsInstance(missing_summary(self.df), pd.DataFrame)
        self.assertEqual(missing_summary(self.df).shape, (5, 2))
        self.assertEqual(missing_summary(self.df, type="rows").shape, (20, 2))
        self.assertEqual(missing_summary(self.df).sum().sum(), 0)
        self.assertEqual(missing_summary(self.df2).loc[:, "count_missing"].sum(), 1)

    def test_stats_summary(self):
        self.assertIsInstance(stats_summary(self.df), pd.DataFrame)
        self.assertEqual(stats_summary(self.df).shape, (5, 3))
        self.assertEqual(stats_summary(self.df, type="rows").shape, (20, 3))
        self.assertTrue(
            (np.array(stats_summary(self.df)["min"]) == self.test_array1).all()
        )
        self.assertTrue(
            (np.array(stats_summary(self.df)["max"]) == self.test_array2).all()
        )
        self.assertEqual(stats_summary(self.df)["mean"].mean(), 49.5)

    def test_all_summary(self):
        self.assertIsInstance(all_summary(self.df), pd.DataFrame)
        self.assertEqual(all_summary(self.df).shape, (5, 5))
        self.assertEqual(all_summary(self.df, type="rows").shape, (20, 5))
        self.assertEqual(all_summary(self.df).loc[:, "count_missing"].sum(), 0)
        self.assertEqual(all_summary(self.df2).loc[:, "count_missing"].sum(), 1)
        self.assertTrue(
            (np.array(all_summary(self.df)["min"]) == self.test_array1).all()
        )
        self.assertTrue(
            (np.array(all_summary(self.df)["max"]) == self.test_array2).all()
        )
        self.assertEqual(stats_summary(self.df)["mean"].mean(), 49.5)

    def test_simple_summary(self):
        test_array3 = np.array([99.0, 0.0, 49.5, 20.0, 5.0, 0.0])
        test_array4 = np.array([99.0, 1.0, 50.0, 20.0, 5.0, 1.0])
        self.assertIsInstance(simple_summary(self.df), pd.DataFrame)
        self.assertEqual(simple_summary(self.df).shape, (6, 1))
        self.assertTrue((simple_summary(df).values.flatten() == test_array3).all())
        self.assertTrue((simple_summary(df2).values.flatten() == test_array4).all())


unittest.main(argv=[""], verbosity=2, exit=False)
