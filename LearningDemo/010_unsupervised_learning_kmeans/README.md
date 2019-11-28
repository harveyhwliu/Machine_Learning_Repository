## ***特征选择***

1、数据降维（特征选择） ：
	1） 这里的维度 ： 是指 特征的数量   （ 而非数组的维度）

	2） 常用方法
		i、特征选择
			原因：
				冗余： 部分特征的相关度高，容易消耗计算性能

				噪声： 部分特征对预测结果有影响
			是什么：
				特征选择就是单纯地从提取到的所有特征中选择部分特征作为训练集特征，特征在选择前和选择后可以改变值，也可以不改变值，但是选择后的特征维数肯定比选择前小，毕竟我们只选择了其中的一部分特征

			主要方法：三大武器
				Filter（过滤式）： VarianceThreshold（方差为0特征进行删除，）
					sklearn.feature_selection.VarianceThreashold
						VarianceThreshod(threshold = 0.0)  删除所有低于该方差值得特征
						Variance.fit_transform(X)   训练集 差异于threshold的特征将被删除，默认值是保留所有非零方差特征，即删除所有样本中具有相同值得特征。


				Embedded(嵌入式)：正则化、决策树
				Wrapper（包裹式）： 不常用

			其他方法：神经网络


		ii、主成分分析 （PCA）  ： （特征数量减少，特征数据也会被响应的改变）
		        0、使用场景：当特征数据达到上百的时候，考虑数据的简化  ，由于高维度数据之前容易出现的问题：  特征之间通过是相关的  （特征间可能是线性相关的）
			1、本质：PCA是一种分析、简化数据集的技术
			2、目的： 是数据维数的压缩，尽可能降低原数据的维数（复杂的），损失少量信息。
			3、作用：可以消减回归分析或者聚类分析中特征的数量




			4、sklearnAPI：
				sklearn.decomposition
			        PCA(n_components)
					小数 ： 取值范围 【0 - 1】  ，通常设置为：  90% ~95%  保留多少的特征
				        整数： 特征减少到的指定维度的特征数据
		iii.常用算法
			奇异值分解(SVD)、主成分分析(PCA)、因子分析(FA)、独立成分分析(ICA)

		Iiii.降维实例1
			1、案例来源 https://www.kaggle.com/c/instacart-market-basket-analysis/data
			2、Instacart  用户和购买的物品类别的关系
			3、数据集合：
				□ Products.csv    商品信息    product_id,product_name,aisle_id,department_id
				□ Order_products__prior.csv  订单和商品信息   order_id,product_id,add_to_cart_order,reordered
				□ Orders.csv  用户订单信息  order_id,user_id,eval_set,order_number,order_dow,order_hour_of_day,days_since_prior_order
				□ Aisles.csv  商品所属具体物品类别    aisle_id,aisle



			4、处理流程：
				1） 合并多张表内容到1张表中  使用pandas.merge(),按照相同键合并
					® Products.csv   和 Order_products__prior.csv 数据 按照  product_id 合并为一张数据,所有数据包括： roduct_id,product_name,aisle_id,department_id，order_id,add_to_cart_order,reordered
					® 然后和Orders.csv  数据  按照 order_id合并为一张数据，所有数据包括 roduct_id,product_name,aisle_id,department_id，order_id,add_to_cart_order,reordered，user_id,eval_set,order_number,order_dow,order_hour_of_day,days_since_prior_order
					® 最后在和aisles.csv 数据 按照aisle_id 合并为_res，最后得到数据 roduct_id,product_name,aisle_id,department_id，order_id,add_to_cart_order,reordered，user_id,eval_set,order_number,order_dow,order_hour_of_day,days_since_prior_order,aisle
				□ 2） 建立一个  行和列 对应的数据    用户user_id  和  商品 aisle_id   需要使用到交叉表
					® 交叉表
						◊ 交叉分析法是用于分析两个变量之间的相互关系的一种基本数据分析法。
						◊  把统计分析数据制作成二维交叉表格，将具有一定联系的变量分别设置为行变量和列变量，两个变量在表格中的交叉结点即为变量值，通过表格体现变量之间的关系，称为交叉分析法。
						◊ 简单说  我们有一组数据  A,B,C,D,E, 我们这里只关心A,B这两个变量，那么以A为行变量，B为列变量，可以查看A与B的关系了
					® Cross = pd.crosstab(_res["user_id"],_res["aisled_id"])   #获取结果是134维数据，这里很多维数据都是很多的0，因此需要进行PCA进行降维，减少后续计算量
					® Pca = PCA(n_components=0.95)
					® Res = Pca.fit_transform(Cross)
					® Print Res.shape    #此时变成了   （206209,1） 新的变量维度只有1维了




	1. 非监督学习  unsupervised learning     ， 主要方法是： k-means

	2. 聚类过程分析：  指定K值（把数据划分为多少个类别）
		a. 随机在数据中抽取三个样本，当做三个类别的中心点（k1,k2,k3）
		b. 计算其余的点 分别到这三个中心点的距离 ，每个样本有三个（a,b,c）,从中选出距离最近的一个点作为自己的标记，形成三个族群
		c. 分别计算这三个族群的平均值（每一个维度的平均值），把三个平均值与之前的三个旧中心点进行比较
			i. 比如相同：   结局聚类过程
			ii. 不相同时：  把这三个平均值当做新的中心点，重复b,c
			iii.
	3. k-means sklearn的API：
		a. sklearn.cluster.Kmeans
			i. sklearn.cluster.Kmeans(n_clusters=8,init="k-means++")
				1) k-means聚类
				2) n_clusters:开始的聚类中心数量
				3) init: 初始化方法 ，  默认是  "k-means++"

				4) labels_:默认标记的类型，可以和真实值比较（不是值比较）
	4. 实例
		a.
	5. Kmeans性能评估指标
		a. 轮廓系数：
			i.
			ii.

			iii.
			iv. 先计算样本点 到自身类别的点 的距离的平均值  ai
			v. 计算样本点    分别到  其他各个类别的   所有点的距离， 求出对应每个类别的平均值， 取其中最小的为bi
			vi. 则该样本点的轮廓系数为：     sci   = （bi-ai） /  (max(bi,ai))
			vii. 当 bi >>  ai,   sci  等于 1  ， 效果最好
			viii. 当ai  >> bi，sci等于-1，效果最差
			ix. 因此样本的轮廓系数 取值为 【-1，1】，趋近于1效果最好      基本0.1效果比较理想了 ，很难超过  0.7
			x. 对每个样本点都计算轮廓系数 ，  最后求一个平均值   ， 得到整个KMeans聚类模型的轮廓系数

		b. Kmeans 性能评估指标API
			i. sklearn.metrics.silhouette_score
			ii. sklearn.metrics.silhouette_score(X,labels)
			iii. 计算所有样本的平均轮廓系数
			iv. X:  特征值
			v. labels:  被聚类标记的目标值

	6. kmeans 总结：
		a. 特点分析：   采用迭代式算法，直观易懂，  实用
		b. 缺点：   容易收敛到局部最优解 （多次距离）
			i. 多次随机进行聚类
			ii.
注意：  聚类一般做在分类之前


