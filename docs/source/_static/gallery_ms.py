from ase.io import read
from batoms import Batoms
from batoms.draw import draw_plane
from batoms.utils.butils import removeAll, set_world
removeAll()
kras = read('datas/kras.pdb')
kras.center(1.0)
kras = Batoms('kras', from_ase = kras)
kras.draw_SAS()
set_world(color = [0.2, 0.2, 0.2, 1.0])
draw_plane(location = [0, 0, min(kras.positions[:, 2]) - 3], 
            size = 5000, color = (0.9, 0.9, 0.9, 1))
# kras.render.viewport = [1, -0.3, 0.3]
kras.render.engine = 'cycles'
kras.render.lights['Default'].energy = 50
kras.render.lights['Default'].direction = [0.4, 0.5, 1]
kras.get_image([1, -0.3, 0.3], padding = [12, 12, 12], 
                output = 'gallery_sas.png')
            
kras.draw_SES()
kras.get_image([1, -0.3, 0.3], padding = [12, 12, 12], 
                output = 'gallery_ses.png')