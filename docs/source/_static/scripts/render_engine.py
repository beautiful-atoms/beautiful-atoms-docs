from ase.build import bulk
from batoms import Batoms
au = bulk('Au', 'fcc', cubic=True)
au = Batoms(label = 'au', from_ase = au)
au.cell.draw()
for engine in ['workbench', 'eevee', 'cycles']:
    au.get_image(viewport = [1, -0.3, 0.1], engine = engine, output = 'render_%s.png'%engine)
