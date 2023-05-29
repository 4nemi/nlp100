#word similarity evaluation
from gensim.models import KeyedVectors
import numpy as np
from scipy.stats import spearmanr

model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

def cal_spearmanr(sim, true):
    correlation, pvalue = spearmanr(sim, true)
    return correlation

with open('conbined.csv') as f:
    next(f)
    lines = f.readlines()
    sim_list = []
    true_list = []
    for line in lines:
        word1, word2, true_sim = line.split(',')
        pred_sim = model.similarity(word1, word2)
        sim_list.append(pred_sim)
        true_list.append(float(true_sim))

print(cal_spearmanr(sim_list, true_list))
