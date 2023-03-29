import math
import os
import sys
import json
from pprint import pprint


directory = os.fsencode(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts')


result_dict = {}

count_of_doc_contain_word = {}  # словарь количества документов содержаших слово

count_doc = len(os.listdir(directory))
for file in os.listdir(directory):
    file_num = file.decode("utf-8").split('.')[0]
    termin_counts = {} # словарь частоты слов в документе

    with open(rf'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts\{file_num}.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    doc_words_count = 0

    for word in data.split():
        doc_words_count += 1
        if termin_counts.__contains__(word):
            termin_counts.update({word: termin_counts.get(word)+1})
        else:
            termin_counts.update({word: 1})

        if count_of_doc_contain_word.__contains__(word):
            count_of_doc_contain_word.get(word).add(file_num)
        else:
            count_of_doc_contain_word.update({word: {file_num}})

    for word in termin_counts.keys():
        if result_dict.__contains__(word):
            if result_dict.get(word).__contains__(file_num):
                result_dict.get(word).get(file_num).update({"TF": round(termin_counts.get(word)/doc_words_count, 6)})
            else:
                result_dict.get(word).update({file_num: {"TF": round(termin_counts.get(word) / doc_words_count, 6)}})
        else:
            result_dict.update({word: {file_num: {"TF": round(termin_counts.get(word)/doc_words_count, 6)}}})

for word in count_of_doc_contain_word.keys():
    for file_num in count_of_doc_contain_word.get(word):
        tf = result_dict.get(word).get(file_num).get("TF")
        idf = math.log(count_doc/len(count_of_doc_contain_word.get(word)))
        result_dict.get(word).get(file_num).update({"IDF": round(idf, 6),
                                                    "TF-IDF": round(tf*idf, 6)})

with open('index.json', 'w') as fp:
    json.dump(result_dict, fp, ensure_ascii=False, indent=4)

