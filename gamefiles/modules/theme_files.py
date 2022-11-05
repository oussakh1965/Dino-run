"""importation des modules"""
import pygame
import os.path
import random
path = os.path.dirname(__file__)
parpath = os.path.join(path, os.pardir)
##################################################################################


def load_assets(player_height, theme):
    '''cette fonction genere en fonction du theme choisi tous les fichiers images du theme choisi

    Parameters :
    ------------------------------
    player_height : int, la hauteur choisie sert de repere pour redimensionner toutes les images du theme
    theme : str, indique le theme

    Returns :
    ------------------------------
    un dictionnaire contenant toutes les images relatives au joueur
    '''
    player_assets = {}
    dinorun1 = pygame.image.load(os.path.join(
        parpath, 'assets', theme, 'Dino', 'DinoRun1.png')).convert_alpha()
    dinorun1 = pygame.transform.scale(
        dinorun1, (player_height*.93, player_height))
    dinorun2 = pygame.image.load(os.path.join(
        parpath, 'assets', theme, 'Dino', 'DinoRun2.png')).convert_alpha()
    dinorun2 = pygame.transform.scale(
        dinorun2, (player_height*.93, player_height))
    player_assets['normal'] = [dinorun1, dinorun2]
    dinodown1 = pygame.image.load(os.path.join(
        parpath, 'assets', theme, 'Dino', 'DinoDuck1.png')).convert_alpha()
    dinodown1 = pygame.transform.scale(
        dinodown1, (player_height*1.25, player_height*.63))
    dinodown2 = pygame.image.load(os.path.join(
        parpath, 'assets', theme, 'Dino', 'DinoDuck2.png')).convert_alpha()
    dinodown2 = pygame.transform.scale(
        dinodown2, (player_height*1.25, player_height*.63))
    player_assets['down'] = [dinodown1, dinodown2]
    dinojump = pygame.image.load(os.path.join(
        parpath, 'assets', theme, 'Dino', 'DinoJump.png')).convert_alpha()
    dinojump = pygame.transform.scale(
        dinojump, (player_height*.93, player_height))
    player_assets['dinojump'] = dinojump
    track = pygame.image.load(os.path.join(
        parpath, 'assets', theme, 'Other', 'Track.png')).convert_alpha()

    if theme == 'xmas':  # Christmas theme has some addictional images
        sky = pygame.image.load(os.path.join(
            parpath, 'assets', theme, 'Other', 'sky.png')).convert_alpha()
        bg = pygame.image.load(os.path.join(
            parpath, 'assets', theme, 'Other', 'bg.png')).convert_alpha()
        player_assets['bg'] = bg
        player_assets['sky'] = sky
    else:
        # a visual bug happens in classic theme without this line
        track.set_colorkey([255, 255, 255])
    player_assets['track'] = track
    return player_assets
#############################################################################


def load_obstacles(obstacletypes, player_height, theme):
    '''loads all images related to obstacles according to the used theme 

    Parameters:
    ----------------
    obstacletypes : list, containing all information related to the obstacles 
    player_height : int, used to normalize all picture sizes
    theme : str, indiquates the  theme

    Returns:
    ------------------
    a dictionary containing all the obstacle assets
    '''
    obstacle_assets = {}
    for i in range(7):
        if i == 6:
            image1 = pygame.image.load(os.path.join(
                parpath, 'assets', theme, 'Bird', 'bird1.png')).convert_alpha()
            image1 = pygame.transform.scale(
                image1, (obstacletypes[i][1]*player_height, obstacletypes[i][2]*player_height))

            image2 = pygame.image.load(os.path.join(
                parpath, 'assets', theme, 'Bird', 'bird2.png')).convert_alpha()
            image2 = pygame.transform.scale(
                image2, (obstacletypes[i][1]*player_height, obstacletypes[i][2]*player_height))
            obstacle_assets['bird'] = [image1, image2]
        else:
            name = obstacletypes[i][0]+'.png'
            image = pygame.image.load(os.path.join(
                parpath, 'assets', theme, 'Cactus', name)).convert_alpha()
            image = pygame.transform.scale(
                image, (obstacletypes[i][1]*player_height, obstacletypes[i][2]*player_height))
            obstacle_assets[obstacletypes[i][0]] = image
    return obstacle_assets
##################################################################


def display_dino(player, timer, game_state, screen, assets):
    '''displays the player in a screen using the loaded assets

    Parameters :
    ----------------
    player : pygame.Rect , player rectange 
    timer: list
    game_state : dictionary containing game state
    screen : pygame.Surface type
    assets : assets dictionary

    Returns:
    ------------------
    timer : list
    '''
    if game_state['game_not_started']:
        screen.blit(assets['dinojump'], (player.x, player.y))

    if game_state['running']:
        screen.blit(assets[game_state['pos']][timer[1]], (player.x, player.y))
        if timer[0] == 12:
            timer[1] = 1-timer[1]
            timer[0] = 0
        else:
            timer[0] += 1
    if game_state['jumping']:
        screen.blit(assets['dinojump'], (player.x, player.y))
    return timer
#####################################################################


