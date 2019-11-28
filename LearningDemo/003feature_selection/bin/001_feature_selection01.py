#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.decomposition import PCA


##特征降维   pca 主成分分析
def pca_00():
    """pca

    :return:
    """
    pca = PCA( n_components = 0.95 )  # 保留95%的特征
    print pca

    text_context = [[1, 2,3,4,5], [1, 6,3,4,5], [1, 10,3,4,5], [1, 18,3,4,5]]  #这里特别注意是针对列进行处理
    X = pca.fit_transform(text_context)  #
    print X



def pca_02():
    """

    :return:
    """
    pca = PCA( n_components = 2 )  # pca 降维到2 维特征
    print pca

    text_context = [[1, 2,3,4,5], [1, 6,3,4,5], [1, 10,3,4,5], [1, 18,3,4,5]]  #这里特别注意是针对列进行处理
    X = pca.fit_transform(text_context)  #
    print X




def main():
    pca_00()
    pca_02()


if __name__ == "__main__":
    main()
