## ***数学知识***  
#### 1.高等数据知识  
   - 微积分 ： 两边夹定理/夹逼定理
      - 说明：
      - ![夹逼定理](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/1_math_jiabidingli.png?raw=true)
   
   - 导数：曲线的斜率，表现了曲线变化的快慢  （标量）
      - *** 二阶导数 *** : 斜率变化的快慢的反应，表征曲线的凸凹性
	  - GIS中，一条二阶导数连续的曲线，称之为“光滑”的
      - 举例：路程一阶导数是速度，二阶导数是加速度
	  - ![常用导数公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/2_daoshu.png?raw=true)

https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/	  
?raw=true

   - 泰勒公式：Maclaurin公式
      - ![泰勒公式](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/3_tyler_gongshi.png?raw=true)
   
   - 方向导数：如果函数z=f(x,y)在点P(X,Y)是可微的，那么，函数在该点P(X,Y)延任一方向L的方向导数都存在,且为：
      - ![方向导数](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/4_fangxiangdaoshu.png?raw=true)  
   
   - 梯度 ：（向量）
      - ![梯度定义](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/5_grad_definition.png?raw=true)  
	  - 性质：
	  - 梯度的方向是函数在该点变化最快的方向
	     - 考虑一座解析式为z=H(x,y)的山，在（x0,y0）的梯度是在该点坡度变化最快的方向（且指向山顶的方向）。
	  - 梯度下降法： *** 坡度变化最快，且指向山底方向  *** 
	     - 思考如下山方向和梯度呈 sita 夹角，下降速度是多少
	  