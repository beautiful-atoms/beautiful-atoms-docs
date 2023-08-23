
================================
Hide atoms
================================

One can control the visibility of atoms by setting the show attribute of the atom to True or False.

Here we show an example of hiding one of the atoms in a molecule. 

>>> from ase.build import molecule
>>> from batoms import Batoms
>>> mol = Batoms("mol", from_ase = molecule("CH3CH2OH"))
>>> # hide the first atom
>>> mol[0].show=False
>>> mol.get_image(padding = 3, output = "hide_mol.png")



One can hide all H atoms:

>>> import numpy as np
>>> mol[np.array(mol.elements) == "H"].show = False



One can hide all atoms with z < 0:

>>> import numpy as np
>>> mol[mol.positions[:, 2]<0].show = False


GUI
=========
It is also possible to hide atoms directly from the GUI panel.