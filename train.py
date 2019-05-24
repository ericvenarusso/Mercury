from machine_learning.classifiers import Classifiers
from tools.aws_tools import AWSTools
from tools.ml_tools import MlTools

import pandas as pd
import os

# AWS Client config
s3 = AWSTools(
        's3', 
        os.environ['ACCESS_KEY'],
        os.environ['SECRET_KEY'],
     )

# Download the preprocess file from S3
s3.download(os.environ['BUCKET_DATA'], 'iris.csv', 'data/s3_iris.csv')

# Read Data
data = pd.read_csv('data/s3_iris.csv')

# Separe columns
X, y = MlTools.separe_columns(data, ['sepallength', 'sepalwidth', 'petallength', 'petalwidth'], 'class')

# Training
model, results = Classifiers.XGB_classifier(X, y)

# Save the model local
model.save_model('model/iris_xgboost.model')

# Upload model to S3
s3.upload('model/iris_xgboost.model', os.environ['BUCKET_MODEL'], 'iris_xgboost.model')