import argparse
from lexibank_chenhmongmien import Dataset as ds
from lingpy import *
from pyconcepticon import Concepticon
from cldfcatalog import Config

parser = argparse.ArgumentParser()
parser.add_argument('--concepticon_ids', help='True or False')
args = parser.parse_args()

concepticon = Concepticon(Config.from_file().get_clone('concepticon'))
wl = Wordlist.from_cldf(
        ds().dir.joinpath('cldf', 'cldf-metadata.json'),
        )

D = {0: wl.columns}
if args.concepticon_ids: 
    for idx, cid in wl.iter_rows('concepticon'):
        if cid:
            D[idx] = wl[idx]
    Wordlist(D).output('tsv', filename='D_Chen_subset', prettify=False)
else:
    wl.output('tsv', filename='D_Chen_subset', prettify=False)


wl = Wordlist('D_Chen_subset.tsv')
print('Wordlist has {0} concepts and {1} varieties across {2} words.'.format(
      wl.height, wl.width, len(wl)))
print(wl.doculect)