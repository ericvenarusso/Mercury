from tools.ml_tools import MlTools
from tools.aws_tools import AWSTools

import pandas as pd
import os

# Read data
iris = pd.read_csv('data/iris.csv')

# Map Target
target_dict = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
iris_preprocessed = MlTools.map_target(iris, 'class', target_dict)

#Save the preprocessed dataframe local
iris_preprocessed.to_csv('data/iris_processed.csv', index=False)

# AWS Client config
s3 = AWSTools(
        's3', 
        os.environ['ACCESS_KEY'],
        os.environ['SECRET_KEY'],
     )

# Upload the preprocess dataframe
s3.upload('data/iris_processed.csv', os.environ['BUCKET_DATA'], 'iris.csv')