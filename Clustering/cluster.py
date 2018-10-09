# coding=utf-8
import csv
import sys
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


# if len(sys.argv) != 3+int(sys.argv[1]):
#     raise SyntaxError("Incorrect arguments. Correct usage is: python3 cluster.py <cluster-amount> <input-file> <cluster0-output-file> <cluster1-output-file>...")


input = sys.argv[2]


texts = {}

for filename in os.listdir(input):
    filee = open(input+filename, "r")
    texts[filename] = str(filee.read())
    filee.close()

finaltexts = []

for key in texts:
    finaltexts.append(texts[key])


true_k = int(sys.argv[1])
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(finaltexts)
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

print("\n")
