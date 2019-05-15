## ***数学知识***  
#### 1.高等数据知识  
   - 微积分 ： 两边夹定理/夹逼定理
      - 说明：
      - ![夹逼定理](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/1_math_jiabidingli.png?raw=true)

   - 导数：曲线的斜率，表现了曲线变化的快慢  （标量）
      - 二阶导数 : 斜率变化的快慢的反应，表征曲线的凸凹性
	  - GIS中，一条二阶导数连续的曲线，称之为“光滑”的
      - 举例：路程一阶导数是速度，二阶导数是加速度
	  - ![常用导数公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/2_daoshu.png?raw=true)

   
   - 泰勒公式：Maclaurin公式
      - ![泰勒公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/3_tyler_gongshi.png?raw=true)

   
   - 方向导数：如果函数z=f(x,y)在点P(X,Y)是可微的，那么，函数在该点P(X,Y)延任一方向L的方向导数都存在,且为：
      - ![方向导数](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/4_fangxiangdaoshu.png?raw=true)  

   
   - 梯度 ：（向量）
      - ![梯度定义](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/5_grad_definition.png?raw=true)  
	  - 性质：
	  - 梯度的方向是函数在该点变化最快的方向
	     - 考虑一座解析式为z=H(x,y)的山，在（x0,y0）的梯度是在该点坡度变化最快的方向（且指向山顶的方向）。
	  - 梯度下降法：  坡度变化最快，且指向山底方向  
	     - 思考如下山方向和梯度呈 θ 夹角，下降速度是多少

   
   - 凸函数 ： 导数递增的  二阶导数>0
      - ![梯度定义](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/6_tuhanshudingyi.png?raw=true)  
	  - 解读：
	     - 琴森不等式 ： f(Ex) <= Ef(x)  应用最广
		 - 
	  - 性质:
         - f(λx1 +(1-λ)x2) <= λf(x1) + (1-λ)f(x2)	  
	     - f是凸函数，则满足：f(θ1x1+...+θnxn)<=θ1f(x1)+...+θnf(xn),其中 0<= θi <=1,θ1+...+θn = 1
		 - 意义 可以在确定函数的凹凸性之后，对函数进行不等式替换
		 
	  - 判定：
	     - 定理f(x) 在区间[a,b]上连续，在（a,b）内二阶可导，那么：
		    - 如果f"(x) >0  则f(x)是凸函数
			- 如果f"(x) <0  则f(x)是凹函数
	     - 简单说： 一元二阶可微的函数在区间上是凸函数，当且仅当它的二阶导数是非负的
		 

#### 2.概率公式知识  
   - 条件概率
      - 说明：P(AB)为事件AB的联合概率，P(A|B)为条件概率，表示在B条件下A的概率，P(B)为事件B的概率。
	  - 理解：事件A和事件B都是同一实验下的不同的结果集合，事件A和事件B一般是有交集的AB，若没有交集（互斥），则条件概率为0.
	  - 推广：对于任何正整数n≥2，当P(A1A2...An-1) > 0 时，有：P(A1A2...An-1An)=P(A1)P(A2|A1)P(A3|A1A2)...P(An|A1A2...An-1)
      - ![条件概率](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/1_tiaojiangailv.png?raw=true)
 
   
   - 全概率公式
      - 说明：
	  - 理解：全概率是条件概率的应用，某一实验所有的可能的样本的集合为Ω，圆圈A代表事件A所能囊括的所有样本，把总集合Ω分为n个小集合，依次为B1、B2···Bn，这些小集合两两互斥，那么显然，A的样本数目可以通过与Bi的交集来获得，也即P(A)=P（A∩B1的样本数）+P（A∩B2的样本数）+····+P（A∩Bn的样本数），再用条件概率P（AB） = P(A/B)*P(B)替换即可
      - ![条全概率公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/2_quangailvgongshi.png?raw=true)
   
   
   - 贝叶斯(Bayes)公式
      - 说明：贝叶斯公式是建立在条件概率的基础上寻找事件发生的原因（即大事件A已经发生的条件下，分割中的小事件Bi的概率），设B1,B2,...是样本空间Ω的一个划分，Bi 常被视为导致试验结果A发生的”原因“，P(Bi)(i=1,2,...)表示各种原因发生的可能性大小，故称先验概率；P(Bi|A)(i=1,2...)则反映当试验产生了结果A之后，再对各种原因概率的新认识，故称后验概率。
      - ![贝叶斯公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/3_bayes.png?raw=true)
 
   
   - 常见的概率分布
      - 说明：
      - ![概率分布](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/4_gailvfenpu.png?raw=true)
      - ![概率分布](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/7_fenbu1.png?raw=true)
      - ![概率分布](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/8_fenbu2.png?raw=true)
   

#### 3、概率统计与机器学习的关系
   - 统计估计的是分布，机器学习训练出来的是模型，模型可能包含了多个分布
   - 训练与预测过程的一个核心评价指标就是模型的误差
   - 误差本身就可以是概率的形式，与概率紧密相关
   - 对误差的不同定义方式就演化了不同的损失函数的定义方式


#### 4、常见统计量
   - 期望： 概率加权下的“平均值”  （一个随机变量）
      - 离散型： E(X) = ∑ xipi
      - 连续性：E(X) = ∫xf(x)dx
   -方差：  （一个随机变量）
      - Var(x) = E{[X-E(X)]²} = E(X²)-E²（X）
	  - Var(c) = 0
	  - Var(x+C) = Var(x)
	  - Var(Kx) = k²Var(x)
	  - X和Y独立，则Var(X+Y) = Var(X)+Var(Y)
	  - 标准差为 方差的平方根
   - 协方差 ： （两个随机变量的线性关系）
      - Cov(X,Y) = E{[X-E(X)][Y-E(Y)]}
      - Cov(X,Y) =Cov(Y,X)
      - Cov(aX+b,cY+d) =acCov(Y,X)	  
      - Cov(X1+X2,Y) =Cov(X1,Y)+Cov(X2,Y)
	  - Cov(X,Y)=E(XY)-E(X)E(Y)
   - 相关系数：
      - 其取值在[－1, 1]之间。相关性η = 1时称为“完全线性相关”（相关性η = －1时称为“完全线性负相关”），此时将Yi对Xi作Y-X 散点图，将得到一组精确排列在直线上的点；相关性数值介于－1到1之间时，其绝对值越接近1表明线性相关性越好，作散点图得到的点的排布越接近一条直线
      - 两个向量的cosΘ
	  - r = (COV(X,Y))/√￣(VAR(X)VAR(Y)) = (a . b)/(||a|| .||b||) = cosΘ

	  
#### 5、矩阵
   - 矩阵运算  ： 列向量的线性组合
   - SVD： 矩阵DATA = 上三角矩阵U*可逆阵∑*（V ）t
   - ![svd](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/svd.bmp?raw=true)