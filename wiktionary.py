# !usr/bin/env python3
# coding: utf-8

from bz2 import BZ2File
import xml.etree.ElementTree as ET
from extraction import extract

path = 'data/enwiktionary-20180120-pages-articles-multistream.xml.bz2'

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
            data = extract(lang=path[5:7], data=element.text) # extraction informations for lexeme
            if not (data is None):
                lexeme_data[title] = data
            tkey = False
        element.clear()

with open('oute.txt', mode='w', encoding='utf-8') as f:
    f.write('Number: ' + str(len(lexeme_data)) + '\n')
    for i,j in lexeme_data.items():
        f.write(i + '\n' + str(j) + '\n\n')

# lexeme_pos = dict() # dict fo known pair of lexeme and pos
# for i,j in lexeme_data.items():
#     lexeme_pos[i] = str(j[0])
#
# lexeme_relations = dict() # dict of relations: lexeme_relations[child] = parent
# for i,j in lexeme_data.items():
#     for lex in j[1]:
#         parent = i + '_' + str(j[0])
#         if (lex in lexeme_pos): child = lex + '_' + lexeme_pos[lex]
#         else: child = lex + '_None'
#         lexeme_relations[child] = parent
#
# lexeme_data = None # allow memory space
#
# with open('output.txt', mode='w', encoding='utf-8') as f:
#     for child,parent in lexeme_relations.items():
#         f.write(child + '\t' + parent + '\n')
