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

class NonCombatNPC(Actor):
    """
    Non Player Character
    """
    def __init__(self, name="Name", hp=10):
        super().__init__(name, hp)

class CombatNPC(Actor):
    """
    Non Player Character
    """
    def __init__(self, name="Name", hp=10):
        super().__init__(name, hp)