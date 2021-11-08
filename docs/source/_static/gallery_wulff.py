from ase.cluster import wulff_construction
from batoms import Batoms
from batoms.bdraw import draw_plane
from batoms.butils import removeAll
removeAll()
surfaces = [(1, 1, 1), (1, 0, 0)]
energies = [1.28, 1.69]
atoms = wulff_construction('Au', surfaces, energies, 500, 'fcc')
del atoms[atoms.positions[:, 2] < 0]
nano = Batoms('wulff', atoms = atoms)
nano.show_unit_cell = False
draw_plane(size = 1000, location = (0, 0, min(nano.positions[:, 2]) - nano['Au'].size[0]),  
        color = [0.9, 0.9, 0.9, 1.0])
nano.render.lights['Default'].energy = 40
nano.render.lights['Default'].direction = [0.7, 0.2, 1]
nano.render.run([1, -0.3, 0.4], engine = 'cycles', 
         padding = 10, output = 'figs/gallery_wulff.png')