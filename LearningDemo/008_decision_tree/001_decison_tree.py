#!/usr/bin/python
#coding:utf-8

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import  DecisionTreeClassifier
from sklearn.tree import export_graphviz

# #全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def  decision_tree():
    """
    决策树模型
    datasets :  http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt
    "row.names","pclass","survived","name","age","embarked","home.dest","room","ticket","boat","sex"
    目标类别是  survived
    :return:
    """
    titan_datas = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    # print titan_datas

    #获取特征值和 目标值
    x = titan_datas[["pclass","age","sex"]]
    y = titan_datas[["survived"]]
    # print x
    # print y

    #缺失值的处理
    x['age'].fillna(x['age'].mean(),inplace=True)


    #分割数据集合    训练集 + 测试集
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)


    #进行  特征工程  特征  -》 类别 - 》onehot编码
    dict_vector = DictVectorizer(sparse=False)

    x_train = dict_vector.fit_transform(x_train.to_dict(orient="records"))   #orient="records"  一行转换成字典

    x_test = dict_vector.transform(x_test.to_dict(orient="records"))

    #onehot 编码  ['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male']  age是数值不进行转换，其他按照特征 0- 1 编码进行转换
    # print  dict_vector.get_feature_names()
    # print x_train
    # print x_test

    #用决策树进行预测：

    # dc = DecisionTreeClassifier()
    #
    # dc.fit(x_train,y_train)
    #
    # #预测准确率
    # print "默认决策树估计器的预测准确率为 ： ",dc.score(x_test,y_test)
    #


    dc = DecisionTreeClassifier(max_depth=5)

    dc.fit(x_train,y_train)

    #预测准确率
    print "最大深度为5的决策树估计器的预测准确率为 ： ",dc.score(x_test,y_test)


    #把决策树  展示出来    - 导出决策树的结构
    export_graphviz(dc,out_file="./tree.dot",feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=女', 'sex=男'])


    #dot  文件转换
    #dot -Tpdf tree.dot -o tree.pdf


def main():
    decision_tree()


if __name__ == "__main__":
    main()
