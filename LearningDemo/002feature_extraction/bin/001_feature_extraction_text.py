#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
import json
import jieba

#文本特征抽取
#https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer
def text_feature_extraction00():
    """
    文本内容的特征抽取
    :return:
    """
    vectorizer = CountVectorizer()
    print vectorizer

    text_context = [
         'This is the first document.',
         'This is the second second document.',
         'And the third one.',
         'Is this the first document?',
     ]
    X = vectorizer.fit_transform(text_context)   #标准化
    print vectorizer.get_feature_names()         #1、统计所有文章当中的所有的词，重复的只看做一次   词的列表
                                                 #2、 对每篇文章，在词的列表里面进行统计每个词出现的次数
                                                 #3、单个字母不统计
    print X,X.toarray()
    print



def text_feature_extraction001():
    """
    中含有文本内容的特征抽取
    :return:
    """
    vectorizer = CountVectorizer()
    print vectorizer

    text_context = [
         '对中文进行处理.',
         '人生 苦短,是的。',
         '我要用 python，好的',
     ]
    X = vectorizer.fit_transform(text_context)   #标准化
    print json.dumps(vectorizer.get_feature_names(),ensure_ascii=False)   #1、对中文文本特征抽取，默认是按照空格分割的
                                                                          #2、为了提高特征提取准确性，需要 分词
                                                                          #3、分词采用jieba分词

    print X,X.toarray()
    print



def text_feature_extraction002():
    """
    对含有中文文本内容的特征抽取，先采用jieba分词
    :return:
    """
    vectorizer = CountVectorizer()
    print vectorizer

    text_context = [
         '对中文进行处理.',
         '人生 苦短,是的。',
         '我要用 python，好的',
     ]

    new_text_context = [" ".join(list(jieba.cut(x))) for x in text_context]  #返回  词语生成器
    # print json.dumps(new_text_context,ensure_ascii=False)


    X = vectorizer.fit_transform(text_context)   #标准化
    print json.dumps(vectorizer.get_feature_names(),ensure_ascii=False)   #1、对中文文本特征抽取，默认是按照空格分割的
                                                                          #2、为了提高特征提取准确性，需要 分词
                                                                          #3、分词采用jieba分词，把列表转换为 以空格隔开的


    Y = vectorizer.fit_transform(new_text_context)   #标准化
    print json.dumps(vectorizer.get_feature_names(),ensure_ascii=False)   #1、对中文文本特征抽取，默认是按照空格分割的
                                                                          #2、为了提高特征提取准确性，需要 分词
                                                                          #3、分词采用jieba分词


    # print X,X.toarray()
    # print Y,Y.toarray()



def main():
    text_feature_extraction00()
    text_feature_extraction001()
    text_feature_extraction002()


if __name__ == "__main__":
    main()
