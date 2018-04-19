# !usr/bin/env python3
# coding: utf-8

# regular expression pattern for language recognition
regex1 = {
    'cs' : r'== čeština ==\n(.*\n)*',
    'en' : r'==English==\n(.*\n)*.*',
    'de' : r'Sprache\|Deutsch.*\n(.*\n)*',
    'fr' : r'== \{\{langue\|cs\}\} ==.*\n(.*\n)*',
    'pl' : r'\{język polski\}.*\n(.*\n)*',

    'ze' : r'==Czech==\n(.*\n)*.*',
    'zd' : r'Sprache\|Tschechisch.*\n(.*\n)*',
    'zf' : r'== \{\{langue\|cs\}\} ==.*\n(.*\n)*',
    'zp' : r'\{język czeski\}.*\n(.*\n)*'
}
