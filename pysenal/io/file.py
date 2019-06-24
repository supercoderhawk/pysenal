def read_lines(filename, encoding=_ENCODING_UTF8, keep_end=False,
               strip=False, skip_empty=False, default=None):
    :param default: returned value when filename is not existed.
                    If it's None, exception will be raised as usual.
    if not os.path.exists(filename) and default is not None:
        return default
def read_lines_lazy(filename, encoding=_ENCODING_UTF8, keep_end=False,
                    strip=False, skip_empty=False, default=None):
    :param filename: source file path
    :param default: returned value when filename is not existed.
                    If it's None, exception will be raised as usual.
    if not os.path.exists(filename) and default is not None:
        return default
    file = open(filename, encoding=encoding)
def read_file(filename, encoding=_ENCODING_UTF8, default=None):
    :param default: returned value when filename is not existed.
                    If it's None, exception will be raised as usual.
    if not os.path.exists(filename) and default is not None:
        return default
def read_json(filename):
    :param filename: source file path
    with open(filename, encoding=_ENCODING_UTF8) as f:
def write_json(filename, data, serialize_method=None):
    :param filename: destination file path
    with open(filename, 'w', encoding=_ENCODING_UTF8) as f:
def read_jsonline(filename, encoding=_ENCODING_UTF8, default=None):
    :param filename: source file path
    :param default: returned value when filename is not existed.
                    If it's None, exception will be raised as usual.
    if not os.path.exists(filename) and default is not None:
        return default
    file = open(filename, encoding=encoding)
def read_jsonline_lazy(filename, encoding=_ENCODING_UTF8, default=None):
    :param filename: source file path
    :param default: returned value when filename is not existed.
                    If it's None, exception will be raised as usual.
    if not os.path.exists(filename) and default is not None:
    file = open(filename, encoding=encoding)
def write_jsonline(filename, items, encoding=_ENCODING_UTF8):
    :param filename: destination file path
    if not filename.endswith('.jsonl'):
    file = open(filename, 'w', encoding=encoding)
def read_ini(filename):
    :param filename: source file path
    config.read(filename)
def write_ini(filename, config_data):
    :param filename: destination file
    with open(filename, 'w') as config_file:
def append_line(filename, line, encoding=_ENCODING_UTF8):
    :param filename: destination file path
    with open(filename, 'a', encoding=encoding) as f:
def append_lines(filename, lines, remove_file=False, encoding=_ENCODING_UTF8):
    :param filename: destination file path
    if remove_file and os.path.exists(filename):
        os.remove(filename)
        append_line(filename, line, encoding)
def append_jsonline(filename, item, encoding=_ENCODING_UTF8):
    :param filename: destination file
    with open(filename, 'a', encoding=encoding) as f:
def append_jsonlines(filename, items, encoding=_ENCODING_UTF8):
    :param filename: destination file
    with open(filename, 'a', encoding=encoding) as f:
        if not isinstance(is_remove, bool):
            raise TypeError('is_remove must be bool value')
        self.logger = get_logger('FileWrapper')
        if not os.path.exists(self.filename):
            raise FileNotFoundError(self.filename)
    def read_line(self, default=None):
        if not os.path.exists(self.filename) and default is not None:
            return default
    def read_lines(self, skip_empty=False, default=None, *args, **kwargs):
        if not os.path.exists(self.filename) and default is not None:
            return default
        self._to_read()
        items = []
        for line in self._file:
            items.append(json.loads(line))
        return items

        self._to_write()
    def append(self, data):
        self._file.write(self._to_string(data))

    def append_line(self, line):
        self.append(line)