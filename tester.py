#!/bin/python3
from lxml import etree

with open("human.svg") as file:
    xml = file.read()

root = etree.fromstring(bytes(xml,encoding = 'utf-8'))

depth = 0

tree = etree.ElementTree(root)
def printspaces(depth): 
    output = ''
    for i in range(0,depth):
        output += ' '
    return(output)

def dispall(element, depth):
    for child in element:
        print(tree.getelementpath(child))
        
        if(child.text):
            print(": "+child.text)
        else:
            print('')

        if(len(child) > 0):
            dispall(child, depth+1)

root.find("svg:g/svg:g[2]/svg:text[7]/svg:tspan/svg:tspan", namespaces={'svg':'http://www.w3.org/2000/svg'}).text = "humma"

print(etree.tostring(root))