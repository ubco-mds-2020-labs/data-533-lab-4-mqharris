import unittest
import pandas as pd
import numpy as np
import quickscreen.analysis.datafill as daf

class TestDataEdit(unittest.TestCase):

    def setUp(self):
        self.data1 = daf.DataEdit(pd.DataFrame(np.arange(12).reshape(3,4)))
        self.data2 = pd.DataFrame(np.array([np.arange(3,7),np.arange(4,8),np.arange(3,7)]))
        self.data3 = daf.DataEdit(pd.DataFrame(np.array([[0,1,np.nan,4],np.arange(4,8),np.arange(4,8)])))
        
        
    def tearDown(self):
        del self.data1
        del self.data2
        del self.data3

    def test_display(self):
        self.assertIsInstance(self.data1.display(),pd.DataFrame,'Not a pandas DataFrame')
        self.assertIsInstance(self.data3.display(),pd.DataFrame, 'Not a pandas DataFrame')

    def test_column_type(self):
        self.assertIsInstance(self.data1.columntype(0),np.dtype, 'Is not a numpy dtype')
        self.assertIsInstance(self.data1.columntype(1),np.dtype, 'Is not a numpy dtype')
    
    def test_add(self):
        self.assertTrue((self.data1+self.data2).display().equals(pd.DataFrame(np.array([np.arange(4),np.arange(4,8),np.arange(8,12),np.arange(3,7),np.arange(4,8),np.arange(3,7)]))),'Is not Equal')


    def test_sub(self):
        self.assertTrue((self.data1-self.data2).display().equals(pd.DataFrame(np.array([np.arange(4),np.arange(8,12)]),index=[0,2]).astype('int64')), 'Is not equal')
    
    def test_remove_duplicates(self):
        self.assertTrue(self.data3.rm_duplicates().display().equals(pd.DataFrame(np.array([[0,1,np.nan,4],np.arange(4,8)]))),'Did not remove duplicates')
 
    def test_remove_nan(self):
        self.assertTrue(self.data3.rm_nan().display().equals(pd.DataFrame([np.arange(4,8),np.arange(4,8)],index=[1,2]).astype('float64')), 'Did not remove NaN')

    def test_quick_clean(self):
        self.assertTrue(self.data3.quick_clean().display().equals(pd.DataFrame(np.array([np.arange(4,8)]),index=[1]).astype('float64')),'Did not quick clean')
    
if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
