import unittest
from pathdict import PathDict


class PathDictTests(unittest.TestCase):
    def setUp(self):
        self.path_dict = PathDict({
            'dogs': {
                'male': 'Xablau',
                'female': 'Xena',
                'nested_list': ['0', '1', '2']
            },
            'enterprises': ['B2W', 'Sieve'],
            'author': '@diogommartins'
        })

    def test_it_access_dict_values_by_key(self):
        self.assertEqual(self.path_dict['author'], '@diogommartins')

    def test_it_access_nested_dict_by_key(self):
        self.assertEqual(self.path_dict['dogs']['male'], 'Xablau')
        self.assertEqual(self.path_dict['dogs']['female'], 'Xena')

    def test_it_access_nested_dict_by_path(self):
        self.assertEqual(self.path_dict['dogs.male'], 'Xablau')
        self.assertEqual(self.path_dict['dogs.female'], 'Xena')

    def test_it_access_nested_lists_inside_nested_dicts_by_path(self):
        self.assertEqual(self.path_dict['dogs.nested_list.2'], '2')

    def test_it_access_nested_list_by_path(self):
        self.assertEqual(self.path_dict['enterprises.0'], 'B2W')
        self.assertEqual(self.path_dict['enterprises.1'], 'Sieve')

    def test_it_updates_dict_with_path_notation(self):
        other = {'dogs.male': 'XxXablau'}
        self.path_dict.update(other)

        self.assertEqual(self.path_dict, {
            'dogs': {
                'male': 'XxXablau',
                'female': 'Xena',
                'nested_list': ['0', '1', '2']
            },
            'enterprises': ['B2W', 'Sieve'],
            'author': '@diogommartins'
        })

    def test_it_updates_dict_with_path_notation_of_list_item(self):
        other = {'enterprises.1': 'Negro Drama'}
        self.path_dict.update(other)

        self.assertEqual(self.path_dict, {
            'dogs': {
                'male': 'Xablau',
                'female': 'Xena',
                'nested_list': ['0', '1', '2']
            },
            'enterprises': ['B2W', 'Negro Drama'],
            'author': '@diogommartins'
        })

    def test_it_deletes_dict_item_with_path_notation(self):
        del self.path_dict['dogs.female']
        self.assertEqual(self.path_dict, {
            'dogs': {
                'male': 'Xablau',
                'nested_list': ['0', '1', '2']
            },
            'enterprises': ['B2W', 'Sieve'],
            'author': '@diogommartins'
        })

    def test_a_non_string_key_isnt_a_valid_path(self):
        self.assertFalse(self.path_dict.is_path(666))
        self.assertFalse(self.path_dict.is_path((123, 321)))
        self.assertFalse(self.path_dict.is_path(('dogs', 'male')))

    def test_separator_can_be_changed(self):
        self.path_dict.separator = '/'
        self.assertEqual(self.path_dict['dogs/male'], 'Xablau')

        self.path_dict.separator = '|'
        self.assertEqual(self.path_dict['dogs|male'], 'Xablau')

    def test_set_to_invalid_path_raises_keyerror(self):
        with self.assertRaises(KeyError):
            self.path_dict['the.answer.to.all.problems'] = 42


class CreateIfNotExistsParameterTests(unittest.TestCase):
    def test_delete_on_invalid_path_raises_keyerror(self):
        path_dict = PathDict(create_if_not_exists=True)

        with self.assertRaises(KeyError):
            del path_dict['dogs.male']
        with self.assertRaises(KeyError):
            del path_dict['Xablau']

    def test_it_creates_nested_items_if_path_is_invalid(self):
        path_dict = PathDict(create_if_not_exists=True)
        path_dict['rio.de.janeiro'] = 'Xablau'

        self.assertEqual(path_dict, {
            'rio': {
                'de': {
                    'janeiro': 'Xablau'
                }
            }
        })
