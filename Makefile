SHELL=/bin/bash

# Czech wiktionary
data/cswiktionary-20181020-pages-articles-multistream.xml.bz2:
	wget 'https://dumps.wikimedia.org/cswiktionary/20181020/cswiktionary-20181020-pages-articles-multistream.xml.bz2' -P 'data/'

cswikti: data/cswiktionary-20181020-pages-articles-multistream.xml.bz2
	python3 -B wiktionary.py -d 'data/cswiktionary-20181020-pages-articles-multistream.xml.bz2' -l 'cs' -o 'releases/cs/cs-wiktiwf-D-1-0.tsv'
	python3 -B buildfamilies.py -i 'releases/cs/cs-wiktiwf-D-1-0.tsv' -o 'releases/cs/cs-wiktiwf-C-1-0.tsv'

# English wiktionary
data/enwiktionary-20181020-pages-articles-multistream.xml.bz2:
	wget 'https://dumps.wikimedia.org/enwiktionary/20181020/enwiktionary-20181020-pages-articles-multistream.xml.bz2' -P 'data/'

enwikti: data/enwiktionary-20181020-pages-articles-multistream.xml.bz2
	python3 -B wiktionary.py -d 'data/enwiktionary-20181020-pages-articles-multistream.xml.bz2' -l 'en' -o 'releases/en/en-wiktiwf-D-1-0.tsv'
	python3 -B buildfamilies.py -i 'releases/en/en-wiktiwf-D-1-0.tsv' -o 'releases/en/en-wiktiwf-C-1-0.tsv'

# Germany wiktionary
data/dewiktionary-20181020-pages-articles-multistream.xml.bz2:
	wget 'https://dumps.wikimedia.org/dewiktionary/20181020/dewiktionary-20181020-pages-articles-multistream.xml.bz2' -P 'data/'

dewikti: data/dewiktionary-20181020-pages-articles-multistream.xml.bz2
	python3 -B wiktionary.py -d 'data/dewiktionary-20181020-pages-articles-multistream.xml.bz2' -l 'de' -o 'releases/de/de-wiktiwf-D-1-0.tsv'
	python3 -B buildfamilies.py -i 'releases/de/de-wiktiwf-D-1-0.tsv' -o 'releases/de/de-wiktiwf-C-1-0.tsv'

# French wiktionary
data/frwiktionary-20181020-pages-articles-multistream.xml.bz2:
	wget 'https://dumps.wikimedia.org/frwiktionary/20181020/frwiktionary-20181020-pages-articles-multistream.xml.bz2' -P 'data/'

frwikti: data/frwiktionary-20181020-pages-articles-multistream.xml.bz2
	python3 -B wiktionary.py -d 'data/frwiktionary-20181020-pages-articles-multistream.xml.bz2' -l 'fr' -o 'releases/fr/fr-wiktiwf-D-1-0.tsv'
	python3 -B buildfamilies.py -i 'releases/fr/fr-wiktiwf-D-1-0.tsv' -o 'releases/fr/fr-wiktiwf-C-1-0.tsv'

# Polish wiktionary
data/plwiktionary-20181020-pages-articles-multistream.xml.bz2:
	wget 'https://dumps.wikimedia.org/plwiktionary/20181020/plwiktionary-20181020-pages-articles-multistream.xml.bz2' -P 'data/'

plwikti: data/plwiktionary-20181020-pages-articles-multistream.xml.bz2
	python3 -B wiktionary.py -d 'data/plwiktionary-20181020-pages-articles-multistream.xml.bz2' -l 'pl' -o 'releases/pl/pl-wiktiwf-D-1-0.tsv'
	python3 -B buildfamilies.py -i 'releases/pl/pl-wiktiwf-D-1-0.tsv' -o 'releases/pl/pl-wiktiwf-C-1-0.tsv'

# Spanish wiktionary
eswikt:
	wget 'https://dumps.wikimedia.org/eswiktionary/20180201/eswiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

elwikt:
	wget 'https://dumps.wikimedia.org/elwiktionary/20180201/elwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

cawikt:
	wget 'https://dumps.wikimedia.org/cawiktionary/20180201/cawiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

cywikt:
	wget 'https://dumps.wikimedia.org/cywiktionary/20180201/cywiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

etwikt:
	wget 'https://dumps.wikimedia.org/etwiktionary/20180201/etwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

fiwikt:
	wget 'https://dumps.wikimedia.org/fiwiktionary/20180201/fiwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

hrwikt:
	wget 'https://dumps.wikimedia.org/hrwiktionary/20180201/hrwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

huwikt:
	wget 'https://dumps.wikimedia.org/huwiktionary/20180201/huwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

itwikt:
	wget 'https://dumps.wikimedia.org/itwiktionary/20180201/itwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

lawikt:
	wget 'https://dumps.wikimedia.org/lawiktionary/20180201/lawiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

ltwikt:
	wget 'https://dumps.wikimedia.org/ltwiktionary/20180201/ltwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

mgwikt:
	wget 'https://dumps.wikimedia.org/mgwiktionary/20180201/mgwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

nlwikt:
	wget 'https://dumps.wikimedia.org/nlwiktionary/20180201/nlwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

mywikt:
	wget 'https://dumps.wikimedia.org/mywiktionary/20180201/mywiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

nowikt:
	wget 'https://dumps.wikimedia.org/nowiktionary/20180201/nowiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

rowikt:
	wget 'https://dumps.wikimedia.org/rowiktionary/20180201/rowiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

ruwikt:
	wget 'https://dumps.wikimedia.org/ruwiktionary/20180201/ruwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

skwikt:
	wget 'https://dumps.wikimedia.org/skwiktionary/20180201/skwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

svwikt:
	wget 'https://dumps.wikimedia.org/svwiktionary/20180201/svwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

ukwikt:
	wget 'https://dumps.wikimedia.org/ukwiktionary/20180201/ukwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'

uzwikt:
	wget 'https://dumps.wikimedia.org/uzwiktionary/20180201/uzwiktionary-20180201-pages-articles-multistream.xml.bz2' -P 'data/'
