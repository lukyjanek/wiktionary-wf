# !usr/bin/env python3
# coding: utf-8

import re

cs_pos = {'podstatné jméno' : 'N', 'přídavné jméno' : 'A', 'zájmeno' : 'P', 'číslovka' : 'C', 'sloveso' : 'V', 'příslovce' : 'D', 'předložka' : 'R', 'spojka' : 'J', 'citoslovce' : 'I', 'částice' : 'T'}

def cs(data): # czech language
    infos = re.search(r'== čeština ==\n(.*\n)*', data) # entry contains information for czech
    if (infos):
        more = re.findall(r'((?<!=)== )', infos.group(0)) # number of languages in entry
        if (len(more) > 1):
            infos = re.search(r'== čeština ==\n(.*\n)*?(== )', infos.group(0)) # extract czech only
        pos = re.search(r'=== ((podstatné jméno)|(přídavné jméno)|(zájmeno)|(číslovka)|(sloveso)|(příslovce)|(předložka)|(spojka)|(citoslovce)|(částice)) ((\(1\) )|(===))', infos.group(0)) # extract pos
        wf = re.search(r'==== související ====\n(([\*\#].*\n)*)', infos.group(0)) #extract wf relations
        if not (wf is None):
            wfs = wf.group(1).replace('==== související ====\n', '') # clean data
            wfs = wfs.replace('* ', '')
            wfs = wfs.replace('# ', '')
            wfs = wfs.replace('[[', '')
            wfs = wfs.replace(']]', '')
            wfs = wfs.replace(']]', '')
            wfs = wfs.replace(', ', '\n')
            if (pos is None): return pos, wfs.strip().split('\n')
            return cs_pos[pos.group(1)], wfs.strip().split('\n')
    return None

def en(data): # english language
    return data
