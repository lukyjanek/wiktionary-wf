#!usr/bin/env python3
# coding: utf-8

"""Dictionaries of part-of-speech tags in all used wiktionary mutations."""


def harmpos(lang, tag):
    """Choose right dictionary and return tag (Hajič's) for given pos name."""
    return pos[lang].get(tag, None)


pos = {
    'cs': {'podstatné jméno': 'N', 'přídavné jméno': 'A', 'zájmeno': 'P',
           'číslovka': 'C', 'sloveso': 'V', 'příslovce': 'D', 'předložka': 'R',
           'spojka': 'J', 'citoslovce': 'I', 'částice': 'T'},

    'en': {'Noun': 'N', 'Adjective': 'A', 'Pronoun': 'P', 'Numeral': 'C',
           'Verb': 'V', 'Adverb': 'D', 'Preposition': 'R', 'Conjugation': 'J'},

    'de': {'Substantiv': 'N', 'Adjektiv': 'A', 'Interrogativpronomen': 'P',
           'Demonstrativpronomen': 'P', 'Numerale': 'C', 'Verb': 'V',
           'Adverb': 'D', 'Präposition': 'R', 'Konjunktion': 'J',
           'Interjektion': 'I', 'Pronominaladverb': 'D', 'Temporaladverb': 'D',
           'Partikel': 'T', 'Komparativ': 'A', 'Superlativ': 'A'},

    'fr': {'verbe': 'V', 'nom': 'N', 'adjectif': 'A', 'prénom': 'N',
           'adverbe': 'D', 'numerál': 'C', 'préposition': 'R',
           'conjonction': 'J', 'particule': 'T', 'interjection': 'I'},

    'pl': {'rzeczownik': 'N', 'rzeczownik': 'N', 'przymiotnik': 'A',
           'przysłówek': 'D', 'czasownik': 'V', 'partykuła': 'T',
           'wykrzyknik': 'I', 'skrótowiec': 'N', 'liczebnik': 'C',
           'zaimek': 'P', 'skrót': 'N', 'imiesłów': 'V', 'przyimek': 'R',
           'spójnik': 'J'}
}
