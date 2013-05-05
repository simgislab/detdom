detdom
======

Набор скриптов для проекта по созданию геоданных по детдомам

Проект: http://gis-lab.info/qa/geodetdom.html

Обсуждение: http://gis-lab.info/forum/viewtopic.php?f=55&t=12594

 	csv2shp.py - конвертортатор и упаковатор, на входе CSV, на выходе CSVT, VRT, SHP, OSM XML
    csv_split_full.py - на входе общий CSV файл со всеми результатами, на выходе куча CSV файлов по областям
    errors-full.py - генератор таблиц комментариев по каждому региону для вики
    list-result-table.py - Создание вики-таблицы результатов
    regions.py - reusable список регионов и кодов для построения таблиц
    wikitable_reformater-rewrite.py - забирает 80 таблиц регионов с веб-адреса и парсит их в CSV с некоторой переработкой для дальнейшей ручной работы с ними
    
It's ugly and platform-dependent, but it works.