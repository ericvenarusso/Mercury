import unittest
from tools.ml_tools import MlTools

import pandas as pd

class TestMlTools(unittest.TestCase):

    def test_maptarget(self):
        data = pd.DataFrame([{'class': 'foo'}, {'class': 'bar'}])
        column = 'class'
        map_dict = {'foo': 0, 'bar': 1}

        data = MlTools.map_target(data, column, map_dict)
        self.assertEqual(data[column].values.tolist(), [0, 1])