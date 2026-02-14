## Classfication : Random Forests
## problem: Customer Items purchase classfication based on price and score input value
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def Item_purchase(wine, score, price):
    df = pd.read_csv('MachineLearning\datasets\sample_data.csv')
    le = LabelEncoder()
    en_wine, en_score, en_price = le.fit_transform(df.wine), le.fit_transform(df.score), le.fit_transform(df.price)
    en_bought = le.fit_transform(df.bought)

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
    rf =  RandomForestClassifier(n_estimators=10)
    Classifier.fit(X, y)
    rf.fit(X, y)

    ##score
    print(f"Decision tree score :  {Classifier.score(X,y)}")
    print(f"Random forest score :  {rf.score(X,y)}")

    #predict
    prediction = rf.predict([[translate[wine], translate[score], translate[price]]])
    value = int(prediction[0])
    print("Value : ", value)
    print('buy the wine: ', wine if value == 1 else 'not choose')


Item_purchase(wine='Red', score='High', price='Low')
Item_purchase(wine='Red', score='High', price='High')

