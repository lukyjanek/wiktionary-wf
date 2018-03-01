SHELL=/bin/bash

cswikt:
	python3 comparison.py -w data/cs_wkt.dat -d data/derinet-1-5-1.tsv -i output/cs/inside.dat -o output/cs/outside.dat -c output/cs/comparatives.dat -n output/cs/noncomparatives.dat -a output/cs/all-relations.dat

enwikt:
	python3 comparison.py -w data/en_wkt.dat -d data/derinet-1-5-1.tsv -i output/en/inside.dat -o output/en/outside.dat -c output/en/comparatives.dat -n output/en/noncomparatives.dat -a output/en/all-relations.dat

dewikt:
	python3 comparison.py -w data/de_wkt.dat -d data/derinet-1-5-1.tsv -i output/de/inside.dat -o output/de/outside.dat -c output/de/comparatives.dat -n output/de/noncomparatives.dat -a output/de/all-relations.dat

merge:
	python3 merging.py -m output/cs/comparatives.dat,output/en/comparatives.dat,output/de/comparatives.dat -o output/merged-comparatives.dat
	python3 merging.py -m output/cs/noncomparatives.dat,output/en/noncomparatives.dat,output/de/noncomparatives.dat -o output/merged-noncomparatives.dat
