#-*- encoding: utf-8 -*-
# Зачем: генератор таблиц комментариев по каждому CSV региона для вики
# Проект: http://gis-lab.info/qa/geodetdom.html
# Обсуждение: http://gis-lab.info/forum/viewtopic.php?f=55&t=12594

from regions import regions
import csv

regions = sorted(regions, key=lambda k: k[1])

for code, name in regions:
    print "===%s===" % name
    print "Таблица результатов уточнения привязки данных по региону. Если вы хотите продолжить уточнять географическую привязку и описателью информацию, скачайте соответствующий набор результатов проекта [http://gis-lab.info/qa/geodetdom.html#.D0.A0.D0.B5.D0.B7.D1.83.D0.BB.D1.8C.D1.82.D0.B0.D1.82.D1.8B отсюда]. Принять участие в уточнение можно [http://gis-lab.info/qa/geodetdom.html#.D0.94.D0.B0.D0.BB.D1.8C.D0.BD.D0.B5.D0.B9.D1.88.D0.B0.D1.8F_.D1.81.D1.83.D0.B4.D1.8C.D0.B1.D0.B0_.D0.B4.D0.B0.D0.BD.D0.BD.D1.8B.D1.85 так]." 
    print """{| class="wikitable mw-collapsible mw-collapsed" border="1" width="100%"
! style="width: 10%%"| ID
! | Адрес
! | Результат привязки
! | Комментарий"""
    
    input = open( "results/" + code + ".csv","rb")
    csvreader = csv.DictReader(input)
    for row in csvreader:
        print "|-"
        print "|" + row['ID']
        print "|" + row['ADDRESS']
        print "|" + row['GEOCODE']
        print "|" + row['COMMENT']
    print "|}"
    input.close()