# !usr/bin/env python3
# coding: utf-8

"""Regular expression pattern for extraction language content."""

regex3 = {
    'cs': r'== čeština ==\n(.*\n)*?(== )',
    'en': r'==English==\n(.*\n)*?(----)',
    'de': r'Sprache\|Deutsch.*\n(.*\n)*?(== )',
    'fr': r'== \{\{langue\|fr\}\} ==.*\n(.*\n)?(== \{\{langue\|)',
    'pl': r'\{język polski\}.*\n(.*\n)*?(\=\=\s\w+)'
}
