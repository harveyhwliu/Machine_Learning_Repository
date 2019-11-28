#!/usr/bin/python
#coding:utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
# from sklearn.linear_model import LogisticRegressionCV  #LogisticRegressionCV是交叉验证版本的逻辑回归
from sklearn.metrics import classification_report  #分类模型效果评估 - 召回率


# #全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def  logistic_regression_func():
    """
    逻辑回归方法 解决  是否有癌症的预测
    :return:
    """

    #获取数据
    """
       #  Attribute                     Domain
       -- -----------------------------------------
       1. Sample code number            id number
       2. Clump Thickness               1 - 10
       3. Uniformity of Cell Size       1 - 10
       4. Uniformity of Cell Shape      1 - 10
       5. Marginal Adhesion             1 - 10
       6. Single Epithelial Cell Size   1 - 10
       7. Bare Nuclei                   1 - 10
       8. Bland Chromatin               1 - 10
       9. Normal Nucleoli               1 - 10
      10. Mitoses                       1 - 10
      11. Class:                        (2 for benign, 4 for malignant)
    """
    #定义数据特征
    _datas_column = ["Sample code number","Clump Thickness","Uniformity of Cell Size","Uniformity of Cell Shape","Marginal Adhesion","Single Epithelial Cell Size","Bare Nuclei","Bland Chromatin","Normal Nucleoli","Mitoses","Class"]

    #pandas默认第一行数据是属性标签，这里需要手动指定属性标签，通过names参数传递给pandas
    _datas = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
                         names=_datas_column)
    # print _datas
    #pandas 进行数据预处理  replace(to_replace="",value="") , dropna():返回数据
    _datas = _datas.replace(to_replace="?",value=np.nan)
    # print _datas

    #填充 fillna    删除 dropna
    _datas = _datas.dropna()
    print _datas

    #分割数据集 到 训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(_datas[_datas_column[1:10]],_datas[_datas_column[10]],test_size=0.25)
    print

    #进行标准化处理   特征值
    #这里是分类问题，只有正例反例两种（4  和  2），因此不需要进行标准化
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    #estimator预测
    #使用逻辑回归方式  预测结果

    logistic_regression_estimator =  LogisticRegression(penalty='l2',C=1.0)
    logistic_regression_estimator.fit(x_train,y_train)
    print "逻辑回归的参数是：",logistic_regression_estimator.coef_

    print "逻辑回归的准确率为：",logistic_regression_estimator.score(x_test,y_test)

    y_predict = logistic_regression_estimator.predict(x_test)
    print "逻辑回归的召回率是：",classification_report(y_test,y_predict,labels=[2,4],target_names=["good","bad"])

def main():
    logistic_regression_func()

if __name__ == "__main__":
    main()
