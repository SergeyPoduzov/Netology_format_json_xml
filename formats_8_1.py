
import os
import json


def opening_json():
    """Функуция открвает json"""
    if os.path.exists('files_json_xml/newsafr.json')==True:
        with open('files_json_xml/newsafr.json', encoding='utf-8') as f:
            json_data = json.load(f)
            new_list=json_data['rss']['channel']['items']
        #Выведем заголовки статей
        words = ''
        for news in new_list:
            words += news['description'] + ''
        return words
    else:
        print("Такого файла json не существует")

def opening_xml():
    if os.path.exists('files_json_xml/newsafr.json') == True:
        import xml.etree.ElementTree as ET
        with open("files_json_xml/newsafr.xml", encoding='utf-8') as f:
            xml_text = f.read()
        xml_tree = ET.fromstring(xml_text)
        xml_news = xml_tree.findall('channel/item')
        words = ''
        for new in xml_news:
            alem = new.find('description').text
            words += alem + " "
        return words
    else:
        print("Такого файла xml не существует")

#Функция на вход примает список и далее ее сортирует и выводит 10 слов самых цитируем и кол-во упоминаний.
def sorting_words(words,n, txt):
    words=words.split()
    set_words=set(words)
    #Уникальные слова более 6 букв
    new_set_words=[]
    for word in set_words:
        if len(word)>=6:
            new_set_words.append(word)
    dict={}
    for word in new_set_words:
        k=0
        for word2 in words:
            if word2==word:
                k +=1
        dict[word]=k
    list_dict=list(dict.items())
    list_dict.sort(key=lambda i: i[1],reverse=True)
    print(txt)
    for word in list_dict[:n]:
        print(word[0],":",word[1])

words=opening_json()
sorting_words(words,10, "\nИтоги первого задания: Слово и количество упоминаний (при импорте json): ")
words=opening_xml()
sorting_words(words,10, "\nИтоги второго задания: Слово и количество упоминаний (при импорте xml): ")