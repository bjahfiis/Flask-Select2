# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2017, Paul Cunningham'

import sys

PY2 = sys.version_info[0] == 2
VER = sys.version_info

if not PY2:
    text_type = str
    string_types = (str,)
    integer_types = (int, )

    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())
    filter_list = lambda f, l: list(filter(f, l))

    def as_unicode(s):
        if isinstance(s, bytes):
            return s.decode('utf-8')

        return str(s)

    def csv_encode(s):
        ''' Returns unicode string expected by Python 3's csv module '''
        return as_unicode(s)

    # Various tools
    from functools import reduce
    from urllib.parse import urljoin, urlparse
else:
    text_type = unicode
    string_types = (str, unicode)
    integer_types = (int, long)

    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
    filter_list = filter

    def as_unicode(s):
        if isinstance(s, str):
            return s.decode('utf-8')

        return unicode(s)

    def csv_encode(s):
        ''' Returns byte string expected by Python 2's csv module '''
        return as_unicode(s).encode('utf-8')

    # Helpers
    reduce = __builtins__['reduce'] if isinstance(__builtins__, dict) else __builtins__.reduce
    from urlparse import urljoin, urlparse