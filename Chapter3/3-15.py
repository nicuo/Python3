#!/usr/bin/env python
life = {
    'animals': {
        'cats': [
            'Henri','Grumpy','Lucy'
        ],
        'octopi': {},
        'emus': {},
        },
    'plants': {},
    'other': {}
}

print( list ( life.keys() ) )
print( list ( life['animals'].keys()) )
print( list ( life['animals']['cats'] ) )
