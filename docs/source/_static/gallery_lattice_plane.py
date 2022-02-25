from batoms.build import bulk
from batoms.utils.butils import removeAll
from batoms.draw import draw_plane
from batoms import Batoms
import numpy as np
removeAll()
au = bulk('au', 'Au', cubic = True)
au.planesetting[(1, 1, 0)] = {'distance': au.cell[0, 0]/np.sqrt(2)}
au.draw_cell()
au.draw_lattice_plane()
au.render.set_world(color = [0.2, 0.2, 0.2, 1.0])
draw_plane(location = [0, 0, -au['Au'].size[0]], size = 200, color = (0.9, 0.9, 0.9, 1))
au.render.viewport = [1, -0.3, 0.3]
au.render.engine = 'cycles'
au.render.lights['Default'].type = 'POINT'
au.render.lights['Default'].lock_light_to_camera = False
au.render.lights['Default'].energy = 50000
au.render.lights['Default'].location = [10, 4, 10]
au.get_image(output = 'figs/gallery_planesetting_plane.png')
