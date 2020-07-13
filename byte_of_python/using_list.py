#!/usr/bin/env python3

# it is my shoplist
shoplist = ['apples', 'mango', 'carrot', 'bananas']

print('I must buy', len(shoplist), 'items.')

print('Items:', end=' ')
for item in shoplist:
    print(item, end=' ')


print('\n\nAlso I need to buy rice.')
shoplist.append('rice')
print('Now my shoplist is:', shoplist)

print('Let\'s sort my list')
shoplist.sort()
print('Sorted list is:', shoplist)

print('The first item in my list is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I was buy', olditem)

print('Now my shoplist is:', shoplist)
