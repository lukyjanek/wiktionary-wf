SHELL=/bin/bash

data = 'data/'

cswikt:
	wget 'https://dumps.wikimedia.org/cswiktionary/20180120/cswiktionary-20180120-pages-articles-multistream.xml.bz2' -P $(data)
	python3 wiktionary.py -d data/cswiktionary-20180120-pages-articles-multistream.xml.bz2 -l cs -o output/cs.wkt -s output/cs.stat

enwikt:
	wget 'https://dumps.wikimedia.org/enwiktionary/20180120/enwiktionary-20180120-pages-articles-multistream.xml.bz2' -P $(data)
	python3 wiktionary.py -d data/enwiktionary-20180120-pages-articles-multistream.xml.bz2 -l en -o output/en.wkt -s output/en.stat

dewikt:
	wget 'https://dumps.wikimedia.org/dewiktionary/20180201/dewiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)
	python3 wiktionary.py -d data/dewiktionary-20180120-pages-articles-multistream.xml.bz2 -l cs -o output/de.wkt -s output/de.stat

frwikt:
	wget 'https://dumps.wikimedia.org/frwiktionary/20180201/frwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

plwikt:
	wget 'https://dumps.wikimedia.org/plwiktionary/20180201/plwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

eswikt:
	wget 'https://dumps.wikimedia.org/eswiktionary/20180201/eswiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

elwikt:
	wget 'https://dumps.wikimedia.org/elwiktionary/20180201/elwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

cawikt:
	wget 'https://dumps.wikimedia.org/cawiktionary/20180201/cawiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

cywikt:
	wget 'https://dumps.wikimedia.org/cywiktionary/20180201/cywiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

etwikt:
	wget 'https://dumps.wikimedia.org/etwiktionary/20180201/etwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

fiwikt:
	wget 'https://dumps.wikimedia.org/fiwiktionary/20180201/fiwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

hrwikt:
	wget 'https://dumps.wikimedia.org/hrwiktionary/20180201/hrwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

huwikt:
	wget 'https://dumps.wikimedia.org/huwiktionary/20180201/huwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

itwikt:
	wget 'https://dumps.wikimedia.org/itwiktionary/20180201/itwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

lawikt:
	wget 'https://dumps.wikimedia.org/lawiktionary/20180201/lawiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

ltwikt:
	wget 'https://dumps.wikimedia.org/ltwiktionary/20180201/ltwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

mgwikt:
	wget 'https://dumps.wikimedia.org/mgwiktionary/20180201/mgwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

nlwikt:
	wget 'https://dumps.wikimedia.org/nlwiktionary/20180201/nlwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

mywikt:
	wget 'https://dumps.wikimedia.org/mywiktionary/20180201/mywiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

nowikt:
	wget 'https://dumps.wikimedia.org/nowiktionary/20180201/nowiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

rowikt:
	wget 'https://dumps.wikimedia.org/rowiktionary/20180201/rowiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

ruwikt:
	wget 'https://dumps.wikimedia.org/ruwiktionary/20180201/ruwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

skwikt:
	wget 'https://dumps.wikimedia.org/skwiktionary/20180201/skwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

svwikt:
	wget 'https://dumps.wikimedia.org/svwiktionary/20180201/svwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

ukwikt:
	wget 'https://dumps.wikimedia.org/ukwiktionary/20180201/ukwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)

uzwikt:
	wget 'https://dumps.wikimedia.org/uzwiktionary/20180201/uzwiktionary-20180201-pages-articles-multistream.xml.bz2' -P $(data)
