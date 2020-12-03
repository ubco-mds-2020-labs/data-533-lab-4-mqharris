import unittest
import pandas as pd
import numpy as np
from quickscreen.summary.summary_stats import missing_summary
from quickscreen.summary.summary_stats import stats_summary
from quickscreen.summary.summary_stats import all_summary
from quickscreen.summary.summary_stats import simple_summary


class TestSummaryStats(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("./data/Carprice.csv")
        self.df2 = self.df.copy()
        self.df2.iloc[0, 0] = np.nan
        self.df3 = pd.DataFrame(np.arange(100).reshape(10, 10))

    def tearDown(self):
        pass

    def test_missing_summary(self):
        self.assertIsInstance(missing_summary(self.df), pd.DataFrame)
        self.assertEqual(missing_summary(self.df).shape, (8, 2))
        self.assertEqual(missing_summary(self.df, type="rows").shape, (205, 2))
        self.assertEqual(missing_summary(self.df).sum().sum(), 0)
        self.assertEqual(missing_summary(self.df2).loc[:, "count_missing"].sum(), 1)

    def test_stats_summary(self):
        test_array1 = np.array([288.0, 48.0, 104.0])
        test_array2 = np.array([16845.0, 23.0, 3643.0])
        self.assertIsInstance(stats_summary(self.df), pd.DataFrame)
        self.assertEqual(stats_summary(self.df).shape, (7, 3))
        self.assertEqual(stats_summary(self.df, type="rows").shape, (205, 3))
        self.assertTrue(
            (np.round(stats_summary(self.df).iloc[2, :].values, 0) == test_array1).all()
        )
        self.assertTrue(
            (
                np.round(stats_summary(self.df, type="rows").iloc[200, :].values, 0)
                == test_array2
            ).all()
        )

    def test_all_summary(self):
        self.assertIsInstance(all_summary(self.df), pd.DataFrame)
        self.assertEqual(all_summary(self.df).shape, (8, 5))
        self.assertEqual(all_summary(self.df, type="rows").shape, (205, 5))
        self.assertEqual(all_summary(self.df3).loc[9, "max"], 99)
        self.assertEqual(all_summary(self.df3).loc[0, "min"], 0)
        self.assertEqual(all_summary(self.df3)["mean"].mean(), 49.5)
        self.assertEqual(all_summary(self.df2)["count_missing"].sum(), 1)

    def test_simple_summary(self):
        test_array1 = np.array([205.0, 205.0, 0.0])
        self.assertIsInstance(simple_summary(self.df), pd.DataFrame)
        self.assertEqual(simple_summary(self.df).shape, (6, 1))
        self.assertTrue(
            (simple_summary(self.df).values.flatten()[3:] == test_array1).all()
        )
        self.assertEqual(simple_summary(self.df).isnull().sum().values[0], 3)


unittest.main(argv=[""], verbosity=2, exit=False)
