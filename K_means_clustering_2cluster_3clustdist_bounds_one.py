"""This program does the machine learning to obtain the clusters and its corresponding centroid. The cluster formation
helps to formulate the UGV route in such a way that the UGV's travel to the centroid point of the cluster is sufficient
enough for the UAVs to cover the mission points around that cluster and such proximity allow UGV to recharge UAVs whenever needed.
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import random_mission_points_distrib_3clusters_bounds_one


def clustered_locations(_locations=None, random_seed=None):
    """!
    Compute the centroids through Kmeans algorithm
    [MOD] put both parameters as optional
    @param random_seed [int]: random seed to generate the number
    @param _locations array(tuple): locations to use as x,y coordinates [MOD]
    @out ctrd array: coordinates of the centroids
    @out _locations
    @out labels array: Attribution array of the points to the clusters [MOD]
    """
    if random_seed is None and _locations is None:
        raise ValueError("Provide at least one of _locations or random seed")
    elif _locations is None:
        _locations = random_mission_points_distrib_3clusters_bounds_one.random_locations(random_seed)

    df = pd.DataFrame(_locations, columns=['x', 'y'])

    kmeans = KMeans(n_clusters=2)
    kmeans.fit(df)

    labels = kmeans.predict(df)
    centroids = kmeans.cluster_centers_

    # print(centroids)
    ctrd = [(13200, 13200)]

    for i in range(len(centroids)):
        ctrd.append((centroids[i][0], centroids[i][1]))
    return ctrd, _locations, labels

def plot_centroids(df, centroids, labels):
    """
    [MOD]: Added completely the function to simplify code
    Plot the points along with the centroids, coloring by cluster.
    @param df DataFrame: Dataframe of the data to plot
    @param centroids array: coordinates of the centroids
    @param labels array: Attribution array of the points to the clusters [MOD]
    """
    fig = plt.figure()

    colmap = {1: 'r', 2: 'g', 3: 'b', 4: 'k', 5: 'y'}

    colors = map(lambda x: colmap[x+1], labels)
    colors1 = list(colors)
    plt.scatter(df['x'], df['y'], color=colors1, alpha=0.5, edgecolor='k')
    for idx, centroid in enumerate(centroids):
        plt.scatter(*centroid, color=colmap[idx+1])
    plt.xlim(0, 26400)
    plt.ylim(0, 26400)
