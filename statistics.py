# !usr/bin/env python3
# coding: utf-8

from collections import defaultdict

class Statistics:
    def __init__(self):
        self.output_vocabulary = set() # vocabulary of lexemes with wf relation (is child or parent)
        self.active_lexemes = 0 # number of active lexeme in wiktionary (findable in search engine)
        self.relations = 0 # number of extracted relations in wiktionary

    def add_active_lexeme(self):
        self.active_lexemes += 1

    def add_vocabulary(self, lexeme):
        self.output_vocabulary.add(lexeme)

    def add_relations(self):
        self.relations += 1

    def get_active_lexeme(self):
        return self.active_lexemes

    def get_vocabulary(self):
        return self.output_vocabulary

    def get_relations(self):
        return self.relations

    def get_pos(self):
        pos = defaultdict(int)
        for i in self.output_vocabulary:
            w = i.split('_')[1]
            pos[w] += 1
        return pos
