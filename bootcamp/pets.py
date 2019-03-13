class Pet:

  allowed = ['dog', 'cat', 'bird', 'lizard']

  def __init__(self, name, species):
    if species not in Pet.allowed:
      raise ValueError(f"You can't have a {species} as a pet!")
    self.name = name
    self.species = species
