import unittest
from tools.ml_tools import MlTools

import pandas as pd

class TestMlTools(unittest.TestCase):


    def test_maptarget(self):
        rows = [{'class': 'foo'}, {'class': 'bar'}]
        data = pd.DataFrame(rows)
        column = 'class'
        map_dict = {'foo': 0, 'bar': 1}

        data = MlTools.map_target(data, column, map_dict)

        self.assertEqual(data[column].values.tolist(), [0, 1])

    def test_separecolumns(self):
        row = {'column1': 'foo', 'column2': 'bar', 'target': 0}
        data = pd.DataFrame([row])

        X, y = MlTools.separe_columns(data, ['column1', 'column2'], 'target')

        self.assertEqual(X.columns.tolist(), ['column1', 'column2'])
        self.assertEqual(y.name, 'target')