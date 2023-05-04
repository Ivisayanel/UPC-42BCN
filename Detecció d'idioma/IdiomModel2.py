import math

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
      
    def add_test(self, test_tri: list, idioma: str, name: str = "random test"):
        self.__test[name] = ({x[0]: x[1] for x in test_tri}, idioma)  ##### test[name] = ({(a, b, c): 3}, spanish)

    def calculate_metric(self):
        for name in self.__test:
            self.__results[name] = []
            for idiom in self.__idioms:
                prob = 0
                for trigram in self.__test[name][0]:
                    if trigram in self.__idioms[idiom][0]:
                        prob += math.log((self.__idioms[idiom][0][trigram] + 0.5)/(self.__idioms[idiom][1] + (0.5 * (26**3))))
                    else:
                        prob += math.log((0 + 0.5)/(self.__idioms[idiom][1] + (0.5 * (26**3))))
                self.__results[name] += [(prob, idiom, self.__test[name][1])]
            self.__results[name] = max(self.__results[name])

    def results(self):
        return self.__results