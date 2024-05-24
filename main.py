import pygame
from game.board import *
from game.actions import *
import game.characters as ch

class Game():
    """
    The main class, which
    will probably run the UI
    """
    def __init__(self, pc=ch.Character()):
        self.pc = pc # player character
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #display


class SpriteSheet():#spritesheet class to get sprites from spritesheets
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour): #frame is the pos of our framed, height and width are dimensions, scale is a scale multiplier, and colour for the surounding
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height)) 
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image


pygame.display.set_caption('Game')#window's title

sprite_sheet_image = pygame.image.load('assets/textures/sprites/spritesheet.png').convert_alpha() #takes the spritesheet from assets (a random one i found open source justr for testing)
sprite_sheet = SpriteSheet(sprite_sheet_image) #creates a SpritSheet obejct

BLACK = (0, 0, 0) #just a background color for testing


frame_0 = SpriteSheet(sprite_sheet_image).get_image(4, 24, 24, 3, BLACK) # frame 1 of the animation
frame_1 = SpriteSheet(sprite_sheet_image).get_image(5, 24, 24, 3, BLACK) # frame 2 of the animation
frame_2 = SpriteSheet(sprite_sheet_image).get_image(6, 24, 24, 3, BLACK) # frame 3 of the animation
frame_3 = SpriteSheet(sprite_sheet_image).get_image(7, 24, 24, 3, BLACK) # frame 4 of the animation
a_sprite = [frame_0, frame_1, frame_2, frame_3] #list for the for boucle with all of the frames
current_stage = "data/stages/test_stage.pickle" 
background = Stage(current_stage).get_stage() 
pos = [0, 0] #starting pos for testing which shall be defined somewhere in the assets in the end
stage = Stage("data/stages/test_stage.pickle").get_stage()  #stage as a np.ndarray
stage_var = movement("player", False, stage, pos, "left")   #stage and moving char for testing which shall be defined somewhere in the assets in the end
is_running = True
while is_running: #main game loop
    stage_var.pos = pos
    for num in range(len(a_sprite)):    #animates the sprite from the spritesheet
        screen.fill(BLACK)              #background black which will eventually be replaced with a beautiful background changing each stage
        screen.blit(a_sprite[num], (display_coords(pos=pos)[0],display_coords(pos=pos)[1])) #moves the sprite from one pos to another
        pygame.display.update() #updates the screen

    for event in pygame.event.get():    #watches the events
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                new_pos = stage_var.deplace("left")   #events to move left
            if event.key == pygame.K_RIGHT :
                new_pos = stage_var.deplace("right")   #events to move right
            if event.key == pygame.K_UP :
                new_pos = stage_var.deplace("up")   #events to move up
            if event.key == pygame.K_DOWN :
                new_pos = stage_var.deplace("down")   #events to move down
            pos = new_pos
            print(pos, stage_var.pos, display_coords(pos)) #juste for testing
        if event.type == pygame.QUIT: #if we click on the red X on top right of the window, the games stops
            is_running = False
            print("game terminated")
    pygame.display.update()
pygame.quit()


