# -*- coding: utf-8 -*-
# Зачем: забирает 80 таблиц регионов с веб-адреса и парсит их в CSV с некоторой переработкой для дальнейшей ручной работы с ними
# Проект: http://gis-lab.info/qa/geodetdom.html
# Обсуждение: http://gis-lab.info/forum/viewtopic.php?f=55&t=12594

import urllib2 as url
from bs4 import BeautifulSoup
import csv
from regions import regions
import codecs
from operator import itemgetter

page = url.urlopen('http://gis-lab.info/qa/geodetdom-coord.html')
path_to_folder = 'c:/temp/deti/step4/'
of = codecs.open(path_to_folder + 'wiki-restructure.csv', 'w', 'utf-8')
fieldnames = "ID;GEOCODE;COMMENT;REGION"

of.write(fieldnames+"\n")

soup = BeautifulSoup(''.join(page))
tables = soup.findAll("table", { "class" : "wikitable mw-collapsible mw-collapsed" })
i = 0
arr = []
for table in tables:
    region = "\"" + regions[i][0] + "\""
    print region
    i = i + 1
    trs = table.findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        if len(tds) != 0:
            idnum = list(tds[0].strings)[0].strip()[0:2]
            id = "\"" + list(tds[0].strings)[0].strip() + "\""
            comment = list(tds[1].strings)[0].strip().replace("\"","'")
            geocode = "\"" + comment.split(",")[0] + "\""
            if len(comment.split(",")) > 1: 
                comment = "\"" + comment[comment.index(",")+1:].strip() + "\""
            else:
                comment = ""
            #form list of lists
            arr.append([id,geocode,comment,unicode(region)])
    
#sort
sorted(arr, key=itemgetter(0))
#write list of records
for item in arr:
    of.write(item[0] + ";" + item[1] + ";" + item[2] + "\n")
of.close()