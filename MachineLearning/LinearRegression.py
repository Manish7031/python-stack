## Linear regression
## Problem: predict wages based on years of experience
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def predict_salary(years_of_experience):
    raw_data = {
        'years_exp':[1,2,3,4,5,6,7,8,9,10,15],
        'salary':[60, 100, 130, 150, 180, 230, 260, 270, 290, 330, 350]
    }

    df = pd.DataFrame(raw_data)

    X = np.array(df['years_exp']).reshape(-1,1)
    y = np.array(df['salary']).reshape(-1,1)

    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=0.25)

    # print('train_X : ', train_X.tolist())
    # print('test_X : ', test_X.tolist())
    # print('train_y : ', train_y.tolist())
    # print('test_y : ',test_y.tolist())
    model = LinearRegression()
    model.fit(train_X, train_y)

    y_prediction = model.predict([[years_of_experience]])
    print(f"expected salary at {years_of_experience} years is : {y_prediction}")

    ##accuracy
    y_test_prediction = model.predict(test_X)
    y_line = model.predict(X)

    print('slope', model.coef_)
    print('Intercept', model.intercept_)
    print("Mean_absolute_error : ", mean_absolute_error(test_y, y_test_prediction))
    print("r2 score", r2_score(test_y, y_test_prediction))

    ##plot
    plt.scatter(X,y,s=12)
    plt.xlabel('years of experience')
    plt.ylabel('expected salary')
    plt.plot(X,y_line,color ='r')
    plt.show()

#prediction
predict_salary(22)
#predict_salary(25)