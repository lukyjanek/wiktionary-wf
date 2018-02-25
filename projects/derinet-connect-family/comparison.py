# !usr/bin/env python3
# coding: utf-8

from collections import defaultdict
from derinet.derinet import DeriNet
from derinet.utils import Node

def load_wkt(path): # loading Wiktionary data
    relations = defaultdict(set)
    wordlist = set()
    with open(path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split('\t')
            relations[line[0]].add(line[1])
            wordlist.add(line[0])
            wordlist.add(line[1])
    return wordlist, relations

def inDeriNet(word): # function given boolean about existence in DeriNet
    lexeme = word.split('_')[0]
    pos = word.split('_')[1]
    try:
        if (pos == 'N') or (pos == 'A') or (pos == 'D') or (pos == 'V'): state = der.get_lexeme(node=lexeme, pos=pos)
        else: state = der.get_lexeme(node=lexeme)
        return True
    except:
        return False

def search(nl, target): # searching in recursive list (DeriNet's subtree of lexeme)
    for node in nl:
        if type(node) is list:
            if search(node, target):
                return True
        if node == target:
            return True
    return False

def exist_in_derinet(der, wordlist):
    inside = set()
    inside_one = set() # set of lexeme in DeriNet consisting of one word
    inside_more = set() # set of lexeme in DeriNet consisting of more words
    outside = set()
    outside_one = set() # set of lexeme out of DeriNet consisting of one word
    outside_more = set() # set of lexeme out of DeriNet consisting of more words

    for word in wordlist:
        if (inDeriNet(word) is True):
            if (' ' in word): inside_more.add(word)
            else: inside_one.add(word)
            inside.add(word)
        else:
            if (' ' in word): outside_more.add(word)
            else: outside_one.add(word)
            outside.add(word)
    return inside, outside, inside_more, inside_one, outside_more, outside_one

def parents_for_derinet_root(der, relations):
    # potential parents from Wiktionary for DeriNet's roots
    allparents = defaultdict(set)
    for nodeid in der._roots:
        root = der.get_lexeme(nodeid).lemma + '_'
        if (root + der.get_lexeme(nodeid).pos[0] in relations):
            for parent in relations[root + der.get_lexeme(nodeid).pos[0]]:
                allparents[root + der.get_lexeme(nodeid).pos].add(parent)
        elif (root + 'None' in relations):
            for parent in relations[root + 'None']:
                allparents[root + der.get_lexeme(nodeid).pos].add(parent)

    # potential parents from Wiktionary for DeriNet's root existed in DeriNet
    existedparents = defaultdict(set)
    for root,parents in allparents.items():
        for parent in parents:
            if (inDeriNet(parent) is True):
                existedparents[root].add(parent)
    return existedparents

def filter_parents_out(der, dic): # filter parents which are childs of root
    parentsout = defaultdict(set)
    for root, parents in dic.items():
        for parent in parents:
            subtree = der.get_subtree(node=root.split('_')[0], pos=root.split('_')[1])
            if (parent.split('_')[1] == 'N') or (parent.split('_')[1] == 'A') or (parent.split('_')[1] == 'V') or (parent.split('_')[1] == 'D'):
                if (search(subtree, der.get_lexeme(node=parent.split('_')[0], pos=parent.split('_')[1])) is False):
                    parentsout[root].add(parent)
            elif (search(subtree, der.get_lexeme(node=parent.split('_')[0])) is False):
                parentsout[root].add(parent)
    return parentsout

def filter_composites(dic):
    noncomposites = defaultdict()
    composites = defaultdict()
    for root,parents in dic.items():
        if (root.split('_')[1][-1] == 'C'):
            composites[root] = parents
        else:
            noncomposites[root] = parents
    return composites, noncomposites

def filter_length(dic):
    out = defaultdict(set)
    for root,parents in dic.items():
        parents = list(parents)
        if (len(parents) == 1):
            if (len(root) < len(parents[0])):
                out[parents[0]].add(root)
            else:
                out[root].add(parents[0])
        else:
            for parent in parents:
                out[root].add(parent)
    return out


def merge_dicts(dic1, dic2):
    outdic = defaultdict(set)
    for root,parents in dic1.items():
        for parent in parents:
            outdic[root].add(parent)
    for root,parents in dic2.items():
        for parent in parents:
            outdic[root].add(parent)
    return outdic

def print_existance(namefolder, nameside, side, side_one, side_more):
    with open('output/' + namefolder + '/wkt-' + nameside + '-derinet.txt', mode='w', encoding='utf-8') as f:
        f.write('Number of lexemes in Wiktionary ' + nameside + ' DeriNet (all): ' + str(len(side)) + '\n')
        f.write('Number of lexemes in Wiktionary ' + nameside + ' DeriNet (one-word): ' + str(len(side_one)) + '\n')
        f.write('Number of lexemes in Wiktionary ' + nameside + ' DeriNet (more-word): ' + str(len(side_more)) + '\n')
        f.write('===========\n')
        f.write('ALL\n')
        f.write('===========\n')
        for w in side:
            f.write(w + '\n')
        f.write('===========\n')
        f.write('ONE-WORD\n')
        f.write('===========\n')
        for w in side_one:
            f.write(w + '\n')
        f.write('===========\n')
        f.write('MORE-WORD\n')
        f.write('===========\n')
        for w in side_more:
            f.write(w + '\n')

def print_root_parents(namefolder, note, dic):
    with open('output/' + namefolder + '/parent-for-derinets-roots-' + note + '.txt', mode='w', encoding='utf-8') as f:
        f.write('Number of DeriNets roots in this file: ' + str(len(dic)) + '\n')
        f.write('===========\n')
        for root in sorted(dic, key=lambda root: len(dic[root]), reverse=True):
            parents = list(dic[root])
            strparents = parents[0]
            for parent in parents[1:]:
                strparents += '; ' + parent
            f.write(root + '\t' + strparents + '\n')

if (__name__ == '__main__'):
    der = DeriNet('data/derinet-1-5-1.tsv')

    # english mutation of Wiktionary
    enwordlist, enrelations = load_wkt('data/en_wkt.txt')
    eninside, enoutside, eninside_more, eninside_one, enoutside_more, enoutside_one = exist_in_derinet(der, enwordlist)
    enexistedparents = parents_for_derinet_root(der, enrelations)
    enjustparents = filter_parents_out(der, enexistedparents)
    encomposites, enothers = filter_composites(enjustparents)

    encomposites = filter_length(encomposites)
    enothers = filter_length(enothers)

    print_existance('en', 'inside', eninside, eninside_one, eninside_more)
    print_existance('en', 'outside', enoutside, enoutside_one, enoutside_more)

    print_root_parents('en', 'comp', encomposites)
    print_root_parents('en', 'notcomp', enothers)

    # czech mutation of Wiktionary
    cswordlist, csrelations = load_wkt('data/cs_wkt.txt')
    csinside, csoutside, csinside_more, csinside_one, csoutside_more, csoutside_one = exist_in_derinet(der, cswordlist)
    csexistedparents = parents_for_derinet_root(der, csrelations)
    csjustparents = filter_parents_out(der, csexistedparents)
    cscomposites, csothers = filter_composites(csjustparents)

    cscomposites = filter_length(cscomposites)
    csothers = filter_length(csothers)

    print_existance('cs', 'inside', csinside, csinside_one, csinside_more)
    print_existance('cs', 'outside', csoutside, csoutside_one, csoutside_more)

    print_root_parents('cs', 'comp', cscomposites)
    print_root_parents('cs', 'notcomp', csothers)

    # merging lists
    mergedcomposites = merge_dicts(cscomposites, encomposites)
    mergedcomposites = filter_length(mergedcomposites)
    print_root_parents('', 'merged-comp', mergedcomposites)

    mergedjust = merge_dicts(csothers, enothers)
    mergedjust = filter_length(mergedjust)
    print_root_parents('', 'merged-notcomp', mergedjust)
