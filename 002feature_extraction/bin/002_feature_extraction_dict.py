#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.feature_extraction import DictVectorizer


##字典特征抽取
def dict_feature_extraction00():
    """
    字典的特征抽取，对字典特征进行特征值化
    :return:
    """
    vectorizer = DictVectorizer(sparse=True)  #产生一个sparse 矩阵
    print vectorizer

    text_context = [{'foo': 1, 'bar': 2000}, {'foo': 32, 'baz': 11}]
    X = vectorizer.fit_transform(text_context)   #
    print X
    print vectorizer.get_feature_names()

def main():
    dict_feature_extraction00()



if __name__ == "__main__":
    main()
