import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("lake-conjola.csv", encoding="utf-8")

kmeans = KMeans(n_clusters=3).fit(df[["Temp (C)", "DO (mg/L)"]])
centroids = kmeans.cluster_centers_

plt.scatter(
    df["Temp (C)"], df["DO (mg/L)"], c=kmeans.labels_.astype(float), s=50, alpha=0.5
)
plt.scatter(centroids[:, 0], centroids[:, 1], c="red", s=50)
plt.show()
