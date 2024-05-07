# Séance 5 du 09/04/2024
# Création du module structure (classe Mur)

# module pyglet principal (qu'on nenomme en pg pour plus de simplicité)
import pyglet as pg
# import des fonctions trigo du module math
from math import cos, sin
# modules du jeu
import joueur as J
import structure as S

# création de la fenêtre pour le plan 2D
# résolution : 320x200 pour le Doom de l'époque
window2d = pg.window.Window(320, 200, "Plan 2D", vsync=True)

# Création d'une instance de Joueur
joueur = J.Joueur(160,100,0)

# Création d'instances de Mur
murs = [S.Mur(0,0,100,100), S.Mur(100,100,100,0), S.Mur(100,0,0,0)]
[mur.debug() for mur in murs]
[mur.tracer() for mur in murs]

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
    window2d.clear()
    joueur.afficher()
    [mur.afficher() for mur in murs]
    
def update(dt):
    if actions['avancer']: joueur.avancer(20)
    if actions['reculer']: joueur.avancer(-20)
    if actions['tourner_gauche']: joueur.tourner(0.2)
    if actions['tourner_droite']: joueur.tourner(-0.2)
    if joueur.deplacement:
        joueur.tracer()
        joueur.deplacement = False

# boucle principale (30 Hz)
pg.clock.schedule_interval(update, 1/30.0)

# lancement du jeu
pg.app.run()