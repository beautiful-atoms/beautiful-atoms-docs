from ase.build import fcc111
from batoms import Batoms
from batoms.utils.butils import removeAll
removeAll()
atoms = fcc111('Au', size=(5, 5, 4), vacuum=0)
au111 = Batoms(label='au111', from_ase=atoms)
au111.cell[2, 2] += 10
au111.cell.draw()
au111.replace([87], "X")
au111[87].scale = 1.2
au111['X'].color = [0.8, 0.0, 0.8, 0.2]
au111.render.viewport = [1, -0.4, 0.4]
au111.render.engine = 'cycles'
au111.render.lights['Default'].energy = 25
au111.get_image(output='au111-vacancy-cycles.png')
