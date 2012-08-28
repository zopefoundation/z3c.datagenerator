##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Data Generators

$Id$
"""
__docformat__ = "reStructuredText"
import csv
import datetime
import os
import random
from zlib import crc32
import zope.interface

from z3c.datagenerator import interfaces


def consistent_hash(buf):
    # Produce a hash of a string that behaves consistently in Python 32 and
    # 64 bit.  The "& 0xffffffff" interprets negative numbers as positive.
    return int(crc32(buf) & 0xffffffff)


class VocabularyDataGenerator(object):
    """Vocabulary-based data generator"""
    zope.interface.implements(interfaces.IDataGenerator)

    def __init__(self, seed, vocabulary):
        self.random = random.Random(consistent_hash(seed))
        self.vocabulary = vocabulary

    def get(self):
        """Select a value from the values list and return it."""
        return self.random.sample(self.vocabulary, 1)[0].value

    def getMany(self, number):
        """Select a set of values from the values list and return them."""
        return [term.value
                for term in self.random.sample(self.vocabulary, number)]


class FileDataGenerator(object):
    """Base functionality for a file data generator."""
    zope.interface.implements(interfaces.IFileBasedGenerator)

    path = os.path.dirname(__file__)

    def __init__(self, seed, filename):
        self.random = random.Random(consistent_hash(seed+filename))
        self.values = self._read(filename)

    def get(self):
        """Select a value from the values list and return it."""
        return self.random.sample(self.values, 1)[0]

    def getMany(self, number):
        """Select a set of values from the values list and return them."""
        return self.random.sample(self.values, number)


class CSVDataGenerator(FileDataGenerator):
    """CSV-based data generator."""

    def _read(self, filename):
        fullpath = os.path.join(self.path, filename)
        reader = csv.reader(file(fullpath), delimiter=';')
        return [[unicode(cell) for cell in row]
                for row in reader]


class TextDataGenerator(FileDataGenerator):
    """Text lines based data generator."""

    def _read(self, filename):
        fullpath = os.path.join(self.path, filename)
        return [unicode(e.strip(), encoding='latin-1')
                for e in open(fullpath, 'r').readlines()]


class DateDataGenerator(object):
    """A date data generator."""
    zope.interface.implements(interfaces.IDateDataGenerator)

    def __init__(self, seed, start=None, end=None):
        self.random = random.Random(consistent_hash(seed+'ssn'))
        self.start = start or datetime.date(2000, 1, 1)
        self.end = end or datetime.date(2007, 1, 1)

    def get(self, start=None, end=None):
        """Create a new date between the start and end date."""
        start = start or self.start
        end = end or self.end
        delta = end - start
        return start + datetime.timedelta(self.random.randint(0, delta.days))

    def getMany(self, number):
        """Select a set of values from the values list and return them."""
        return [self.get() for count in xrange(number)]
