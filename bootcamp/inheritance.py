class Human:
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self._age = int(max(age, 0))

  @property
  def full_name(self):
    """
    Returns first and last name of Human instance\n
    Type: string
    """
    return f'{self.first} {self.last}'

  @property
  def age(self):
    """
    Returns Human instance _age value\n
    Type: int
    """
    return self._age

  @age.setter
  def age(self, value):
    if value >= 0:
      self._age = value
    else:
      raise ValueError('Age cannot be negative!')

  def __repr__(self):
    return f'Name: {self.first} {self.last}\nAge: {self._age}'


class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def make_sound(self, sound):
    print(f'This animal says {sound}')

  def __repr__(self):
    return f'{self.name} is a {self.species}'


class Cat(Animal):
  def __init__(self, name, breed, toy):
    super().__init__(name, species='Cat')
    self.breed = breed
    self.toy = toy

  @property
  def play(self):
    return f'{self.name} plays with {self.toy}'
    

blue = Cat('Blue', 'Scottish Fold', 'String')
print(blue)
print(blue.play)

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
        
        
class NPC(Character):
    def __init__(self, name, hp, level, speech):
        super().__init__(name, hp, level)
        self.speech = speech
        
    def speak(self):
        print(self.speech)


aeon = NPC('Aeon', 9999, 99, 'Rarrraggh!!')
print(aeon.name)
aeon.speak()





