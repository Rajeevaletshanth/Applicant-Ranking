import docx2txt
import nltk

res = open("ClearText2.txt").read()

pos = open("posemo.txt").read()
neg = open("negemo.txt").read()
soc = open("Social.txt").read()

pos_txt = [res, pos]
neg_txt = [res, neg]
soc_txt = [res, soc]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
pos_count_matrix = cv.fit_transform(pos_txt)
neg_count_matrix = cv.fit_transform(neg_txt)
soc_count_matrix = cv.fit_transform(soc_txt)

from sklearn.metrics.pairwise import cosine_similarity

Pos_match = cosine_similarity(pos_count_matrix)[0][1]
Pos_match = Pos_match*100
Pos_match = round(Pos_match, 2)

Neg_match = cosine_similarity(neg_count_matrix)[0][1]
Neg_match = Neg_match*100
Neg_match = round(Neg_match, 2)

Soc_match = cosine_similarity(soc_count_matrix)[0][1]
Soc_match = Soc_match*50
Soc_match = round(Soc_match, 2)

print("Positive : ", Pos_match)
print("Negative : ", Neg_match)
print("Social : ", Soc_match)
Final = round((Pos_match + Soc_match) - Neg_match, 2)
print("Final Points : ", Final)