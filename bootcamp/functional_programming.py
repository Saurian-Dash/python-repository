# Functional Programming Style

# A style of programming which uses immutable data structures to perform computation based on the evaluation of functions.

import collections
import csv
import json

source_file = open('scientists.csv', 'r')

def csv_to_json(f):
  with source_file:

    fields = next(csv.reader(source_file, delimiter=','))
    values = csv.DictReader(source_file, fields, delimiter=',')
    output = json.dumps(
      [
        {
          'name':         row['name'],
          'field':        row['field'],
          'born':         row['born'],
          'nobel_prize':  row['nobel_prize'],
          'extract_ref':  row['name'].replace(' ', '_').lower()
        } for row in values
      ]
    )

    return output


print(csv_to_json(source_file))

# Working with immutable data structures

Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel_prize'])

# A tuple containing a number of items, which are also tuples, is an immutable data structure:
# scientists = (
#     Scientist(name = 'Ada Lovelace', field = 'maths', born = 1815, nobel_prize = False),
#     Scientist(name = 'Emmy Noether', field = 'maths', born = 1882, nobel_prize = False),
#     Scientist(name = 'Marie Curie', field = 'physics', born = 1867, nobel_prize = True),
#     Scientist(name = 'Tu Youyou', field = 'chemistry', born = 1930, nobel_prize = True),
#     Scientist(name = 'Ada Yanoth', field = 'chemistry', born = 939, nobel_prize = True),
#     Scientist(name = 'Vera Rubin', field = 'astronomy', born = 1928, nobel_prize = False),
#     Scientist(name = 'Sally Ride', field = 'physics', born = 1951, nobel_prize = False)
# )

# # output = [x for x in filter(lambda x: x.nobel_prize == True, scientists)]
# # print(output)

# ts = tuple(filter(lambda x: x.nobel_prize, scientists))

# for x in ts:
#   print(x)

# print('Functional re-write:')

# # Functional programs consist of small, single-job chunks of code which can be easily composed.
# # The above code re-written functionally to improve readability:

# def nobel_filter(x):
#   return x.nobel_prize is True


# [print(x) for x in tuple(filter(nobel_filter, scientists))]

# print('Generator re-write:')

# # Same code using a generator function
# print(tuple(x for x in scientists if x.nobel_prize))

# print('Pythonic re-write:')

# # Crushing it down further with a list comprehension (the 'Pythonic' way):
# [print(x) for x in scientists if x.nobel_prize]
