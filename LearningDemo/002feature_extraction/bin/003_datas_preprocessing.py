#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
import numpy as np


##数据数据预处理  归一化
def normalization_test():
    """
    对特征向量进行归一化  默认 归一化被  映射到   【0-1】
    作用于 每一列

    X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    X_scaled = X_std * (max - min) + min

    :return:
    """
    min_max_scaler = MinMaxScaler()  # 默认 归一化被  映射到   【0-1】
    print min_max_scaler

    text_context = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]  #这里特别注意是针对列进行处理
    X = min_max_scaler.fit_transform(text_context)  #
    print X

##数据数据预处理  归一化
def normalization_test01():
    """
    对特征向量进行归一化  通过 feature_range  指定 归一化被  映射到   区间
    作用于 每一列

    X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    X_scaled = X_std * (max - min) + min

    :return:
    """
    min_max_scaler = MinMaxScaler(feature_range=(1,2))  # 通过指定feature_range指定 归一化后 值域  映射到   【1-2】
    print min_max_scaler

    text_context = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]  #这里特别注意是针对列进行处理
    X = min_max_scaler.fit_transform(text_context)  #
    print X


##数据数据预处理  标准化
def normalization_test03():
    """
    对特征向量进行标准化  将数据进行变化到  均值为0 标准差为1的附近
    作用于 每一列

    X_std = (X - mean)) / (deta))

    :return:
    """
    std_scaler = StandardScaler()
    print std_scaler

    text_context = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]  #这里特别注意是针对列进行处理
    X = std_scaler.fit_transform(text_context)  #
    print X

    print std_scaler.mean_
    print std_scaler.scale_

##数据数据预处理  缺失值
def normalization_test04():
    """
    缺失值处理
    axis =0  按照行列理   axis =1 按照行处理  和 pandas 处理的一样的
    :return:
    """
    imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)  #nan NaN
    print imputer

    text_context = [[-1, 2], [-0.5, 6], [np.nan, 10], [1, 18]]  #这里特别注意是针对列进行处理
    X = imputer.fit_transform(text_context)  #
    print X




def main():
    normalization_test()
    normalization_test01()
    normalization_test03()
    normalization_test04()

if __name__ == "__main__":
    main()
