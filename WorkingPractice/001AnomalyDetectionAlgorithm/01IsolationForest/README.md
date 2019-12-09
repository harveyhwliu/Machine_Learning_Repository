## 01 Isolation Forest：孤立森林算法

&emsp;&emsp;南大周志华老师的团队在2010年提出一个异常检测算法Isolation Forest，在工业界很实用，算法效果好，时间效率高，能有效处理高维数据和海量数据，这里对这个算法进行简要总结。<br/>


## Q/A：
###  1. IsolationForest 中用户设置样本中异常点的比例的问题
&emsp;&emsp;IsolationForest算法参数中需要设置一个重要参数contamination，contamination : float in (0., 0.5), optional (default=0.1) 这是最关键的参数，用户设置样本中异常点的比例，但是作为一个无监督算法，这个合理参数的设定在我看来，不亚于要为每个样本打上标签的工作。
举一个实际应用案例，假设我需要对每次输入的序列（长度为N），判断当前时刻输入的数据是否有异常，那么我输入的序列有可能是全部正常的（虽然数据有波动），或者存在异常数据点（数据波动较大），那这种场景下我应该如何使用IForest呢？这种场景下，我想到的解决方案是，重写手写一个IForest，将对异常的判断，改写为满足业务侧需求（配置化异常比阈值threshold：比如异常比阈值定义为：异常值数据 / 序列9分位数 >= threshold）?
请问大家上述问题有没有更优解呢？ 另外，大家对序列的异常检测（简单的低纬度序列）有什么好的实战经验么？<br/>
###  1. 回复
&emsp;&emsp;基于阈值或分位值的做法通常都基于一个前提：特征在训练集和测试集上的分布是一致的，而当测试数据的分布发生变化，或出现大量未知样本，一定会出现误报。解决办法通常是通过重新训练设置阈值(Life Long Learning)，或采用某种方式(如TrAdaBoost、TCA)将训练集上与测试集上的特征分布进行迁移(Transfer Learning)，具体效果因场景而论。<br/>
序列异常检测，比较经典的有统计类方法(三倍方差、t检验)、基于聚类方法(特征聚类)、时间序列DTW对齐、 基于预测的置信度检验等，随着深度神经网络的兴起，LSTM-AutoEncoder也有不错的效果。<br/>



[参考1:<<Isolation Forest算法原理详解>>](https://blog.csdn.net/u013709270/article/details/73436588)<br/>
[参考2: <<IsolationForest算法简介以及Python实现>>](https://blog.csdn.net/slx_share/article/details/87872420)<br/>
[参考3:<<iForest （Isolation Forest）孤立森林 异常检测 入门篇>>](https://www.jianshu.com/p/5af3c66e0410)<br/>
[参考4:<<孤立森林(Isolation Forest)>>](https://blog.csdn.net/extremebingo/article/details/80108247)<br/>
[参考5:<<Python机器学习（1）——异常点检测>>](https://blog.csdn.net/FlySky1991/article/details/80526257)<br/>
[参考6:<<异常检测（二）——IsolationForest>>](https://blog.csdn.net/ye1215172385/article/details/79762317)<br/>
