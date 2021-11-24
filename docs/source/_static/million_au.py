from ase.build import bulk
from batoms import Batoms
au = bulk('Au', cubic = True)
au = Batoms(label = 'au', atoms = au, segments = [6, 6])
au.repeat([50, 50, 100])
au.get_image(viewport = [1, 0, 0])
