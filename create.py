from spreadsheet import datatable 
from svg_generator import builder
import subprocess

table = datatable('/home/LaserBread/Downloads/NoP Infocards Master Table.xlsx')
build = builder("./assets/template.svg")
for sp in table.get_all():
    build.build(sp)
    subprocess.run(['inkscape',  '--export-filename=./export/'+sp.name+'.png',  "--export-area-page", 'tmp.svg'])