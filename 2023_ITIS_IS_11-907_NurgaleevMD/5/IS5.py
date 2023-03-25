import math
import os
import re
import json
import operator
from sklearn.metrics.pairwise import cosine_similarity
from pymorphy2 import MorphAnalyzer

with open(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\3\index.json', 'r', encoding='utf-8') as file:
    data = dict(json.load(file))


texts_directory = os.fsencode(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts')
doc_count = len(os.listdir(texts_directory))

morph = MorphAnalyzer()

def lemmatize(doc, stopwords = []):
    patterns = "[^а-яА-Я]+"
    doc = re.sub(patterns, ' ', doc)
    tokens = []
    for token in doc.split():
        if token and token not in stopwords:
            token = token.strip()
            token = morph.normal_forms(token)[0]

            tokens.append(token)
    if len(tokens) > 0:
        return tokens
    return None

def get_url(index):
    with open(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\1\index.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    result = None
    for file in data:
        num = file.split(" -> ")[0].split(".")[0]
        url = file.split(" -> ")[1][:-1]
        if str(num) == str(index):
            result = url
    return result


def get_tf_idf(termin, index):
    tf_idf_dict = {}

    tf_array = []
    num_documents = doc_count # колличество документов
    document_contain_word_count = 0 # колличество документов содержащих термин
    for file in os.listdir(texts_directory):
        file_num = file.decode("utf-8").split('.')[0]
        words_counts = {} # словарь частоты слов в документе
        with open(rf'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts\{file_num}.txt', 'r', encoding='utf-8') as file:
            data = file.read()
        contain_word = False
        count_word_in_document = 0
        for word in data.split():
            if word == termin:
                count_word_in_document += 1
                contain_word = True
            if word in words_counts:
                words_counts.update({word: words_counts.get(word) + 1})
            else:
                words_counts.update({word: 1})
        tf = count_word_in_document/len(data.split())
        if count_word_in_document > 0:
            tf_array.append([file_num, count_word_in_document, len(data.split()), tf])
        if contain_word:
            document_contain_word_count += 1
    try:
        idf = round(math.log(num_documents/document_contain_word_count), 6)
    except:
        return 0
    # tf_idf_dict.update({termin: {i[0]:{"TF": round(i[3], 6), "IDF": idf, "TF-IDF": round(i[3]*idf, 6)} for i in tf_array}})
    tf_idf_dict.update({termin: {i[0]:{"TF-IDF": round(i[3]*idf, 6)} for i in tf_array}})

    try:
        return tf_idf_dict.get(termin).get(str(index)).get("TF-IDF")
    except:
        return 0

def query_tf_idf(token, query):
    try:
        doc_with_token_count = len(data.get(token))
    except:
        return 0

    q_tf = query.count(token) / len(query)
    q_idf = math.log(doc_count / doc_with_token_count)

    return round(q_tf * q_idf, 6)




def search(query):
    query = lemmatize(query)

    query_vector = []

    for token in query:
        query_vector.append(query_tf_idf(token, query))

    vectors_distances = {}

    for file in os.listdir(texts_directory):
        index = file.decode("utf-8").split('.')[0]

        document_vector = []

        for token in query:
            try:
                tf_idf = get_tf_idf(token, index)
                document_vector.append(tf_idf)
            except KeyError:
                document_vector.append(0.0)

        vectors_distances[index] = cosine_similarity([query_vector], [document_vector])[0][0]


    searched_indices = sorted(vectors_distances.items(), key=operator.itemgetter(1), reverse=True)

    for index in searched_indices:
        doc_id, tf_idf = index

        url = get_url(doc_id)
        print("Index: {}\nURL:{}\nCosine:{}\n".format(doc_id, url, tf_idf))



search(input())
