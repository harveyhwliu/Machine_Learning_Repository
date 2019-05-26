## ***核心总结：***  
知识回顾：

算法分类：
	• 监督学习(supervised learning)： 有训练样本集+测试样本集，有标签数据
		○ 分类(classification algorithm)     ： 目标值是连续的
		○ 回归 (regresssion algorithm)     ：目标值是离散的

	• 无监督学习(unsupervised learning)：可以没有测试样本集，没有标签
		○ 聚类算法 ： 不用关心类别，仅需要设计相似度即可，把样本聚类为不同的类别



1、Sklearn 数据集 与 估计器
	1） 数据集划分

		○ Sklearn 数据集
		○ 其他数据集 ： 使用pandas 获取
		○ 数据集划分：
			• 训练样本集： 用于训练，构建模型
			• 测试样本集： 在模型校验时使用，用于评估模型是否有效
			• 常见问题：
				□ 如果训练样本集和测试样本集 是同一份，容易导致模型过拟合
				□ 如果训练样本集过少，容易导致欠拟合
				□ 训练集 ： 测试集   =  7 : 3   |   8 :  2  |  75%  : 25%( 效果验证比较理想的)
				□


	2） sklearn 数据集接口介绍
		○ 数据集划分API：
			• sklearn.model_selection.train_test_split

		○ sklearn.datasets
			• 加载获取流行数据集

			• datasets.load_*()
				□ 获取小规模的数据集，数据包含在datasets里

			• datasets.fetch_*(data_home=None)
				□ 获取大规模数据集，需要从网络上下载，函数的第一个参数是data_home,表示数据集下载的目录，默认是~/scikit_learn_data/

		○ 获取数据集的返回类型：
			• load*和fetch*返回的数据类型datasets.base.Bunch(字典类型)
			• data:特征数据数组，是【n_samples * n_features】的二维numpy.ndarray 数组
			• target:标签数组，是n_samples的一维numpy.ndarray 数组
			• DESCR：数据描述
			• feature_names:特征名，新闻数据，手写数据，回归数据集没有这个feature_names
			• target_names:标签名
			• filename:数据集保存的文件路径

		○ 数据集实例

			•

		○ 数据集进行分割：
			• sklearn.model_selection.train_test_split(*arrays,**options) :
				□ x  数据集的特征值
				□ y 数据值的标签值
				□ test_size  测试集的大小，一般为float
				□ random_state 随机数种子，不同的种子会造成不同的随机采样结果。相同的种子采样结果相同
				□ return 训练集特征集，测试集特征值，训练标签，测试标签（默认随机取,就是乱序的）

		○ 用于分类的大数据集
			• sklearn.datasets.fetch_20newsgroups(data_home=None,subset="train")
				□ subset: "train"或者 “test”,"all",可选，选择要加载的数据集
				□ 训练集的“训练”，测试集的“测试”，两者的“全部”
			• datasets.clear_data_home(data_home=None)
				□ 清除目录下的数据


	3）sklearn 分类数据集

		○


	4）sklearn 回归数据集
		○


	5)  拓展

		○ 转换器：
			• 特征工程 的步骤：
				□ 实例化 （实例化的是一个转换器类  Transformer）
				□ 调用fit_transform(对于文档建立分类词频矩阵，不能同时调用)

				□

			• fit_transform: 输入数据，直接转换
				□ fit: 输入数据，但不做转换数据  (比如计算平均值 ，方差，词频等数据)
				□ transform: 进行数据的转换
				□ fit_transform = fit+transform  （前提是，fit的数据输入和transform的数据输入必须是一样的才行）
			•
			• 转换器 是特征工程的API

		○ 估计器： sklearn 机器学习算法的实现
			• 估计器estimator  是 一个重要的角色，是一类实现了算法的API

			• 用于分类的估计器：
				□ sklearn.neighbors  k - 近邻算法
				□ sklearn.naive_bayes  贝叶斯
				□ sklearn.linear_model.LogisticRegression 逻辑回归
				□ sklearn.tree  决策树 与 随机森林

			• 用于 回归的估计器：
				□ sklearn.linear_model.LinearRegression 线性回归
				□ sklearn.linear_model.Ridge 岭回归
			• 用于聚类的估计器：
				□ pass
		○ 估计器的使用流程：
			• 调用fit    fit(x_train,y_train)  (输入训练样本集的  特征值和目标值)
			• 调用预测 ： y_predict =  predict(x_test)  (获取预测值，输入的是测试特征数据)
			• 预测的准确性： score(x_test,y_test)(输入的是测试的目标值，预测的目标值，获取算法的准确率)
