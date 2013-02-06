===============
Data Generators
===============

Data Generators are meant to create data for your application quickly. They
are most useful for generating sample data. Sample Data, in turn, allows you
to test your application with much more realistic data volumes and is
considered for some development groups as essential as tests themselves.

An essential part of this package is a consistent hash generator.  Verify
its output.

  >>> from z3c.datagenerator import generator
  >>> generator.consistent_hash('seed') == 1149756166
  True
  >>> generator.consistent_hash('') == 0
  True
  >>> generator.consistent_hash('0') == 4108050209
  True


Generic Generators
==================

Date Generator
--------------

This generator creates a date from a given range:

  >>> import datetime
  >>> gen = generator.DateDataGenerator(
  ...     'seed',
  ...     start=datetime.date(2012, 1, 1),
  ...     end=datetime.date(2013, 1, 1))

  >>> gen.get()
  datetime.date(2012, 11, 20)
  >>> gen.getMany(2)
  [datetime.date(2012, 7, 11), datetime.date(2012, 8, 26)]


ID Generator
------------

This generator can create a wide variety of IDs.

  >>> gen = generator.IdDataGenerator(
  ...     'seed',
  ...     prefix='ID',
  ...     separator='*',
  ...     numbers=3,
  ...     max_value=8000)

  >>> gen.get()
  'ID4954*7244*4825'
  >>> gen.getMany(3)
  ['ID4056*571*7689', 'ID1794*3687*5166', 'ID2585*1495*6947']


Demographics Generators
=======================

This module contains a set of every day demographics data generators.

  >>> from z3c.datagenerator import demographics


Last Name Generator
-------------------

This generator creates last names from a predefined set.

  >>> gen = demographics.LastNameGenerator('seed')

  >>> gen.get()
   u'Lambert'
  >>> gen.getMany(3)
  [u'Oliver', u'Meyer', u'Jones']


First Name Generator
--------------------

This generator creates first names from a predefined set.

  >>> gen = demographics.FirstNameGenerator('seed')

  >>> gen.get()
  u'Agnieszka'
  >>> gen.getMany(3)
  [u'Lisa', u'Tony', u'Madison']


SSN Generator
-------------

This generator creates valid US social security numbers (SSN).

  >>> gen = demographics.SSNDataGenerator('seed')

  >>> gen.get()
  u'958-10-9260'
  >>> gen.getMany(3)
  [u'428-28-5754', u'975-01-6049', u'351-79-6709']


US Address Generator
--------------------

This generator creates US addresses that look realistic but are completely
randomly generated. Street and city names are selected from a pre-defined
set. Note that you can change all the data files to generate addresses of
other contries.

  >>> gen = demographics.AddressDataGenerator('seed')

  >>> gen.get()
  (u'440 Graymalkin Cove', u'Whitefield', u'RI', u'63293')
  >>> gen.getMany(1)
  [(u'1963 Bryn Mahr Cove', u'Ashfield', u'NV', u'20388')]

You can also get all components by themselves:

  >>> gen.getStreet()
  u'1629 Clinton Terrace'
  >>> gen.getCity()
  u'Farmington'
  >>> gen.getState()
  u'PA'
  >>> gen.getZip()
  u'19658'


US Phone Number Generator
-------------------------

This generator creates correctly formatted US-style phone numbers.

  >>> gen = demographics.PhoneDataGenerator('seed')

  >>> gen.get()
  u'889-666-7726'
  >>> gen.getMany(3)
  [u'410-163-7715', u'668-898-5122', u'868-998-6087']


You can also force the area code to be "555", which is a dummy area code.

  >>> gen = demographics.PhoneDataGenerator('seed', True)
  >>> gen.get()
  u'555-877-6664'

Network Generators
==================

This module contains a set of computer and network related generators

  >>> from z3c.datagenerator import net


IPv4 Generator
--------------

This generator creates valid IPv4 addresses.

  >>> gen = net.IPv4DataGenerator('seed')

  >>> gen.get()
  '163.085.173.022'
  >>> gen.getMany(3)
  ['108.209.065.019', '236.049.181.080', '075.110.011.122']


Username Generator
------------------

This generator creates usernames from real names.

  >>> gen = net.UsernameDataGenerator('seed')

  >>> gen.get()
  u'alambert'
  >>> gen.getMany(3)
  [u'loliver', u'tmeyer', u'mjones']

You can also pass in the first and last name to the generator method.

  >>> gen.get('Stephan', 'Richter')
  u'srichter'

Let's change the pattern:

  >>> gen = net.UsernameDataGenerator(
  ...     'seed', u'%(firstName).s%(lastName)s.%(number)s')
  >>> gen.get()
  u'lambert.13'

The available variables are:

* firstName
* firstInitial
* lastName
* lastInitial
* number


E-mail Generator
----------------

This generator creates properly formatted E-mail addresses with proper TLDs.

  >>> gen = net.EMailDataGenerator('seed')

  >>> gen.get()
  u'alambert@answering.edu'
  >>> gen.getMany(3)
  [u'loliver@acclimated.edu', u'tmeyer@skillfulness.mil', u'mjones@monks.biz']

You can also pass in the username to the generator method.

  >>> gen.get('srichter')
  u'srichter@plaque.info'
