# from random import choice

# random_list = ['Carmine', 'Aeon', 'Scutes', 'Ki.Keema']

# def display_random_name(x):
#   return choice(x)

# print(display_random_name(random_list))

# for name in random_list:
#   print(name)


# def partition(l, callback):
#     return [[l.pop(l.index(i)) for i in l if callback(i)],l]


# def calculate(**kwargs):

#     # Lookup table of operations
#     operations = {
#         'add': kwargs.get('first', 0) + kwargs.get('second', 0),
#         'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
#         'multiply': kwargs.get('first', 0) * kwargs.get('second', 0),
#         'divide': kwargs.get('first', 0) / kwargs.get('second', 1)
#     }

#     # Perform calculation based on lookup table results
#     calculation = operations[kwargs.get('operation', 'add')]

#     # Output control flow
#     if kwargs.get('make_float'):
#         return '{} {}'.format(kwargs.get('message', 'The result is'), float(calculation))
#     return '{} {}'.format(kwargs.get('message', 'The result is'), int(calculation))

input_fields = ['Booking Id', 'Booking Name', 'Lead Guest Name', 'Currency Code', 'Total Price']


def convert_fields(fields):
    output_fields = [{'name': field.lower().replace(' ', '_'),'data_type': 'string','extract_ref': field} for field in fields]
    print(output_fields)


convert_fields(input_fields)

nums = [1,2,3,4,5,6]

my_list = [print(n**2) for n in nums]

my_list = map(lambda n: n**2, nums)

# Lambda function: An anonymous function which runs in place
# Lambda syntax: lambda obj: action

lambda n: n**2

# Map function: Run a function on each item in an iterable object
map_list = map(lambda n: n**2, nums)

# Map with declared function
def square_root(n):
  return n**2

another_map_list = map(square_root, nums)



