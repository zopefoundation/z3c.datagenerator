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
"""Demographics Data Generators

$Id$
"""
__docformat__ = "reStructuredText"
import os
import random
import zope.interface

from z3c.datagenerator import generator

class LastNameGenerator(generator.TextDataGenerator):
    """Last Name Generator"""

    def __init__(self, seed):
        super(LastNameGenerator, self).__init__(seed, 'lastnames.txt')


class FirstNameGenerator(generator.TextDataGenerator):
    """First Name Generator"""

    def __init__(self, seed):
        super(FirstNameGenerator, self).__init__(seed, 'firstnames.txt')


class SSNDataGenerator(object):
    """A social security data generator."""

    def __init__(self, seed):
        self.random = random.Random(generator.consistent_hash(seed+'ssn'))

    def get(self):
        """Compute a social security number."""
        randint = self.random.randint
        return u'%.3i-%.2i-%.4i' %(
            randint(1, 999), randint(1, 99), randint(1, 9999))

    def getMany(self, number):
        """Select a set of values from the values list and return them."""
        return [self.get() for count in xrange(number)]


class AddressDataGenerator(object):
    """An address data generator."""

    streetNamesFile = 'us-street-names.txt'
    streetPostfixFile = 'us-street-postfix.txt'
    citiesFile = 'us-cities.txt'
    statesFile = 'us-states.txt'
    apts = True

    def __init__(self, seed):
        self.random = random.Random(generator.consistent_hash(seed+'address'))
        path = os.path.dirname(__file__)

        file = open(os.path.join(path, self.streetNamesFile), 'r')
        self.streetNames = [unicode(e.strip()) for e in file.readlines()]

        file = open(os.path.join(path, self.streetPostfixFile), 'r')
        self.streetPostfix = [unicode(e.strip()) for e in file.readlines()]

        file = open(os.path.join(path, self.citiesFile), 'r')
        self.cities = [unicode(e.strip()) for e in file.readlines()]

        file = open(os.path.join(path, self.statesFile), 'r')
        self.states = [unicode(e.strip()) for e in file.readlines()]

    def getStreet(self):
        street = u'%i ' % self.random.randint(1, 2000)
        street += u'%s ' % self.random.sample(self.streetNames, 1)[0]
        street += self.random.sample(self.streetPostfix, 1)[0]
        if self.apts and self.random.random() < 0.3:
            street += u' Apt. %i' %self.random.randint(1, 30)
        return street

    def getCity(self):
        return self.random.sample(self.cities, 1)[0]

    def getState(self):
        return self.random.sample(self.states, 1)[0]

    def getZip(self):
        return u'%.5i' % self.random.randint(1000, 99999)

    def get(self):
        """Select a value from the values list and return it."""
        return self.getStreet(), self.getCity(), self.getState(), self.getZip()

    def getMany(self, number):
        """Select a set of values from the values list and return them."""
        return [self.get() for count in xrange(number)]


class PhoneDataGenerator(object):
    """A phone data generator."""

    template = u'%i-%.3i-%.4i'

    def __init__(self, seed):
        self.random = random.Random(generator.consistent_hash(seed+'ssn'))

    def get(self):
        """Compute a social security number."""
        randint = self.random.randint
        return self.template %(
            randint(100, 999), randint(1, 999), randint(1, 9999))

    def getMany(self, number):
        """Select a set of values from the values list and return them."""
        return [self.get() for count in xrange(number)]
