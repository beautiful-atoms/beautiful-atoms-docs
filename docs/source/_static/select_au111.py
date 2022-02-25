from batoms.batoms import Batoms
from ase.build import molecule, fcc111
import numpy as np
au111 = fcc111("Au", (4, 4, 4), vacuum=0)
au111 = Batoms("au111", from_ase=au111)
mol = Batoms("mol", from_ase=molecule("CH3CH2OH"))
mol.translate([5, 5, 10])
au111 = au111 + mol
au111.cell[2, 2] += 10
sel1 = au111.selects.add("mol", np.where(au111.arrays["species"] != "Au")[0])
au111.selects["mol"].model_style = 1
au111.get_image(output = 'figs/select_au111.png')