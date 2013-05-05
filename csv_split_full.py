# -*- encoding: utf-8 -*-
# Зачем: на входе общий CSV файл со всеми результатами, на выходе куча CSV файлов по областям
# Проект: http://gis-lab.info/qa/geodetdom.html
# Обсуждение: http://gis-lab.info/forum/viewtopic.php?f=55&t=12594

import csv
from regions import regions

for code, name in regions:
    input = open('results/RU-RU.csv ', 'rb')
    output = open('results/%s.csv' % code, 'wb')
    csvreader = csv.DictReader(input)
    #csvwriter = csv.DictWriter(output, fieldnames=csvreader.fieldnames)
    fieldnames = ("ID","GEOCODE","COMMENT","LON","LAT","NAME","ADDRESS","REGION","DISTRICT","TYPE","COMPUTERS","ACTIVITIES","COMMUNICAT","WORK_CAB","BUILDINGS","LIBRARY","TOYS","EDUCATION","STAFF","NEEDS","CHILDREN","TREATMENT","FARMING","PRINCIPLE","FOUNDATION","DEVIATED","PARENT","HOLIDAYS","DIRECTOR","PHONE","URL","BANK","PATRONAGE","AGE","VEHICLES","FED_DISTR","PUBS","VOLUNTEERS","ORPHANS","HISTORY")
    csvwriter = csv.DictWriter(output, fieldnames=fieldnames)
    csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
    for row in csvreader:
        if row['REGION'] == name:
            #csvwriter.writerow(row)
            csvwriter.writerow(dict(ID=row['ID'],
                                    GEOCODE=row['GEOCODE'],
                                    COMMENT=row['COMMENT'],
                                    LON=row['LON'],
                                    LAT=row['LAT'],
                                    NAME=row['NAME'],
                                    ADDRESS=row['ADDRESS'],
                                    REGION=row['REGION'],
                                    DISTRICT=row['DISTRICT'],
                                    TYPE=row['TYPE'],
                                    COMPUTERS=row['COMPUTERS'],
                                    ACTIVITIES=row['ACTIVITIES'],
                                    COMMUNICAT=row['COMMUNICAT'],
                                    WORK_CAB=row['WORK_CAB'],
                                    BUILDINGS=row['BUILDINGS'],
                                    LIBRARY=row['LIBRARY'],
                                    TOYS=row['TOYS'],
                                    EDUCATION=row['EDUCATION'],
                                    CHILDREN=row['CHILDREN'],
                                    TREATMENT=row['TREATMENT'],
                                    FARMING=row['FARMING'],
                                    PRINCIPLE=row['PRINCIPLE'],
                                    FOUNDATION=row['FOUNDATION'],
                                    DEVIATED=row['DEVIATED'],
                                    PARENT=row['PARENT'],
                                    HOLIDAYS=row['HOLIDAYS'],
                                    DIRECTOR=row['REGION'],
                                    PHONE=row['PHONE'],
                                    URL=row['URL'],
                                    BANK=row['BANK'],
                                    PATRONAGE=row['PATRONAGE'],
                                    AGE=row['AGE'],
                                    VEHICLES=row['VEHICLES'],
                                    FED_DISTR=row['FED_DISTR'],
                                    PUBS=row['PUBS'],
                                    VOLUNTEERS=row['VOLUNTEERS'],
                                    ORPHANS=row['ORPHANS'],
                                    HISTORY=row['HISTORY']))
    output.close()
    input.close()


