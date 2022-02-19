from ase.build import nanotube
from batoms import Batoms
from batoms.bdraw import draw_plane
from batoms.butils import removeAll, set_world
import numpy as np
removeAll()
cnt = nanotube(12, 0, length=8)
cnt.new_array('species', np.array(cnt.get_chemical_symbols(), dtype = 'U10'))
l = max(cnt.positions[:, 2]) - min(cnt.positions[:, 2])
colors = {}
n = len(cnt)
for i in range(n):
    ind = int((cnt[i].z/1))
    kind = cnt[i].symbol + '_{0}'.format(ind)
    cnt.arrays['species'][i] = kind
    c = cnt[i].z/l
    colors[kind] = [c, 1-c, 0]

cnt = Batoms(label = 'cnt', atoms = cnt)
for kind, color in colors.items():
    cnt[kind].color = color

cnt.model_style = 1
# # draw polyhedral model manually and not show the edge
set_world(color = [0.2, 0.2, 0.2, 1.0])
cnt.render.lights['Default'].energy = 50
cnt.render.lights['Default'].direction = [0.4, 0.5, 1]
cnt.render.engine = 'cycles'
cnt.get_image([1, -0.3, 0.3], canvas = [12, 12, 12], 
        output = 'gallery_cnt.png')

# for graphene, use wave modifer