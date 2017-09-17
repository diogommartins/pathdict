import unittest
from pathdict import PathDict


class PathDictTests(unittest.TestCase):
    def setUp(self):
        self.path_dict = PathDict({
            'dogs': {
                'male': 'Xablau',
                'female': 'Xena'
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

    def test_it_access_nested_list_by_path(self):
        self.assertEqual(self.path_dict['enterprises.0'], 'B2W')
        self.assertEqual(self.path_dict['enterprises.1'], 'Sieve')

    def test_it_updates_dict_with_path_notation(self):
        other = {'dogs.male': 'XxXablau'}
        self.path_dict.update(other)

        self.assertEqual(self.path_dict, {
            'dogs': {
                'male': 'XxXablau',
                'female': 'Xena'
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
                'female': 'Xena'
            },
            'enterprises': ['B2W', 'Negro Drama'],
            'author': '@diogommartins'
        })

    def test_it_deletes_dict_item_with_path_notation(self):
        del self.path_dict['dogs.female']
        self.assertEqual(self.path_dict, {
            'dogs': {
                'male': 'Xablau'
            },
            'enterprises': ['B2W', 'Sieve'],
            'author': '@diogommartins'
        })

    def test_a_non_string_key_isnt_a_valid_path(self):
        self.assertFalse(self.path_dict.is_path(666))
        self.assertFalse(self.path_dict.is_path((123, 321)))
        self.assertFalse(self.path_dict.is_path(('dogs', 'male')))
