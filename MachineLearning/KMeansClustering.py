## clustering: K Means
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

def clustering():
    ## Kid, women and Men data
    raw_data= {
        'weight':[1, 5, 2, 6, 20, 25, 28, 30, 50, 55, 60, 62],
        'height':[10, 15, 18, 20, 100, 110, 105,115, 160, 162, 170, 175]
    }

    df = pd.DataFrame(raw_data)
    # of cluster
    k=3
    model = KMeans(n_clusters=k)
    model.fit(df)
    labels =  model.labels_
    print("Labels: ", labels)

    centroids = model.cluster_centers_
    colours = ['red', 'green', 'blue', 'purple']
    y=0
    for x in labels:
        plt.scatter(df.iloc[y,0], df.iloc[y,1], color=colours[x])
        y = y+1

    for x in range(k):
        crossess=plt.plot(centroids[x,0], centroids[x,1], 'kx')
        plt.setp(crossess, ms=10.0, mew=3.0)

    plt.show()

##prediction
clustering()