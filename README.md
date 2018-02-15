# Wiktionary word-formation
This repository contains codes for the extraction of the derivational word-formation relations for several languages from [Wiktionary](https://www.wiktionary.org/). The Wiktionary data comes from [WikiMedia dumps](https://dumps.wikimedia.org/backup-index.html).

After extraction, the harmonization of the data structure will be done. The output data structure (after harmonization) should look like as a rooted tree as well as in _Czech derivation word-formation resource_ [DeriNet](http://ufal.mff.cuni.cz/derinet) from [UFAL, MFF, Charles University, Prague](http://ufal.mff.cuni.cz/).

## Usage
This repository does not contain any data. The (input) Wiktionary data can be downloaded by `Makefile` to the folder `data/`, and the (output) extracted data can be made (to the `output/` folder) by running scripts after downloading the input data. Because of all these data could be large, mentioned folders are ignored by git (in `.gitignore`).

It is possible to use a predefined version of the extraction process (e.g., the extraction of English from the English mutation of Wiktionary etc.), or define custom extraction process using the regular expression (described bellow).

### Setting custom extraction process
soon step-by-step...

**This repository is still under construction.**

## The list of languages with the WF relations in Wiktionary
state Language (Czech name) \[abbreviation in Wiktionary\]
- [x] Czech (čeština) \[cs\]
- [x] English (angličtina) \[en\]
- [ ] French (francouzština) \[fr\]
- [ ] Malga (malgaština) \[mg\]
- [ ] Catalan (katalánština) \[ca\]
- [ ] German (němčina) \[de\]
- [ ] Estonian (estonština) \[et\]
- [ ] Greek (řečtina) \[el\]
- [ ] Spanish (španělština) \[es\]
- [ ] Italian (italština) \[it\]
- [ ] Lithuanian (litevština) \[lt\]
- [ ] Hungarian (maďarština) \[hu\]
- [ ] Dutch (holandština) \[nl\]
- [ ] Norwegian (norština) \[no\]
- [ ] Uzbek (uzbečtina) \[uz\]
- [ ] Polish (polština) \[pl\]
- [ ] Romanian (rumunština) \[ro\]
- [ ] Rusiian (ruština) \[ru\]
- [ ] Swedish (švédština) \[sv\]
- [ ] Finnish (finština) \[fi\]
- [ ] Welsh (velština) \[cy\]
- [ ] Croatian (chorvatština) \[hr\]
- [ ] Slovak (slovenština) \[sk\]
- [ ] Latin (latina) \[la\]
- [ ] Ukrainian (ukrajinština) \[uk\]
