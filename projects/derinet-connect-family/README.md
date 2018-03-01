# Connections DeriNet's root with parents using Wiktionary data
This folder contains codes for the project builded on the extraction of the derivational word-formation relations from [Wiktionary](https://www.wiktionary.org/). The goal of this project is to connect unconnected lexemes in DeriNet using the extracted Wiktionary data for Czech language.

## Using step-by-step
- download wiktionary data and extract wf relations (both using the main project)
```
make cswiktionary
make enwiktionary
...
python3 wiktionary.py -d ... -l ... -o ...
```
- make comparison of builded data with DeriNet's data (using `Makefile` in this project)
```
make cswkt
make enwkt
...
```
- merge created files for better manual annotating in future
```
make merge
```

## Notes
- folder `derinet` comes from [DeriNet repository](https://github.com/vidraj/derinet) as well as the DeriNet's data (version 1.5.1).
- folder `data` and `output` is ignored by `.gitignore`
