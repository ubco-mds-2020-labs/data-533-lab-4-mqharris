import unittest


from test_summary_stats import TestSummaryStats
from test_summary_classes import TestDfInfo
from test_summary_classes import TestMissing
from test_summary_classes import TestStats


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestSummaryStats))
    suite.addTest(unittest.makeSuite(TestDfInfo))
    suite.addTest(unittest.makeSuite(TestMissing))
    suite.addTest(unittest.makeSuite(TestStats))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))


my_suite()
