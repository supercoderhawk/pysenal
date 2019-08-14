# -*- coding: UTF-8 -*-
from types import GeneratorType
import pytest
from pysenal.utils.utils import *


def test_get_chunk():
    r1 = range(100)
    chunk_r1 = get_chunk(r1, 12)
    assert type(chunk_r1) == GeneratorType
    assert next(chunk_r1) == range(12)

    l1 = [1, 3, 5, 7, 9]
    chunk_l1 = get_chunk(l1, 5)
    assert next(chunk_l1) == l1
    with pytest.raises(StopIteration):
        next(chunk_l1)

    chunk_l1 = get_chunk(l1, 10)
    assert next(chunk_l1) == l1

    g1 = (i for i in [1, 10, 100, 3, 4, 'a'])
    chunk_g1 = get_chunk(g1, 2)
    assert type(chunk_g1) == GeneratorType
    assert next(chunk_g1) == [1, 10]
    assert next(chunk_g1) == [100, 3]

    g2 = (i for i in [20, 100, 40, 123])
    chunk_g2 = get_chunk(g2, 3)
    assert next(chunk_g2) == [20, 100, 40]
    assert next(chunk_g2) == [123]

    g3 = (i for i in [10, 100, 200])
    chunk_g3 = get_chunk(g3, 5)
    assert next(chunk_g3, [10, 100, 200])
    with pytest.raises(StopIteration):
        next(chunk_g3)
