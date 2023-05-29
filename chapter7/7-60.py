#GoogleNews-vectors-negative300.bin.gzをダウンロードして、"United States"の単語ベクトルを表示。
import subprocess
import gdown

import numpy as np
import pandas as pd
from gensim.models import KeyedVectors


model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
# "United States"の単語ベクトルを表示
print(model['United_States'])