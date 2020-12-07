import unittest


from test_summary_stats import TestSummaryStats
from test_summary_classes import TestDfInfo
from test_summary_classes import TestMissing
from test_summary_classes import TestStats

from test_plotter import TestPlotter
from test_grapher import TestGrapher


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    # test summary
    suite.addTest(unittest.makeSuite(TestSummaryStats))
    suite.addTest(unittest.makeSuite(TestDfInfo))
    suite.addTest(unittest.makeSuite(TestMissing))
    suite.addTest(unittest.makeSuite(TestStats))

    # test plott
    suite.addTest(unittest.makeSuite(TestPlotter))
    suite.addTest(unittest.makeSuite(TestGrapher))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))


my_suite()
