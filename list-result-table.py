#-*- encoding: utf-8 -*-
# Зачем: создание вики-таблицы результатов
# Проект: http://gis-lab.info/qa/geodetdom.html
# Обсуждение: http://gis-lab.info/forum/viewtopic.php?f=55&t=12594

from regions import regions

regions = sorted(regions, key=lambda k: k[1])

print """{| class="wikitable" border="1" width="100%"
! Код
! Регион
! Количество объектов
! ESRI Shape
! OSM XML
! CSV
|-
| РФ
| Россия целиком
| [http://gis-lab.info/data/detdom/RU-RU_det.7z скачать]
| 
|
|-
| 
| 
| 
| 
|
"""

for code, name in regions:
    numlines = len(open(code + ".csv").readlines()) - 1
    print """|-
| [[Координационная страница проекта по созданию слоя детских учреждений#%s|%s]]
| %s
| %s
| [%s/%s_shp.zip скачать]
| [%s/%s_osm.zip скачать]
| [%s/%s_csv.zip скачать]""" % (name, code, name, numlines, "http://gis-lab.info/data/detdom", code, "http://gis-lab.info/data/detdom", code, "http://gis-lab.info/data/detdom", code)

print """|}
"""