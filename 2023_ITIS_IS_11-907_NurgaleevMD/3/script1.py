import os
import sys

json = dict()

directory = os.fsencode(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts')
count = 0
for file in os.listdir(directory):
    file_num = file.decode("utf-8").split('.')[0]

    with open(rf'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts\{file_num}.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    for word in data.split(' '):
        if word in json:
            json.get(word).add(file_num)
        else:
            json[word] = {file_num}

with open(rf'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\3\index.json', 'w', encoding='utf-8') as file:
    file.write(str(json))

print('Success')