## ***数学知识***  
#### 1.高等数据知识  
   - 微积分 ： 两边夹定理/夹逼定理
      - 说明：
      - ![夹逼定理](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/1_math_jiabidingli.png?raw=true)
   
   
   ===
   
   - 导数：曲线的斜率，表现了曲线变化的快慢  （标量）
      - 二阶导数 : 斜率变化的快慢的反应，表征曲线的凸凹性
	  - GIS中，一条二阶导数连续的曲线，称之为“光滑”的
      - 举例：路程一阶导数是速度，二阶导数是加速度
	  - ![常用导数公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/2_daoshu.png?raw=true)


   ===
   
   - 泰勒公式：Maclaurin公式
      - ![泰勒公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/3_tyler_gongshi.png?raw=true)
   
   
   ===
   
   - 方向导数：如果函数z=f(x,y)在点P(X,Y)是可微的，那么，函数在该点P(X,Y)延任一方向L的方向导数都存在,且为：
      - ![方向导数](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/4_fangxiangdaoshu.png?raw=true)  
   
   ===
   
   - 梯度 ：（向量）
      - ![梯度定义](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/5_grad_definition.png?raw=true)  
	  - 性质：
	  - 梯度的方向是函数在该点变化最快的方向
	     - 考虑一座解析式为z=H(x,y)的山，在（x0,y0）的梯度是在该点坡度变化最快的方向（且指向山顶的方向）。
	  - 梯度下降法：  坡度变化最快，且指向山底方向  
	     - 思考如下山方向和梯度呈 θ 夹角，下降速度是多少
   
   
   ===
   
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
		 
	
   ===
   
   ===
#### 2.概率公式知识  
   - 条件概率
      - 说明：
      - ![条件概率](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/1_tiaojiangailv.png?raw=true)
   
   ===
   
   - 全概率公式
      - 说明：
      - ![条全概率公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/2_quangailvgongshi.png?raw=true)
   
   ===
   
   - 贝叶斯(Bayes)公式
      - 说明：
      - ![贝叶斯公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/3_bayes.png?raw=true)
   
   ===
   
   
https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/	  
?raw=true

