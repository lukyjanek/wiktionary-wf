# !usr/bin/env python3
# coding: utf-8

from derinet.derinet import DeriNet
from derinet.utils import Node

def wkt_data(path): # loading data
    relations = dict()
    wordlist = set()
    with open(path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split('\t')
            relations[line[0]] = line[1]
            wordlist.add(line[0])
            wordlist.add(line[1])
    return relations, wordlist

def comparison(der, wordlist, relations, name):
    # comparison 1: is lexeme from Wiktionary in or out of DeriNet
    def inDeriNet(word):
        lexeme = word.split('_')[0]
        pos = word.split('_')[1]
        try:
            if (pos == 'N') or (pos == 'A') or (pos == 'D') or (pos == 'V'): state = der.get_lexeme(node=lexeme, pos=pos)
            else: state = der.get_lexeme(node=lexeme)
            return True
        except:
            return False
    inside = 0
    outside = 0
    outside_list = list()
    for word in wordlist:
        if (inDeriNet(word) is True): inside +=1
        else:
            outside += 1
            outside_list.append(word)
    one_word = list()
    more_word = list()
    for w in outside_list:
        if (' ' in w): more_word.append(w)
        else: one_word.append(w)
    with open('output/' + name[:2].lower() + '-in-or-out-derinet.txt', mode='w', encoding='utf-8') as f:
        f.write(name + ' MUTATION OF WIKTIONARY COMPARED WITH DERINET\n')
        f.write('Number of lexemes in Wiktionary AND DeriNet: ' + str(inside) + '\n')
        f.write('Number of lexemes in Wiktionary NOT in DeriNet: ' + str(outside) + '\n')
        f.write('- one-word lexemes: ' + str(len(one_word)) + '\n')
        f.write('- more-word lexemes: ' + str(len(more_word)) + '\n')
        f.write('List of those lexemes:\n')
        for w in one_word:
            f.write(w + '\n')
        for w in more_word:
            f.write(w + '\n')
    # comparison 2: has or has not lexeme from DeriNet parents in Wiktionary (without harmonization)
    with_parent = 0
    with_parent_dict = dict()
    parent_in_derinet = 0
    derinet_roots = list()
    for node in der._data:
        if (node.parent_id == ''):
            derinet_roots.append(node)
    for node in derinet_roots:
        if (node.lemma + '_' + node.pos in relations):
            with_parent += 1
            with_parent_dict[node.lemma + '_' + node.pos] = relations[node.lemma + '_' + node.pos]
            if (inDeriNet(relations[node.lemma + '_' + node.pos]) is True): parent_in_derinet +=1
        elif (node.lemma + '_None' in relations):
            with_parent += 1
            with_parent_dict[node.lemma + '_' + node.pos] = relations[node.lemma + '_None']
            if (inDeriNet(relations[node.lemma + '_None']) is True): parent_in_derinet +=1
    with open('output/' + name[:2].lower() + '-parent-wkt-not-derinet.txt', mode='w', encoding='utf-8') as f:
        f.write(name + ' MUTATION OF WIKTIONARY COMPARED WITH DERINET\n')
        f.write('Number of lexemes having parent in Wiktionary and not in DeriNet (and founded parent exists in DeriNet a lexeme): ' + str(parent_in_derinet) + '\n')
        f.write('Number of lexemes having parent in Wiktionary and not in DeriNet: ' + str(with_parent) + '\n')
        f.write('List of those lexemes:\n')
        f.write('[DeriNet root | parent]\n')
        for child,parent in with_parent_dict.items():
            f.write(child + '\t' + parent + '\n')

if (__name__ == '__main__'):
    der = DeriNet('data/derinet-1-5-1.tsv')
    relations, wordlist = wkt_data('data/cs_wkt.txt')
    comparison(der, wordlist, relations, 'CZECH')
    relations, wordlist = wkt_data('data/en_wkt.txt')
    comparison(der, wordlist, relations, 'ENGLISH')
