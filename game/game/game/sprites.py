import pygame 
import sprite_sheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT =500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image_idle = pygame.image.load(r'game\Punk\Punk_idle.png').convert_alpha()
sprite_sheet_image_run = pygame.image.load(r'game\Punk\Punk_run.png').convert_alpha()
sprite_sheet_image_jump = pygame.image.load(r'game\Punk\Punk_jump.png').convert_alpha()

sprite_sheet_image_idle_left = pygame.image.load(r'game\Punk\Punk_idle_left.png').convert_alpha()
sprite_sheet_image_run_left = pygame.image.load(r'game\Punk\Punk_run_left.png').convert_alpha()
sprite_sheet_image_jump_left = pygame.image.load(r'game\Punk\Punk_jump_left.png').convert_alpha()

spritSheetIdle = sprite_sheet.SpriteSheet(sprite_sheet_image_idle)
spritSheetRun = sprite_sheet.SpriteSheet(sprite_sheet_image_run)
spritSheetJump = sprite_sheet.SpriteSheet(sprite_sheet_image_jump)

spritSheetIdle_left = sprite_sheet.SpriteSheet(sprite_sheet_image_idle_left)
spritSheetRun_left = sprite_sheet.SpriteSheet(sprite_sheet_image_run_left)
spritSheetJump_left = sprite_sheet.SpriteSheet(sprite_sheet_image_jump_left)

BG = (50,50,50)
BLACK = (0,0,0)

animation_list = []

animation_idle = [4]
animation_run = [6]
animation_jump = [4]

animation_idle_left = [4]
animation_run_left = [6]
animation_jump_left = [4]

action = 0

last_update = pygame.time.get_ticks()
animation_cd = 190
frame = 0

def create_animation(sprite_sheet, animation_steps, step_counter, animation_list, black):
    for animation in animation_steps:
        temp_img_list = []
        for _ in range(animation):
            temp_img_list.append(sprite_sheet.get_image(step_counter, 48, 34, 3, black))
            step_counter += 1
        animation_list.append(temp_img_list)

def create_reverse_animation(sprite_sheet, animation_steps, step_counter, animation_list, black):
    for animation in animation_steps:
        temp_img_list = []
        # Start from the last frame to the first for left animation
        for i in range(animation - 1, -1, -1):
            temp_img_list.append(sprite_sheet.get_image(step_counter + i, 48, 34, 3, black))
        animation_list.append(temp_img_list)
        step_counter += animation  # Update step_counter for the next animation


create_animation(spritSheetIdle, animation_idle, 0, animation_list, BLACK)
create_animation(spritSheetRun, animation_run, 0, animation_list, BLACK)
create_animation(spritSheetJump, animation_jump, 0, animation_list, BLACK)

create_reverse_animation(spritSheetIdle_left, animation_idle_left, 0, animation_list, BLACK)
create_reverse_animation(spritSheetRun_left, animation_run_left, 0, animation_list, BLACK)
create_reverse_animation(spritSheetJump_left, animation_jump_left, 0, animation_list, BLACK)

run = True
last_direction = 0
while run:

    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cd:
        frame+=1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame=0

    screen.blit(animation_list[action][frame],(210,190))

    keys = pygame.key.get_pressed()
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
   
        else:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT and action != 1:  
                    action = 1 
                    frame = 0 
                    last_direction=0
                if event.key == pygame.K_UP and action != 2: 
                    if last_direction == 0:
                        action = 2 
                    else:
                        action = 5 
                    frame = 0  

                if event.key == pygame.K_LEFT and action != 4:
                    action = 4  
                    frame = 0 
                    last_direction=1

            else:
                if last_direction == 0:
                    action=0
                if last_direction==1:
                    action=3
                frame=0
            
    pygame.display.update()






