# Dictionaries are unordered mappings for storing objects.
# Prviously we saw how list store objects in ordered sequence,
# Dictionaries use a key:value pairing instead.

# This key:value pairing allows users to quickly grab objects
# without needing to know an index location

# Synatx
# Dictionaries use curly braces and colons to signify the
# keys and their associated alues.s

# {'key1':'value1', 'key2':'value2'}s

# Dictionaries vs list

# Dictionaries: Objects retrived by key name
#   Unordered and can not be sorted.

# Lists: Objects retrieved by location.
#   Ordered sequences can be indexed or sliced.

# Examples
import os

os.system('clear')

price_lookup = {'apple':2.99, 'orange':1.49, 'milk':5.99}
print("Price of apple: ${}".format(price_lookup['apple']))


extra_dict = {'k1':123, 'k2':[1, 2, 3],'k3':{'insideKey':1000}}
print("extracting data from the nested dictionary structure and the vlaue is: {}".format(extra_dict['k3']['insideKey']))


