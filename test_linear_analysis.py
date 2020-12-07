import unittest
import pandas as pd
import numpy as np
import quickscreen.analysis.linear_analysis as la

class TestDataEdit(unittest.TestCase):

    def setUp(self):
        self.data1 = la.Lm( )
        self.data2 = la.Lm(pd.DataFrame(np.array([np.arange(3,7),np.arange(5,9),np.arange(3,7)])))
        self.data3 = la.Lm(pd.DataFrame(np.array([[0,1,np.nan,4],np.arange(5,9),np.arange(5,9)])))
        
        
    def tearDown(self):
        self.data1.destroy()
        self.data2.destroy()
        self.data3.destroy()
    
    def test_single_linear(self):
        self.assertEqual(self.data1.single_linear(0,1), np.array([0,1,2]),'The output does not match')

    def test_single_linear_eqn(self):
        self.assertEqual(self.data1.single_linear_eqn(0,1)['Coefficient'],1,'The coefficient is wrong')
        self.assertEqual(self.data1.single_linear_eqn(0,1)['Intercept'],0,'The coefficient is wrong')
        


    
    
