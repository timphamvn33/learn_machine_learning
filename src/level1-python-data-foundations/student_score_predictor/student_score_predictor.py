# import numpy as np
# import linearregression from linear_model
# import mean_absolute_error and mean_square_error from sklearn.metrics
# import train_test_split from sklearn.model_selection 

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_absolute_error, mean_squared_error, r2_score)
from sklearn.model_selection import train_test_split

# need to load data. x will be (a, b) a is dimensions of array and b is number of dimensions. y will be (a,). scikitlearn requires x will be samples x feautures. y is expected 1 dimensional target array
def load_data():
    # return matrix x and return vector y
    x = np.array([[1],
                 [2],
                 [3],
                 [4],
                 [5],
                 [6],
                 [7],
                 [8],], dtype=float)
    y = np.array([35, 40, 50, 55, 65, 70, 80, 90], dtype=float)

    return x, y

# x, y = load_data()
# print(x.shape)
# print(x.ndim)

def train_model(x_train, y_train):
    # train an linear regression model
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model

# next we need evaluate the model and predict_score from model

def evaluate_model(model, x_test, y_test):
    predictions = model.predict(x_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    return({
        "mae": mae,
        "mse": mse,
        "rmse": rmse,
        "r2": r2
    })

def predict_score(model, hours):
    if hours < 0:
        print("hours can't smaller than 0")
    predict = model.predict(np.array([[hours]], dtype=float))

    return predict[0]

def main():
    x, y = load_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

    model = train_model(x_train, y_train)
    results = evaluate_model(model, x_test, y_test)

if __name__ == "__main__":
    main()


