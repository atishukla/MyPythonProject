"""
 This is the way we will populate the data in the python application.

"""


scientists = [

    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False}

]

"""
 There are few issues with this.
 1. Mutable datastructure which can be issue
 2. Multithreaded programming we do not have to wory about changing data
 3. Other thing is that in dict we are using a lot of keys. This can lead to typos like name can be neme
    Thats why we will use collections module

"""

scientists[0]['name'] = 'Edu Lovelace'

print(scientists)
