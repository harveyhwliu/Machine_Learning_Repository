#!/usr/bin/python
#coding:utf8
from pyod.models.knn import KNN  # imprt kNN分类器


def main():

    # 训练一个kNN检测器
    clf_name = 'kNN'
    clf = KNN()  # 初始化检测器clf
    clf.fit(X_train)  # 使用X_train训练检测器clf

    # 返回训练数据X_train上的异常标签和异常分值
    y_train_pred = clf.labels_  # 返回训练数据上的分类标签 (0: 正常值, 1: 异常值)
    y_train_scores = clf.decision_scores_  # 返回训练数据上的异常值 (分值越大越异常)

    # 用训练好的clf来预测未知数据中的异常值
    y_test_pred = clf.predict(X_test)  # 返回未知数据上的分类标签 (0: 正常值, 1: 异常值)
    y_test_scores = clf.decision_function(X_test)  # 返回未知数据上的异常值 (分值越大越异常)

    # 评估预测结果
    print("\nOn Test Data:")
    evaluate_print(clf_name, y_test, y_test_scores)

    # 可视化
    visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred,
        y_test_pred, show_figure=True, save_figure=False)


if __name__ == "__main__":
    main()
