from lingpy import *
from lingpy.compare.partial import Partial

try:
    part = Partial('D_Chen_partial.bin.tsv')
except:
    part = Partial('D_Chen_subset.tsv', segments='tokens')
    part.get_partial_scorer(runs=10000)
    part.output('tsv', filename='D_Chen_partial.bin', ignore=[], prettify=False)
    print('[i] saved the scorer')
finally:
    part.partial_cluster(
            method='lexstat',
            threshold=0.55,
            ref='cogids',
            mode='global',
            gop=-2,
            cluster_method='infomap'
            )

part.output('tsv', filename='D_Chen_partial', prettify=False)
