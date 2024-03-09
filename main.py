class Actor():
    """
    Mother class of 
    Character and NPC
    """
    def __init__(self, name="Name", hp=10):
        self.name = name
        self.hp = hp # hit points

class Character(Actor):
    """
    The player character
    """
    def __init__(self, name="Name", hp=10):
        super().__init__(name, hp)

class NPC(Actor):
    """
    Non Player Character
    """
    def __init__(self, name="Name", hp=10):
        super().__init__(name, hp)

class Game():
    """
    The main class, which
    will probably run the UI
    """
    def __init__(self, pc=Character()):
        self.pc = pc # player character