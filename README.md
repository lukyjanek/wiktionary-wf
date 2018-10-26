# Wiktionary word-formation (WiktiWF)
WiktiWF is **still an ongoing project** with ambition to extract and provide word-formation relations (derivation, compounding, derivational compounding) from [Wiktionary.org](https://www.wiktionary.org/) for 25 languages (listed bellow). This repository contains codes for the extraction and also published extracted data under the Creative Common license [CC BY-SA-NC 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The input Wiktionary data comes from [WikiMedia dumps](https://dumps.wikimedia.org/backup-index.html).

## Published data
All published datasets are included into the folder `releases/x` (language abbreviation instead of *x*). They all are published under [CC BY-SA-NC 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Part-of-speech tagging is also extracted from Wiktionary (if pos tag was present) and then harmonized to the [Hajič's pos tagset](https://ufal.mff.cuni.cz/pdt/Morphology_and_Tagging/Doc/hmptagqr.html#POS). Digits, abbreviations, and multiword expressions and units were excluded from the data.

The process of creating them is described in one of the next section. Each language mutation is published in two data structures.

**A direct graphs of lexemes** (name: *abbrev-wiktiwf-D-ver.tsv*) are the main data structure of derivational families extracted from Wiktionary. Published format of this structure is two-columns format (in order: parent, child) separated by tabulator:
 ```
great_A	greatly_D
great_A	greatness_N
hand_N	backhand_N
hand_N	deadhand_X
hit_V	hitman_N
 ```
**A complete graphs of lexemes** (name format: *abbrev-wiktiwf-C-ver.tsv*) organize each derivational family on separate line (lexemes are separated by tabulator):
```
great_A	greatly_D	greatness_N
Americanize_V	American_N	Americanism_N	Americanoid_A	Americanization_N
androgenize_V	androgenous_A	androgen_N	antiandrogen_N	androgenemia_N	xenoandrogen_N	androgenic_A
```

## Table of already published or processed data
| Language (in Czech) | Abbrev. | Date of dump | Version |
| --- | --- | --- | ---| --- |
| Czech (čeština) | cs | 20181020 | 1.0 (26/10/2018) |
| English (angličtina) | en | 20181020 | 1.0 (26/10/2018) |
| French (francouzština) | fr | 20181020 | 1.0 (26/10/2018) |
| German (němčina) | de | 20181020 | 1.0 (26/10/2018) |
| Polish (polština) | pl | 20181020 | 1.0 (26/10/2018) |
| Malga (malgaština) | mg | | | |
| Catalan (katalánština) | ca | | |
| Estonian (estonština) | et | | |
| Greek (řečtina) | el | | |
| Spanish (španělština) | es | | |
| Italian (italština) | it | | |
| Lithuanian (litevština) | lt | | |
| Hungarian (maďarština) | hu | | |
| Dutch (holandština) | nl | | |
| Norwegian (norština) | no | | |
| Uzbek (uzbečtina) | uz | | |
| Romanian (rumunština) | ro | | |
| Rusiian (ruština) | ru | | |
| Swedish (švédština) | sv | | |
| Finnish (finština) | fi | | |
| Welsh (velština) | cy | | |
| Croatian (chorvatština) | hr | | |
| Slovak (slovenština) | sk | | |
| Latin (latina) | la | | |
| Ukrainian (ukrajinština) | uk | | |

## How to build WiktiWF
Each language mutation of WiktiWF has prepared own target in `Makefile`. For example for Czech:
```makefile
data/cswiktionary-20180120-pages-articles-multistream.xml.bz2:
	wget 'https://dumps.wikimedia.org/cswiktionary/20180120/cswiktionary-20180120-pages-articles-multistream.xml.bz2' -P 'data/'

cswikti: data/cswiktionary-20180120-pages-articles-multistream.xml.bz2
	python3 -B wiktionary.py -d 'data/cswiktionary-20180120-pages-articles-multistream.xml.bz2' -l 'cs' -o 'releases/cs/cs-wiktiwf-D-1-0.tsv'
	python3 -B buildfamilies.py -i 'releases/cs/cs-wiktiwf-D-1-0.tsv' -o 'releases/cs/cs-wiktiwf-C-1-0.tsv'
```

First, the target downloads Wiktionary dump of specific language mutation. Because of the Wiktionary dumps are published almost every month, the target might not download the current version of dump. However, it can be manually changed in `Makefile`.

After that, the target extracts derivational relations (`wiktionary.py`) and saves them to `releases/x` (language abbreviation instead of *x*). The main used data structure of derivational families is the directed graphs of lexemes. Used flags: *-d* means input data, *-l* means language abbreviations, *-o* means output data.

Then, the target converts derivational families from the directed graphs of lexemes into the complete graphs of lexemes (`buildfamilies.py`). Used flags: *-i* means input data, *-o* means output data.

--
File `extraction.py` contains functions for extraction and cleaning extracted data (is used by `wiktionary.py`) from semi-structured Wiktionary. Specific regular expressions are included in individual files (used by `extraction.py`) in folder `patterns/`.
