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


    
    
