import unittest
import pandas as pd
import numpy as np
import quickscreen.analysis.datafill as daf

class TestDataEdit(unittest.TestCase):

    def setUp(self):
        self.data1 = daf.DataEdit(pd.DataFrame(np.arange(12).reshape(3,4)))
        self.data2 = daf.DataEdit(pd.DataFrame(np.array([np.arange(3,7),np.arange(5,9),np.arange(3,7)])))
        self.data3 = daf.DataEdit(pd.DataFrame(np.array([[0,1,np.nan,4],np.arange(5,9),np.arange(5,9)])))
        
        
    def tearDown(self):

    def test_display(self):
        self.assertIsInstance(self.data1,pd.DataFrame,'Not a pandas DataFrame')
        self.assertIsInstance(self.data2,pd.DataFrame, 'Not a pandas DataFrame')

    def test_column_type(self):
        self.assertIsInstance(self.data1.columntype(0),np.dtype, 'Is not a numpy dtype')
        self.assertIsInstance(self.data1.columntype(1),np.dtype, 'Is not a numpy dtype')
    
    def test_add(self):
        self.assertEqual(self.data1+self.data2, pd.DataFrame(np.array([np.arange(4),np.arange(5,9),np.arange(9,13),np.arange(3,7),np.arange(5,9),np.arange(3,7)])),'Is not Equal')

    def test_sub(self):
        self.assertEqual(self.data1-self.data2, pd.DataFrame(np.array([np.arange(4),np.arange(9,13)])), 'Is not equal')
    
    def test_remove_duplicates(self):
        self.assertEqual(self.data2, pd.DataFrame(np.array([np.arange(3,7),np.arange(5,9)])), 'Did not remove duplicates')
        self.assertEqual(self.data3,pd.DataFrame(np.array([[0,1,np.nan,4],np.arange(5,9)])),'Did not remove duplicates')
 
    def test_remove_nan(self):
        self.assertEqual(self.data3, pd.DataFrame([np.arange(5,9),np.arange(3,7)]), 'Did not remove NaN')

    def test_quick_clean(self):
        self.assertEqual(self.data3,pd.DataFrame(np.array([np.arange(5,9)])))
    

