#!/usr/bin/python
#coding:utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def showDataStatisticsInfo():
    """
    展示数据的一些描述性统计信息
    count  8.00000   #数量
    mean   4.50000   #均值
    std    2.44949   #标准差
    min    1.00000   #最小值
    25%    2.75000   #下四分位,Q1 序列长度n=8，(1+n)/4=2.25，说明上四分位数在第2.25个位置数，实际上这个数是不存在的，但我们知道这个位置是在第2个数与第3个数之间的。假设从第2个数到第3个数之间是均匀分布的。那么第2.25个数就是第二个数*0.25+第三个数*0.75，即2*0.25+3*0.75=0.5+2.25=2.75。
    50%    4.50000   #中位数,中位数Q2,
    75%    6.25000   #上四分位 Q3, (1+n)/4*3=6.75，这个是个介于第六个位置与第七个位置之间的地方。对应的具体的值是0.75*6+0.25*7=6.25
    max    8.00000   #最大值

    四分位距IQR=Q3-Q1 = 6.25-2.75 = 3.5

    上限=（Q3+1.5IQR，max）取最小,即min(3.5*1.5+6.25,8) = 11.5
    下限=（Q1-1.5IQR ，min)取最大,max(2.25 - 1.5*3.5,1) = 1

    :return:
    """
    num = [1,2,3,4,5,6,7,8]
    res = pd.DataFrame(num).describe()
    # print type(res)
    # print res
    # res.columns:每个columns对应的keys
    # res.shape:形状，（a，b）, index长度为a, columns数为b
    # res.index;.values:返回index列表；返回value二维array
    # res.head();.tail();
    print res.columns[0]
    print res.shape
    print res.index
    print res.values
    print res.head()
    print res.tail()

    # percentiles:设置输出的百分位数，默认为[.25，.5，。75]，返回第25，第50和第75百分位数。
    # eg:df.describe(percentiles=[.8, .9])
    # print pd.DataFrame(num).describe(percentiles=[0.8,0.9])

    # include:默认只输出数值型数据的统计信息(如上),设置参数为'all'则输入的所有列都在输出中,设置为O则只输出离散型变量的统计信息
    # eg:df.describe(include='all')
    # eg:df.describe(include='O')
    # print pd.DataFrame(num).describe(include='all')

"""
单变量异常检测 , 在处理单变量异常时，有一条准则：极端值可以当做异常值
   1.  IQR（四分位距，75分位与25分位的差）。第一种是比25分位值减去IQR*1.5小的值；第二种是比75分为大IQR*1.5的值
   2. Z-scores 得分绝对值大于3的观测值可认为是异常值
"""
""" """
def showPictureDemo():
    """
    同一数轴上，几批数据的箱线图并行排列，几批数据的中位数、尾长、异常值、分布区间等形状信息便昭然若揭。
    如图，可直观得看出第三季度各分公司的销售额大体都在下降。
    ts.plot(kind='line',
       label = 'hehe',
       style = '--g.',
       color = 'red',
       alpha = 0.4,
       use_index = True,
       rot = 45,
       grid = True,
       ylim = [-50,50],
       yticks = list(range(-50,50,10)),
       figsize = (8,4),
       title = 'test',
       legend = True)
        #plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5",axis = 'x')  # 网格
ts.plot(kind='line',
       label = 'hehe',
       style = '--g.',
       color = 'red',
       alpha = 0.4,
       use_index = True,
       rot = 45,
       grid = True,
       ylim = [-50,50],
       yticks = list(range(-50,50,10)),
       figsize = (8,4),
       title = 'test',
       legend = True)
#plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5",axis = 'x')  # 网格
plt.legend()
# Series.plot()：series的index为横坐标，value为纵坐标
# kind → line,bar,barh...（折线图，柱状图，柱状图-横...）
# label → 图例标签，Dataframe格式以列名为label
# style → 风格字符串，这里包括了linestyle（-），marker（.），color（g）
# color → 颜色，有color指定时候，以color颜色为准
# alpha → 透明度，0-1
# use_index → 将索引用为刻度标签，默认为True
# rot → 旋转刻度标签，0-360
# grid → 显示网格，一般直接用plt.grid
# xlim,ylim → x,y轴界限
# xticks,yticks → x,y轴刻度值
# figsize → 图像大小
# title → 图名
# legend → 是否显示图例，一般直接用plt.legend()
# 也可以 → plt.plot()
    :return:
    """
    data = {
        'China': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2500],
        'America': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],
        'Britain': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
        "Russia": [800, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
    }
    df = pd.DataFrame(data)
    df.plot.box(title="Consumer spending in each country")
    plt.grid(linestyle="--", alpha=0.5)
    plt.show()


def showPictureDemo():
    """

    :return:
    """
    data = {
        'China': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2500],
        'America': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],
        'Britain': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
        "Russia": [800, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
    }
    df = pd.DataFrame(data)
    df.plot.box(title="Consumer spending in each country")
    plt.grid(linestyle="--", alpha=0.5)
    plt.show()

if __name__ == '__main__':
    showDataStatisticsInfo()
    showPictureDemo()
    x = ('This will build a very long long '
         'long long long long long long string')


