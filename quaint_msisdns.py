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

__author__ = "Piotr Pawlaczek"
__version__ = "1.0"
__status__ = "Prototype"


from itertools import ifilterfalse

PH_RANGE = (
    48732001501, 48732051501 + 1
)


def is_sequence(n):
    """
    Checks if given number is positive
    or negative sequence
    """

    first = int(n[0])
    if int(n[1]) - 1 == first:
        seq = 1
    elif int(n[1]) + 1 == first:
        seq = -1
    else:
        return False
    for digit in n[1:]:
        if (int(digit) == first + seq and seq) or \
                (int(digit) == first - seq and not seq):
            first = int(digit)
        else:
            return False
    return True


def is_quaint(no, nslice, repeat):
    """
    Tries to detect if given number is `quaint`
    where `quaint` means what author of this script
    perceived as `quaint` ;)

    - nslice + repeat params can be used for tuning this alg
      giving more quantity but in general less attractive results
    """

    def unique_everseen(iterable, key=None):
        seen = set()
        seen_add = seen.add
        if key is None:
            for element in ifilterfalse(seen.__contains__, iterable):
                seen_add(element)
                yield element
        else:
            for element in iterable:
                k = key(element)
                if k not in seen:
                    seen_add(k)
                    yield element

    for s in nslice:
        _repeat = repeat if s == 6 else repeat + 1
        n = no[s:]
        if ((is_sequence(n) or
             len(set(unique_everseen(n))) < _repeat)):

            return True


def find_quaint_numbers(_range, nslice=(5, 6), repeat=2):
    """
    Tries to generate an attractive msisdn
    number(s) from given range
    """

    prefix = str(_range[0])[4:]
    for no in xrange(*_range):
        if prefix in str(no)[nslice[0]]:
            yield no
        elif is_quaint(no=str(no),
                       repeat=repeat,
                       nslice=nslice):
                yield no


if __name__ == '__main__':
    print
    s = []
    for idx, n in enumerate(sorted(find_quaint_numbers(PH_RANGE))):
        s.append(' +{0}{1} {2}{3}{4} {5}{6}{7} {8}{9}{10}'.format(*str(n)))
        if len(s) >= 5:
            print '\t'.join(s)
            s = []
            if not (idx + 1) % 3:
                print
    print idx
