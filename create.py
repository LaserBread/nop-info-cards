#!/bin/python3
from spreadsheet import datatable 
from svg_generator import builder
import subprocess
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
table = datatable('./card-table.xlsx')
build = builder("./assets/template.svg")
for sp in table.get_all():
    build.build(sp)
    subprocess.run(['inkscape',  '--export-filename=./export/'+sp.name+'.png',  "--export-area-page", 'tmp.svg'])
    
os.remove("./tmp.svg")
