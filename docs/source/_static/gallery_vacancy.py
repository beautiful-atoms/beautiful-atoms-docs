from ase.build import fcc111
from batoms import Batoms
atoms = fcc111('Au', size = (5, 5, 4), vacuum=0)
au111 = Batoms(label = 'au111', atoms = atoms)
au111.cell[2, 2] += 10
au111.draw_cell()
au111.replace('Au', 'X', [87])
au111['X'].scale = 6
au111['X'].color = [0.8, 0.0, 0.8, 0.2]
au111.render.light_energy = 25
au111.render.run([1, -0.4, 0.4], engine = 'cycles', num_samples = 64, output = 'au111-vacancy-cycles.png')