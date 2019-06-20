# -*- coding: UTF-8 -*-
import tempfile
import pytest
from pysenal.io.file import *
from tests import TEST_DATA_DIR


@pytest.fixture("module")
def example_lines():
    lines = ['This is an example.   ',
             'This is a different example.',
             '',
             '    Hahaha.']
    return lines


def test_read_lines(example_lines):
    filename = TEST_DATA_DIR + 'a.txt'
    lines = read_lines(filename)
    assert lines == example_lines
    skip_lines = read_lines(filename, skip_empty=True)
    assert skip_lines == [l for l in example_lines if l]
    assert read_lines(TEST_DATA_DIR + 'a.txt.gbk', 'gbk') == ['你好', '这是一个例子。']


def test_read(example_lines):
    filename = TEST_DATA_DIR + 'a.txt'
    text = read_file(filename)
    true_text = '\n'.join(example_lines)
    assert text == true_text


def test_read_json():
    read_json(TEST_DATA_DIR + 'a.json')


def test_write_lines(example_lines):
    dirname = tempfile.gettempdir() + '/'
    filename = dirname + 'a.txt'
    if os.path.exists(filename):
        os.remove(filename)

    write_lines(filename, example_lines)
    with open(filename) as f:
        assert f.read().splitlines() == example_lines

    if os.path.exists(filename):
        os.remove(filename)


def test_text_file(example_lines):
    true_text = '\n'.join(example_lines)
    text_file = TextFile(TEST_DATA_DIR + 'a.txt')
    text = text_file.read()
    lines = text_file.read_lines()
    assert text == true_text
    assert lines == example_lines
    expected_write_text = 'New Example\n\n'
    text_file.write(expected_write_text)
    print(text_file.read())
    assert text_file.read() == expected_write_text
    written_lines = ['A', '', 'BBB\n', 'C']
    text_file.write_lines(written_lines)
    expected_write_lines = ['A', '', 'BBB', 'C']
    assert text_file.read_lines() == expected_write_lines

    text_file.write(true_text)
