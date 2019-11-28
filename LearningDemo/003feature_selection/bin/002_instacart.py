#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from sklearn.decomposition import PCA
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
print _res.head(10)f

#建立交叉表
cross = pd.crosstab(_res["user_id"],_res["aisle"])
print cross.head(20)

#获取的结果是一个多维的特征结果，但是很多维数据都是0 ，因此需要进行PCA 降维

pca = PCA(n_components=.095)
res = pca.fit_transform(cross)
print res.shape
