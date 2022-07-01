import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
import pyfiglet
import os

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

    @staticmethod
    def semantic_stuff(words):

        os.system('clear')
        print(f'{pyfiglet.figlet_format("Text_Proc")}\n\n\n\n            Insira o termo-chave que será buscado : \n\n\n\n')
        user_input_term = input("Option  : ")

        os.system('clear')
        print(f'{pyfiglet.figlet_format("Text_Proc")}\n\n\n\n            1) Opção     1 - Similaridades\
                                                     \n\n\n\n            2) Opção     2 - Concordâncias\
                                                     \n\n\n\n            3) Opção     3 - Bigramas\
                                                     \n\n\n\n            4) Opção     4 - Trigramas\
                                                     \n\n\n\n')
        user_input = input("Opção  : ")

        if user_input == '1':
            print(words.similar(user_input_term))
        elif user_input == '2':
            print(words.concordance(user_input_term))
        elif user_input == '3':
            print(list(nltk.bigrams(words)))
        elif user_input == '4':
            print(list(nltk.trigrams(words)))
        else:
            os.system('clear')

corpus = Loader.words_loader()
clean = Loader.stopwords_cleaner(corpus)
#freq = Loader.freq_stuff_dist_50(clean)
semantic = Loader.semantic_stuff(corpus)
