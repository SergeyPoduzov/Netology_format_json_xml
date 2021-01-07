
import os
import json
file_json='files_json_xml/newsafr.json'
file_xml='files_json_xml/newsafr.xml'

def opening_json():
    """Функуция открвает json"""
    if os.path.exists(file_json)==True:
        with open(file_json, encoding='utf-8') as f:
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
    if os.path.exists(file_xml) == True:
        import xml.etree.ElementTree as ET
        with open(file_xml, encoding='utf-8') as f:
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
def sorting_words(words,n,num_digitals, txt):
    words=words.split()
    set_words=set(words)
    #Уникальные слова более 6 букв
    new_set_words=[]
    for word in set_words:
        if len(word)>=num_digitals:
            new_set_words.append(word)
    dict={}
    for word in new_set_words:
        dict[word]=words.count(word)

    list_dict=list(dict.items())
    list_dict.sort(key=lambda i: i[1],reverse=True)
    print(txt)
    for word in list_dict[:n]:
        print(word[0],":",word[1])

words=opening_json()
sorting_words(words,10,6, "\nИтоги первого задания: Слово и количество упоминаний (при импорте json): ")
words=opening_xml()
sorting_words(words,10,6, "\nИтоги второго задания: Слово и количество упоминаний (при импорте xml): ")