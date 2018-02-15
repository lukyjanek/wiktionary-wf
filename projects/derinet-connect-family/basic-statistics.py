# !usr/bin/env python3
# coding: utf-8

from collections import defaultdict
from derinet.derinet import DeriNet

def wkt(path, name):
    def counting(dic, x): # counting function for questions 4 and 5
        item_number = defaultdict(int)
        y = 0
        for i,j in dic.items():
            item_number[len(j)] += 1
            y += 1
        item_number[0] = x - y
        return item_number
    # 1. how many relations does this resource contain?
    relations = dict()
    # 2. how many lexemes does this resource contain?
    wordlist = set()
    with open(path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split('\t')
            relations[line[0]] = line[1]
            wordlist.add(line[0])
            wordlist.add(line[1])
    # 3. how many lexemes does the part-of-speech tags include?
    word_pos = defaultdict(int)
    for word in wordlist:
        word = word.split('_')
        word_pos[word[1]] += 1
    # 4. how many children has every parent got?
    parent_children = dict()
    for child,parent in relations.items():
        if not (parent in parent_children):
            parent_children[parent] = list()
        parent_children[parent].append(child)
    parent_children = counting(parent_children, len(wordlist))
    # 5. how many parents has every child got?
    child_parents = dict()
    for child,parent in relations.items():
        if not (child in child_parents):
            child_parents[child] = list()
        child_parents[child].append(parent)
    child_parents = counting(child_parents, len(wordlist))
    # 6. how many propriums does Wiktioary contain?
    # 7. how many more-word lexemes Wiktionary contain?
    propriums = 0
    more_word = 0
    for word in wordlist:
        if (word[:1].isupper() is True): propriums += 1
        if (' ' in word): more_word += 1
    # save results
    with open('output/' + name[:2].lower() + '-basic-statistics.txt', mode='a', encoding='utf-8') as f:
        f.write(name + ' MUTATION OF WIKTIONARY\n')
        f.write('Number of lexemes: ' + str(len(wordlist)) + '\n')
        f.write('Number of relations: ' + str(len(relations)) + '\n')
        f.write('Number of propriums: ' + str(propriums) + '\n')
        f.write('Number of more-word lexemes: ' + str(more_word) + '\n')
        f.write('Number of lexemes by part-of-speech [columns: pos|number]\n')
        for w,p in sorted(word_pos.items()):
            f.write(str(w) + '\t' + str(p) + '\n')
        f.write('Number of children by lexeme [columns: children|lexeme]\n')
        for i,n in sorted(parent_children.items()):
            f.write(str(i) + '\t' + str(n) + '\n')
        f.write('Number of parents by lexeme [columns: parents|lexeme]\n')
        for i,n in sorted(child_parents.items()):
            f.write(str(i) + '\t' + str(n) + '\n')

def derinet(path, name):
    der = DeriNet(path)
    # 1. how many lexemes does this resource contain?
    wordlist = len(der._data)
    relations = 0
    propriums = 0
    more_word = 0
    word_pos = defaultdict(int)
    parent_children = defaultdict(int)
    for node in der._data:
        # 2. how many relations does this resource contain?
        if not (node.parent_id == ''):
            relations += 1
        # 3. how many lexemes does the part-of-speech tags include?
        word_pos[node.pos[0]] += 1
        # 4. how many children has every parent got?
        parent_children[len(node.children)] += 1
        # 5. how many propriums does Wiktioary contain?
        if (node.lemma[:1].isupper() is True): propriums += 1
        # 6. how many more-word lexemes Wiktionary contain?
        if (' ' in node.lemma): more_word += 1
    # 7. how many parents has every child got?
    child_parents = {0 : len(der._roots), 1 : len(der._data)-len(der._roots)}
    # save results
    with open('output/' + name[:3].lower() + '-basic-statistics.txt', mode='a', encoding='utf-8') as f:
        f.write(name + '\n')
        f.write('Number of lexemes: ' + str(wordlist) + '\n')
        f.write('Number of relations: ' + str(relations) + '\n')
        f.write('Number of propriums: ' + str(propriums) + '\n')
        f.write('Number of more-word lexemes: ' + str(more_word) + '\n')
        f.write('Number of lexemes by part-of-speech [columns: pos|number]\n')
        for w,p in sorted(word_pos.items()):
            f.write(str(w) + '\t' + str(p) + '\n')
        f.write('Number of children by lexeme [columns: children|lexeme]\n')
        for i,n in sorted(parent_children.items()):
            f.write(str(i) + '\t' + str(n) + '\n')
        f.write('Number of parents by lexeme [columns: parents|lexeme]\n')
        for i,n in sorted(child_parents.items()):
            f.write(str(i) + '\t' + str(n) + '\n')

if (__name__ == '__main__'):
    wkt('data/cs_wkt.txt', 'CZECH')
    wkt('data/en_wkt.txt', 'ENGLISH')
    derinet('data/derinet-1-5-1.tsv', 'DERINET')