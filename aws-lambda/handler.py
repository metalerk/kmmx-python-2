import json
import pandas as pd

def get_line_number(path):
    with open('matrices.csv', 'r') as f:
        f.__next__()
        for line in f.readlines():
            print(line)

def main(event, context):
    matrices = pd.read_csv('matrices.csv')
    print(matrices)
    get_line_number('matrices.csv')