#!usr/bin/env python3
# coding: utf-8

"""Code for extraction WF relations using regular expressions."""

import re

# Importing patterns for extraction
from patterns.langrecog import regex1
from patterns.langsepar import regex2
from patterns.lemmacont import regex3
from patterns.lemmapost import regex4
from patterns.lemmawfs import regex5
from patterns.posdict import harmpos


# Extraction
def extract(lang, data):
    """Extract wf relations and return them."""
    # entry containing information for language
    infos = re.search(regex1[lang], data)

    if infos:
        # number of languages in entry
        more = re.findall(regex2[lang], infos.group(0))
        if len(more) > 1:
            # extract one language only
            infos = re.search(regex3[lang], infos.group(0))
            if not infos:
                return None

        # extract pos
        pos = re.search(regex4[lang], infos.group(0))
        if pos is not None:
            pos = harmpos(lang, pos.group(1))

        # extract wf relations
        wf = ''
        for reg in regex5[lang]:
            derivations = re.search(reg, infos.group(0))
            if derivations is not None:
                wf += derivations.group(0)

        # cleaning wf relations
        wfs = None
        if wf:
            wfs = eval(lang)(wf)

        # returning data
        return pos, wfs
    return None


# Cleaning extrated data
def cs(text):
    """Clean Czech extracted data."""
    text = text.replace('=\n', '')
    text = text.replace(' související ', '')

    text = re.sub(r'\<.*\>', '', text)
    text = re.sub(r'\(.*?\)', '', text)

    rep = ('_', '=', '* ', '# ', '(', ')', ']', '[')
    for sign in rep:
        text = text.replace(sign, '')

    text = re.sub(r'(\#.*?)\, ', '', text)

    text = text.replace(' / ', '\n')
    text = text.replace('/', '\n')
    text = text.replace(', ', '\n')

    return set([t for t in text.strip().split('\n') if t])


def en(text):
    """Clean English extracted data."""
    def clean(entry):
        rep = ('(', ')', '{', '}', '* ', '# ', '] ', ']', '[')
        for sign in rep:
            entry = entry.replace(sign, '')
        return entry

    text = text.replace('_', '')
    text = text.replace('|pedia=1', '')

    text = re.sub(r'\{\{(rel)|(der)\-.*?(\}\})', '', text)
    text = re.sub(r'\(.*?(\))|\{[\{\(]taxlink\|.*?(\))', '', text)
    text = re.sub(r'ver=[0-9]*', '', text)
    text = re.sub(r'noshow=1(\s\-\s)*', '', text)
    text = re.sub(r'\|pos=.*?(\}|\|)', '', text)
    text = re.sub(r"[Tt]erm(s)* derived.*?(\}|\])", '', text)

    text = text.replace('\n', '')

    wfs = list()
    r1 = r"(\|\-*[\w+['’\.\-\s]{1,}]*\-*[\}\]])"
    wfs += re.findall(r1, text, flags=re.UNICODE)

    r2 = r"([\*\#][\s.\w]*\[\[\-*[\w+[’'\.\-\s]*]*\]\])"
    wfs += re.findall(r2, text, flags=re.UNICODE)

    wfs += re.findall(r"(\{der[0-9].*\}\})", text, flags=re.UNICODE)

    out = set()
    if wfs != list():
        for entry in wfs:
            if entry[0] == '{':
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

                [out.add(w.strip()) for w in entry.split('\n') if w.strip()]

            else:
                entry = clean(entry)
                if entry.strip():
                    out.add(entry.strip())
    return out


def de(text):
    """Clean German extracted data."""
    rep = ('_', '=', ':', '{', '}')
    for sign in rep:
        text = text.replace(sign, '')

    rep = ('/', ';', 'Wortbildungen', 'Verkleinerungsformen', 'Wortbildungen',
           'Weibliche Wortformen', 'Männliche Wortformen', 'Koseformen')
    for sign in rep:
        text = text.replace(sign, ',')

    text = re.sub(r'\[([0-9][\,\s\-\–]*)*\]', '', text)
    text = re.sub(r'[\-\–].*?(\,|\n)', ',', text)
    text = re.sub(r'\#.*?(\])', '', text)
    text = re.sub(r"\'.*\'", '', text)
    text = re.sub(r'(\#.*?)\, ', '', text)

    rep = ("'", '\n', '[', ']', '(', ')')
    for sign in rep:
        text = text.replace(sign, '')

    wfs = set()
    [wfs.add(word.strip()) for word in text.split(',') if word.strip()]

    return wfs


def fr(text):
    """Clean French extracted data."""
    text = re.findall(r'[\{\[](.*?[?\]\}])', text)

    wfs = set()
    for item in text:
        rep = ('_', 'dérivés', 'apparentés', 'gentilés', 'composés',
               'déverbaux', 'comp', 'super', 'lien|', 'recons', 'cf')
        for sign in rep:
            item = item.replace(sign, '')

        item = re.sub(r'sens\=\w+', '', item)
        item = re.sub(r'\|cs(\||\})', '', item)
        item = re.sub(r'\#cs.*?(\])', '', item)

        rep = '|{}[]=#*():'
        for i in rep:
            item = item.replace(i, '')

        [wfs.add(word.strip()) for word in item.split(',') if word.strip()]

    return wfs


def pl(text):
    """Clean Polish extracted data."""
    text = text.replace('_', '')
    text = re.findall(r'\[\[(.*?)\]\]', text)
    return set(text)
