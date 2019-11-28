#!/usr/bin/python
#coding:utf-8

import pandas as pd
from sklearn.datasets import fetch_20newsgroups  #加载大数据集，需要常网上下载的
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import  MultinomialNB
from sklearn.metrics import classification_report


# #全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def navie_beyes():
    _datas = fetch_20newsgroups(subset="all")

    #数据分割为训练 测试样本集

    x_train,x_test,y_train,y_test = train_test_split(_datas.data,_datas.target,test_size=0.2)
    # print type(x_train),len(x_train)
    # print y_train,len(y_train)
    #对数据集 进行特征抽取  （文本特征向量化）   原始文本转化为tf-idf的特征矩
    tf = TfidfVectorizer()


    #以训练集当中的词的列表进行每篇文章重要性统计['a','b','c','d']

    x_train = tf.fit_transform(x_train)
    # print tf.get_feature_names()
    # print x_train.shape,x_train.toarray()

    x_test = tf.transform(x_test)
    # print x_test.shape,x_test.toarray()
    #进行朴素贝叶斯算法的预测

    mlt = MultinomialNB(alpha=1.0)

    mlt.fit(x_train,y_train)

    y_predict = mlt.predict(x_test)

    print "预测的文章类别是",y_predict
    #得出准确率

    _score = mlt.score(x_test,y_test)

    print "准确率为 %.3f"%(_score)

    print  "分类模型的评估标准（每个类别的精确率和召回率）如下：\n"

    # print _datas.keys()
    print classification_report(y_test,y_predict,target_names=_datas.target_names)

def main():
    navie_beyes()


if __name__ == "__main__":
    main()
