# -*- coding: UTF-8 -*-
import copy
from collections import Iterable


def get_chunk(l, n):
    """
    get a chunk in iterable object
    :param l: iterable object
    :param n: chunk size
    :return: a chunk in list type
    """
    if not isinstance(l, Iterable):
        raise TypeError('input value is not iterable')
    if hasattr(l, '__getitem__'):
        for i in range(0, len(l), n):
            yield l[i:i + n]
    else:
        chunk = []
        for i in l:
            chunk.append(i)
            if len(chunk) == n:
                yield chunk
                chunk = []

        if chunk:
            yield chunk


def list2dict(l, key, pop_key=False):
    """
    convert list of dict to dict
    :param l: list of dict
    :param key: key name, which value of dict in list as returned dict key
    :param pop_key: whether pop the key in list of
    :return: assembled dict
    """
    if type(l) not in {list, tuple}:
        raise TypeError('input must in list or tuple type')
    d = {}
    for item in l:
        if not isinstance(item, dict):
            raise TypeError('item {0} is not dict'.format(item))
        if key not in item:
            raise KeyError('key is not in item')
        new_item = copy.deepcopy(item)
        if pop_key:
            new_item.pop(key)
        d[item[key]] = new_item
    return d
