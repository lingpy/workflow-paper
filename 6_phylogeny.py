from lingpy.compare.partial import Partial
from lingpy.convert.plot import plot_tree
from sys import argv

if 'all' in argv:
    fname='A_Chen_'
else:
    fname='D_Chen_'

part = Partial(fname+'partial.tsv')
part.add_cognate_ids('cogids', 'cogid', idtype='strict')

part.calculate('distance', ref='cogid')
part.calculate('tree', tree_calc='neighbor')

part.output('dst', filename=fname+'distance')
part.output('tre', filename=fname+'tree')

plot_tree(str(part.tree), degree=180, filename=fname+'tree')


