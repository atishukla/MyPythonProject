import collections
from pprint import pprint

# Create a named tuple
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])


scientist = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu yoyu', field='chemistry', born=1930, nobel=True),
    Scientist(name='Vera Radim', field='astronomy', born=1928, nobel=False)
)


pprint(scientist)
