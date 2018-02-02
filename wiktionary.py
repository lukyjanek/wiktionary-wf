# !urs/bin/env python3
# coding: utf-8

from bz2 import BZ2File
import xml.etree.ElementTree as ET
from extraction import *

path = 'data/cswiktionary-20180120-pages-articles-multistream.xml.bz2'

lexeme_data = dict()
with BZ2File(path) as xml_file:
    parser = ET.iterparse(xml_file)
    tkey = False
    for event, element in parser:
        if (element.tag[43:] == 'title'): # lexeme
            title = element.text
        elif (element.tag[43:] == 'ns') and (element.text == '0'): # unlock saving lexeme if it is lexeme
            tkey = True
        elif (element.tag[43:] == 'text') and (tkey is True): # save informations about lexeme
            data = eval(path[5:7])(element.text) # choose right function for extraction (how dangerous 'eval()' is?)
            if not (data is None):
                lexeme_data[title] = data
            tkey = False
        element.clear()

with open('pokus.txt', mode='w', encoding='utf-8') as f:
    f.write('Number of lexemes: ' + str(len(lexeme_data)) + '\n\n')
    for i,j in lexeme_data.items():
        f.write(i + '\n' + j + '\n')
