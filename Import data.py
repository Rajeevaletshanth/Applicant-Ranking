import nltk
import numpy
import pandas as df
import gensim
from gensim import corpora, models, similarities
from gensim.models import Word2Vec, keyedvectors
from gensim.models.callbacks import CallbackAny2Vec

df = df.read_csv("Book1.csv")

Total = df['Y'].sum()
print(Total)



