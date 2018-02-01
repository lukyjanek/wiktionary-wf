# !urs/bin/env python3
# coding: utf-8

from bz2 import BZ2File
import xml.etree.ElementTree as ET

path = 'data/enwiktionary-20180120-pages-articles-multistream.xml.bz2'

c = 0
with BZ2File(path) as xml_file:
    parser = ET.iterparse(xml_file)
    for event, element in parser:
        # print(event, element.tag[43:], element.attrib, element.text)
        c += 1
        element.clear()
print(c)
