from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
words = ["running", "runs", "easily", "fairly", "happiness", "playing", "played", "better", "walking", "talking"]

stemmed_words = [ps.stem(word) for word in words]
print(stemmed_words)
