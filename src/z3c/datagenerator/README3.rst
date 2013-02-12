===============
Data Generators
===============

:Note: This is the Python 3 version of the documentation. The random number
       generator changed, so that the output will differ!

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
  datetime.date(2012, 9, 25)
  >>> gen.getMany(2)
  [datetime.date(2012, 11, 29), datetime.date(2012, 4, 16)]


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
  'ID5073*3888*7417'
  >>> gen.getMany(3)
  ['ID035*4940*3819', 'ID4152*7603*585', 'ID6058*7872*7015']


Demographics Generators
=======================

This module contains a set of every day demographics data generators.

  >>> from z3c.datagenerator import demographics


Last Name Generator
-------------------

This generator creates last names from a predefined set.

  >>> gen = demographics.LastNameGenerator('seed')

  >>> gen.get()
  "O'Doherty"
  >>> gen.getMany(3)
  ['Black', 'Tan', 'Rivera']


First Name Generator
--------------------

This generator creates first names from a predefined set.

  >>> gen = demographics.FirstNameGenerator('seed')

  >>> gen.get()
  'Al'
  >>> gen.getMany(3)
  ['Amy', 'Sean', 'Malgorzata']


SSN Generator
-------------

This generator creates valid US social security numbers (SSN).

  >>> gen = demographics.SSNDataGenerator('seed')

  >>> gen.get()
  '982-17-1631'
  >>> gen.getMany(3)
  ['508-91-7006', '122-35-9428', '914-91-0060']


US Address Generator
--------------------

This generator creates US addresses that look realistic but are completely
randomly generated. Street and city names are selected from a pre-defined
set. Note that you can change all the data files to generate addresses of
other contries.

  >>> gen = demographics.AddressDataGenerator('seed')

  >>> gen.get()
  ('451 Archer Lane', 'Clarksburg', 'MI', '04382')
  >>> gen.getMany(1)
  [('1970 Ninth Lane Apt. 25', 'Chatham', 'MO', '48781')]

You can also get all components by themselves:

  >>> gen.getStreet()
  '82 Morton Circle'
  >>> gen.getCity()
  'Maynard'
  >>> gen.getState()
  'VT'
  >>> gen.getZip()
  '60332'


US Phone Number Generator
-------------------------

This generator creates correctly formatted US-style phone numbers.

  >>> gen = demographics.PhoneDataGenerator('seed')

  >>> gen.get()
  '998-100-5657'
  >>> gen.getMany(3)
  ['651-167-3489', '890-004-8393', '172-875-9973']


You can also force the area code to be "555", which is a dummy area code.

  >>> gen = demographics.PhoneDataGenerator('seed', True)
  >>> gen.get()
  '555-899-1588'


Network Generators
==================

This module contains a set of computer and network related generators

  >>> from z3c.datagenerator import net


IPv4 Generator
--------------

This generator creates valid IPv4 addresses.

  >>> gen = net.IPv4DataGenerator('seed')

  >>> gen.get()
  '163.128.170.133'
  >>> gen.getMany(3)
  ['174.045.216.212', '210.131.039.157', '237.098.199.244']


Username Generator
------------------

This generator creates usernames from real names.

  >>> gen = net.UsernameDataGenerator('seed')

  >>> gen.get()
  'aodoherty'
  >>> gen.getMany(3)
  ['ablack', 'stan', 'mrivera']

You can also pass in the first and last name to the generator method.

  >>> gen.get('Stephan', 'Richter')
  'srichter'

Let's change the pattern:

  >>> gen = net.UsernameDataGenerator(
  ...     'seed', u'%(firstName).s%(lastName)s.%(number)s')
  >>> gen.get()
  'odoherty.16'

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
  'aodoherty@averages.jobs'
  >>> gen.getMany(3)
  ['ablack@actresses.biz', 'stan@overwhelmingly.mil', 'mrivera@wile.cat']

You can also pass in the username to the generator method.

  >>> gen.get('srichter')
  'srichter@sander.museum'
