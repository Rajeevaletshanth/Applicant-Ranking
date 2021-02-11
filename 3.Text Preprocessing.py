import nltk
from nltk.corpus import stopwords
import spacy
import gensim
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from string import punctuation
from collections import Counter
import re
import unidecode

res = open("ResumeStr.txt").read()

#Lower case conversion
def lower_case_convertion(text):
	"""
	Input :- string
	Output :- lowercase string
	"""
	lower_text = text.lower()
	return lower_text

res = lower_case_convertion(res)

# HTML tags removal Implementation using regex module
def remove_html_tags(text):
	"""
	Return :- String without Html tags
	input :- String
	Output :- String
	"""
	html_pattern = r'<.*?>'
	without_html = re.sub(pattern=html_pattern, repl=' ', string=text)
	return without_html

res = remove_html_tags(res)

# Implementation of Removing URLs  using python regex
def remove_urls(text):
	"""
	Return :- String without URLs
	input :- String
	Output :- String
	"""
	url_pattern = r'https?://\S+|www\.\S+'
	without_urls = re.sub(pattern=url_pattern, repl=' ', string=text)
	return without_urls

res = remove_urls(res)

# Implementation of accented text to ASCII converter in python
def accented_to_ascii(text):
	"""
	Return :- text after converting accented characters
	Input :- string
	Output :- string
	"""
	# apply unidecode function on text to convert
	# accented characters to ASCII values
	text = unidecode.unidecode(text)
	return text

res = accented_to_ascii(res)

## Implementation of lemmatization using nltk
def lemmatization(text):
	"""
	Result :- string after stemming
	Input :- String
	Output :- String
	"""
	# word tokenization
	tokens = nltk.word_tokenize(text)

	for index in range(len(tokens)):
		# lemma word
		lemma_word = lemma.lemmatize(tokens[index])
		tokens[index] = lemma_word

	return ' '.join(tokens)

# initialize lemmatizer object
lemma = WordNetLemmatizer()
res = lemmatization(res)

# Implementation of removing punctuations using string library
def remove_punctuation(text):
	"""
	Return :- String after removing punctuations
	Input :- String
	Output :- String
	"""
	return text.translate(str.maketrans('', '', punctuation))

res = remove_punctuation(res)

# Implementation of removing stopwords using all stop words from nltk, spacy, gensim
def remove_stopwords(text):
	"""
	Return :- String after removing stopwords
	Input :- String
	Output :- String
	"""
	text_without_sw = []
	# tokenization
	text_tokens = nltk.word_tokenize(text)
	for word in text_tokens:
		# checking word is stopword or not
		if word not in all_stopwords:
			text_without_sw.append(word)

	# joining all tokens after removing stop words
	without_sw = ' '.join(text_without_sw)
	return without_sw


# list of stopwords from nltk
stopwords_nltk = list(stopwords.words('english'))
sp = spacy.load('en_core_web_sm')
# list of stopwords from spacy
stopwords_spacy = list(sp.Defaults.stop_words)
# list of stopwords from gensim
stopwords_gensim = list(gensim.parsing.preprocessing.STOPWORDS)

# unique stopwords from all stopwords
all_stopwords = []
all_stopwords.extend(stopwords_nltk)
all_stopwords.extend(stopwords_spacy)
all_stopwords.extend(stopwords_gensim)
# all unique stop words
all_stopwords = list(set(all_stopwords))
print(f"Total number of Stopwords :- {len(all_stopwords)}")

res = remove_stopwords(res)



# Removing Extra Whitespaces
def remove_extra_spaces(text):
	"""
	Return :- string after removing extra whitespaces
	Input :- String
	Output :- String
	"""
	space_pattern = r'\s+'
	without_space = re.sub(pattern=space_pattern, repl=" ", string=text)
	return without_space

res = remove_extra_spaces(res)



# Implementation of Removing numbers  using python regex
def remove_numbers(text):
	"""
	Return :- String without numbers
	input :- String
	Output :- String
	"""
	number_pattern = r'\d+'
	without_number = re.sub(pattern=number_pattern,
 repl=" ", string=text)
	return without_number

# calling remove_numbers function with example text (ex_numbers)
res = remove_numbers(res)



## Implementation of lemmatization using nltk
def lemmatization(text):
	"""
	Result :- string after stemming
	Input :- String
	Output :- String
	"""
	# word tokenization
	tokens = nltk.word_tokenize(text)

	for index in range(len(tokens)):
		# lemma word
		lemma_word = lemma.lemmatize(tokens[index])
		tokens[index] = lemma_word

	return ' '.join(tokens)

# initialize lemmatizer object
lemma = WordNetLemmatizer()

res = lemmatization(res)




# Program without using any external library
l = res.split()
k = []
for i in l:

	# If condition is used to store unique string
	# in another list 'k'
	if (res.count(i) > 1 and (i not in k) or res.count(i) == 1):
		k.append(i)
res = ' '.join(k)


print(res)

with open("ClearText.txt", "w") as text_file:
    print(res, file=text_file)