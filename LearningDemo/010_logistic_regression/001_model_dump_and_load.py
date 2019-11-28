#!/usr/bin/python
#coding:utf-8

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from sklearn.metrics import mean_squared_error

# #全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def  modle_dump_for_lr():
    """
    线性回归  使用 正规方程 方法 求解,然后把模型保存下来
    :return:
    """

    #获取数据
    _boston_datas  = load_boston()

    #分割数据集 到 训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(_boston_datas.data,_boston_datas.target,test_size=0.25)

    #进行标准化处理   特征值   +  目标值  都需要进行标准化处理  ，实例化两个标准化API
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1,1))  #这个版本要求（0.19）输入是二维数据，0.18不要求

    #estimator预测
    #使用正规方程方式预测结果
    lr = LinearRegression()
    lr.fit(x_train,y_train)
    print "采用正规方程方法，获的的线性回归模型的回归系数为：",lr.coef_

    print  "进行LR模型的保存："
    joblib.dump(lr,"./cache/linear_regression.plk")




def model_use_cache_for_lr():
    """
    线性回归   直接预测房子价格    使用离线保存的模型进行预测
    :return:
    """
#获取数据
    _boston_datas  = load_boston()

    #分割数据集 到 训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(_boston_datas.data,_boston_datas.target,test_size=0.25)

    #进行标准化处理   特征值   +  目标值  都需要进行标准化处理  ，实例化两个标准化API
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1,1))  #这个版本要求（0.19）输入是二维数据，0.18不要求

    #estimator预测
    #使用正规方程方式预测结果,模型从 缓存文件中获取
    lr = joblib.load("./cache/linear_regression.plk")
    lr.fit(x_train,y_train)
    print "采用正规方程方法，获的的线性回归模型的回归系数为：",lr.coef_

    #预测测试集的房子价格
    y_predict = lr.predict(x_test)   #进行了标准化，因此预测结果都很小，需要进行转换回来

    y_predict_new  = std_y.inverse_transform(y_predict)

    print "采用正规方程方法，测试样本的房子预测价格是： ",y_predict_new
    print "采用正规方程方法的模型均方误差为：",mean_squared_error(std_y.inverse_transform(y_test),y_predict_new)






def main():
    # modle_dump_for_lr()
    print "-----------------"
    model_use_cache_for_lr()

if __name__ == "__main__":
    main()