def display_obstacles(obstacles, obstacle_assets, screen, obstacletimer):
    '''displays the obstacles in a screen using the loaded assets,obstacletimer used to animate the bird

    Parameters :
    ----------------
    obstacles : list, contains all obstacle rectangles 
    obstacle_assets : 
    screen : pygame.Surface type
    obstacle_assets : obstacle assets dictionary

    Returns:
    ------------------
    obstacletimer : list
    '''
    if obstacletimer[0] == 20:
        obstacletimer[1] = 1-obstacletimer[1]
        obstacletimer[0] = 0
    else:
        obstacletimer[0] += 1
    for obstacle in obstacles:
        if obstacle[0] == 'bird':
            screen.blit(
                obstacle_assets[obstacle[0]][obstacletimer[1]], (obstacle[1].x, obstacle[1].y))
        if obstacle[0] != 'bird':
            screen.blit(obstacle_assets[obstacle[0]],
                        (obstacle[1].x, obstacle[1].y))
    return obstacletimer
#########################################################################################


def track_scroll(track, trackx, speed, screen, game_not_started):
    '''animates the track when the game is started

    Parameters:
    -----------------
    track : pygame.Surface, track image
    trackx : int, current track position
    speed : int, track scrolling speed
    screen : game screen
    game_not_started : bool, indiquates if the game is started

    Returns:
    ----------------
    bgx : int, current position
    '''
    screen.blit(track, (trackx, 215))
    screen.blit(track, (trackx+2404, 215))
    if not game_not_started:
        trackx -= speed
        if trackx <= -2404:
            screen.blit(track, (trackx+2404, 215))
            trackx = 0
    return trackx
########################################


def create_cloud():
    '''creates a cloud in the right side of the screen with random y_coordinate

    Parameters:
    ---------------
    None

    Returns:
    ---------------
    a list containing the cloud image and its coordinates
     '''
    image = pygame.image.load(os.path.join(
        parpath, 'assets', 'Classic', 'Other', 'Cloud.png')).convert_alpha()
    return [image, [600, random.randint(0, 175)]]
#####################################################################


def process_clouds(clouds, screen):
    '''animates all the clouds in the screen 

    Parameters:
    -----------------
    clouds : a list containing all the clouds in the screen
    screen : game screen 

    Returns:
    -----------------
    the processed list of clouds
    '''
    for i, cloud in sorted(enumerate(clouds), reverse=True):
        if cloud[1][0] < -100:
            clouds.pop(i)
        else:
            screen.blit(cloud[0], cloud[1])
            clouds[i][1][0] -= 1
    return clouds
####################################################################


def process_background(bg, bgx, screen, game_not_started):
    '''processes the background in the Christmas theme

    Parameters:
    ---------------
    bg : pygame.Surface ,background image
    bgx : current background position
    screen : game screen 
    game_not_started : bool, idiquates if game started 

    Returns :
    bgx : int, current background position
    '''
    screen.blit(bg, (bgx, 25))
    screen.blit(bg, (bgx+1396, 25))
    if not game_not_started:
        bgx -= 1
        if bgx <= -1396:
            screen.blit(bg, (bgx+1396, 25))
            bgx = 0

    return bgx


def process_sky(sky, skyx, screen, game_not_started):
    '''animates the sky in the Christmas theme 

    WORKS THE SAME WAY AS proccess_background
    '''
    screen.blit(sky, (skyx, -120))
    screen.blit(sky, (skyx+600, -120))
    if not game_not_started:
        skyx -= .25
        if skyx <= -600:
            screen.blit(sky, (skyx+1396, 25))
            skyx = 0
    return skyx
########################################################################


def process_snow(snow_list, screen, game_not_started, state):
    '''makes the snawfall animation 

    Parameters :
    ---------------
    snow_list : list, contains all snow particles as pygame circle objects
    screen : game screen 
    game_not_started : bool, indiquates if game started 
    state : int, indiquates snow type, 0 no snow, 1 slow snow, 2 fast snow

    Returns:
    ---------------
    the updated snow_list
    '''
    if state == 1:
        delta_v = 0
    else:
        delta_v = 2
    if not game_not_started:
        if len(snow_list) < 500*state:
            for j in range(state):
                chance = random.choices(
                    [True, False], weights=(70, 30), k=1)[0]
                if chance:
                    coordinate_x = random.randint(0, 600)
                    coordinate_y = 0
                else:
                    coordinate_x = 600
                    coordinate_y = random.randint(0, 250)
                velocity_x = random.randint(-20, 1)/20 - delta_v*3
                velocity_y = random.randint(20, 25)/10 + delta_v*2
                snow_list.append(
                    [[coordinate_x, coordinate_y], [velocity_x, velocity_y]])
        for i, particle in sorted(enumerate(snow_list), reverse=True):
            pygame.draw.circle(screen, 'white', particle[0], 2)
            if particle[0][0] < -1 or particle[0][0] > 601 or particle[0][1] > 251:
                snow_list.pop(i)
            else:
                snow_list[i][0][0] += snow_list[i][1][0]
                snow_list[i][0][1] += snow_list[i][1][1]
    return snow_list
#######################################################################


def load_animation():
    animation = []
    sound = pygame.mixer.Sound(os.path.join(
        parpath, 'assets', 'wip', 'sound.wav'))
    for i in range(44):
        number = i
        if number < 10:
            id = '0'+str(number)
        else:
            id = str(number)
        name = 'frame_{}_delay-0.1s.gif'.format(id)
        image = pygame.image.load(os.path.join(
            parpath, 'assets', 'wip', name)).convert()
        animation.append(image)
    return animation, sound
