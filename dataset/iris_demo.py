# -*- coding:utf-8 -*-  

__author__ = 'lishulong.never@gmail.com'
__time__ = '2017/11/11'
__msg__ = '学不可以已'

from sklearn.datasets import load_iris

iris = load_iris()

print(iris.data.shape)

print(iris.target.shape)

print(list(iris.target_names))

data, target = load_iris(return_X_y=True)

print(data.shape)
print(target.shape)

print(data)
