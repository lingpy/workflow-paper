from lingpy.compare.partial import Partial
from lingpy.convert.plot import plot_tree
from sys import argv
from clldutils.text import strip_brackets, split_text
from collections import defaultdict
from lingpy import basictypes

if 'all' in argv:
    fname='A_Chen_'
else:
    fname='D_Chen_'

part = Partial(fname+'crossids.tsv')
part.add_cognate_ids('crossids', 'crossid', idtype='strict')
part.add_entries('cog', 'crossid,concept', lambda x, y: str(x[y[0]])+x[y[1]])
part.renumber('cog')

part.calculate('distance', ref='cogid')
part.calculate('tree', tree_calc='neighbor')

part.output('dst', filename=fname+'distance')
part.output('tre', filename=fname+'tree')

if 'plot' in argv:
    plot_tree(str(part.tree), degree=350, filename=fname+'tree')


