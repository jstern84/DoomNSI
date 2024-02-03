# Séance 3 du 30/01/2024
# Déplacement avec touches maintenues

# module pyglet principal (qu'on nenomme en pg pour plus de simplicité)
import pyglet as pg
# import des fonctions trigo du module math
from math import cos, sin

# création de la fenêtre pour le plan 2D
# résolution : 320x200 pour le Doom de l'époque
window2d = pg.window.Window(320, 200, "Plan 2D", vsync=False)

# variables globales 
x, y, a = 160, 100, 0 # position et angle du joueur
# "batch" du joueur
joueur = pg.graphics.Batch()
# création du dico contenant les actions actives (True) ou inactives (False)
actions = { 'avancer': False, 'reculer': False,
            'tourner_gauche': False, 'tourner_droite': False }

# détection d'un touche pressée au clavier
@window2d.event
def on_key_press(symbol, modifiers):
    # Touche Q : on quitte le jeu  
    if symbol == pg.window.key.Q: pg.app.exit()
    # touches de déplacement
    if symbol == pg.window.key.UP: actions['avancer'] = True
    if symbol == pg.window.key.DOWN: actions['reculer'] = True
    # touches pour tourner
    if symbol == pg.window.key.LEFT: actions['tourner_gauche'] = True
    if symbol == pg.window.key.RIGHT: actions['tourner_droite'] = True
          
# détection d'un touche relâchée au clavier
@window2d.event
def on_key_release(symbol, modifiers):
    # touches de déplacement
    if symbol == pg.window.key.UP: actions['avancer'] = False
    if symbol == pg.window.key.DOWN: actions['reculer'] = False
    # touches pour tourner
    if symbol == pg.window.key.LEFT: actions['tourner_gauche'] = False
    if symbol == pg.window.key.RIGHT: actions['tourner_droite'] = False

# évènement principal : rendu graphique
@window2d.event
def on_draw():
    global x, y, a
    window2d.clear()
    # le joueur comme un cercle
    circle = pg.shapes.Circle(x, y, 10, color =(50, 225, 30), batch = joueur)
    # segment "vecteur vitesse" qui pointe vers la direction de visée
    visée = pg.shapes.Line(x, y, x + 20*cos(a), y + 20*sin(a), width=5, batch = joueur)
    # on dessine le "batch"
    joueur.draw()
    
def update(dt):
    global x, y, a
    if actions['avancer']:
        x += 20*cos(a)	#avancer
        y += 20*sin(a)
    if actions['reculer']:
        x -= 20*cos(a)	#reculer
        y -= 20*sin(a)
    if actions['tourner_gauche']:
        a += 0.2 	# rotation gauche
    if actions['tourner_droite']:
        a -= 0.2	# rotation droite

# boucle principale (30 Hz)
pg.clock.schedule_interval(update, 1/30.0)

# lancement du jeu
pg.app.run()