"""importation des modules"""
import os.path
import random
import pygame
from pygame.locals import RESIZABLE, QUIT, USEREVENT  # pylint: disable=no-name-in-module
from pygame.constants import K_DOWN, K_SPACE, K_UP, KEYDOWN, KEYUP, K_ESCAPE  # pylint: disable=no-name-in-module
from pygame import display
import pygame.freetype
##################################################################################
pygame.mixer.init()
#################################################################################
# fixing the directory not found problem
path = os.path.dirname(__file__)
parpath = os.path.join(path, os.pardir)
###############################
gosound = pygame.mixer.Sound(os.path.join(
    parpath, 'sounds', 'game.over.sound.wav'))
jumpsound = pygame.mixer.Sound(os.path.join(parpath, 'sounds', 'jump.wav'))
score100 = pygame.mixer.Sound(os.path.join(
    parpath, 'sounds', 'score100.wav'))
PLAYER_HEIGHT = 40
obstacletypes = [['big1', .48, .95], ['big2', .99, .95], ['big3', 1.02, .95],
                 ['small1', .4, .71], ['small2', .68, .71], ['small3', 1.05, .71],
                 ['bird1', .97, .68, 233], [
                     'bird2', .97, .68, 233-PLAYER_HEIGHT*.63],
                 ['bird3', .97, .68, 160]]
default_state = {'game_not_started': True, 'running': False, 'jumping': False,
                 'pos': 'normal', 'player_pos': [[80, 235], [0, 0]], 'crashed': False,
                 'player': pygame.Rect(80, 235-PLAYER_HEIGHT, PLAYER_HEIGHT*.93, PLAYER_HEIGHT)}
############################# functions #############################################


def check_events(game_state, obstacles, SPAWNOBSTACLE):
    """cette fonction permet de changer game_state, générer des obstacles
    et initialiser le jeu

    Parameters
    -----------------------
    game_state : dictionnaire
    obstacles : list
    SPAWNOBSTACLE : event

    Returns :
    ----------------------
    game_state
                variables contrôllant le jeu
    obstacles
                liste des obstacles à afficher
    main_running : boolean
                lancer la boucle du jeu dans play.py
    """
    main_running = True  # pylint: disable=redefined-outer-name
    for event in pygame.event.get():
        if event.type == QUIT:
            game_state['crashed'] = True
            main_running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state['crashed'] = True
            if game_state['game_not_started']:
                game_state['running'] = True
                game_state['game_not_started'] = False
                game_state['start_time'] = pygame.time.get_ticks()
                pygame.time.set_timer(SPAWNOBSTACLE, 1000)
            if event.key == K_UP or event.key == K_SPACE:
                if not game_state['jumping']:
                    game_state['jumping'] = True
                    game_state['player_pos'][1][1] = -11
                    game_state['running'] = False
                    jumpsound.play()
            if event.key == K_DOWN:
                if game_state['jumping']:
                    game_state['player_pos'][1][1] = 7
                game_state['pos'] = "down"
        if event.type == KEYUP:
            if event.key == K_DOWN:
                game_state['pos'] = "normal"
            if event.key == K_UP:
                if game_state['player_pos'][1][1] <= -2:
                    game_state['player_pos'][1][1] = -2
        if not game_state['game_not_started']:
            if event.type == SPAWNOBSTACLE:
                obstacles.append(create_obstacle())
                pygame.time.set_timer(SPAWNOBSTACLE, random.randint(600, 1000))
    return game_state, obstacles, main_running
###############################################################################


def create_obstacle():
    """
    create_obstacle permet de générer les obstacles et
     les rectangles associés qui permettent de gérer les collisions

    Parameters :
    -------------------
    None

    Returns:
    -------------------
    name : str
                type d'obstacle
    rectangle qui permet la gestion de collision
    """
    obstacle = random.choice(obstacletypes)
    width = obstacle[1]*PLAYER_HEIGHT
    height = obstacle[2]*PLAYER_HEIGHT
    coordinates_x = 600
    if obstacle[0] in ['bird1', 'bird2', 'bird3']:
        name = 'bird'
        coordinates_y = obstacle[3]-height
    else:
        coordinates_y = 235-height
        name = obstacle[0]
    return name, pygame.Rect(coordinates_x, coordinates_y, width, height)
##################################################################################


def process_obstacle(obstacles, player, crashed, vel_x, screen, theme='default'):  # pylint: disable=too-many-arguments
    """
    process_obstacle permet d'animer les obstacles stockes dans la liste obstacles

    Parameters :
    -------------------
    obstacles : list
    player : pygame.Rect class
    crashed ; boolean
    screen
    theme : str

    Returns:
    ------------------
    obstacle_copy : list
                liste des obstacles après les modifications de position
    crashed : boolean
                permet de detecter la presence d'une collision
    """
    obstacle_copy = obstacles.copy()
    obstacle_copy = obstacles.copy()
    if len(obstacles) > 0:
        for i, rectangle in sorted(enumerate(obstacle_copy), reverse=True):
            if rectangle[1].x <= -50:
                obstacle_copy.pop(i)
            else:
                if pygame.Rect.colliderect(obstacle_copy[i][1], player):
                    gosound.play()
                    crashed = True
                if theme == 'default':
                    pygame.draw.rect(screen, 'red', obstacle_copy[i][1])
                obstacle_copy[i][1].x -= vel_x
    return obstacle_copy, crashed
##########################################################################


