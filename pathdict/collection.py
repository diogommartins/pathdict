from collections import UserDict, UserList


class StringIndexableList(UserList):
    def __getitem__(self, item):
        if isinstance(item, str):
            item = int(item)
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if isinstance(key, str):
            key = int(key)
        return super().__setitem__(key, value)


class PathDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.separator = kwargs.get('separator', '.')
        super().__init__(*args, **kwargs)

    def is_path(self, item) -> bool:
        if not isinstance(item, str):
            return False
        return self.separator in item

    def __getpath__(self, path: str):
        current_item = self.data
        for item in path.split(self.separator):
            current_item = current_item[item]
        return current_item

    def __setpath__(self, path: str, value):
        current_item = self.data
        previous_item = None
        for item in path.split(self.separator):
            previous_item = current_item
            current_item = current_item[item]
        previous_item[item] = value

    def __delpath__(self, path: str):
        current_item = self.data
        previous_item = None
        for item in path.split(self.separator):
            previous_item = current_item
            current_item = current_item[item]
        del previous_item[item]

    def __getitem__(self, item):
        if self.is_path(item):
            return self.__getpath__(item)
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if self.is_path(key):
            return self.__setpath__(key, value)
        if isinstance(value, list):
            value = StringIndexableList(value)
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        if self.is_path(key):
            return self.__delpath__(key)
        return super().__delitem__(key)
