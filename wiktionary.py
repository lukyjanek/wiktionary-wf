#!usr/bin/env python3
# coding: utf-8

"""Main script for creating wf relation database using wiktionary data."""

import argparse
import string as str
from bz2 import BZ2File
import xml.etree.ElementTree as ET
from collections import defaultdict
from extraction import extract


# Arguments parsing
parser = argparse.ArgumentParser()

parser.add_argument('-d', action='store', dest='d', required=True,
                    help='path to the .bz2 Wiktionary data')
parser.add_argument('-l', action='store', dest='l', required=True,
                    help='language abr. of Wiktionary data')
parser.add_argument('-o', action='store', dest='o', required=True,
                    help='path to the output file')

par = parser.parse_args()


# Preprocessing and extraction
print('Info: Loading and extracting data...')
lexeme_wfs = defaultdict()  # dict of extracted wfs for lemma
lexeme_pos = defaultdict()  # dict of pos for lemma
with BZ2File(par.d) as xml_file:
    parser = ET.iterparse(xml_file)
    tkey = False

    for event, element in parser:
        # extract main lemma
        if element.tag[43:] == 'title':
            title = element.text

        # unlock saving lemma if it is lemma
        elif element.tag[43:] == 'ns' and element.text == '0':
            tkey = True

        # extract information about lemma
        elif element.tag[43:] == 'text' and tkey is True:
            # extract pos and wf: data = ('pos', {child1, child2, ...})
            data = None
            if element.text is not None:
                data = extract(lang=par.l, data=element.text)

            if data is not None:  # save pos
                if data[0] is not None:
                    lexeme_pos[title] = data[0]

                if data[1] not in (None, set()):  # save wfs
                    wfs = set([lem for lem in data[1] if lem != title])
                    lexeme_wfs[title] = wfs

            tkey = False
        element.clear()
print('Info: Data loaded and extracted.')


# Part-of-speech tagging from wiktionary and WF relations connecting
print('Info: Tagging lemmas of extracted wf relations...')
separator = '_'
lexeme_relations = defaultdict(set)  # dict of pos tagged relations
for parent, wfs in lexeme_wfs.items():
    parent += separator + lexeme_pos.get(parent, 'X')

    for child in wfs:
        child += separator + lexeme_pos.get(child, 'X')

        # exclude: digits, afixes, multiword units, abbreviations
        res = list()
        res.append(any(i.isdigit() for i in parent))  # digits
        res.append(any(i.isdigit() for i in child))  # digits
        res.append(parent[0] in str.punctuation)  # afixes
        res.append(parent[-3] in str.punctuation)  # afixes
        res.append(child[0] in str.punctuation)  # afixes
        res.append(child[-3] in str.punctuation)  # afixes
        res.append(any(i in (' ', '-') for i in parent))  # multiword units
        res.append(any(i in (' ', '-') for i in child))  # multiword units
        res.append(parent.isupper())  # abbreviations
        res.append(child.isupper())  # abbreviations

        if not any(res):
            lexeme_relations[parent].add(child)
print('Info: Lemmas tagged.')


# Saving data
print('Info: Saving data to file...')
with open(par.o, mode='w', encoding='utf-8') as f:
    for parent in sorted(lexeme_relations):
        for child in sorted(lexeme_relations[parent]):
            f.write(parent + '\t' + child + '\n')
print('Info: Data saved.')
print('Info: Complete.')
