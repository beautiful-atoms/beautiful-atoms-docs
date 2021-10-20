from ase.build import bulk
from batoms import Batoms
from batoms.bdraw import draw_plane
from batoms.butils import removeAll
import numpy as np
removeAll()
# make a dislocation
fe = bulk('Fe', cubic = True)
del fe[0]
fe = fe*[7, 6, 6]
fe = Batoms(label = 'Fe', atoms = fe)
fe.bondsetting['Fe-Fe'] = [0, 3.5, 1, False]
fe.bondsetting['Fe-Fe'].color1 = [0.2, 0.8, 0.4, 1.0]
#-------------------------------------
# click "Tab" key to "Eidt" mode:
# select one column of Fe atoms and delete (click "X")
# ajust the positions of Fe atoms.
# ajust the bondsetting
# ajust the color, materials of Fe atoms
#----------------------------------------------
# set rendering
fe.model_type = 1
fe.render.set_world(color = [0.2, 0.2, 0.2, 1.0])
draw_plane(location = [0, 0, min(fe.positions[:, 2]) - fe['Fe'].size[0]], 
            size = 200, color = (0.9, 0.9, 0.9, 1))
fe.render.camera_type = 'PERSP'
fe.render.camera_target = fe.get_center_of_mass()
l = fe.cell[0, 0]
fe.render.camera_loc = [l/2, 3*l, l/2]
fe.render.light_type = 'POINT'
fe.render.lock_light_to_camera = False
fe.render.light_energy = 50000
fe.render.light_loc = [l/2, l+5, l/2 + 1]
fe.render.run(canvas = np.array([[-l, -l, -l], [l, l, l]]), 
        engine = 'eevee', output = 'gallery_fe.png')