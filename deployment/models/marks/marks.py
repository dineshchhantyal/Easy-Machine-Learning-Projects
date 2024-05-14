import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os


def marks_prediction(marks):
    file_path = f'{os.getcwd()}/models/marks/scores.csv'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    df = pd.read_csv(file_path)
    X = df['Hours']
    y = df['Scores']

    X = X.values.reshape(-1, 1)
    y = y.values.reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, y)

    X_test = np.array([marks], dtype=np.float64).reshape(-1, 1)
    y_pred = model.predict(X_test)

    return y_pred[0][0]


def get_dataset():
    file_path = f'{os.getcwd()}/models/marks/scores.csv'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    df = pd.read_csv(file_path)
    return df.to_dict(orient='records'), df.describe().to_dict()
