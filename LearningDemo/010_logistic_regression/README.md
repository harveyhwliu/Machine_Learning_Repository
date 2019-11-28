## ***核心总结：***  

	1. 模型的保存和加载
		a. sklearn模型的保存和加载
			i. from  sklearn.externals   import  joblib
				1) 保存模型  ：
					a) joblib.dump(rf,"test.pkl")
				2) 加载模型：
					a) estimator = joblib.load("test.pkl")
				3) 注意：
					a) 文件格式 是   pkl        python (pickle  文件   )

	2. 逻辑回归     -  分类算法
		a. 应用场景 ：
			i. 广告点击率，是否是垃圾邮件，是否患病，金融诈骗，虚假账号
			ii. 解决二分类问题
			iii. 逻辑回归输入(和线性回归一样)：  Z(w) = w0+w1x1+w2x2+.. = wTx
			iv. sigmoid函数   ：将输入转换到 0 - 1
				1)

				2)
				3) 优点：
					® Sigmoid函数的输出映射在(0,1)之间，单调连续，输出范围有限，优化稳定，可以用作输出层。
					® 求导容易。
				4) 缺点：
					® 由于其软饱和性，容易产生梯度消失，导致训练出现问题。
					® 其输出并不是以0为中心的。

			v. 逻辑回归函数：

				e = 2.71
				z = 回归的输入
				h(x)  是 输出的概率值


			vi. 逻辑回归的损失函数 ：
				1) 与线性回归原理相同，但由于是分类问题，损失函数不一样，只能通过梯度下降求解
				2) 对数似然损失函数：
					a)
					b) cost损失的值越小，那么预测的类别准确度越高
					c)  理解：
						i)
						ii)
						iii)   逻辑回归，只判断  属于某个单一类别的概率，比如y为1的概率，则，y=0的概率 = 1-h(x)
							One. 某一类类别少，判定概率值是属于这个类别的概率

						iv)
			vii. sklearn 逻辑回归API
				1) sklearn.linear_model.LogisticRegression
				2)  sklearn.linear_model.LogisticRegression(penalty='l2',C=1.0)
					a) logistic 回归分类器
					b) coef_:  回归系数
					c) 逻辑回归属于线性回归，因此也存在过拟合问题，但是sklearn API  自带正则化
					d) 只能处理二分类问题
			viii. 逻辑回归实例 ：
				1) 数据：
					a)  https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data
					b) 良/ 恶性 乳腺癌肿数据
					c) 数据描述 ：
						i) 699条样本，工11列数据，第一例用于检索的ID，后9列分别是于肿瘤相关的医学特征，最后一列表示肿瘤类型的数值 。
						ii) 包含16个缺失值，用”？“标出
				2) 分类流程：
					a) 网上获取数据   比如使用工具  pandas
					b) 数据的缺失值处理（先替换，再决定删除  或者  写0 等处理方式），标准化（分类问题，目标值可以不进行标准化）
					c) LogisticRegression估计器流程
					d)
			ix. LogisticRegression总结：
				1) 应用：  广告点击率预测，是否患病，金融诈骗，是否是虚假账号      等二分类问题
				2) 优点：  适合需要得到一个分类概率的场景，简单，速度快
				3) 缺点：  不好处理多分类问题
					a) 多分类问题 解决：   神经网络（图像识别 ）
						i) softmax方法 - 逻辑回归在多分类问题上的推广
				4) 和朴素贝叶斯的关系：
					a) 生成模型   和 判别模型   的区别 在于 会否需要先求出先验概率p(c)
						i) 逻辑回归 属于判别模型    ，  朴素贝叶斯 属于生成模型
						ii) k-近邻，决策树，随机森林，神经网络都是判别模型  ，  隐形马尔科夫模型属于  生成模型

					b) 逻辑回归仅能解决二分类问题，朴素贝叶斯 可以处理多分类问题
					c) 应用场景主要是所有二分类需求场景，  朴素贝叶斯仅  使用于  文本分类
					d)  逻辑回归有参数调优 ，比如正则化粒度等 ，朴素贝叶斯不需要参数调优



	1.    误差函数分析：
		a. 均方误差：
			i. 不存在多个局部最低点，只有一个最小值

		b. 对数似然损失：  尽管没有全局最低点，但是效果都是不错的
			i. 多个局部最小值    ，只能接近，无法解决
				1) 优化方案：
					a) 多次随机初始化，多次比较最小值结果，尽量改善
					b) 在求解过程中 ， 调整学习率，尽量改善



