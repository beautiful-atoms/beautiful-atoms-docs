from ase.build import bulk
from batoms import Batoms
au = bulk('Au', 'fcc', cubic=True)
au = Batoms(label = 'au', from_ase = au)
au.cell.draw()
au.render.engine = 'workbench'
for light in ["Default", "basic.sl", "outdoor.sl", "paint.sl", "rim.sl", "studio.sl",]:
    au.get_image(viewport = [1, -0.3, 0.1],  studiolight = light, output = 'studiolight_%s.png'%light)
