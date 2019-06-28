#!/usr/bin/python
#Filename: pickling.py

import cPickle as p

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'orange']

f = file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()

del shoplist

f = file(shoplistfile)
storedlist = p.load(f);
print storedlist