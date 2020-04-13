from library import read_query, remove, tokenize, read_inverted_index, stopwords, stem, read_most_word, read_data
import math
from os import system as a

def run():
    print("Proyek Mesin Pencarian Sederhana dengan Cranfield Collection")
    term = read_inverted_index()

    for query in read_query():
        print(str(query['query number']) + '. ', query['query'])

    choice = input("Masukan id dari query yang ingin dicari = ")
    a("cls")
    print("Proyek Mesin Pencarian Sederhana dengan Cranfield Collection")
    for query in read_query():
        if query['query number'] == int(choice):
            selected_query = query['query']

    selected_query = remove(selected_query)
    selected_query = tokenize(selected_query)

    tf = {}
    term_doc = {}
    for token in selected_query:
        token = stem(token)
        if token not in stopwords() and len(token) > 1:
            if token not in tf.keys():
                tf[token] = {}
                tf[token]['query'] = 1
                term_doc[token] = term.get(token)
            else:
                tf[token]['query'] += 1

    max_idf = {}
    ranked_doc = {}
    for term, doc in term_doc.items():
        max_idf[term] = len(term_doc[term])
        for id, total in doc.items():
            if id not in ranked_doc:
                ranked_doc[id] = 0
            if id not in tf[term]:
                tf[term][id] = total

    for word, data in tf.items():
        for id, sum in data.items():
            if id != "query":
                tf[word][id] = 0.5 + (0.5 * (tf[word][id] / read_most_word()[id]))

    idf = {}
    for term in tf.keys():
        idf[term] = math.log2(1400 / max_idf[term])

    for word, data in tf.items():
        for id, sum in data.items():
            if id != "query":
                ranked_doc[id] += tf[word][id] * idf[word]

    sorted_doc = sorted(ranked_doc.items(), key=lambda x: x[1], reverse=True)
    doc = read_data()

    sum = int(input("Masukan banyak dokumen relevan yang ini di tampilkan = "))
    for i in range(sum):
        print(str(i + 1) + ". " + str(doc[int(sorted_doc[i][0]) - 1]['title']) + " | similarity coefficient = " + str(
            sorted_doc[i][1]))
    a("pause")
    a("cls")
    start()

def about():
    print("Proyek Mesin Pencarian Sederhana dengan Cranfield Collection")
    print("Team Member :")
    print("Proyek Mesin Pencarian Sederhana dengan Cranfield Collection")
    print("1. Laurensius Joshua Anrico Agustinus    (14117141)")
    print("2. Maria Andini                          (14117041)")
    print("3. Rana Diastri Zahrina                  (14117147)")
    print("4. Yosua Tan Siswanto                    (14117060)")
    a("pause")
    a("cls")
    start()

def exit():
    print("Terima Kasih Telah Menggunakan Aplikasi ini")
    a("exit")


def error():
    print("Proyek Mesin Pencarian Sederhana dengan Cranfield Collection")
    print("1. Memilih Query")
    print("2. About Team")
    print("3. Exit")
    pilihan = int(input("Pilihan tidak tersedia silahkan masukan kembali = "))
    if pilihan == 1:
        a("cls")
        run()
    elif pilihan == 2:
        a("cls")
        about()
    elif pilihan == 3:
        a("cls")
        exit()
    else:
        a("cls")
        error()


def start():
    print("Proyek Mesin Pencarian Sederhana dengan Cranfield Collection")
    print("1. Memilih Query")
    print("2. About Team")
    print("3. Exit")
    pilihan = int(input("Masukan Pilihan = "))
    if pilihan == 1:
        a("cls")
        run()
    elif pilihan == 2:
        a("cls")
        about()
    elif pilihan == 3:
        a("cls")
        exit()
    else:
        a("cls")
        error()


start()



