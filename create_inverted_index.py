from library import read_data, remove, tokenize, stem, stopwords, write_inverted_index, write_most_word

files = {}
word_count = {}

for data in read_data():
    data['body'] = remove(data['body'])
    data['body'] = tokenize(data['body'])
    for token in data['body']:
        token = stem(token)
        if token not in stopwords() and len(token) > 1:
            if data['id'] not in word_count.keys():
                word_count[data['id']] = {}
            elif token not in word_count[data['id']].keys():
                word_count[data['id']][token] = 1
            else:
                word_count[data['id']][token] += 1
            if token not in files.keys():
                files[token] = {data['id']: 1}
            elif token in files and data['id'] not in files[token]:
                files[token][data['id']] = 1
            else:
                files[token][data['id']] += 1

most_word = {}
for words, counter in word_count.items():
    word_counts = 0
    for word, value in counter.items():
        if word_counts < value:
            word_counts = value
    most_word[words] = word_counts

write_inverted_index(files)
write_most_word(most_word)
