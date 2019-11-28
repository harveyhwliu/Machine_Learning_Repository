## ***核心总结：***  

	1. 常用的分类模型评估方法：
        -. estimastor.score(x_test,y_test)   一般最常见的使用准确率，即预测结果正确的百分比


  2.   混淆矩阵 ：
       -.  在分类任务下，预测结果（Predicted Condition）与正确标记 （True Condition）之间存在四种不同的组合，构成混淆矩阵  （适合于分类）
       -.
	                                预测结果
				正例	假例
		真实	正例	真正例TP(true positive)	伪反例FN(false negative)
		结果	假例	伪正例FP(false positive)	真反例TN(true negative)

     -. 评估标准
	  -.    准确率：
	         -.   (TP+TN)/(TP+FP+TN+FN)

	  -.    精确率：
	         -.  预测结果为正例样本中真实为正例的比例
	         -.  查的准
	         -.   TP/(TP+FP)


	  -.    召回率：
	         -.  真实为正例的样本中预测结果为正例的比例
	         -.  查的全，对正样本的区分能力
	         -.  TP/(TP+FN)



	-. F1-score:  反映了模型的稳健性
	            -.  F1 = 2TP/(2TP+FN+FP)  = 2*Precision*Recall/(Precision+Recall)

    3. 分类模型评估的API
       -.  sklearn.metrics.classification_report（y_true,y_pre,target_names=None）
               -.  y_true : 真实目标值
               -.  y_pred: 估计器预测目标值
               -.  target_names:  目标类别名称
               -.  return  :  每个类别精确率与召回率


    4. 模型选择与调优：
              -.  交叉验证：所有数据分成n等分(一份作为验证集，其他作为训练集，称为n折交叉验证)   ，常用的n取值为10.
                      -. 目的：让被评估的模型更加的准确  可信
                      -. 流程：
                                1.   把训练样本集  划分为  两部分： 训练集 +验证集
                                2.    反复交叉验证  训练集和验证集  得出模型 n的准确率
                                3. 求模型1到模型n的平均准确率，得到模型的平均值

                                4.  如下是 4折交叉验证


                               5.  例子：
                                     -.  对于KNN，k取值 1，3，5，7 后通过交叉验证，得到平均准确率值最大的k值，则模型更准确


             -. 网格搜索：调参数，也称为超参数搜索
                      -.  通常情况下，有很多参数是需要手动指定的（如k-近邻算法中的K值），这种叫超参数。但是手动过程繁杂，所以需要对模型预设集中超参数组合。每组超参数都采用交叉验证进行评估。最后选出最有参数组合建立模型。
                      -.   如果存在多组参数值，择对多组参数进行笛卡尔积选择后，再进行网格搜索。
				K值	K=1	K=3	K=5
				模型	模型1 	模型2	模型3

                      -.  超参数搜索 - 网格搜索API    (CV  = cross validation)
                            -.    sklearn.model_selection.GridSearchCV(estimator,param_grid=None,cv=None )
                                  -.  对估计器的指定参数值进行详尽搜索
                                  -.  estimator  ： 估计器对象
                                  -.  param_grid :  估计器参数（dict）{"n_neighbors":[1,3,5]}
                                  -.  cv : 指定几折交叉验证
                                  -.  fit:   输入训练数据
                                  -.  score:准确率
                                  -.  结果分析：
                                  -.  best_socre_  :  在交叉验证中验证的最好结果
                                  -.  best_estimator _ : 最好的参数模型
                                  -.  cv_results_:  每次交叉验证后的测试集准确率结果和训练集结果








