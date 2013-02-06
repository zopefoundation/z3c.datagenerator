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
"""Demographics Data Generators"""
__docformat__ = "reStructuredText"
import os
import random
import zope.interface

from z3c.datagenerator import demographics, generator, interfaces


@zope.interface.implementer(interfaces.IDataGenerator)
class IPv4DataGenerator(object):
    """IPv4 generator."""

    def __init__(self, seed):
        self.random = random.Random(generator.consistent_hash(seed+'ip'))

    def get(self):
        """Select a value from the values list and return it."""
        return '%.3i.%.3i.%.3i.%.3i' %(
            self.random.randint(1, 255), self.random.randint(0, 255),
            self.random.randint(0, 255), self.random.randint(0, 255))

    def getMany(self, number):
        """Select a set of values from the values list and return them."""
        return [self.get() for count in range(number)]


@zope.interface.implementer(interfaces.IDataGenerator)
class UsernameDataGenerator(object):
    """Username generator."""

    pattern = u'%(firstInitial)s%(lastName)s'

    def __init__(self, seed, pattern=None):
        self.random = random.Random(generator.consistent_hash(seed+'username'))
        self.firstNames = demographics.FirstNameGenerator(seed)
        self.lastNames = demographics.LastNameGenerator(seed)
        if pattern:
            self.pattern = pattern

    def get(self, firstName=None, lastName=None):
        """Select a value from the values list and return it."""
        fname = firstName or self.firstNames.get()
        lname = lastName or self.lastNames.get()
        return self.pattern % {
            'firstName':     ''.join(c for c in fname.lower() if c.isalnum()),
            'lastName':      ''.join(c for c in lname.lower() if c.isalnum()),
            'firstInitial':  fname[0].lower(),
            'lastInitial':   lname[0].lower(),
            'number':        self.random.randint(1, 100)}

    def getMany(self, number):
        """Select a set of values from the values list and return them."""
        return [self.get() for count in range(number)]


@zope.interface.implementer(interfaces.IDataGenerator)
class EMailDataGenerator(object):
    """E-Mail generator."""

    wordsFile = 'words.txt'
    tldsFile = 'gTLD.csv'

    pattern = '%(uname)s@%(domain)s%(tld)s'

    def __init__(self, seed):
        self.random = random.Random(generator.consistent_hash(seed+'enail'))
        self.usernames = UsernameDataGenerator(seed)
        self.words = generator.TextDataGenerator(seed, self.wordsFile)
        self.tlds = generator.CSVDataGenerator(seed, self.tldsFile)


    def get(self, username=None):
        """Select a value from the values list and return it."""
        return self.pattern %{
            'uname': username or self.usernames.get(),
            'domain': self.words.get(),
            'tld': self.tlds.get()[0]}


    def getMany(self, number):
        """Select a set of values from the values list and return them."""
        return [self.get() for count in range(number)]
