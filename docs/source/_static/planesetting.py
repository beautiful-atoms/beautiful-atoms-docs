from batoms.build import bulk
from batoms.utils.butils import removeAll
from batoms import Batoms
import numpy as np
removeAll()
au = bulk('au', 'Au', cubic = True)
au.lattice_plane.setting[(1, 1, 0)] = {'distance': au.cell[0, 0]/np.sqrt(2)}
au.draw_cell()
au.draw()
au.get_image(viewport = [0.2, -1, 0.4], output = 'figs/planesetting_au_plane.png')

au.lattice_plane.setting[(1, 1, 0)].crystal = True
au.lattice_plane.setting[(1, 1, 0)].symmetry = True
au.lattice_plane.setting[(1, 1, 0)].color = [0, 0, 1, 1]
au.draw_crystal_shape()
au.render.engine = 'cycles'
au.get_image(viewport = [0.2, -1, 0.4], output = 'figs/planesetting_au_crystal.png')
