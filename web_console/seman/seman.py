# -*- coding: utf-8 -*-
from gensim import models
semanticAnalysis = models.Word2Vec.load('word2vec.model')  # Should Defined Project DIR in settings.py (L17)

def analysis(query):
    if query:
        q_list = query.split()
        if len(q_list) == 1:
            res = semanticAnalysis.wv.most_similar(query, topn=3)
        elif len(q_list) == 2:
            res = str(semanticAnalysis.wv.similarity(q_list[0], q_list[1]))
        else:
            for i in semanticAnalysis.wv.most_similar([q_list[0], q_list[1]], [q_list[2]], topn=3):
                res = ",".join(i)
        return res
