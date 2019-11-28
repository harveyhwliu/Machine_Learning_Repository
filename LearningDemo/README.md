## ***核心总结：***  
#### 1.机器学习领域图  
   - 模式识别
   - 计算机视觉
   - 数据挖掘
   - 语音识别 ： 科大讯飞
   - 统计学习
   - 自然语言处理 : 谷歌翻译(深度学习)
   
#### 2.机器学习分类
   - 监督学习 ：主要用于预测 - ( 特征1 .. 特征n 标签1;...;特征1 .. 特征n 标签m;) - > 监督学习算法  训练(训练集)/学习（测试集等） 进行预热 
	 - 分类  离散值的预测
	 - 回归  连续值的预测
   - 无监督学习 ： 主要用于聚类/分类  - ( 特征1 .. 特征n;...;特征1 .. 特征n) - > 无监督学习算法  训练(训练集)/学习（测试集等） 
     - 聚类
	 - 关联规则
   - 半监督学习  - ( 特征1 .. 特征n 标签1;...;特征1 .. 特征n) - > 半监督学习算法  训练集有的有标签，有的无标签 
     - TODO
   - 强化学习
     - Q-learning
	 - 时间差学习

#### 3.得分函数
   - 输入是特征， 输出是得分函数，得分函数的未知量就是参数z的各个权重值
      - ![得分函数](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/1_score_function.png?raw=true)  
   - 损失函数的最优化问题
      - 找到参数权重sita 使得损失函数最小的 得分函数
	  - 非凸函数 vs 凸函数  如何求最优化问题
      - ![损失函数的最优化问题](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/2_loss_function.png?raw=true)
	  
#### 4.机器学习算法表
   - sklearn 库 和 算法表(scikit-learn algorithm cheat-sheet)
   - ![机器学习算法表](https://github.com/harveyhwliu/Machine_Learning_Repository/blob/master/001math/image/3_MLA.png?raw=true)
   
