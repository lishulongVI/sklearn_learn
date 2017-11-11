# -*- coding:utf-8 -*-  

__author__ = 'lishulong.never@gmail.com'
__time__ = '2017/11/11'
__msg__ = '学不可以已'

from sklearn.datasets import load_digits

digits = load_digits()

print(digits.data.shape)

print(digits.images.shape)

print(digits.target.shape)

print(list(digits.target_names))

data, target = load_digits(return_X_y=True)

print(data.shape)
print(target.shape)

import matplotlib.pyplot as plot

print(type(digits.images))

plot.matshow(digits.images[0])

plot.show()
