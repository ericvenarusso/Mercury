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
s3.download(os.environ['BUCKET_NAME'], 'iris.csv', 'data/s3_iris.csv')

#Read Data
data = pd.read_csv('data/s3_iris.csv')

#Separe columns
X, y = MlTools.separe_columns(data, ['sepallength', 'sepalwidth', 'petallength', 'petalwidth'], 'class')