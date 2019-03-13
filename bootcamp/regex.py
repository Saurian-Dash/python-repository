# # Basic REGEX key symbols

# \d digit (0-9)
# \w word (any character but whitespace)
# \s whitespace (inc new line)

# # Capitalised symbols usually mean opposite

# \D not a digit
# \W not a word
# \S not whitespace

# # Basic quantifiers

# {3} exactly this many
# {3, 5} within this range
# {4,} four or more
# ? one or zero (optional)
# + one or more
# * zero or more

# # Character classes (groups of characters)

# # Anchors and boundaries

# ^ start of string
# $ end of string
# \b word boundary

# 0171 534-5967

# # Find 3 numbers between brackets
# \(\d{3}\)

# (123)
# 123
# (ABC)

# # Find properly formatted surnames (including hypenated)
# ^(Mr\.|Mrs\.)\s[\w-]+$

# Mr. Anderson
# Mr Roberts
# Mr. Smith
# Mrs. West

# # Find properly formatted full names
# ^(Mr\.|Mrs\.)\s([\w-]+)\s([\w]+)$

# Mr Johnson
# Mrs. Jones

# Find properly formatted emails 
# ^[a-zA-Z0-9-_\.]+@[a-z-A-Z0-9-_\.]+\.[a-zA-Z0-9]+$

# saurian_dash@runbox.com
# saur.dash@secretescapes.com
# saur dash@runbox.com
# saur_dash@secret@escapes.com

# # Extract domain from email address
# saurian_dash@secretescapes.com

# Intro to the re module

import re

# Define REGEX pattern
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# Search a string with pattern
res = pattern.search('Call me on 415 555-4242!')

# print(res)

def extract_phone(input):

  phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
  match = phone_regex.search(input)

  try:
    print(f'Matched phone number: {match.group()}')
    return match.group()
  except Exception:
    print(f'No match found for REGEX: {phone_regex}')


def is_valid_phone(input):
  
  phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
  match = phone_regex.findall(input)

  if match:
    return True
  return False


extract_phone('012 4532-9954')
extract_phone('012 432-1487')


def extract_all_phones(input):
  
  phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
  match = phone_regex.findall(input)

  try:
    print(match)
    return match
  except Exception:
    print(f'No match found for REGEX: {phone_regex}')


extract_all_phones('Call me on 456 422-6579 or 012 598-1127')


print(is_valid_phone('124 885-4512'))
print(is_valid_phone('124 88s5-4512'))
print(is_valid_phone('124 8815-4512a'))


# Object oriented programming example:

def phone_number_looper(input):
  output = [{is_valid_phone(x): x} for x in input]
  print(output)
  return output


phone_number_looper(extract_all_phones('Give me a call on 01523 575015 or 020 752-5229. Or failing that: 012 779-4512'))

# Perfect Python email REGEX
 	
email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

'01001101 01 01001110 1010110 101000 10100 1010   10101101'

# Group naming
# ?P<name>
# Example (?P<first>[a-zA-Z]+)

input_text = 'Mr. Saur Dash'

def group_naming(s):

  word_regex = re.compile(r'^(?P<title>Mr\.|Mrs\.|Ms\.)\s(?P<first>[a-zA-Z]+)\s(?P<last>[a-zA-Z]+)')
  matches = word_regex.search(s)
  title = matches.group(1).replace('.', '')
  first_name = matches.group(2)
  last_name = matches.group(3)

  print({'title': title, 'first': first_name, 'last': last_name})
  return (title, first_name, last_name)


print(group_naming(input_text))


# Perfect REGEX date parser

uk_date_regex = re.compile(r'^(?:(?:31(\/|-|\.|,)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.|,)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.|,)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.|,)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$', re.VERBOSE)

def parse_date(s, p):
    
    pattern = re.compile(p)
    match = pattern.search(s)
    
    if match:
        return match.group()

    return None

print(parse_date('14-06-1978', uk_date_regex))

# REGEX compilation flags

# VERBOSE flag

fugly_pattern = r'^(?P<day>\d{2})[\/|\-|\.|,](?P<month>\d{2})[\/|\-|\.|,](?P<year>\d{4})$'

pretty_pattern = re.compile(r"""
  ^
  (?P<day>\d{2})    # Day element: 2-digit check
  [\/|\-|\.|,]      # Allows a single '/', '.' or ',' delimiter
  (?P<month>\d{2})  # Month element: 2-digit check
  [\/|\-|\.|,]      # Allows a single '/', '.' or ',' delimiter
  (?P<year>\d{4})   # Year element: 4-digit check
  $
  # re.VERBOSE or re.X
""", re.X)
