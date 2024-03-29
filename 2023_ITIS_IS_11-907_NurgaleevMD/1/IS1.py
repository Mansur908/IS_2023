import os

import requests
from bs4 import BeautifulSoup

sites = list(input().split())

links = []
for i in sites:
    if not links.__contains__(i):
        links.append(i)

count = 0
i = 0

path = r'C:\Users\mansu\Desktop\2023_ITIS_IS_11-907_NurgaleevMD\1'
if not os.path.exists(fr'{path}\texts'):
    os.makedirs(fr'{path}\texts')

while count < 100:
    if not links[i].__contains__('http'):
        i += 1
        continue
    current_site = links[i]
    i += 1

    try:
        r = requests.get(current_site)
    except:
        print(f'Ошибка при запросе на сайт: {current_site}')
        continue

    soup = BeautifulSoup(r.text, 'lxml')
    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    num_words = len(text.split())

    all_a = soup.find_all('a')

    for a in all_a:
        if not links.__contains__(a.get('href')):
            links.append(a.get('href'))
    if num_words >= 1000:
        count += 1
        with open(fr"{path}\texts\{count}.txt", "w", encoding="utf-8") as myfile:
            myfile.write(text)
            myfile.close()
        with open(fr"{path}\index.txt", "a") as myfile:
            myfile.write(f"{count}.txt -> {current_site}\n")
    print(count)

print("Success")
import os

import requests
from bs4 import BeautifulSoup

sites = list(input().split())

links = []
for i in sites:
    if not links.__contains__(i):
        links.append(i)

count = 0
i = 0

path = r'C:\Users\mansu\Desktop\2023_ITIS_IS_11-907_NurgaleevMD\1'
if not os.path.exists(fr'{path}\texts'):
    os.makedirs(fr'{path}\texts')

while count < 100:
    if not links[i].__contains__('http'):
        i += 1
        continue
    current_site = links[i]
    i += 1

    try:
        r = requests.get(current_site)
    except:
        print(f'Ошибка при запросе на сайт: {current_site}')
        continue

    soup = BeautifulSoup(r.text, 'lxml')
    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    num_words = len(text.split())

    all_a = soup.find_all('a')

    for a in all_a:
        if not links.__contains__(a.get('href')):
            links.append(a.get('href'))
    if num_words >= 1000:
        count += 1
        with open(fr"{path}\texts\{count}.txt", "w", encoding="utf-8") as myfile:
            myfile.write(text)
            myfile.close()
        with open(fr"{path}\index.txt", "a") as myfile:
            myfile.write(f"{count}.txt -> {current_site}\n")
    print(count)

print("Success")
