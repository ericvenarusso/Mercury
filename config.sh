#!/bin/bash

# Downloading Data
wget -P data/ https://pkgstore.datahub.io/machine-learning/iris/iris_csv/data/8bce8766530bf404228ea3fc026dfee3/iris_csv.csv

# Change file name
mv data/iris_csv.csv data/iris.csv

# Create folder model
mkdir model