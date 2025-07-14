#Python program to create an instance of an Ordered dict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order.
d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}

# create an instance of OrderedDict

from collections import OrderedDict

od = OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))

# print the members of the dictionary in reverse order

for key in od:
    print(key, od[key])
