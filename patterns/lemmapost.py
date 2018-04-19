# !usr/bin/env python3
# coding: utf-8

# regular expression pattern for part-of-speech extraction
regex4 = {
    'cs' : r'=={1,} ((podstatné jméno)|(přídavné jméno)|(zájmeno)|(číslovka)|(sloveso)|(příslovce)|(předložka)|(spojka)|(citoslovce)|(částice)) ((\(1\) )|(=={1,}))',
    'en' : r'=={1,}((Noun)|(Adjective)|(Pronoun)|(Numeral)|(Verb)|(Adverb)|(Preposition)|(Conjugation))(( \(1\) )|(=={1,}))',
    'de' : r'Wortart\|((Substantiv)|(Adjektiv)|(Interrogativpronomen)|(Demonstrativpronomen)|(Numerale)|(Verb)|(Adverb)|(Präposition)|(Konjunktion)|(Interjektion)|(Pronominaladverb)|(Temporaladverb)|(Partikel)|(Komparativ)|(Superlativ))',
    'fr' : r'S\|((nom)|(adjectif)|(prénom)|(verbe)|(adverbe)|(numerál)|(préposition)|(conjonction)|(particule)|(interjection))\|',
    'pl' : r'\{\{znaczenia\}\}\n\'\'((rzeczownik)|(rzeczownik)|(przysłówek)|(przymiotnik)|(czasownik)|(partykuła)|(wykrzyknik)|(skrótowiec)|(liczebnik)|(zaimek)|(skrót)|(imiesłów)|(przyimek)|(spójnik))[\s\,\']',

    'ze' : r'=={1,}((Noun)|(Adjective)|(Pronoun)|(Numeral)|(Verb)|(Adverb)|(Preposition)|(Conjugation))(( \(1\) )|(=={1,}))',
    'zd' : r'Wortart\|((Substantiv)|(Adjektiv)|(Interrogativpronomen)|(Demonstrativpronomen)|(Numerale)|(Verb)|(Adverb)|(Präposition)|(Konjunktion)|(Interjektion)|(Pronominaladverb)|(Temporaladverb)|(Partikel)|(Komparativ)|(Superlativ))',
    'zf' : r'S\|((nom)|(adjectif)|(prénom)|(verbe)|(addverbe)|(numerál)|(préposition)|(conjonction)|(particule)|(interjection))\|',
    'zp' : r'\{\{znaczenia\}\}\n\'\'((rzeczownik)|(rzeczownik)|(przysłówek)|(przymiotnik)|(czasownik)|(partykuła)|(wykrzyknik)|(skrótowiec)|(liczebnik)|(zaimek)|(skrót)|(imiesłów)|(przyimek)|(spójnik))[\s\,\']'
}
