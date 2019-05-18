#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import jieba




def text_feature_extraction000():
    """
    对含有中文文本内容的特征抽取，先采用jieba分词,采用tf-idf 评估 词的重要性
    :return:
    """
    vectorizer = TfidfVectorizer()
    print vectorizer

    text_context = [
         '对中文进行处理.',
         '人生 苦短,中文是的。',
         '我要用 python，好的',
     ]

    new_text_context = [" ".join(list(jieba.cut(x))) for x in text_context]  #返回  词语生成器
    # print json.dumps(new_text_context,ensure_ascii=False)

    Y = vectorizer.fit_transform(new_text_context)   #标准化
    print json.dumps(vectorizer.get_feature_names(),ensure_ascii=False)   #1、对中文文本特征抽取，默认是按照空格分割的
                                                                          #2、为了提高特征提取准确性，需要 分词
                                                                          #3、分词采用jieba分词
    # 1.tf  term frequency : 词的频率
    # 2.idf  inverse document frequency 逆文档频率     log(总文档数量/改词出现的文档数)
    # 3. 计算指标 ： 重要性程度 ： tf*idf


    print Y
    print Y.toarray()



def main():
    text_feature_extraction000()


if __name__ == "__main__":
    main()
