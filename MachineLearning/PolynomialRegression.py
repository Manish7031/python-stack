## polynomial Regression
## timeseries sales analysis
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def predict_sales(time):
    raw_data = {
        'year': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'sales': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    }

    df = pd.DataFrame(raw_data)
    X = np.array(df['year'].tolist())
    y = np.array(df['sales'].tolist())

    model = np.poly1d(np.polyfit(X, y, deg=10))
    y_prediction = model(time)
    y_prediction_test = model(X)

    print("prediction : ", y_prediction)
    print(f"mean absolute error : {mean_absolute_error(y, y_prediction_test)}")
    print(f"r2 score : {r2_score(y, y_prediction_test)}")

    curve_line = np.linspace(1,10,10)
    plt.scatter(X,y)
    plt.plot(curve_line, model(curve_line))
    plt.show()


predict_sales(10.5)