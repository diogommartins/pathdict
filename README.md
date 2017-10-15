# PathDict

[![Build Status](https://travis-ci.org/diogommartins/simple_json_logger.svg?branch=master)](https://travis-ci.org/diogommartins/pathdict)
[![codecov](https://codecov.io/gh/diogommartins/simple_json_logger/branch/master/graph/badge.svg)](https://codecov.io/gh/diogommartins/pathdict)

Extended dict with the capability of accessing and manipulating nested itens 
using a path notation.

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

Everything you do with a normal python `dict` will work.

## Customization

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

It is possible to let `PathDict` generate the steps to a given path:

```python
from pathdict import PathDict


path_dict = PathDict(create_if_not_exists=True)
path_dict['the.answer.to.all.problems'] = 42

print(path_dict)
>>> {'the': {'answer': {'to': {'all': {'problems': 42}}}}}

```

By default, list values inside a `PathDict` are type casted to a 
`pathdict.collection.StringIndexableList`. You can change that behavior with the
`list_class` keyword argument. Beware that if the `list_class` class doesn't 
implement the StringIndexableList Protocol, pathdict's lists path will fail.  

```python
from pathdict import PathDict


path_dict = PathDict()

path_dict["list"] = [1, 2, 3]
type(path_dict["list"])
>>> pathdict.collection.StringIndexableList

path_dict["list.1"]
>>> 2

custom_path_dict = PathDict(list_class=list)
type(custom_path_dict["list"])
>>> list

custom_path_dict["list.1"]
>>> TypeError: list indices must be integers or slices, not str

``` 