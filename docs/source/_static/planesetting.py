from batoms.build import bulk
from batoms.butils import removeAll
from batoms import Batoms
import numpy as np
removeAll()
au = bulk('au', 'Au', cubic = True)
au.planesetting[(1, 1, 0)] = {'distance': au.cell[0, 0]/np.sqrt(2)}
au.draw_cell()
au.draw_lattice_plane()
au.render.run(direction = [0.2, -1, 0.4], engine = 'eevee', output = 'figs/planesetting_au_plane.png')

au.planesetting[(1, 1, 0)].crystal = True
au.planesetting[(1, 1, 0)].symmetry = True
au.planesetting[(1, 1, 0)].color = [0, 0, 1, 1]
au.draw_crystal_shape()
au.render.run(direction = [0.2, -1, 0.4], engine = 'cycles', output = 'figs/planesetting_au_crystal.png')
