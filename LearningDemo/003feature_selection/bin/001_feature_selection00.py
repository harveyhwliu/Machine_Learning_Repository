#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.feature_selection import VarianceThreshold


##特征降维   过滤式  方差低于 threshold 的特征将会被删除
def variance_threshold_00():
    """

    :return:
    """
    variance_threshold = VarianceThreshold(threshold=0.0)  # 方差小于0.0的进行过滤特征
    print variance_threshold

    text_context = [[1, 2], [1, 6], [1, 10], [1, 18]]  #这里特别注意是针对列进行处理
    X = variance_threshold.fit_transform(text_context)  #
    print X





def main():
    variance_threshold_00()


if __name__ == "__main__":
    main()
