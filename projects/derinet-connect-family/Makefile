SHELL=/bin/bash

all: cswikt enwikt dewikt frwikt plwikt merge

cswikt:
	python3 ../../wiktionary.py -d ../../data/cswiktionary-20180120-pages-articles-multistream.xml.bz2 -l cs -o data/cs.wkt -s data/cs.stat
	python3 comparison.py -w data/cs.wkt -d data/derinet-1-5-1.tsv -i output/cs/inside.dat -o output/cs/outside.dat -c output/cs/composites.dat -n output/cs/noncomposites.dat -a output/cs/all-relations.dat

enwikt:
	python3 ../../wiktionary.py -d ../../data/enwiktionary-20180120-pages-articles-multistream.xml.bz2 -l ze -o data/cs-en.wkt -s data/cs-en.stat
	python3 comparison.py -w data/cs-en.wkt -d data/derinet-1-5-1.tsv -i output/cs-en/inside.dat -o output/cs-en/outside.dat -c output/cs-en/composites.dat -n output/cs-en/noncomposites.dat -a output/cs-en/all-relations.dat

dewikt:
	python3 ../../wiktionary.py -d ../../data/dewiktionary-20180120-pages-articles-multistream.xml.bz2 -l zd -o data/cs-de.wkt -s data/cs-de.stat
	python3 comparison.py -w data/cs-de.wkt -d data/derinet-1-5-1.tsv -i output/cs-de/inside.dat -o output/cs-de/outside.dat -c output/cs-de/composites.dat -n output/cs-de/noncomposites.dat -a output/cs-de/all-relations.dat

frwikt:
	python3 ../../wiktionary.py -d ../../data/frwiktionary-20180120-pages-articles-multistream.xml.bz2 -l zf -o data/cs-fr.wkt -s data/cs-fr.stat
	python3 comparison.py -w data/cs-fr.wkt -d data/derinet-1-5-1.tsv -i output/cs-fr/inside.dat -o output/cs-fr/outside.dat -c output/cs-fr/composites.dat -n output/cs-fr/noncomposites.dat -a output/cs-fr/all-relations.dat

plwikt:
	python3 ../../wiktionary.py -d ../../data/plwiktionary-20180120-pages-articles-multistream.xml.bz2 -l zp -o data/cs-pl.wkt -s data/cs-pl.stat
	python3 comparison.py -w data/cs-pl.wkt -d data/derinet-1-5-1.tsv -i output/cs-pl/inside.dat -o output/cs-pl/outside.dat -c output/cs-pl/composites.dat -n output/cs-pl/noncomposites.dat -a output/cs-pl/all-relations.dat

merge:
	python3 merging.py -m output/cs/composites.dat,output/cs-en/composites.dat,output/cs-de/composites.dat,output/cs-fr/composites.dat,output/cs-pl/composites.dat -o output/merged-composites.dat
	python3 merging.py -m output/cs/noncomposites.dat,output/cs-en/noncomposites.dat,output/cs-de/noncomposites.dat,output/cs-fr/noncomposites.dat,output/cs-pl/noncomposites.dat -o output/merged-noncomposites.dat
