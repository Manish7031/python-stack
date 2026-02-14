## Multiple regression
## Problem: predict the vehicle distance travel based on parameter fuel consumption, electicmodel etc.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def predict_distance(fuel_consumption_l, electric_prcnt):
    raw_data = {
        'fuel_consumption_l': [1,2,3,3,4,5,6,7],
        'electric_prcnt':[0.20, 0.20, 0.60, 0.70, 0.90, 0.90, 0.50, 0.90],
        'total_distance_miles':[200, 240, 560, 570, 990, 1200, 800, 1400]
    }

    df = pd.DataFrame(raw_data)
    X = np.array(df[['fuel_consumption_l','electric_prcnt']])
    y = np.array(df['total_distance_miles']).reshape(-1,1)

    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=0.25)

    model = LinearRegression()
    model.fit(train_X, train_y)
    
    y_prediction = model.predict([[fuel_consumption_l, electric_prcnt]])
    print(f"prediction : {y_prediction}")

    ##accuracy
    y_test_prediction = model.predict(test_X)
    print(f"mean absolute error : {mean_absolute_error(test_y, y_test_prediction)}")
    print(f"r2 score : {r2_score(test_y,y_test_prediction)}")
    print('slope', model.coef_)
    print('Intercept', model.intercept_)

##prediction
predict_distance(3, 0.60)
