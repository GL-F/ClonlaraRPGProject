import numpy as np
import pickle
SCREEN_WIDTH = 960  #initialize pygame's  screen
SCREEN_HEIGHT = 960 #width

class Case:
    def __init__(
            self, 
            name:str,        #name, idk if this will be used, but it's here
            hp:int,          #the amount of HPs the case has
            hardness:float,  #hardness, is a parameter that define wether the case takes damages in function of what do you break it with
            blast_res:float, #hardness but for explosions (water have infinite).
            crossable:bool,  #is the case crossable by an entity.
            tags:list,       #tags that will say about everything about the case, if it has the tag "rock" for exemple, then, every event that targets allOf("rock") will target it.
            
            ):
        self.name = name
        self.hp = hp
        self.hardness = hardness
        self.blast_res = blast_res
        self.crossable = crossable
        self.tags = tags
def get_case(number): #returns a Case object
    return cases_dict[number]
        
cases_dict = { #interger -> Case
    0: Case("border",9999,9999.0, 9999.0, True, ["unbreakable"]), # name = rock, HPs = 9999, hardness = 9999, blast_res = 9999, can't be crossed, has "unbreakable" tag
    1: Case("t1_rock", 20, 20.0, 40.0, True, ["material/rock","block_vision"]),
    2: Case("grass",9999, 9999.0, 9999.0, True, []),
    3: Case("t2_rock", 50, 50.0, 100.0, True, ["material/rock"]),
    10:Case("t3_rock", 150, 150.0, 225.0, True, ["material/rock"])
}
class Stage:
    def __init__(self, path:str):
        self.path = path

    def get_stage(self): #gets the stage from a pickle binary file and make it a numpy ndarray
        with open(self.path, "rb") as s : #open
            file = pickle.load(s) # load
        
        return file #can be replace
    
    def write_stage(name:str, stage:np.ndarray): #has no use while game is running but is used to writte maps into pickles binary files
        with open("data/stages/{name}", "wb") as path:
            pickle.dump(stage, path)

""""use example :"""
#   my_stage = np.array(
#       [
#           [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [3,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [3,0,0,3,3,0,0,0,0,0,0,0,0,0,0],
#           [3,0,0,3,0,0,0,3,0,0,0,0,0,0,0],
#           [3,3,3,3,3,3,3,3,0,0,0,0,0,0,0],
#           [0,0,0,0,0,3,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,3,3,3,3,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#       ]
#   )
#   Stage("data/stages/my_stage").write_stage(my_stage)