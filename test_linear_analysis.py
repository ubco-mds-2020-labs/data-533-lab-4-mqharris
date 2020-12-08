import unittest
import pandas as pd
import numpy as np
import quickscreen.analysis.linear_analysis as la

class TestLm(unittest.TestCase):

    def setUp(self):
        self.data1 = la.Lm(pd.DataFrame(np.array([[0,0],[1,1],[2,2]])))
        
        
    def tearDown(self):
        del self.data1
    
    def test_single_linear(self):
        self.assertTrue(np.ndarray.all(self.data1.single_linear(0,1)==np.array([0,1,2])),'The output does not match')

    def test_single_linear_eqn(self):
        self.assertEqual(self.data1.single_linear_eqn(0,1)['Coefficient'],1.0,'The coefficient is wrong')
        self.assertEqual(self.data1.single_linear_eqn(0,1)['Intercept'],0.0,'The intercept is wrong')

if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)

    
    
