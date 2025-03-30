# Module d'outils divers
import pyglet as pg

# produit vectoriel (coordonnée z)
def calc_PV(u, v):
    return u[0]*v[1]-u[1]*v[0]

# produit scalaire
def calc_PS(u, v):
    return u[0]*v[0] + u[1]*v[1]

# vecteur entre 2 points
def calc_AB(A, B):
    return (B[0] - A[0], B[1] - A[1])

# batch avec ses références
class Dessin:
    def __init__(self):
        self.batch = pg.graphics.Batch()
        self.dessins = []
    def ajout(self, dessins):
        self.dessins.extend(dessins)
    def reset(self):
        self.dessins = []
    def dessiner(self):
        self.batch.draw()
