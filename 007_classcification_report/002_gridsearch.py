#!/usr/bin/python
#coding:utf-8

import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from  sklearn.model_selection import GridSearchCV

def knn():
    _datas = pd.read_csv("/Users/harveyhwliu/scikit_learn_data/facebook-predicting/train.csv")
    # print _datas.head(10)

    #处理数据
    #1、缩小数据,查询数据筛选  dataFrame
    _datas.query("x > 1.0 & x <1.01 & y >2.0 & y < 2.01")


    # print _datas.head(10)
    _time_value = pd.to_datetime(_datas["time"],unit="s")

    #把日期格式 转换成 字典格式

    _time_dict = pd.DatetimeIndex(_time_value)

    #构造特征：
    _datas["year"] = _time_dict.year
    # _datas["month"] = _time_dict.month
    # _datas["day"] = _time_dict.day
    # _datas["hour"] = _time_dict.hour
    # _datas["weekday"] = _time_dict.weekday
    # _datas["minute"] = _time_dict.minute
    # _datas["second"] = _time_dict.second
    # _datas["microsecond"] = _time_dict.microsecond

    #把时间戳特征删除
    _datas = _datas.drop(["time"],axis=1) #pandas  axis =1 是列数据

    # print _datas.head(10)




    #把签到数据少于n个的目标位置删除
    place_count = _datas.groupby("place_id").count()

    # print place_count.head(10)

    tf = place_count[place_count.row_id>3].reset_index() #次数大于3的重新设置一下  reset_index 把索引数据值 转换成列数据

    # print tf.head(10)

    _datas = _datas[_datas["place_id"].isin(tf.place_id)]

    # print _datas.head(10)


    #取出数据中的特征值和目标值
    y = _datas["place_id"]     #获取目标值
    x = _datas.drop(["place_id"],axis=1) #按列进行删除，保留其他数据，去掉标签值  获取特征值

    x = x.drop(["row_id"],axis=1)  #无效的特征值
    # print y
    # print x.head(10)
    #进行数据的分割训练集 和 测试集合
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

    std = StandardScaler()


    #特征工程  对测试集 和 训练集 的特征值  进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    #进行算法流程
    # knn = KNeighborsClassifier(n_neighbors=5)

    # #训练 并预测
    # knn.fit(x_train,y_train)
    #
    # #得到预测结果
    # y_predict = knn.predict(x_test)
    #
    # print "预测的biao为：",y_predict
    # #得出准确率
    # score = knn.score(x_test,y_test)

    #使用网格搜索进行超参数调优
    knn =KNeighborsClassifier()
    gc = GridSearchCV(estimator=knn,param_grid={"n_neighbours":[1,3,5,7,9]},cv=2)#cv 通常设置为10，表示10折交叉验证
    gc.fit(x_train,y_train)

    print "在测试样本集上的准确率为：" ,gc.score(x_test,y_test)
    print "交叉验证中验证的最好结果是： ",gc.best_score_
    print "交叉验证中最好的模型参数是：",gc.best_estimator_
    print "每次交叉校验证的结果是：",gc.cv_results_
    print gc.best_index_
    print gc.best_params_




def main():
    knn()


if __name__ == "__main__":
    main()
