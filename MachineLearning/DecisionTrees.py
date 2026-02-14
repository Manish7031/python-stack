## Classificaiton: Decision Tree
## proeblem: Decision to Items bought to selected person
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def wine_decision(wine_type, score, price):
    raw_data = {
        'wine': ['Red', 'Red', 'Red', 'white', 'white', 'white'],
        'score': ['High', 'High', 'Low', 'High', 'Low', 'Low'],
        'price': ['High', 'Low','Low', 'Low', 'High', 'Low'],
        'bought': ['Yes', 'Yes', 'No', 'Yes', 'No', 'No']
    }

    df = pd.DataFrame(raw_data)

    le = LabelEncoder()
    en_wine, en_score, en_price = le.fit_transform(df.wine), le.fit_transform(df.score), le.fit_transform(df.price)
    en_bought = le.fit_transform(df.bought)
    # print(en_wine)
    # print(en_score)
    # print(en_price)
    # print(en_bought)
    translate = {
        'Red': 0, 'white': 1,
        'High': 0, 'Low': 1,
        'Yes': 1, 'No': 0
    }

    features = list(zip(en_wine, en_score, en_price))
    X = np.array(features)
    y = np.array(en_bought)
    train_X, test_X, train_y, test_y =  train_test_split(X, y, test_size=0.25)

    Classifier = tree.DecisionTreeClassifier()
    Classifier.fit(X, y)

    prediction = Classifier.predict([[translate[wine_type], translate[score], translate[price]]])
    value = int(prediction[0])
    print("Value : ", value)
    print('buy the wine: ', wine_type if value == 1 else 'not choose')


##prediction
wine_decision(wine_type='Red', score='High', price='Low')


