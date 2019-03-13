import pdb

class User:

  active_users = 0
  
  @classmethod
  def display_active_users(cls):
    return f'Active users: {cls.active_users}'

  @classmethod
  def from_string(cls, data_str):
    first, last, age = data_str.split(',')
    return cls(first, last, int(age))

  # Initialise instance
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age = int(age)
    User.active_users += 1

  def __repr__(self):
    return f'Name: {self.full_name()}\nAge: {self.age}'

  # Instance methods
  def full_name(self):
    return f'{self.first}{self.last}'

  def initials(self):
    return f'{self.first[0]}.{self.last[0]}.'.upper()

  def intro(self):
    return f'My name is {self.first} {self.last} and I am {self.age} years old.'
    

user1 = User('Aeon', 'Calcos', 35)
user2 = User('Saur', 'Dash', 40)

print(user1.first)
print(user1.last)
print(user1.age)
print(user1.full_name())
print(user1.initials())
print(user1.intro())


def error_handler():
  try:
    num = int(input('Please enter a number: '))
  except (TypeError, ValueError):
    print('Error: Input must be a number')
  else:
    return f'You entered: {num}'
  finally:
    print('***This line runs no matter what***')


user3 = User.from_string('John, Smith, 24')

print(User.display_active_users())
print(user3)
