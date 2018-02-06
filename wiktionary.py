# !usr/bin/env python3
# coding: utf-8

from bz2 import BZ2File
import xml.etree.ElementTree as ET
from extraction import extract
from statistics import Statistics

path = 'data/cswiktionary-20180120-pages-articles-multistream.xml.bz2'

stat = Statistics() # for output statistics

# Preprocessing and extraction
lexeme_data = dict()
with BZ2File(path) as xml_file:
    parser = ET.iterparse(xml_file)
    tkey = False
    for event, element in parser:
        if (element.tag[43:] == 'title'): # lexeme
            title = element.text
        elif (element.tag[43:] == 'ns') and (element.text == '0'): # unlock saving lexeme if it is lexeme
            tkey = True
            stat.add_active_lexeme()
        elif (element.tag[43:] == 'text') and (tkey is True): # save informations about lexeme
            data = extract(lang=path[5:7], data=element.text) # extraction informations for lexeme
            if not (data is None):
                if not (data[1] == set()):
                    lexeme_data[title] = data
            tkey = False
        element.clear()

# # Testing
# with open('oute.txt', mode='w', encoding='utf-8') as f:
#     f.write('Number: ' + str(len(lexeme_data)) + '\n')
#     for i,j in lexeme_data.items():
#         f.write(i + '\n' + str(j) + '\n\n')

# Part-of-speech tagging
lexeme_pos = dict() # dict for known pair of lexeme and pos
for i,j in lexeme_data.items():
    lexeme_pos[i] = str(j[0])

# Part-of-speech tagging and WF relations making
lexeme_relations = dict() # dict of relations: lexeme_relations[child] = parent
for i,j in lexeme_data.items():
    for lex in j[1]:
        parent = i + '_' + str(j[0])
        if (lex in lexeme_pos): child = lex + '_' + lexeme_pos[lex]
        else: child = lex + '_None'
        lexeme_relations[child] = parent
        stat.add_vocabulary(child)
        stat.add_vocabulary(parent)
        stat.add_relations()

lexeme_data = None # allow memory space

# Saving data
with open('output/' + path[5:7] + '_data.txt', mode='w', encoding='utf-8') as f:
    for child,parent in lexeme_relations.items():
        f.write(child + '\t' + parent + '\n')

# Saving statistics
with open('output/STATISTICS.txt', mode='a', encoding='utf-8') as f:
    f.write(path[5:7].upper() + '\n')
    f.write('Number of active lexemes in Wiktionary: ' + str(stat.get_active_lexeme()) + '\n')
    f.write('Number of extracted lexemes with wf from Wiktionary: ' + str(len(stat.get_vocabulary())) + '\n')
    f.write('Number of extracted wf relations: ' + str(stat.get_relations()) + '\n')
    f.write('Number of lexemes by part-of-speech:' + '\n')
    for pos,num in sorted(stat.get_pos().items()):
        f.write(str(pos) + '\t' + str(num) + '\n')
    f.write('\n\n')
