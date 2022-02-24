from ase.build import molecule
from batoms import Batoms
from batoms.bdraw import draw_plane
from batoms.butils import removeAll, set_world
import numpy as np
removeAll()
c60 = molecule('C60')
pos = c60.get_center_of_mass()
c60 = Batoms(label = 'c60', from_ase = c60)
c60['C'].color = [0.1, 0.1, 0.1, 1.0]
c60.bonds.setting[('C', 'C')].style = '0'
c60.bonds.setting[('C', 'C')].color1 = [0.2, 0.8, 0.1, 1.0]
# we add a ghost site (species ``X``) at the center of a cavity
x = Batoms('x', {'X':[pos]})
c60 = c60 + x
# add bond `X-C`, and set polyhedra to True
c60.bonds.setting[('X', 'C')] = {'min': 0, 'max': 10, 'search': 2, 'polyhedra': True}
c60.polyhedras.setting['X'].color = [0.4, 0.4, 0, 1.0]
c60.polyhedras.setting['X'].show_edge = False
c60.model_style = 1
# # draw polyhedral model manually and not show the edge
c60.draw_polyhedras()
set_world(color = [0.2, 0.2, 0.2, 1.0])
draw_plane(location = [0, 0, min(c60.positions[:, 2]) - c60['C'].size[0]], 
            size = 200, color = (0.9, 0.9, 0.9, 1))
c60.render.viewport = [1, -0.3, 0.3]
c60.render.engine = 'cycles'
c60.render.lights['Default'].energy = 50
c60.render.lights['Default'].direction = [0.4, 0.5, 1]
c60.get_image(canvas = [12, 12, 12], 
                output = 'gallery_c60.png')