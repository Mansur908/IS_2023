import os
import re

from pymorphy2 import MorphAnalyzer


directory = os.fsencode(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\1\texts')


patterns = "[^а-яА-Я]+"

with open(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = file.read()
stopwords = stopwords.split(sep='\n')
morph = MorphAnalyzer()

def lemmatize(doc):
    doc = re.sub(patterns, ' ', doc)
    tokens = []
    for token in doc.split():
        if token and token not in stopwords:
            token = token.strip()
            token = morph.normal_forms(token)[0]

            tokens.append(token)
    if len(tokens) > 2:
        return tokens
    return None

path = r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2'
if not os.path.exists(fr'{path}\texts'):
    os.makedirs(fr'{path}\texts')


for file in os.listdir(directory):
    file_num = file.decode("utf-8").split('.')[0]

    with open(rf'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\1\texts\{file_num}.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    print(file_num)

    result = ' '.join(lemmatize(data))

    with open(rf'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts\{file_num}.txt', 'w', encoding='utf-8') as file:
        file.write(result)


print('Success')
