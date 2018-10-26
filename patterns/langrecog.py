# !usr/bin/env python3
# coding: utf-8

"""Regular expression patterns for language recognition."""

regex1 = {
    'cs': r'== čeština ==\n(.*\n)*',
    'en': r'==English==\n(.*\n)*.*',
    'de': r'Sprache\|Deutsch.*\n(.*\n)*',
    'fr': r'== \{\{langue\|fr\}\} ==.*\n(.*\n)*',
    'pl': r'\{język polski\}.*\n(.*\n)*'
}
