#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score  #轮廓系数
import matplotlib.pyplot as plt

base_path="~/Desktop/instacart-market-basket-analysis/"

#读取四张表内容
prior = pd.read_csv(base_path+"order_products__prior.csv")
product = pd.read_csv(base_path+"products.csv")
orders = pd.read_csv(base_path+"orders.csv")
aisles = pd.read_csv(base_path+"aisles.csv")

#合并为一张表
_t = pd.merge(prior,product,on=["product_id","product_id"])
_t = pd.merge(_t,orders,on=["order_id","order_id"])
_res = pd.merge(_t,aisles,on=["aisle_id","aisle_id"])

#查看数据
# print _res.head(10)

#建立交叉表
cross = pd.crosstab(_res["user_id"],_res["aisle"])
# print cross.head(20)

#获取的结果是一个多维的特征结果，但是很多维数据都是0 ，因此需要进行PCA 降维

pca = PCA(n_components=.095)
res = pca.fit_transform(cross)
# print res.shape


#取其中的一部分数据进行计算（原始样本太大，计算耗时太长时间）
x = res[:1000]


#KMeans 聚类过程
km = KMeans(n_clusters=5)
km.fit(x)

y_predict = km.predict(x)

print "kmeans聚类标签为：",y_predict

#Kmeans 的效果评估，轮廓系数

print "Kmeans聚类效果评估，轮廓系数为：",silhouette_score(x,y_predict)

#显示聚类的结果
plt.figure(figsize=(10,10))
#颜色效果如下：
color_l = ["blue","orange","green","purple","red"]

#将目标值替换成对应颜色标记
colored = [color_l[i] for i in y_predict]

#画出某个特征和  目标值的  聚类关系图
plt.scatter(x[ : , 1],x[ : , 20],color=colored)

plt.xlabel("所有样本的第1个特征")
plt.ylabel("所有样本的第20个特征")
plt.show()

