import numpy as np

if __name__ == "__main__":
    import board as board
else:
    import game.board as board
class attack: 
    def __init__(self, atk:float, shield:float, atk_lock:bool, buff:str, properties:str=None):
        self.atk = atk              #attack points
        self.shield = shield        #deffensive points
        self.atk_lock = atk_lock    #weather attack is locked (if ur frozen for exemple)
        self.buff = buff            #any buff that can - or + values
        self.properties = properties#if you want the deg caculation to be executate différently
    def dealt_damages(self):
        if self.atk_lock == True:
            return False
        if self.properties == None :
            exec(self.buff)
            deg = self.atk - self.shield
        exec(self.properties)
        return deg
    
class movement:
    def __init__(self, char, lock:bool, stage:np.ndarray, pos:list, dir:str):          
        self.char = char    #who moves ? 
        self.lock = lock    #weather the player is able to move, he cannot move durring a combat for exemple 
        self.stage = stage  #the stage
        self.pos = pos      #position = [x, y] in the level
        self.dir = dir      #direction up, down, right, left
     
    def deplace(self):
        backup_pos = self.pos
        y = self.pos[0] #highness
        x = self.pos[1] #widthness
        if self.lock == True: 
            return backup_pos #returns the starting position if the character is locked, like in a fight or a dialog
        try :       
            if self.dir == "up" and board.get_case(self.stage[x, y+1]).crossable == True:      #if the direction is "up" adds 1 y      unless the up case is not "crossable"
                self.pos[1] += 1                                                                    #
            if self.dir == "down" and board.get_case(self.stage[x, y-1]).crossable == True:    #if the direction is "down" removes 1 y unless the down case is not "crossable"
                self.pos[1] -= 1                                                                    #
            if self.dir == "right" and board.get_case(self.stage[x+1, y]).crossable == True:   #if the direction is "right" add 1 x    unless the right case is not "crossable"
                self.pos[0] += 1                                                                    #
            if self.dir == "left" and board.get_case(self.stage[x-1, y]).crossable == True:    #if the direction is "left" removes 1 x unless the left case is not "crossable"
                self.pos[0] -= 1
            return self.pos
        except IndexError :     #unless it's the end of the map (indexError OutOfBound)
            return backup_pos   #returns the starting position ; doesn't move
        
""""mixes pg'sdisplay coords where 0,0 is on left top with np ones where 0,0 is on left down"""
def  display_coords(pos:list):  #pos = [x,y] with 0,0 on left bottom
    display_x = pos[0]*64       #x
    display_y = board.SCREEN_HEIGHT - (pos[1]*64) #y
    display_pos=[display_x,display_y]           #[x,y] with 0,0 on left top ; what we needed for display
    return display_pos          


