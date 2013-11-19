#!/usr/bin/env python
"""
Generates attractive msisdn numbers
from defined pool range

Usage:
    $ python this_script.py # example

    >> from this_script import find_quaint_numbers
    >> q_gen = find_quaint_numbers(PHONE_RANGE)
    >> print set(q_gen)
"""

__author__ = "Jonathan Slenders, Piotr Pawlaczek"
__version__ = "2.0"
__status__ = "Improved Prototype"

PH_RANGE = (48732001501, 48732051502)

def is_sequence(n):
    """ True if sequence. """
    return n in '0123456789' or n in '9876543210'

def is_quaint(n):
    """ True when this is a quant number.  """
    return is_sequence(n[6:]) or len(set(n[5:])) < 3 or len(set(n[6:])) < 2

def find_quaint_numbers(range_):
    """ Iterator which yields quaint numbers in this range. """
    return (n for n in xrange(*range_) if is_quaint(str(n)))

if __name__ == '__main__':
    print
    print ''.join(' +{0}{1} {2}{3}{4} {5}{6}{7} {8}{9}{10}'.format(*str(n)) + [
            '\t', '\t', '\t', '\t', '\n',
            '\t', '\t', '\t', '\t', '\n',
            '\t', '\t', '\t', '\t', '\n\n'][i % 15]
        for i, n in enumerate(find_quaint_numbers(PH_RANGE)))
    print
