from google.colab import drive
drive.mount('/content/drive')

import csv
# with open('/content/drive/My Drive/GSF_test.csv', newline='') as csvfile:
with open('/content/drive/My Drive/GSF_test.csv', "r", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

import json
import os

with open('/content/drive/My Drive/GSF_test1.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
