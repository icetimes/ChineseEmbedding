# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 16:19
# @Author  : huyulan
# @Email   : huyulan@boe.com.cn
# @File    : gensim_word2vec_train.py


import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')
warnings.filterwarnings(action='ignore',category=FutureWarning,module='gensim')
from gensim.models import word2vec
from gensim.models import KeyedVectors


def not_empty(word):
    return word and word.strip()

def read_setences(train_path):
    sentences = []
    with open(train_path, "r", encoding="utf-8") as f:
        for line in f:
            tmps = list(line.strip())
            if len(tmps) > 0:
                tmps = list(filter(not_empty, tmps))
                print(tmps)

                sentences.append(tmps)
    return sentences


'''基于gensim训练字向量'''


def train_vector(train_path, model_path):
    sentences = read_setences(train_path)
    model = word2vec.Word2Vec(sentences, size=300, window=5, min_count=5)  # 训练skip-gram模型,默认window=5
    model.wv.save_word2vec_format(model_path, binary=False)


if __name__ == '__main__':
    train_path = "D:/boe-data/服务器访问/数据资源/text8/document.txt"
    model_path = "./tmp/model.bin"
    # train_vector(train_path, model_path)

    model = KeyedVectors.load_word2vec_format(model_path, binary=False)
    print(model)

    vocab = list(model.wv.vocab)
    print(vocab)
    print(model['吃'])

    # 计算两个词的相似度/相关程度
    y1 = model.similarity("药", "病")
    print(u"药和病的相似度为：", y1)

    # 计算某个词的相关词列表，20个最相关的
    y2 = model.most_similar("思", topn=20)
    print(u"和思最相关的词有：\n")
    for item in y2:
        print(item[0], item[1])