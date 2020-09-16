# !/usr/bin/python
# -*- coding:utf-8 -*-
import pandas as pd
import jieba
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


df_news = pd.read_table('F:/essay/dd.txt',
                        names=['category', 'theme', 'URL', 'content'],
                        encoding='utf-8')
df_news = df_news.dropna()
df_news = df_news[(df_news['category'] == '体育') |
                  (df_news['category'] == '健康')|
                  (df_news['category'] == '军事') |
                  (df_news['category'] == '汽车') |
                  (df_news['category'] == '科技') |
                  (df_news['category'] == '财经')]


print(df_news.head())
content = df_news.content.values.tolist()

content_S = []
for line in content:
    current_segment = jieba.lcut(line)
    if len(current_segment) > 1 and current_segment != '\r\n':  # 换行符
        content_S.append(current_segment)
# print('content_S',content_S)
df_content = pd.DataFrame({'content_S': content_S})
print(df_content.head())


stopwords = pd.read_csv("F:/essay/stopwords.txt", index_col=False, sep="\t", quoting=3, names=['stopword'],
                        encoding='utf-8')


def drop_stopwords(contents, stopwords):
    contents_clean = []
    all_words = []
    for line in contents:
        line_clean = []
        for word in line:
            if word in stopwords:
                continue
            line_clean.append(word)
            all_words.append(str(word))
        contents_clean.append(line_clean)
    return contents_clean, all_words


contents = df_content.content_S.values.tolist()
stopwords = stopwords.stopword.values.tolist()
contents_clean, all_words = drop_stopwords(contents, stopwords)
# print(contents_clean[4])
print(contents_clean,'111111111111')
df_train = pd.DataFrame({'contents_clean': contents_clean, 'label': df_news['category']})
print(df_train.head())
# 分为训练集

x_train, x_test, y_train, y_test = train_test_split(df_train['contents_clean'].values,
                                                    df_train['label'].values,
                                                    test_size=0.30, random_state=11)


words = []
for line_index in range(len(x_train)):
    try:
        # x_train[line_index][word_index] = str(x_train[line_index][word_index])
        words.append(' '.join(x_train[line_index]))
    except:
        print('error')



"""
   从下面开始是算法
   """
test_words = []
for line_index in range(len(x_test)):
    try:
        # x_train[line_index][word_index] = str(x_train[line_index][word_index])
        test_words.append(' '.join(x_test[line_index]))
    except:
        print('ss')

#  以TF-IDF向量为特征
print(words)

vecTf = CountVectorizer(lowercase=False)

vecTf_model = vecTf.fit(words)

tra = vecTf_model.transform(words)


tes = vecTf_model.transform(test_words)
tratfidf_df = pd.DataFrame(tra.toarray())
testfidf_df = pd.DataFrame(tes.toarray())


from sklearn.feature_selection import SelectKBest, chi2
ch2 = SelectKBest(chi2, k=100)
ch2.fit_transform(tratfidf_df, y_train)
ch2_sx_featuresindex=ch2.get_support(indices=True)
print('ch2_sx_featuresindex', ch2_sx_featuresindex,'ch2_sx_featuresindex')
print(type(ch2_sx_featuresindex))

x_tra=tratfidf_df.iloc[:, ch2_sx_featuresindex]# tfidf法筛选后的词向量矩阵训练

x_tes=testfidf_df.iloc[:,ch2_sx_featuresindex]# tfidf法筛选后的词向量矩阵测试
a=vecTf_model.vocabulary_
dict_keys=list(a.keys())
dict_val= list(a.values())
z=[]
for j in ch2_sx_featuresindex:
    y=dict_keys[dict_val.index(j)]
    z.append(y)
print('1111111111\n',z,'\n1111111111111')
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB

NBclassifier = MultinomialNB()
NBclassifier.fit(x_tra, y_train)
bayes_ytest = NBclassifier.predict(x_tes)

print('MultinomialNB混淆概率\n', classification_report(y_test, bayes_ytest))
print('MultinomialNB混淆矩阵值 \n', confusion_matrix(y_test, bayes_ytest))
print('MultinomialNB正确率', accuracy_score(y_test, bayes_ytest))


from sklearn.svm import SVC

linearsvmmodel = SVC(C=1.0, kernel='linear', gamma='auto')
linearsvmmodel.fit(x_tra, y_train)
svmlinear_y_testfit = linearsvmmodel.predict(x_tes)
print('svmlinear混淆概率\n', classification_report(y_test, svmlinear_y_testfit))
print('svmlinear混淆矩阵值 \n', confusion_matrix(y_test, svmlinear_y_testfit))
print('svmlinear正确率', accuracy_score(y_test, svmlinear_y_testfit))
