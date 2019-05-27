## ***核心总结：***  

1、分类依据：
	离散型数据，通过K个“邻居”的标签来确定 测试数据的类别
	相似的样本，特征之间的值应该是相近的

2、定义：
	• 如果一个样本在特征空间中的K个最相似的（即特征空间中最邻近的样本中的大多数属于某一个类别），则该样本也属于这个类别。
	• KNN算法最早是由Cover和Hart提出的一种分类算法


3、距离公式：
	• 欧式距离： 两个样本a（a1,a2,a3）,b(b1,b2,b3)的距离的平方是  （a1-b1)^2 + (a2-b2)^2+(a3-b3)^2
	• 1


4、k-近邻算法注意点：
	• 1） 需要对数据进行标准化处理
	• 2）K的取值问题


5、sklearn k-近邻算法的API
	• sklearn.neighbors.KNeighborsClassifier(n_neighbors=5,algorithm='auto')
		○ n_neighbors: int 默认值是5，k_neighbors查询默认使用的邻居数
		○ algorithm:{"auto","ball_tree","kd_tree","brute"}，可选用与计算最近邻居的算法，“ball_tree”将会使用BallTree,"kd_tree"将使用KDTree,"auto"将尝试根据传递给fit方法的值决定最合适的算法（不同实现方式影响效率）
6、实例分析：
	• Kaggle: https://www.kaggle.com/c/facebook-v-predicting-check-ins/rules
	•
	• 特征值确定 ： x,y坐标 ,accuracy,time,
	• 目标确定： place_id
	• 问题确定： 分类问题  -  k-近邻算法（需要标准化处理）
	• 特征工程：
		○  0<x <10, 0<y<10
		○ time 时间戳需要处理   =》 把时间戳转换为 年， 月，日，周，时，分，秒等新的特征
		○ 签到数较少的点，直接ignore
			§ _datas.query("x > 1.0 & x <1.25 & y >2.5 & y < 2.75")
	• 数据处理：
		○ 1、缩小数据寄范围
			§ _datas.query("x > 1.0 & x <1.25 & y >2.5 & y < 2.75")
		○ 2、处理日期数据：
			§ time 时间戳需要处理   =》 把时间戳转换为 年， 月，日，周，时，分，秒等新的特征
			§ Pandas.to_datetime
			§ Pandas.DatetimeIndex
		○ 3、增加分割的日期数据
			§ _datas["day"] = _time_dict.day
			§  _datas["hour"] = _time_dict.hour
			§ _datas["weekday"] = _time_dict.weekday
		○ 4、删除没有用的数据
			§ DataFrame.drop()       _datas.drop(["time"],axis=1) #pandas  axis =1 是列数据
		○ 5、将签到数位置 少于N的用于删除
			§ _datas 实际是pandas中的DataFrame
			§     place_count = _datas.groupby("place_id").count()
			§     tf = place_count[place_count.row_id>3].reset_index() #次数大于3的重新设置一下  reset_index 把索引
			§     _datas = _datas[_datas["place_id"]].isin(tf.place_id)






	• 模型评估：
		○ 如果score很低，那么是否有其他不相干特征没有删除的？是否需要进行标准化了？









