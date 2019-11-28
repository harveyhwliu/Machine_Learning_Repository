## ***核心总结：***  


    1.  认识决策树：
        -.   决策树是一种树形结构，其中每个内部节点表示一个属性上的测试，每个分支代表一个测试输出，每个叶节点代表一种类别。
        -.   决策点，是对几种可能方案的选择，即最后选择的最佳方案。如果决策属于多级决策，则决策树的中间可以有多个决策点，以决策树根部的决策点为最终决策方案
        -.   状态节点，代表备选方案的经济效果（期望值），通过各状态节点的经济效果的对比，按照一定的决策标准就可以选出最佳方案。由状态节点引出的分支称为概率枝，概率枝的数目表示可能出现的自然状态数目每个分枝上要注明该状态出现的概率。
        -.   结果节点，将每个方案在各种自然状态下取得的损益值标注于结果节点的右端。
        -.




    2.  信息论基础  - 银行贷款分析
        -.   香农   信息的单位 ： 比特   （计算机中的比特的来源  ）
        -.   信息熵 ： H，单位比特，计算公式  ： H（x） =  - ∑ (P（x）* logP（x))
        -.   信息和消除不确定是相联系的，信息熵大，不确定性大，信息熵小，不确定小 。
        -.   信息增益： 决策树的划分依据之一

             -.   特征A  对 训练数据集D   的  信息增益g(D,A) ,定义  为  集合D  的信息熵 H(D) 与  特征A  给定条件下D的  信息条件熵H（D|A）之差。

             -.   g(D,A) = H(D) - H(D|A)   =  初始信息熵大小  -  特征A带来的信息熵大小

             -.   信息增益  表示 得知 特征X  的信息而 使得  类Y 的  信息不确定性减少 的程度

             -.   信息增益的计算


                     -.  举例：



                      -.   类别只有2个，总的信息熵大小是：   H(D) = -∑（p(x)*log (p(x))） = -(  (9/15) *log( 9/15 ) + (6/15)*log(6/15)  )
                      -.   信息增益 ：  g(D,年龄) = H（D） -  H(D | A)  =   -(  (9/15) *log( 9/15 ) + (6/15)*log(6/15)  )   -  ( - (  5/15 * H(青年)  + 5/15 * H(中年)  +5/15*H(老年)) )
                              -.  H(青年) = -( 3/5 *log(3/5) +2/5*log(2/5))
                              -.  H(中年) = -( 3/5 *log(3/5) +2/5*log(2/5))
                              -.  H(老年) = -( 4/5 *log(4/5) +1/5*log(1/5))
                      -.  以此可以求出  年龄，工作，房子，信贷 4个特征 对训练样本集D 的信息增益g(D,年龄)，g(D,工作)，g(D,房子)，g(D,信贷)，并找到信息增益最大的特征，为 最优的特征。


    3.  决策树的生成
        -.   常见的决策树使用的算法：
               -. ID3 :  信息增益最大的准则
               -. C4.5:  信息增益比  最大的准则
               -. CART:
                      -.  回归树 ： 平方误差最小
                      -.  分类树  ： 基尼系数  最小的准则，在sklearn 中可以选择划分的原则
                           -. 基尼系数的 划分  粒度更细


        -. sklearn 决策树的API
               -.  class.sklearn.tree.DecisionTreeClassifier(criterion='gini',max_depth=None,random_state=None)
               -.  决策树分类器
               -.  criterion  :  默认是“gini”基尼系数， 也可以选择信息增益的熵  ‘entropy’
               -.  max_depth : 树的深度大小   （这个会影响对测试集的预测结果）
               -.  random_state : 随机数种子

               -.  method:
               -.  decision_path :  返回决策树的路径

              -.  决策树的结构 、 本地保存
                   -.  sklearn.tree.export_graphviz()  该函数能够导出DOT格式
                       -.  tree.export_graphviz(estimator,out_file="tree.dot",feature_name=["",""])     feature_name 是（比如是one-hot编码后的）特征结合
                       -.
                   -.   工具 ： 能工将dot文件转换为pdf 、png
                        -.   安装graphviz    brew install  graphviz
                   -.   运行命令  dot -Tpng tree.dot -o tree.png

        -.
        -.
        -.

     4.  泰坦尼克号乘客生存分类
        -.    datasets :  http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt
        -.   处理流程  ：
             -.   pd 读取数据 pd.read_csv()
             -.   选择有影响的特征，处理缺失值
             -.  进行特征工程，pd转换成字典，特征抽取 x_train.to_dict(orient="records")
             -.  决策树估计流程
             -.
             -.
     5.  决策树的优缺点  以及 改进
        -.    优点 ：
             -.   简单的理解和解释，决策树依据可视化
             -.   需要很少的数据准备，其他技术通常需要数据归一化
             -.
        -.   缺点 ：
             -.   决策树学习者可以创建不能很好地推广数据的过于复杂的数，称之为  过拟合


        -.   改进 ：  解决过拟合
             -.   剪枝  CART 算法（决策树API当中已经实现，随机森林参数调优有相关介绍）
                   -.  DecisionTreeClassifier 定义的时候有两个参数  ： min_samples_split=2 和min_samples_leaf=1,   通过调整着两个参数，保证训练样本点samples 值小于一定值则不进行继续决策树分裂了。

             -.   随机森林
             -.
        -.   企业重要决策，由于决策树很好的分析能力，在决策过程应用较多

     6.  集成学习方法 - 随机森林
        -.     随机森林：

             -.   集成学习方法  通过 建立几个模型组合 来解决单一预测问题。 它的工作原理是 生成多个分类器 /模型，各自独立地学习和作出预测。这些预测最后结合成单预测，因此 优于 任何一个单分类的做出预测  。

             -.   定义：  在机器学习中，随机森林就是一个包含了多个决策树的分类器，并且其输出的类别是由个别树输出的类别的众数而定。

             -.   如果训练了5个树， 其中4个树的结果是True,1个树的结果是False,那么最后的结果是True

             -.   随机森林建立多个决策树的过程：  随机有放回的抽取  ： bootstrap 抽样
                  -.  单个树的建立过程 ：
                            -.  随机在N个样本当中选择一个样本，重复N次，样本有可能重复。

                            -.  随机在M个特征中选出m个特征，m<< M 建立决策树
                            -.  采用bootstrap 抽样   （随机有放回的抽样）
                  -.   为什么要  随机抽样训练集？

                            -.  如果不进行随机抽样，每颗树的训练集都一样，那么最终的训练处的树分类结果也是完全一样的

                  -.  为什么要有放回地抽样？

                            -.  如果不是有放回的抽样，那么每颗树的训练样本都是不同的，都是没有交集的，这样每棵树都是有“偏好的”，也就是说每棵树训练出来都是有很大的差异的；而  随机森林最后分类取决于多棵树（若分类器）的投票表决。

        -.    随机森林的API
             -.  class sklearn.ensemble.RandomForestClassifier(n_estimators=10,criterion="gini",max_depth=None,bootstrap=True,random_state=None)
                       -.  随机森林分类器
                       -.  n_estimators : interger,  optional   (default=10)  森林里面树木数量  120，200，300，500，800，1200
                       -.  criteria   : string  可选（default = “gini”）,分割特征的测量方法
                       -.  max_depth :  interger 或者None ,可选 （默认 = 无） ， 树的最大深度  5，8，15，25，30
                       -.  max_features="auto"，每个决策树的最大特征数量
                       -.  IF “auto ”, "max_features = sqrt(n_features)"
                       -.  IF “sqrt”, "max_features = sqrt(n_features)"
                       -.  IF “log2”, "max_features = log2(n_features)"
                       -.  IF “None”, "max_features = (n_features)"
                       -.  bootstrap : boolean , optional ( default=True) , 是否在构建树时，使用放回抽样
                       -.
                       -.

             -.   随机森林的优点：
                       -.  在当前所有算法中，具有很好的准确率
                       -.  能够有效地 运行在大数据集上
                       -.  能够处理具有高维特征的输入样本，且不需要降维
                       -.  能够评估各个特征在分类问题上的重要性

             -.   随机森林的缺点：
                       -.   随机森林在某些噪音较大的分类或回归问题上会过拟合
                       -.   对于有不同取值的属性的数据，取值划分较多的属性会对随机森林产生更大的影响
             -.
