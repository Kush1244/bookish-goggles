import numpy as np
import pandas as pd


def read_files(path):
    return pd.read_csv(path)


class training_dataset:
    def __init__(self):
        self.dataset = read_files("./dataset/train.csv")
        pass

    
    def get_data(self):
        return self.dataset


class testing_dataset:
    def __init__(self):
        self.dataset = read_files("./dataset/test.csv")

    def get_data(self):
        return self.dataset