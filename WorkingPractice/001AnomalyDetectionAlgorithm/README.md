## 001 异常检测算法

## pyod

### 0. 参考资料：
   -. https://pypi.org/project/pyod/
   -. https://zhuanlan.zhihu.com/p/58313521

### 1. 安装文档：
   -. 安装方式1，通过pip安装

    ```python
    pip install pyod            # normal install
    pip install --upgrade pyod  # or update if needed
    pip install --pre pyod      # or include pre-release version for new features
```

   -. 安装方式2，通过setup文件安装

    ```python
    git clone https://github.com/yzhao062/pyod.git
    cd pyod
    pip install .
```

### 2. API介绍与实例（API References & Examples）
  特别需要注意的是，异常检测算法基本都是无监督学习，所以只需要X（输入数据），而不需要y（标签）。
  PyOD的使用方法和Sklearn中聚类分析很像，它的检测器（detector）均有统一的API。所有的PyOD检测器clf均有统一的API以便使用，完整的API使用参考可以查阅（API CheatSheet - pyod 0.6.8 documentation）：
     -. fit(X): 用数据X来“训练/拟合”检测器clf。即在初始化检测器clf后，用X来“训练”它。
     -. fit_predict_score(X, y): 用数据X来训练检测器clf，并预测X的预测值，并在真实标签y上进行评估。此处的y只是用于评估，而非训练
     -. decision_function(X): 在检测器clf被fit后，可以通过该函数来预测未知数据的异常程度，返回值为原始分数，并非0和1。返回分数越高，则该数据点的异常程度越高
     -. predict(X): 在检测器clf被fit后，可以通过该函数来预测未知数据的异常标签，返回值为二分类标签（0为正常点，1为异常点）
     -. predict_proba(X): 在检测器clf被fit后，预测未知数据的异常概率，返回该点是异常点概率

   当检测器clf被初始化且fit(X)函数被执行后，clf就会生成两个重要的属性：
        -. decision_scores: 数据X上的异常打分，分数越高，则该数据点的异常程度越高
        -. labels_: 数据X上的异常标签，返回值为二分类标签（0为正常点，1为异常点）
   不难看出，当我们初始化一个检测器clf后，可以直接用数据X来“训练”clf，之后我们便可以得到X的异常分值（clf.decision_scores）以及异常标签（clf.labels_）。当clf被训练后（当fit函数被执行后），我们可以使用decision_function()和predict()函数来对未知数据进行训练。



