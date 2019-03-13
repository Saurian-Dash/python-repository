# Python Tricks

def message(txt):
  return f'Do I remember {txt}?'

print(message('python'))


class MyClass():
  def __init__(self, prm1, prm2):
    self.prm1 = prm1
    self.prm2 = prm2
  

  def __repr__(self):
    return f'Parameter 01: {self.prm1}\nParameter 02: {self.prm2}'


my_instance = MyClass('Aeon', 'Calcos')
print(my_instance)

my_dict = [
  {
    'id': 1,
    'name': 'jane',
    'email': 'jane@runbox.com'
  },
  {
    'id': 2,
    'name': 'dave',
    'email': 'dave@runbox.com'
  },
  {
    'id': 3,
    'name': 'john',
    'email': 'john@runbox.com'
  }
]

my_listing = [print(i) for i in my_dict]
my_listing

