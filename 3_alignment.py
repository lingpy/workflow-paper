from sinopy import segments
from lingpy import *
from lingrex.align import template_alignment



alms = Alignments('D_Chen_partial.tsv', ref='cogids')
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



alms.output('tsv', filename='D_Chen_aligned', prettify=False)


# print out for inspection
#for idx, cp, tok, structure in wl.iter_rows('concept', 'tokens', 'structure'):
#    print(wl[idx, 'doculect'], cp, tok, structure)
