## classification: SVM implementation

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score
from sklearn.model_selection import train_test_split

def sample_dots(sample):
    green_dot = np.random.randint(0,200,size=(sample, 2)).tolist()
    red_dot = np.random.randint(50, 150, size=(sample, 2)).tolist()

    color = np.concatenate((np.zeros(sample), np.ones(sample))).flatten().tolist()

    return {'green_dot' : green_dot, 'red_dot' : red_dot, 'colour': color}


def generate_color(a, b):
    data = sample_dots(100)
    green_dot, red_dot = data['green_dot'], data['red_dot']
    dots = green_dot+red_dot
    colour = data['colour']

    X = np.array(dots)
    y = np.array(colour)
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.20)

    classifier = SVC(kernel='linear', C=5)
    knn = KNeighborsClassifier(n_neighbors=15)

    classifier.fit(train_X, train_y)
    knn.fit(train_X,train_y)

    print("SVC score :" ,classifier.score(test_X, test_y))
    print("KNN score :" ,knn.score(test_X, test_y))
    prediction_svm = classifier.predict([[a, b]])
    prediction_KNN = knn.predict([[a, b]])

    #convert to int
    classifier_value, knn_value = int(prediction_svm[0]), int(prediction_KNN[0])
    print("SVC value:  ", classifier_value, 'Red' if classifier_value ==1  else 'green')
    print("KNN value: ", knn_value, 'Red' if classifier_value ==1  else 'green')

    #plot
    red_scatter = [np.array(red_dot)[:,0], np.array(red_dot)[:,1]]
    green_scatter = [np.array(green_dot)[:,0], np.array(green_dot)[:,1]]
    plt.scatter(red_scatter[0], red_scatter[1], c='r')
    plt.scatter(green_scatter[0],green_scatter[1], c='g')
    support_vector = classifier.support_vectors_
    plt.scatter(support_vector[:,0], support_vector[:, 1], c='b', marker='o')
    plt.scatter(a, b, color='blue', s=200, marker='X')
    plt.show()

generate_color(100,100)



