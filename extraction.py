# !usr/bin/env python3
# coding: utf-8

import re

# translation of pos tag
cs_pos = {'podstatné jméno' : 'N', 'přídavné jméno' : 'A', 'zájmeno' : 'P', 'číslovka' : 'C', 'sloveso' : 'V', 'příslovce' : 'D', 'předložka' : 'R', 'spojka' : 'J', 'citoslovce' : 'I', 'částice' : 'T'}
en_pos = {'Noun' : 'N', 'Adjective' : 'A', 'Pronoun' : 'P', 'Numeral' : 'C', 'Verb' : 'V', 'Adverb' : 'D', 'Preposition' : 'R', 'Conjugation' : 'J'}

# language recognition
regex1 = {'cs' : r'== čeština ==\n(.*\n)*', 'en' : r'==English==\n(.*\n)*'}

# number of languages for lexeme recognitions
regex2 = {'cs' : r'((?<!=)== )', 'en' : r'((?<!=)==[A-Z])'}

# extraction language
regex3 = {'cs' : r'== čeština ==\n(.*\n)*?(== )', 'en' : r'==English==\n(.*\n)*?(----)'}

# extraction pos
regex4 = {'cs' : r'=={1,} ((podstatné jméno)|(přídavné jméno)|(zájmeno)|(číslovka)|(sloveso)|(příslovce)|(předložka)|(spojka)|(citoslovce)|(částice)) ((\(1\) )|(=={1,}))', 'en' : r'=={1,}((Noun)|(Adjective)|(Pronoun)|(Numeral)|(Verb)|(Adverb)|(Preposition)|(Conjugation))(( \(1\) )|(=={1,}))'}

# extraction wf
regex5 = {'cs' : r'==={1,} související ==={1,}\n(([\*\#].*\n)*)', 'en' : r'==={1,}Derived terms==={1,}\n(.*\n)*?(\n|={1,})'}

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
    text = re.sub(r'\<.*\>', '', text)
    text = text.replace('=', '')
    text = text.replace('* ', '')
    text = text.replace('# ', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace(', ', '\n')
    return set(text.strip().split('\n'))

def en(text):
    def clean(entry):
        entry = entry.replace('{', '')
        entry = entry.replace('}', '')
        entry = entry.replace('* ', '')
        entry = entry.replace('# ', '')
        entry = entry.replace('] ', '')
        entry = entry.replace('[', '')
        entry = entry.replace(']', '')
        entry = entry.replace('|', '')
        return entry
    text = text.replace('|pedia=1', '')
    text = re.sub(r'\{\{(rel)|(der)\-.*?(\}\})', '', text)
    text = re.sub(r'\(.*?(\))|\{[\{\(]taxlink\|.*?(\))', '', text)
    text = re.sub(r'ver=[0-9]*', '', text)
    text = re.sub(r'noshow=1(\s\-\s)*', '', text)
    text = re.sub(r'\|pos=.*?(\}|\|)', '', text)
    text = re.sub(r"[Tt]erm(s)* derived.*?(\}|\])", '', text)
    text = text.replace('\n', '')
    wfs1 = re.findall(r"(\|\-*[\w+['’\.\-\s]{1,}]*\-*[\}\]])", text, flags=re.UNICODE)
    wfs2 = re.findall(r"([\*\#][\s.\w]*\[\[\-*[\w+[’'\.\-\s]*]*\]\])", text, flags=re.UNICODE)
    wfs3 = re.findall(r"(\{der[0-9].*\}\})", text, flags=re.UNICODE)
    wfs = wfs1 + wfs2 + wfs3
    out = set()
    if not (wfs == []):
        for entry in wfs:
            if (entry[0] == '{'):
                entry = re.sub(r'\|\s*\|', '|', entry)
                entry = re.sub(r'\{der[0-9]\|', '', entry)
                entry = re.sub(r'\<.*\>', '', entry)
                entry = re.sub(r'\|*title=.*?(\|)', '', entry)
                entry = re.sub(r'\|*lang=.*?((\|)|(\}\}))', '', entry)
                entry = re.sub(r'\{vern?(\|)', '', entry)
                entry = re.sub(r'\{l\|.*?(\|)', '', entry)
                entry = entry.replace('], ', '\n')
                entry = entry.replace('| ', '\n')
                entry = entry.replace('|', '\n')
                entry = clean(entry)
                entry = re.sub(r'\n.\n', '\n', entry)
                entry = entry.split('\n')
                for w in entry:
                    if not (w == ''): out.add(w.strip())
            else:
                entry = clean(entry)
                if not (entry == ''): out.add(entry.strip())
    return out
