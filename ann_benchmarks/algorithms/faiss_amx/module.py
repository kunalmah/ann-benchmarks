import sys

sys.path.append("install/lib-faiss")  # noqa
import faiss
import numpy
import os
import sklearn.preprocessing
import tensorflow as tf

from ..base.module import BaseANN


class Faiss(BaseANN):
    def query(self, v, n):
        if self._metric == "angular":
            v /= numpy.linalg.norm(v)
        D, I = self.index.search(numpy.expand_dims(v, axis=0).astype(numpy.float32), n)
        return I[0]

    def batch_query(self, X, n):
        if self._metric == "angular":
            X /= numpy.linalg.norm(X)
        self.res = self.index.search(X.astype(numpy.float32), n)

    def get_batch_results(self):
        D, L = self.res
        res = []
        for i in range(len(D)):
            r = []
            for l, d in zip(L[i], D[i]):
                if l != -1:
                    r.append(l)
            res.append(r)
        return res

class FaissIndexFlatIP_AMX(Faiss):
    def __init__(self, metric, hold):
        print("### __init__ arg hold: " + str(hold))
        self._metric = metric

    def fit(self, X):
        if self._metric == "angular":
            X = sklearn.preprocessing.normalize(X, axis=1, norm="l2")

        if X.dtype != numpy.float32:
            X = X.astype(numpy.float32)

        # self.quantizer = faiss.IndexFlatIP(X.shape[1])
        index = faiss.IndexFlatIP(X.shape[1])
        index.train(X)
        index.add(X)
        self.index = index
    
    def set_query_arguments(self, hold):
        print("### set_query_arguments arg hold: " + str(hold))
        return

    def __str__(self):
        return "FaissIndexFlatIP_AMX"
    
class FaissIndexFlatIP_BF16_AMX(Faiss):
    def __init__(self, metric, hold):
        print("### __init__ arg hold: " + str(hold))
        self._metric = metric

    def fit(self, X):
        if self._metric == "angular":
            X = sklearn.preprocessing.normalize(X, axis=1, norm="l2")

        if X.dtype != numpy.float32:
            X = X.astype(numpy.float32)

        X = tf.cast(X, tf.bfloat16)
        
        # self.quantizer = faiss.IndexFlatIP(X.shape[1])
        index = faiss.IndexFlatIP_bf16(X.shape[1])
        index.train(X)
        index.add(X)
        self.index = index
    
    def set_query_arguments(self, hold):
        print("### set_query_arguments arg hold: " + str(hold))
        return

    def __str__(self):
        return "FaissIndexFlatIP_BF16_AMX"
