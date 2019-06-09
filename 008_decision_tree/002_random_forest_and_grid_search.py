#!/usr/bin/python
#coding:utf-8
# -*- coding:UTF-8 -*-

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.tree import export_graphviz

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
    print dict_vector.get_feature_names()
    print x_train
    print " ------ "
    print x_test


    #随机森林    使用网格搜索进行超参数调优
    rf = RandomForestClassifier(n_estimators=10,max_depth=5,)

    #网格搜索  与  交叉验证
    params = {"n_estimators":[10,120,200,300,500,800,1200],"max_depth":[5,8,15,25,30]}
    grid_seach = GridSearchCV(rf,param_grid=params,cv= 2)  # 2折交叉验证

    grid_seach.fit(x_train,y_train)
    print "测试样本集上的准确率是：",grid_seach.score(x_test,y_test)

    print "查看交叉验证的参数模型是：\n",grid_seach.best_estimator_

    best_rf = grid_seach.best_estimator_

    #最优的随机森林参数进行训练 和预测
    best_rf.fit(x_train,y_train)

    print "随机森林估计器的准确率是：",best_rf.score(x_test,y_test)



    #把随机森林  展示出来    - 导出随机森林的结构
    #  这里有点问题，没有解决
    export_graphviz(best_rf,out_file="./forest.dot",feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=女', 'sex=男'])

    #dot  文件转换
    #dot -Tpdf forest.dot -o forest.pdf


def main():
    decision_tree()


if __name__ == "__main__":
    main()
