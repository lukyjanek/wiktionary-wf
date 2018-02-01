# Wiktionary word-formation
This repository contains codes for the extraction of the derivational word-formation relations from [Wiktionary](https://www.wiktionary.org/). The Wiktionary data comes from [WikiMedia dumps](https://dumps.wikimedia.org/backup-index.html).

This repository does not contain any data. The (input) Wiktionary data can be downloaded by _Makefile_ to the folder _data/_. Because of these data could be large, this folder is ignored by git (in _.gitignore_).

This repository is still under construction. Workflow step-by-step:
- extract WF data for Czech language,
- extract WF data for other languages containing WF information,
- harmonization of the data structure.

The output data structure (after harmonization) should look like as a rooted tree as well as in Czech derivation word-formation resource [DeriNet](http://ufal.mff.cuni.cz/derinet) from [UFAL, MFF, Charles University, Prague](http://ufal.mff.cuni.cz/).
