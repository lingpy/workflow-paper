"""
Create a subselection of doculects and concepts from the dataset of Chén (2012).
"""
from lexibank_chenhmongmien import Dataset
from lingpy import *
from pyconcepticon import Concepticon
from cldfcatalog import Config
from tabulate import tabulate

from sys import argv

ds = Dataset()
concepticon = Concepticon(Config.from_file().get_clone('concepticon'))
wl = Wordlist.from_cldf(
        ds.dir.joinpath('cldf', 'cldf-metadata.json'),
        )

# languages
languages = [
        "EasternLuobuohe",
        "WesternLuobuohe",
        "Chuanqiandian",
        "CentralGuizhouChuanqiandian",
        "WesternXiangxi",
        "EasternXiangxi",
        "Bana",
        "Younuo",
        "Numao",
        "EasternBahen",
        "WesternBaheng",
        "EasternQiandong",
        "WesternQiandong",
        "BiaoMin",
        "ZaoMin"]  

# concepts
concepts = set()
for clist in [
        'Blust-2008-210', 
        'Swadesh-1952-200', 
        'Swadesh-1955-100',
        'Comrie-1977-207', 
        'Matisoff-1978-200',
        'Sagart-2019-250',
        'Liu-2007-201',
        'SoHartmann-1988-280',
        'BeijingDaxue-1964-905',
        ]:
    for concept in concepticon.conceptlists[clist].concepts.values():
            if concept.concepticon_id:
                concepts.add(concept.concepticon_id)

if not 'all' in argv:
    D = {0: wl.columns}
    for idx, doculect, cid in wl.iter_rows('doculect', 'concepticon'):
        if doculect in languages and cid in concepts:
            D[idx] = wl[idx]
    
    Wordlist(D).output('tsv', filename='D_Chen_subset', prettify=False)
else:
    wl.output('tsv', filename='D_Chen_subset', prettify=False)

# revise columns commend
wl = Wordlist('D_Chen_subset.tsv')
wl.output('tsv', filename='D_Chen_subset',
        prettify=False, ignore='all')
print('Wordlist has {0} concepts and {1} varieties across {2} words.'.format(
      wl.height, wl.width, len(wl)))

# print statistics on coverage
table = [[doculect, items, items/wl.height] for doculect, items in wl.coverage().items()]
print(tabulate(table, headers=['Doculect', 'Words', 'Coverage'],
    tablefmt='pipe', floatfmt='.2f'))

