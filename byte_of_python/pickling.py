#!/usr/bin/env python3
import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apples', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

# Reading data from storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)
