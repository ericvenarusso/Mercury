import unittest
from machine_learning.classifiers import Classifiers

import xgboost as xgb

import pandas as pd

class TestClassifiers(unittest.TestCase):

    def test_xgboost(self):

        X = pd.DataFrame([{'foo': 1, 'bar': 2}])
        y = pd.Series([0])


        model, results = Classifiers.XGB_classifier(X, y)

        self.assertEqual(type(model), type(xgb.XGBClassifier()))
        self.assertEqual(type(results), type(dict()))