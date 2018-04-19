# !usr/bin/env python3
# coding: utf-8

import re

# Extraction patterns
from patterns.langrecog import regex1
from patterns.langsepar import regex2
from patterns.lemmacont import regex3
from patterns.lemmapost import regex4
from patterns.lemmawfs import regex5
from patterns.posdict import *

# Extraction script
def extract(lang, data):
    # entry contains information for language
    infos = re.search(regex1[lang], data)

    if (infos):
        # number of languages in entry
        more = re.findall(regex2[lang], infos.group(0))
        if (len(more) > 1):
            # extract one language only
            infos = re.search(regex3[lang], infos.group(0))
            if not (infos): return None

        # extract pos
        pos = re.search(regex4[lang], infos.group(0))

        # extract wf relations
        wf = ''
        for reg in regex5[lang]:
            derivations = re.search(reg, infos.group(0))
            if not (derivations is None): wf += derivations.group(0)

        # cleaning and returning data
        if not (wf is ''):
            # cleaning data
            wfs = eval(lang)(wf)
            if (pos is None): return pos, wfs
            return eval(lang+'_pos')[pos.group(1)], wfs
    return None

# Cleaning extracted data
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

def de(text):
    text = text.replace('=', '')
    text = text.replace(':', '')
    text = text.replace('{', '')
    text = text.replace('}', '')
    text = text.replace('/', ',')
    text = text.replace(';', ',')
    text = text.replace('Wortbildungen', ',')
    text = text.replace('Verkleinerungsformen', ',')
    text = text.replace('Weibliche Wortformen', ',')
    text = text.replace('Männliche Wortformen', ',')
    text = text.replace('Koseformen', ',')
    text = re.sub(r'\[([0-9][\,\s\-\–]*)*\]', '', text)
    text = re.sub(r'[\-\–].*?(\,|\n)', ',', text)
    text = re.sub(r'\#.*?(\])', '', text)
    text = re.sub(r"\'.*\'", '', text)
    text = text.replace("'", '')
    text = text.replace('\n', '')

    wfs = set()
    for word in text.split(','):
        word = word.strip()
        word = word.replace('[', '')
        word = word.replace(']', '')
        if not (word == ''):
            wfs.add(word)

    return wfs

def fr(text):
    text = re.findall(r'[\{\[](.*?[?\]\}])', text)
    wfs = set()
    for item in text:
        item = item.replace('dérivés', '')
        item = item.replace('apparentés', '')
        item = item.replace('gentilés', '')
        item = item.replace('composés', '')
        item = item.replace('déverbaux', '')
        item = item.replace('comp', '')
        item = item.replace('super', '')
        item = item.replace('lien|', '')
        item = item.replace('recons', '')
        item = item.replace('cf', '')
        item = re.sub(r'sens\=\w+', '', item)
        item = re.sub(r'\|cs(\||\})', '', item)
        item = re.sub(r'\#cs.*?(\])', '', item)
        rep = '|{}[]=#*():'
        for i in rep:
            item = item.replace(i, '')
        item = item.split(',')
        for word in item:
            if not (word == ''):
                wfs.add(word.strip())
    return wfs

def pl(text):
    text = re.findall(r'\[\[(.*?)\]\]', text)
    return set(text)

# project derinet-connect-family (cleaning)
def ze(text):
    return en(text)

def zd(text):
    return de(text)

def zf(text):
    return fr(text)

def zp(text):
    return pl(text)
