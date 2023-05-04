import math
from nltk.collocations import TrigramCollocationFinder

class Id_identifier:
    def __init__(self):
        self.__idioms = {}
        self.__test = {}
        self.__results = {}

    def add_train(self, f_trigrams: list, idioma: str):
        size = 0
        for x in f_trigrams:
            size += x[1]
        self.__idioms[idioma] = ({x[0]: x[1] for x in f_trigrams}, size) ##### idioms[idioma] = ({(a, b, c): 3}, 3)
      
    def add_test(self, sentences: list, idioma: str, name: str = "random test"):
        self.__test[name] = (sentences, idioma)  ##### test[name] = ({(a, b, c): 3}, spanish)

    def calculate_metric(self):
        i = 0
        for name in self.__test:
            self.__results[name] = ({x: 0 for x in self.__idioms}, self.__test[name][1])
            for sentence in self.__test[name][0]:
                predict = []
                finder_tr = TrigramCollocationFinder.from_words(sentence)
                trigrams = [tr[0] for tr in finder_tr.ngram_fd.items()]
                for idiom in self.__idioms:
                    prob = 0
                    for trigram in trigrams:
                        if trigram in self.__idioms[idiom][0]:
                            prob += math.log((self.__idioms[idiom][0][trigram] + 0.5)/(self.__idioms[idiom][1] + (0.5 * (26**3))))
                        else:
                            prob += math.log((0 + 0.5)/(self.__idioms[idiom][1] + (0.5 * (26**3))))
                    predict += [(prob, idiom)]
                predicted_idiom = max(predict)[1]
                self.__results[name][0][predicted_idiom] += 1

    def results(self):
        return self.__results