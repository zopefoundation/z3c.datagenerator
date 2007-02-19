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
"""Data Generators Interfaces

$Id$
"""
__docformat__ = "reStructuredText"
import zope.interface
import zope.schema

class IDataGenerator(zope.interface.Interface):
    """Base functionality for data generators."""

    random = zope.interface.Attribute(
        '''An instance of the standard Python random number generator. This
        attribute is public, so that tests can implement predictable versions
        -- for example by setting the same seed all the time.''')

    def get(self):
        """Select a value from the values list and return it."""

    def getMany(self, number):
        """Select a set of values from the values list and return them."""


class IFileBasedGenerator(IDataGenerator):
    """Data generator using a single file extract data.

    Specific implementations include a simple line-based and a CSV one.
    """

    path = zope.interface.Attribute(
        'The path to the file providing the data.')


class IDateDataGenerator(IDataGenerator):
    """A date data generator.

    This generator creates dates/times between the start and end dates/times.
    """

    start = zope.schema.Datetime(
        title=u'Start Date/Time',
        description=u'This field descibres the earliest date/time generated.',
        required=True)

    end = zope.schema.Datetime(
        title=u'End Date/Time',
        description=u'This field descibres the latest date/time generated.',
        required=True)

    def get(self, start=None, end=None):
        """Create a new date between the start and end date.

        The start and end date/time can be overridden here, since you
        sometimes want to generate sequences of dates.
        """
