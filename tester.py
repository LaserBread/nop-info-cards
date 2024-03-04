#!/bin/python3
from lxml import etree

with open("human.svg") as file:
    xml = file.read()

root = etree.fromstring(bytes(xml,encoding = 'utf-8'))
image = root.getroot()
para = image.findall('svg')

for e in para:
    etree.dump(e)