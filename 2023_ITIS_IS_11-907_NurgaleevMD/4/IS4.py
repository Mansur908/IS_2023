import math
import os
import sys

termin = input()

directory = os.fsencode(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts')

num_documents = len(os.listdir(directory)) # колличество документов
document_contain_word_count = 0 # колличество документов содержащих термин


tf_array = []

for file in os.listdir(directory):
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
    tf_array.append([f"{file_num}.txt", count_word_in_document, len(data.split()), tf])
    if contain_word:
        document_contain_word_count += 1


try:
    idf = round(math.log(num_documents/document_contain_word_count), 6)
except:
    print("Термина нет в документах")
    sys.exit()



columns = ['Файл', 'Количество вхождений термина в документе     ', 'Количество слов в документе', 'tf', 'idf', 'tf-idf']

max_columns = [7, 20, 40, 25, 27, 27] # список максимальной длинны колонок

# печать шапки таблицы
for n, column in enumerate(columns):
    print(f'{column:{max_columns[n]+1}}', end='')
print()

# печать разделителя шапки '='
r = f'{"="*sum(max_columns)+"="*5}'
print(r[:-1])

# печать тела таблицы
for i in tf_array:
    for n, col in enumerate([i[0], i[1], i[2], round(i[3], 6), idf, round(i[3]*idf, 6)]):
        print(f'{col:{max_columns[n]+1}}', end='') # выравнвание по правому краю >
    print()