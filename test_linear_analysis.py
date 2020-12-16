import unittest
import pandas as pd
import numpy as np
import quickscreen.analysis.linear_analysis as la

class TestLm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db1=pd.DataFrame(np.array([[0,0],[1,1],[2,2]]))
        cls.db2=pd.DataFrame(np.array([[0,1],[1,3],[2,5]]))
        cls.db3=pd.DataFrame(np.array([[0,3],[1,2.5],[2,2]]))
        print("Class Setup")

    @classmethod
    def tearDownClass(cls):
        del cls.db1
        del cls.db2
        del cls.db3
        print("Class Teardown")

    def setUp(self):
        self.data1 = la.Lm(self.db1)
        self.data2 = la.Lm(self.db2)
        self.data3 = la.Lm(self.db3)
        
    def tearDown(self):
        del self.data1
        del self.data2
        del self.data3
    
    def test_single_linear(self):
        self.assertTrue(np.ndarray.all(self.data1.single_linear(1,0).reshape(1,3)[0].round()==np.array([0,1,2])),'The output does not match')
        self.assertTrue(np.ndarray.all(self.data2.single_linear(1,0).reshape(1,3)[0].round()==np.array([1,3,5])),'The output does not match')
        self.assertTrue(np.ndarray.all(self.data3.single_linear(1,0).reshape(1,3)[0].round(2)==np.array([3,2.5,2])),'The output does not match')
        self.assertIsNone(self.data3.single_linear(1,'error'), "Does not catch Pandas Dataframe error in estimator")
        self.assertIsNone(self.data3.single_linear('error',0), "Does not catch Pandas Dataframe error in predictor")

    def test_single_linear_eqn(self):
        self.assertEqual(self.data1.single_linear_eqn(1,0)['Coefficient'],1.0,'The coefficient is wrong')
        self.assertEqual(self.data1.single_linear_eqn(1,0)['Intercept'],0.0,'The intercept is wrong')
        self.assertEqual(self.data2.single_linear_eqn(1,0)['Coefficient'],2.0,'The coefficient is wrong')
        self.assertEqual(self.data2.single_linear_eqn(1,0)['Intercept'],1.0,'The intercept is wrong')
        self.assertEqual(self.data3.single_linear_eqn(1,0)['Coefficient'],-0.5,'The coefficient is wrong')
        self.assertEqual(self.data3.single_linear_eqn(1,0)['Intercept'],3.0,'The intercept is wrong')
        self.assertIsNone(self.data3.single_linear_eqn(1,'error'), "Does not catch Pandas Dataframe error in estimator")
        self.assertIsNone(self.data3.single_linear_eqn('error',0), "Does not catch Pandas Dataframe error in predictor")

    def test_single_linear_plot(self):
        self.assertIsNone(self.data3.single_linear_plot(1,'error'), "Does not catch Pandas Dataframe error in estimator")
        self.assertIsNone(self.data3.single_linear_plot('error',0), "Does not catch Pandas Dataframe error in predictor")

if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)

    
    
