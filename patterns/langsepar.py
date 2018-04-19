# !usr/bin/env python3
# coding: utf-8

# regular expression pattern for languages separator
regex2 = {
    'cs' : r'((?<!=)== )',
    'en' : r'((?<!=)==[A-Z])',
    'de' : r'Sprache\|\w+',
    'fr' : r'\{\{langue\|\w+',
    'pl' : r'\=\=\s\w+',

    'ze' : r'((?<!=)==[A-Z])',
    'zd' : r'Sprache\|\w+',
    'zf' : r'\{\{langue\|\w+',
    'zp' : r'\=\=\s\w+'
}
