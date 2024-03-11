import game.characters as ch

class Game():
    """
    The main class, which
    will probably run the UI
    """
    def __init__(self, pc=ch.Character()):
        self.pc = pc # player character