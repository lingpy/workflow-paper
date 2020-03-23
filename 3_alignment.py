from sinopy import segments
from lingpy import *
from lingrex.align import template_alignment
from sys import argv

if 'all' in argv:
    fname='A_Chen_'
else:
    fname='D_Chen_'



alms = Alignments(fname+'partial.tsv', ref='cogids')
alms.add_entries(
        'structure',
        'tokens',
        lambda x: basictypes.lists(
            ' + '.join([' '.join(y) for y in segments.get_structure(
                x)]))
        )
print('[i] added segments')
D = {0: [c for c in alms.columns]}
for idx, tokens, structure in alms.iter_rows('tokens', 'structure'):
    if len(tokens.n) != len(structure.n):
        print('[!!!]', tokens, structure)
    elif len(tokens) != len(structure):
        print('[!]', tokens, structure)
    else:
        D[idx] = alms[idx]
alms = Alignments(D, ref='cogids')

template_alignment(alms,
                   ref='cogids',
                   template='imnct+imnct+imnct+imnct+imnct+imnct',
                   structure = 'structure',
                   fuzzy=True,
                   segments='tokens')

alms.output('tsv', filename=fname+'aligned', prettify=False)
