import ast
import sys

a = input()

arr = a.split(' ')

if len(arr) != 5:
    sys.exit('Некорректное выражение')


with open(r'C:\Users\mansu\Desktop\IS_2023\2023_ITIS_IS_11-907_NurgaleevMD\3\index.json', 'r', encoding='utf-8') as file:
    index = ast.literal_eval(file.read())

all = set(range(1,101))

new_arr = []

for i in range(len(arr)):
    if i % 2 == 0:
        if arr[i].startswith('!'):
            if index.get(arr[i][1:]) == None:
                sys.exit('Слова из выражения не существуют')
            new_arr.append(all - index.get(arr[i][1:]))
            arr[i] = arr[i][1:]
        else:
            if index.get(arr[i]) == None:
                sys.exit('Слова из выражения не существуют')
            new_arr.append(index.get(arr[i]))


if arr[1] == '|' or arr[1] == 'ИЛИ':
    if arr[3] == '|' or arr[3] == 'ИЛИ':
        result = new_arr[0] | new_arr[1] | new_arr[2]
    elif arr[3] == '&' or arr[3] == 'И':
        result = new_arr[0] | new_arr[1] & new_arr[2]
elif arr[1] == '&' or arr[1] == 'И':
    if arr[3] == '|' or arr[3] == 'ИЛИ':
        result = new_arr[0] & new_arr[1] | new_arr[2]
    elif arr[3] == '&' or arr[3] == 'И':
        result = new_arr[0] & new_arr[1] & new_arr[2]

if len(result) == 0:
    print("не найдено")
else:
    print(result)
