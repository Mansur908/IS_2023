import os
import sys
import json as j

json = dict()

directory = os.fsencode(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts')
count = 0
for file in os.listdir(directory):
    file_num = file.decode("utf-8").split('.')[0]

    with open(rf'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\2\texts\{file_num}.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    for word in data.split(' '):
        if word in json:
            if not json.get(word).__contains__(file_num):
                json.get(word).append(file_num)
        else:
            json[word] = [file_num]


print(len(json.keys()))
# with open(rf'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\3\index.json', 'w', encoding='utf-8') as file:
#     j.dump(json, file, ensure_ascii=False)

print('Success')