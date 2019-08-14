# -*- coding: UTF-8 -*-
from typing import Iterable


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
