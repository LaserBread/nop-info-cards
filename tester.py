#!/bin/python3
from lxml import etree

with open("human.svg") as file:
    xml = file.read()

root = etree.fromstring(bytes(xml,encoding = 'utf-8'))
print(root.tag)