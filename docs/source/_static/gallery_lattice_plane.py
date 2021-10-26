from batoms.build import bulk
from batoms.butils import removeAll
from batoms.bdraw import draw_plane
from batoms import Batoms
import numpy as np
removeAll()
au = bulk('au', 'Au', cubic = True)
au.planesetting[(1, 1, 0)] = {'distance': au.cell[0, 0]/np.sqrt(2)}
au.draw_cell()
au.draw_lattice_plane()
au.render.set_world(color = [0.2, 0.2, 0.2, 1.0])
draw_plane(location = [0, 0, -au['Au'].size[0]], size = 200, color = (0.9, 0.9, 0.9, 1))
au.render.light_type = 'POINT'
au.render.lock_light_to_camera = False
au.render.light_energy = 50000
au.render.light_loc = [10, 4, 10]
au.render.run([1, -0.3, 0.3], engine = 'cycles', output = 'figs/gallery_planesetting_plane.png')
