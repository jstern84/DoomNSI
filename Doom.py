# pip install --force-reinstall -v "pyglet==1.5.28"

# module pyglet principal (qu'on nenomme en pg pour plus de simplicité)
import pyglet as pg
# import des fonctions trigo du module math
from math import cos, sin, pi
# modules du jeu
import config as C
import joueur as J
import structure as S

# création de la fenêtre pour le plan 2D et le rendu 3D
# résolution : 320x200 pour le Doom de l'époque
window3d = pg.window.Window(800, 600, "Plan 3D", vsync=True)
window2d = pg.window.Window(800, 600, "Plan 2D", vsync=True)

# Création d'une instance de Joueur
joueur = J.Joueur(600,400,0)

# Création d'instances de Mur
murs = [S.Mur(400,100,800,100), S.Mur(800,100,1000,300), S.Mur(1000,300,1000,500), S.Mur(800,700,1000,500),
        S.Mur(400,700,800,700), S.Mur(200,500,400,700), S.Mur(200,300,200,500), S.Mur(200,300,400,100)]

[mur.debug() for mur in murs]
[mur.tracer() for mur in murs]

# création du dico contenant les actions actives (True) ou inactives (False)
actions = { 'avancer': False, 'reculer': False,
            'tourner_gauche': False, 'tourner_droite': False, 'gauche': False, 'droite': False}

# détection d'un touche pressée au clavier
@window2d.event
def on_key_press(symbol, modifiers):
    # Touche Q : on quitte le jeu  
    if symbol in C.INTERFACE().T_QUITTER: pg.app.exit()
    # touches de déplacement
    if symbol in C.JOUEUR().T_AVANCER: actions['avancer'] = True
    if symbol in C.JOUEUR().T_RECULER: actions['reculer'] = True
    if symbol in C.JOUEUR().T_STRAFE_G: actions['gauche'] = True
    if symbol in C.JOUEUR().T_STRAFE_D: actions['droite'] = True
    # touches pour tourner
    if symbol in C.JOUEUR().T_TOURNER_G: actions['tourner_gauche'] = True
    if symbol in C.JOUEUR().T_TOURNER_D: actions['tourner_droite'] = True
    
          
# détection d'un touche relâchée au clavier
@window2d.event
def on_key_release(symbol, modifiers):
    # touches de déplacement
    if symbol in C.JOUEUR().T_AVANCER: actions['avancer'] = False
    if symbol in C.JOUEUR().T_RECULER: actions['reculer'] = False
    if symbol in C.JOUEUR().T_STRAFE_G: actions['gauche'] = False
    if symbol in C.JOUEUR().T_STRAFE_D: actions['droite'] = False
    # touches pour tourner
    if symbol in C.JOUEUR().T_TOURNER_G: actions['tourner_gauche'] = False
    if symbol in C.JOUEUR().T_TOURNER_D: actions['tourner_droite'] = False

# évènement principal : rendu graphique
@window2d.event
def on_draw():
    window2d.clear()
    joueur.afficher()
    [mur.afficher() for mur in murs]
    
@window3d.event
def on_draw():
    window3d.clear()
    
def update(dt):
    if actions['avancer']: joueur.avancer(joueur.PAS, joueur.a, murs)
    if actions['reculer']: joueur.avancer(-joueur.PAS, joueur.a, murs)
    if actions['gauche']: joueur.avancer(joueur.PAS, joueur.a+pi/2, murs)
    if actions['droite']: joueur.avancer(-joueur.PAS, joueur.a+pi/2, murs)
    if actions['tourner_gauche']: joueur.tourner(joueur.ROT)
    if actions['tourner_droite']: joueur.tourner(-joueur.ROT)
    if joueur.deplacement:
        joueur.tracer()
        joueur.deplacement = False

# boucle principale (30 Hz)
pg.clock.schedule_interval(update, 1/30.0)

# version de pyglet
print("Version de Pyglet : ",pg.version)
# lancement du jeu
pg.app.run()