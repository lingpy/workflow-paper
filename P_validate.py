import argparse
from lingpy import Wordlist
from lingpy.basic import ops
from lingrex.copar import density

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file')
parser.add_argument('--column')
args = parser.parse_args()
#print(args) 
wl = Wordlist(args.input)

# cognate density 
cdensity = density(wl, ref=args.column)
print('The cognate density: ', cdensity)
# calculate the distance via shared cognates
wl.calculate('dst', taxa='doculect', concepts='concepts', ref=args.column)

# output
wl.output('dst', filename='D_Chen_distance')