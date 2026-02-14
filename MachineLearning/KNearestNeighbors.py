## classification: KNN implementation
## problem: based on height and weight classification of person health fit or not.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def health_analyze(weight, height):
    overweigth_people = [[99, 89],[119,99],[199,174],[79,99],[39,59]]
    fit_people = [[59,174],[89,189],[79,179],[49,139],[29,119]]

    people = fit_people+overweigth_people
    is_fit = [1,1,1,1,1,0,0,0,0,0]

    X = np.array(people)
    y = np.array(is_fit)

    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=0.20)
    #model
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(train_X,train_y)
    #score
    print(f"model score : {model.score(test_X,test_y)}")
    prediction = model.predict([[weight, height]])

    print(f"prediction : ({prediction[0]})", 'fit'
            if int(prediction[0]) == 1 else 'not fit')
    
    #plot
    plt.scatter(X[:,0],X[:,1])
    plt.scatter(weight, height, color='r',s=100)
    plt.ylabel('height')
    plt.xlabel('weights')
    plt.show()
    
health_analyze(95,170)


