import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt

class Loader:
    def __init__(self):
        os.system('clear')

    @staticmethod
    def words_loader():
        files = ".*\.txt"
        corpus = PlaintextCorpusReader("corpus/", files)
        words  = nltk.Text(corpus.words())
        return words

    @staticmethod
    def stopwords_cleaner(words):
        s = set(string.punctuation)
        stopwords = nltk.corpus.stopwords.words('portuguese')
        filtered_word = [word for word in words if (word.lower() not in stopwords) and (word.lower() not in s)]
        return filtered_word

    @staticmethod
    def freq_stuff_dist_50(filtered_word):
        fdist = FreqDist(filtered_word)
        comum = fdist.most_common()[:50]
        data = {comum[i][0] : comum[i][1] for i in range(len(comum))}
        palavras = list(data.keys())
        quants = list(data.values())
        fig = plt.figure(figsize = (10, 10))
        plt.barh(palavras, quants, color ='maroon')
        plt.xlabel("Frequencia")
        plt.ylabel("Palavras")
        plt.title("Frequencia das 50 palavras mais recorrentes")
        plt.show()

corpus = Loader.words_loader()
clean = Loader.stopwords_cleaner(corpus)
freq = Loader.freq_stuff_dist_50(clean)