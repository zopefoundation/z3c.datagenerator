===============
Data Generators
===============

Data Generators are meant to create data for your application quickly. They
are most useful for generating sample data. Sample Data, in turn, allows you
to test your application with much more realistic data volumes and is
considered for some development groups as essential as tests themselves.

An essential part of this package is a consistent hash generator.  Verify
its output.

  >>> from z3c.datagenerator.generator import consistent_hash
  >>> consistent_hash('seed') == 1149756166
  True
  >>> consistent_hash('') == 0
  True
  >>> consistent_hash('0') == 4108050209
  True

(More tests needed, obviously.)
