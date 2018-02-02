SHELL=/bin/bash

data = 'data/'

cswiktionary:
	wget 'https://dumps.wikimedia.org/cswiktionary/20180120/cswiktionary-20180120-pages-articles-multistream.xml.bz2' -P $(data)

enwiktionary:
	wget 'https://dumps.wikimedia.org/enwiktionary/20180120/enwiktionary-20180120-pages-articles-multistream.xml.bz2' -P $(data)
