from ase.build import fcc111
from batoms import Batoms
atoms = fcc111('Au', size = (4, 4, 5), vacuum=0)
au111 = Batoms(label = 'au111', from_ase = atoms)
au111.cell[2, 2] += 10
au111.draw_cell()
data = {(0, 0, 1):'top', (1, 0, 0):'front', (0, 1, 0):'right', (1, -0.3, 0.1):'any'}
for viewport, name in data.items():
    au111.get_image(viewport = viewport, output = 'render_direction_%s.png'%name)
