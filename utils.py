# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 13:52
# @Author  : huyulan
# @Email   : huyulan@boe.com.cn
# @File    : test.py
# @Software: PyCharm

import pandas as pd


def run_with_one_corpus_for_quora(self, file_path):
    corpus = {}

    df = pd.read_csv(file_path)

    qid1 = list(df['qid1'])
    qid2 = list(df['qid2'])
    question1 = list(df['question1'])
    question2 = list(df['question2'])
    is_duplicate = list(df['is_duplicate'])

    for x1, x2 in zip(qid1, question1):
        corpus[x1] = x2
    for x1, x2 in zip(qid2, question2):
        corpus[x1] = x2

    rel = [(label, qid1, qid2) for label, qid1, qid2 in zip(is_duplicate, qid1, qid2)]
    return corpus, rel


if __name__ == '__main__':
    run_with_one_corpus_for_quora("")

