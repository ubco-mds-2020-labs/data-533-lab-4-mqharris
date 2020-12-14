import unittest
import pandas as pd
import numpy as np
import quickscreen.analysis.datafill as daf

class TestDataEdit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db1 = pd.DataFrame(np.arange(12).reshape(3,4))
        cls.db2 = pd.DataFrame(np.array([np.arange(3,7),np.arange(4,8),np.arange(3,7)]))
        cls.db3 = pd.DataFrame(np.array([[0,1,np.nan,4],np.arange(4,8),np.arange(4,8)]))
        

    @classmethod
    def tearDownClass(cls):
        del cls.db1
        del cls.db2
        del cls.db3
        del cls.db4

    def setUp(self):
        self.data1 = daf.DataEdit(self.db1)
        self.data2 = self.db2
        self.data3 = daf.DataEdit(self.db3)
        self.data4 = 'error'
        
    def tearDown(self):
        del self.data1
        del self.data2
        del self.data3

    def test__init__(self):
        self.assertIsNone(daf.DataEdit(self.data4),"Fails to detect not Pandas DataFrame")

    def test_display(self):
        self.assertIsInstance(self.data1.display(),pd.DataFrame,'Not a Pandas DataFrame')
        self.assertIsInstance(self.data3.display(),pd.DataFrame, 'Not a Pandas DataFrame')

    def test_column_type(self):
        self.assertIsInstance(self.data1.columntype(0),np.dtype, 'Is not a numpy dtype')
        self.assertIsInstance(self.data1.columntype(1),np.dtype, 'Is not a numpy dtype')
        self.assertIsNone(self.data1.columntype('not a column'),'Column error not caught')
    
    def test_add(self):
        self.assertTrue((self.data1+self.data2).display().equals(pd.DataFrame(np.array([np.arange(4),np.arange(4,8),np.arange(8,12),np.arange(3,7),np.arange(4,8),np.arange(3,7)]))),'Is not Equal')
        self.assertIsNone(self.data1+self.data4, 'Not a Pandas Dataframe')


    def test_sub(self):
        self.assertTrue((self.data1-self.data2).display().equals(pd.DataFrame(np.array([np.arange(4),np.arange(8,12)]),index=[0,2]).astype('int64')), 'Is not equal')
        self.assertIsNone(self.data1-self.data4, 'Not a Pandas Dataframe')
    
    def test_remove_duplicates(self):
        self.assertTrue(self.data3.rm_duplicates().display().equals(pd.DataFrame(np.array([[0,1,np.nan,4],np.arange(4,8)]))),'Did not remove duplicates')
 
    def test_remove_nan(self):
        self.assertTrue(self.data3.rm_nan().display().equals(pd.DataFrame([np.arange(4,8),np.arange(4,8)],index=[1,2]).astype('float64')), 'Did not remove NaN')

    def test_quick_clean(self):
        self.assertTrue(self.data3.quick_clean().display().equals(pd.DataFrame(np.array([np.arange(4,8)]),index=[1]).astype('float64')),'Did not quick clean')
    
if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
