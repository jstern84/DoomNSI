# Séance 4 du 13/02/2024
# création du module joueur

# module pyglet principal (qu'on nenomme en pg pour plus de simplicité)
import pyglet as pg
# import des fonctions trigo du module math
from math import cos, sin

class Joueur: # la classe Joueur
    def __init__(self, x, y, a):
        # position et angle
        self.x = x
        self.y = y
        self.a = a
        self.deplacement = True
        # "batch" du joueur
        self.batch = pg.graphics.Batch()
        self.dessin = {}
    def avancer(self, pas):
        self.x += pas*cos(self.a)
        self.y += pas*sin(self.a)
        self.deplacement = True
    def tourner(self, angle):
        self.a += angle
        self.deplacement = True
    def tracer(self):
        # le joueur comme un cercle
        self.dessin['corps'] = pg.shapes.Circle(self.x, self.y, 10, color =(50, 225, 30), batch = self.batch)
        # segment "vecteur vitesse" qui pointe vers la direction de visée
        self.dessin['visée'] = pg.shapes.Line(self.x, self.y, self.x + 20*cos(self.a), self.y + 20*sin(self.a), width=5, batch = self.batch)
    def afficher(self):
        self.batch.draw()