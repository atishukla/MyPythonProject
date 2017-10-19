import collections
from pprint import pprint

# named tuple is immutable
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])


scientists = [
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emy Noether', field='math', born=1882, nobel=False)
]

# Now we cannot edit the key but we can still delete the first scientist

del(scientists[0])  # This way so instead of creating a list we can create a tuple

pprint(scientists)
