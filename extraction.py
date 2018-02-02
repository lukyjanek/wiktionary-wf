# !usr/bin/env python3
# coding utf-8

import re

def cs(data): # czech language
    infos = re.search(r'== čeština ==\n(.*\n)*', data) # entry contains information for czech
    if (infos):
        more = re.findall(r'((?<!=)== )', infos.group(0)) # number of languages in entry
        if (len(more) > 1):
            only = re.search(r'== čeština ==\n(.*\n)*?(== )', infos.group(0)) # extract czech only
            return only.group(0)
        else:
            return infos.group(0)
    return None

def en(data): # english language
    return data
