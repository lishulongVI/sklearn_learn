# -*- coding:utf-8 -*-  

__author__ = 'lishulong.never@gmail.com'
__time__ = '2017/11/11'
__msg__ = '学不可以已'

from sklearn.datasets import load_boston

boston = load_boston()
print(boston.data.shape)

data, target = load_boston(return_X_y=True)

print(data.shape)
print(target.shape)

print(target)
