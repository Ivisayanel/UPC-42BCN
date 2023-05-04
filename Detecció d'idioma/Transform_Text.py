from nltk.collocations import TrigramCollocationFinder
from IdiomModel import *
from functions import *
import nltk
import pandas as pd

nltk.download('punkt')

model = Id_identifier()
tr = ["deu", "eng", "fra", "ita", "nld", "spa"]
for idiom in tr:
    # Open files: file
    with open(f'./Data/{idiom}_trn.txt', 'r', encoding = 'UTF-8') as content_file:
        content = content_file.read()

    a = nltk.sent_tokenize(content)

    finder_tr = TrigramCollocationFinder.from_words(separation(a[0:30001]))
    finder_tr.apply_freq_filter(5)

    list_of_trigrams_tr = [tr for tr in finder_tr.ngram_fd.items()]
    model.add_train(list_of_trigrams_tr, idiom)
test = tr
for i_test in test:
    test = f'./Data/{i_test}_tst.txt'
    with open(test, 'r', encoding = 'UTF-8') as content_file:
        content = content_file.read()

    a = nltk.sent_tokenize(content)

    text = separation (a[0:10001])

    model.add_test(nltk.sent_tokenize(text), i_test, test)



model.calculate_metric()
results = model.results()
print(results)

# data = {'y_true': [],
#         'y_predicted': []}
# for x in results:
#     data['y_true'] += [results[x][1]]
#     data['y_predicted'] += [results[x][2]]

# true_values = 0
# for x in results:
#     if results[x][1] == results[x][2]:
#         true_values += 1

# df = pd.DataFrame(data)
# cm = pd.crosstab(df['y_true'], df['y_predicted'], rownames=['True'], colnames = ['Predict'])
# print(cm)

# print("Acc: ", true_values / len(results))