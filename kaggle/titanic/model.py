__author__ = 'asos'
import csv as csv
import numpy as np

csv_file = csv.reader(open('train.csv', 'rb'))
header = csv_file.next()

data = []
for row in csv_file:
    data.append(row)

data = np.array(data)

