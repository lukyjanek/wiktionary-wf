# !usr/bin/env python3
# coding: utf-8

class Statistics:
    def __init__(self):
        self.active_lexemes = 0 # number of active lexeme in wiktionary (findable in search engine)
        self.active_one_lang = 0 # number of active lexeme in wiktionary containing information only for output language
        self.active_more_lang = 0 # number of active lexeme in wiktionary containing informations for more language (including output language)
        self.output_vocabulary = set() # vocabulary of lexemes with wf relation (is child or parent)
        self.relations = 0 # number of extracted relations in wiktionary

    def add_active_lexeme(self):
        self.active_lexemes += 1

    def add_active_one_lang(self):
        self.active_one_lang += 1

    def add_active_more_lang(self):
        self.active_more_lang += 1

    def add_vocabulary(self, lexeme):
        self.output_vocabulary.add(lexeme)

    def add_relations(self):
        self.relations += 1

    def get_active_lexeme(self):
        return self.active_lexemes

    def get_active_one_lang(self):
        return self.active_one_lang

    def get_active_more_lang(self):
        return self.active_more_lang

    def get_vocabulary(self):
        return self.output_vocabulary

    def get_relations(self):
        return self.relations

    def get_pos(self):
        pos = dict()
        for i in self.output_vocabulary:
            pos[i.split('_')[1]] += 1
        return pos
