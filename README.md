# PathDict

Extended dict with the capability of accessing nested itens using a path notation.

## Installation

```
pip install pathdict
```

## Examples

You can change your chained multiple access operator with a dotted path notation:

```python
from pathdict import PathDict


path_dict = PathDict({
    'dogs': {
        'male': 'Xablau',
        'female': 'Xena'
    },
    'enterprises': ['B2W', 'Sieve'],
    'author': '@diogommartins'
})

# Same as path_dict['dogs']['female']
print(path_dict['dogs.female'])
>>> 'Xena'
```

Lists are also accessible by the path notation:

```python
from pathdict import PathDict


path_dict = PathDict({
    'mammalia': {
        'ferae': {
            'carnivora': [
                'carnidae',
                'felidae',
                'mustelidae',
                'ursidae',
                'viverridae'
            ]       
        },
        'something': {
            'wiki': 'pedia'
        }
    }
})

# Same as path_dict['mammalia']['ferae']['carnivora'][3]
print(path_dict['mammalia.ferae.carnivora.3'])
>>> 'ursidae'
```

Everything else you do with a normal python `dict` will work.

## Customization

[![Build Status](https://travis-ci.org/diogommartins/simple_json_logger.svg?branch=master)](https://travis-ci.org/diogommartins/pathdict)
[![codecov](https://codecov.io/gh/diogommartins/simple_json_logger/branch/master/graph/badge.svg)](https://codecov.io/gh/diogommartins/pathdict)

The default `separator` is `.` but you can change it using the `separator` kwarg.

```python
from pathdict import PathDict


path_dict = PathDict({
    'mammalia': {
        'ferae': {
            'carnivora': [
                'carnidae',
                'felidae',
                'mustelidae',
                'ursidae',
                'viverridae'
            ]
        },
        'something': {
            'wiki': 'pedia'
        }
    }
}, separator='/')


print(path_dict['mammalia/ferae/carnivora/3'])
>>> 'ursidae'
```

