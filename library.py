import json
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer as sno

stop_words = set(stopwords.words("english"))
stop_words = stop_words.union(",", "(", ")", "[", "]", "{", "}", "#", "@", "!", ":", ";", ".", "?", "")


def stem(data):
    stemming = sno('english')
    data = stemming.stem(data)
    return data


def tokenize(data):
    return data.split()


def stopwords():
    return stop_words


def read_data():
    return json.load(open('cranfield_data.json'))


def read_query():
    return json.load(open('cran.qry.json'))


def read_relevance():
    return json.load(open('cranqrel.json'))


def read_inverted_index():
    return json.load(open('inverted_index.txt'))


def write_inverted_index(data):
    with open('inverted_index.txt', 'w') as DICT:
        json.dump(data, DICT, sort_keys=True)


def read_most_word():
    return json.load(open('word_count.txt'))


def write_most_word(data):
    with open('word_count.txt', 'w') as DICT:
        json.dump(data, DICT, sort_keys=True)


def remove(data):
    for char in data:
        if char.isdigit():
            data = data.replace(char, '')
        if char in " ?.!/;:'!@#$%^&*(),=-+":
            data = data.replace(char, ' ')

    return data
