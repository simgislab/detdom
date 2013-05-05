#-*- encoding: utf-8 -*-
# Зачем: Конвертортатор и упаковатор, на входе CSV, на выходе CSVT, VRT, SHP, OSM XML
# Проект: http://gis-lab.info/qa/geodetdom.html
# Обсуждение: http://gis-lab.info/forum/viewtopic.php?f=55&t=12594

import glob
import shutil
import os

def make_vrt(f,fr):
    fvrtname = fr + ".vrt"
    flyrname = fr
    
    vrt = """<OGRVRTDataSource>
    <OGRVRTLayer name="%s">
        <SrcDataSource relativeToVRT="1">%s</SrcDataSource>
        <LayerSRS>EPSG:4326</LayerSRS>
        <GeometryType>wkbPoint</GeometryType>
        <GeometryField encoding="PointFromColumns" x="LON" y="LAT"/>
    </OGRVRTLayer>
</OGRVRTDataSource>""" % (flyrname,f)
    
    fcsvt = open(fvrtname,"w")
    fcsvt.write(vrt)
    fcsvt.close()

def make_csvt(f,fr):
    fcsv = open(f,"r")
    ss = fcsv.readlines()[0]
    fcsv.close()
    
    fields = ss.split(",")
    ss = ""
    for field in fields:
        ss = ss + "\"String(255)\","
    
    fcsvtname = fr + ".csvt"
    fcsvt = open(fcsvtname,"w")
    fcsvt.write(ss[:-1])
    fcsvt.close()
    
def make_shp(f,fr):
    fcsv = open(f,"r")
    ss = fcsv.readlines()[0]
    fcsv.close()
    
    flyrname = fr
    fshpname = fr + ".shp"
    cmd = "ogr2ogr -lco ENCODING=UTF-8 -s_srs \"EPSG:4326\" " + fshpname + " " + f.replace(".csv",".vrt")
    print(cmd)
    os.system(cmd)
    
    shp_7zname = f.replace(".csv","_shp.zip")
    cmd = "C:/tools/zip.exe " + shp_7zname + " " + flyrname+".shp " + flyrname+".shx " + flyrname+".dbf " + flyrname+".prj " + flyrname+".cpg" 
    os.system(cmd)

def csv_7z(f,fr):
    csv_7zname = fr + "_csv.zip"
    cmd = "C:/tools/zip.exe " + csv_7zname + " " + fr + "*"
    os.system(cmd)
    
def make_osm(f,fr):
    fcsv = open(f,"r")
    ss = fcsv.readlines()[0]
    fcsv.close()
    
    cmd = "python c:\gis\osm2shp\ogr2osm.py " + fr + ".vrt"
    os.system(cmd)

def osm_7z(f,fr):
    osm_7zname = fr + "_osm.zip"
    if os.path.isfile(fr + ".osm"):
        cmd = "C:/tools/zip.exe " + osm_7zname + " " + fr + ".osm"
        os.system(cmd)
    
if __name__ == '__main__':
    #working folder, todo: move to params
    os.chdir("results")
    for f in glob.glob("*.csv"):
        fr = f.replace(".csv","")
    
        make_csvt(f,fr)
        make_vrt(f,fr)
        csv_7z(f,fr)
        make_shp(f,fr)
        make_osm(f,fr)
        osm_7z(f,fr)