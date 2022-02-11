from sklearn.metrics.pairwise import cosine_distances
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
import pickle
import re


stemmer = SnowballStemmer(language='english')

with open('main_data.pickle', 'rb') as f:
    data = 0
    data = pickle.load(f)
with open('index.pickle', 'rb') as f:
    index_invert = 0
    index_invert = pickle.load(f)


def stemm(query, stemmer):
    return set(stemmer.stem(i) for i in re.sub(r'[^\w\s]', '', query).lower().split())


def listing(first, second):
    arr3 = []
    index1 = 0
    index2 = 0
    len_of_arr1 = len(first)
    len_of_arr2 = len(second)
    while len_of_arr1 != index1 and len_of_arr2 != index2:
        if first[index1] == second[index2]:
            arr3.append(first[index1])
        if first[index1] > second[index2]:
            index2 += 1
        else:
            index1 += 1
    return arr3


def score(original, document):
    return cosine_distances(original, document)[0][0]


def retrieve(query):
    candidates = []
    for i in stemm(query, stemmer):
        if i in index_invert:
            candidates.append(index_invert[i])
    if len(candidates) != 0:
        for i in candidates:
            candidates[0] = listing(candidates[0], i)
        if len(candidates[0]) != 0:
            corpus = [" ".join(stemm(query, stemmer))
                      ]
            indexs = []
            if len(candidates[0]) != 0:
                for i in candidates[0]:
                    corpus.append(" ".join(data[i].stem_form))
                    indexs.append(data[i])
                Y = TfidfVectorizer().fit_transform(corpus).todense()
                original = Y[0]
                candidates = Y[1:]
                for i in range(len(indexs)):
                    indexs[i] = [candidates[i], indexs[i]]
                return original, indexs
        return set(), set()
    return set(), set()
