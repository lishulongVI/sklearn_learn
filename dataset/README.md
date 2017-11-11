# machine learning

```
设置国内镜像

(/Users/lishulong/data_center_env) lishulongdeMBP:Sklearn_demo lishulong$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
(/Users/lishulong/data_center_env) lishulongdeMBP:Sklearn_demo lishulong$ conda config --set show_channel_urls yes

remove .....
conda config --remove channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'

```

## Sklearn (Scikit learn)

### 常用函数


  | application | algorithm
---|---|---
classification (分类)| 异常检测，图像识别 | KNN,SVM
clustering （聚类））| 图像分割，群体划分 | K-Means,谱聚类
regression (回归)）| 价格预测，趋势预测| 线性回归,SVR
dimension reduction（降维）） | 可视化 | PCA,NMF

### 机器学习 周志华 西瓜书
### PRML phD
### machine learning 吴恩达
### cs231n lifeifei 视觉
### Reinforcement Learning
[课程主页](http://t.cn/Rw0rwtU/)

## Sklearn 库的安装

<html>
sklearn 库是在 numpy scipy matplotlib的基础上开发而成的
<br>
在安装Sklearn之前 先安装 依赖
</html>

```
Numpy: nmerical python 是一个开源的Python科学计算库

Scipy:是sklearn 库的基础，他是基于numpy的一个集成了多种数学算法的函数的python 模块。

matplotlib:是基于numpy的一套Python工具包提供了大量的数据绘图工具
```

安装 numpy scipy matplotlib sklearn

conda install is NAN pip install

## sklearn 库中的标准数据集及基本功能

数据集名称 | 调用方式| 适用算法 | 数据规模
---|---|---|---
波士顿房价数据集 | load_boston()| 回归|506*13
鸢尾花数据集 | load_iris()| 分类|150*4
糖尿病 | load_diabetes()| 回归|442*10
手写数字 | load_figits()| 回归|5060*64
olivetti脸部图像 | fetch_olivetti_faces()| * |-
新闻分类 | fetch_20newsgroups()| -|-
带标签的人脸数据集 | fetch_lfw_peopele()| 回归|-
路透社新闻语料数据集 | fetch_rcv1()| 分类|506*13


## sklearn 库的基本功能

sklearn 库 分为六大部分，分别用于完成分类任务，回归任务，聚类任务，降维任务，模型选择以及数据的预处理

### 分类任务

支持向量机 svm

回归任务

聚类任务
K-means

降维任务
主成分分析

实例对算法的使用方式进行介绍
# 无监督学习


```
无标签的数据学习数据的分布或数据与数据之间的关系，被称作为无监督学习

监督学习和无监督学习得最大区别在于数据是否有标签
无监督学习最常应用的场景是聚类和降维

```

### 聚类
根据数据的相似性 将数据分为多类的过程。

欧式距离
欧式空间两点的距离

曼哈顿距离 二维

马氏距离

夹角余弦

sklean 聚类

cluster 这个模块

#### sklearn.cluster


算法名称| 参数 | 可扩展性 | 相似性度量
---|---|---|---
K-means | 聚类个数 | 大规模数据| 点间距离
DBSCAN | 邻域大小 | 大规模数据 | 点间距离
Gaussian Mixtures | 聚类个数以及其他超参| 复杂度高，不适合处理大规模数据| 玛氏距离
Brich | 分支银子，阀值等其他超参| 大规模数据|两点间的欧式距离