def dino_jump(game_state):
    """"
    dino_jump permet d'animer le saut du dinosaur avec une vitesse
     qui varie tout au long du saut afin de le rendre plus realiste

    Paremeters :
    -------------------
    game_state : dictionnaire

    Returns :
    -------------------
    game_state :
                dictionnaire modifié (position, jumping, running)
    """
    game_state['player_pos'][0][1] += game_state['player_pos'][1][1]
    game_state['player_pos'][1][1] += 0.6
    if game_state['player_pos'][0][1] >= 235:
        game_state['jumping'] = False
        game_state['running'] = True
        game_state['player_pos'][0][1] = 235
        game_state['player_pos'][1][1] = 0
    return game_state
#####################################################################


def detplayer(game_state):
    """
    detplayer permet de mettre à jour le rectangle du joueur avec sa position
    pour gérer les collision

    Parameters:
    ------------------
    game_state : dictionnaire

    Returns :
    ------------------
    player : pygame.Rect class
    """
    coordinates_x, coordinates_y = game_state['player_pos'][0]
    if game_state['pos'] == 'normal' or game_state['jumping']:
        player = pygame.Rect(coordinates_x, coordinates_y-PLAYER_HEIGHT,
                             PLAYER_HEIGHT*.93, PLAYER_HEIGHT)
        return player
    if game_state['pos'] == 'down':
        player = pygame.Rect(coordinates_x, coordinates_y-PLAYER_HEIGHT*.63,
                             PLAYER_HEIGHT*1.25, PLAYER_HEIGHT*.63)
        return player
############################# fonction #############################################


def score(game_state, font, screen, dark_text=True):
    """
    score permet d'afficher le score

    Parameters :
    ------------------------
    game_state : dictionnaire
    font : pygame class
    screen
    dark_text : booleen indique si le text est sombre ou non

    Returns :
    ------------------------
    delta_time : int
                represente le score
    """
    if dark_text:
        color = (100, 100, 100)
    else:
        color = (255, 255, 255)
    if game_state['game_not_started']:
        delta_time = 0
    else:
        current_time = pygame.time.get_ticks()
        delta_time = (current_time - game_state['start_time']) // 100
    score_text = "score : {}".format(delta_time)
    text_surf, text_rect = font.render(
        score_text, color, size=12)
    margin = 20
    size = (600, 250)
    text_pos = (size[0] - text_rect.width - margin,
                + text_rect.height + margin)
    screen.blit(text_surf, text_pos)
    if delta_time % 100 == 0 and delta_time > 0:
        score100.play()
    return delta_time
######################################################################


def difficulty(vel_x, score, old_score, step):
    """
    difficulty permet d'augmenter la difficulté du jeu en fonction du score

    Parameters :
    ----------------------
    vel_x : int
    score : int
    old_score : int
    step : int
                represente le pas d'incrementation de la vitesse

    Returns :
    ----------------------
    vel_x
                vitesse variée
    step
                pas variée
    """
    if score % step == 0 and old_score % step != 0:
        vel_x += 1
        step *= 4
    return vel_x, step
######################################################################################


def create_frame(game_state, obstacles, vel_x, screen, theme='default'):
    """
    create_frame permet d'animer les rectangle du games ;
     si le mode est en MVP elle les affiche sinon elle les sauvegarde

    Parameters :
    ------------------
    game_state : dictionnaire
    obstacles : list
    vel_x : int
    screen
    theme : str

    Returns:
    ------------------
    game_state :
                parametres contrôllant le jeu après modification
    obstacles :
                listes des obstacles rafraîchit
    """
    obstacles, game_state['crashed'] = process_obstacle(
        obstacles, game_state['player'], game_state['crashed'], vel_x, screen, theme)
    if game_state['jumping']:
        game_state = dino_jump(game_state)
    game_state['player'] = detplayer(game_state)
    if theme == 'default':
        pygame.draw.rect(screen, 'yellow', game_state['player'])
    return game_state, obstacles


####################################################################################################
# evenement virtuel pour générer les obstacles et les nuages
SPAWNOBSTACLE = USEREVENT
####################################################################################################


def play_game_mvp(vel_x):
    pygame.init()
    font = pygame.freetype.SysFont('Consolas', 30)
    gamedisplay = pygame.display.set_mode((1200, 600), RESIZABLE)
    screen = pygame.Surface((600, 250))
    clock = pygame.time.Clock()
    obstacles = []
    game_state = default_state.copy()
    game_state['player_pos'] = [[80, 235], [0, 0]]
    step = 100
    score_player = 0
    while not game_state['crashed']:
        screen.fill('white')
        game_state, obstacles, main_running = check_events(
            game_state, obstacles, SPAWNOBSTACLE)
        old_score = score_player
        score_player = score(game_state, font, screen)
        vel_x, step = difficulty(vel_x, score_player, old_score, step)
        game_state, obstacles = create_frame(
            game_state, obstacles, vel_x, screen)
        width, height = pygame.display.get_surface().get_size()
        h_1 = width*.416
        surf = pygame.transform.scale(screen, (width, h_1))
        gamedisplay.blit(surf, (0, (height-h_1)/2))
        display.update()
        clock.tick(60)
    if main_running:
        return True, score_player, main_running
    return False, score_player, main_running


#############################################################################
if __name__ == "__main__":
    gameover, player_score, main_running = play_game_mvp(5)
    pygame.quit()
    print('game over, your score is : {} '.format(player_score))
