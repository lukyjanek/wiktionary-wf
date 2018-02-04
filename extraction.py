# !usr/bin/env python3
# coding: utf-8

import re

# translation of pos tag
cs_pos = {'podstatné jméno' : 'N', 'přídavné jméno' : 'A', 'zájmeno' : 'P', 'číslovka' : 'C', 'sloveso' : 'V', 'příslovce' : 'D', 'předložka' : 'R', 'spojka' : 'J', 'citoslovce' : 'I', 'částice' : 'T'}
en_pos = {'Noun' : 'N', 'Adjective' : 'A', 'Pronoun' : 'P', 'Numeral' : 'C', 'Verb' : 'V', 'Adverb' : 'D', 'Preposition' : 'R', 'Conjugation' : 'J'}

# language recognition
regex1 = {'cs' : r'== čeština ==\n(.*\n)*', 'en' : r'==English==\n(.*\n)*'}

# number of languages for lexeme recognitions
regex2 = {'cs' : r'((?<!=)== )', 'en' : r'----'}

# extraction language
regex3 = {'cs' : r'== čeština ==\n(.*\n)*?(== )', 'en' : r'==English==\n(.*\n)*?(----)'}

# extraction pos
regex4 = {'cs' : r'=={1,} ((podstatné jméno)|(přídavné jméno)|(zájmeno)|(číslovka)|(sloveso)|(příslovce)|(předložka)|(spojka)|(citoslovce)|(částice)) ((\(1\) )|(=={1,}))', 'en' : r'=={1,}((Noun)|(Adjective)|(Pronoun)|(Numeral)|(Verb)|(Adverb)|(Preposition)|(Conjugation))(( \(1\) )|(=={1,}))'}

# extraction wf
regex5 = {'cs' : r'==={1,} související ==={1,}\n(([\*\#].*\n)*)', 'en' : r'==={1,}Derived terms==={1,}\n(.*\n)*?(\n)'}

def extract(lang, data):
    infos = re.search(regex1[lang], data) # entry contains information for language
    if (infos):
        more = re.findall(regex2[lang], infos.group(0)) # number of languages in entry
        if (len(more) > 1):
            infos = re.search(regex3[lang], infos.group(0)) # extract one language only
            if not (infos): return None
        pos = re.search(regex4[lang], infos.group(0)) # extract pos
        wf = re.search(regex5[lang], infos.group(0)) # extract wf relations
        if not (wf is None):
            wfs = eval(lang)(wf.group(0)) # cleaning data, how dangerous 'eval()' is?
            if (pos is None): return pos, wfs
            return eval(lang+'_pos')[pos.group(1)], wfs # how dangerous 'eval()' is?
    return None

# cleaning wf relations
def cs(text):
    text = text.replace('=\n', '')
    text = text.replace(' související ', '')
    text = text.replace('=', '')
    text = text.replace('* ', '')
    text = text.replace('# ', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace(', ', '\n')
    return text.strip().split('\n')

def en(text):
    text = text.replace('|pedia=1', '')
    text = text.replace('\n', '')
    wfs = re.findall(r"(\|\-*\w+(['\-\s]\w+)*\})|([\*\#]\s\[\[\-*\w+(['\-\s]\w+)*\]\])|(\{der[0-9].*?(\}\}))", text, flags=re.UNICODE)
    out = list()
    for i in wfs:
        for j in i:
            if not (j == ''):
                if not (j[0] == '{'):
                    j = j.replace('|', '')
                    j = j.replace('}', '')
                    j = j.replace('* ', '')
                    j = j.replace('# ', '')
                    j = j.replace('[', '')
                    j = j.replace(']', '')
                    out.append(j)
                else:
                    j = re.sub(r'\{der[0-9]\|', '', j)
                    j = re.sub(r'\<.*\>', '', j)
                    j = re.sub(r'\|*lang=.*?((\|)|(\}\}))', '', j)
                    j = re.sub(r'\{l\|.*?(\|)', '', j)
                    j = j.replace('{', '')
                    j = j.replace('}', '')
                    j = j.replace('[', '')
                    j = j.replace('], ', '|')
                    j = j.replace('] ', '')
                    j = j.replace(']', '')
                    j = j.replace('|', '\n')
                    j = j.split('\n')
                    for k in j:
                        out.append(k)
    return out
