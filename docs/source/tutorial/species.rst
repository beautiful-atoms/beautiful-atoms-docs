===================
Species
===================

Why we use species instead of element? Because some atoms are special:

* Different color for element.
* Different properties for element, sunch as: spin up and down.
* ghost atoms: vacancy, highlight sphere, cavity
* atoms with different bondsetting

The parameter ``species`` in :class:`Batom` object is used to specify the symobl of species. 

>>> from batoms import Batom
>>> h1 = Batom(label = 'h2o', species = 'H_1', element = 'H', positions = [[0, 0, 0]])
>>> h2 = Batom(label = 'h2o', species = 'H_2', element = 'H', positions = [[2, 0, 0]])
>>> h1.scale = 1.0
>>> h2.scale = 2.0

Here we define different species in ASE atoms. We store the ``species`` infomation in ``atoms.arrays['species']`` for ASE atoms. Then set color for different platinum species:

>>> from ase.build import fcc111
>>> from batoms import Batoms
>>> import numpy as np
>>> atoms = fcc111('Pt', (7, 7, 3), vacuum=3.0)
>>> atoms.new_array('species', np.array(atoms.get_chemical_symbols(), dtype = 'U10'))
>>> for i in range(len(atoms)):
>>>     ind = int((atoms[i].x/5))
>>>     kind = atoms[i].symbol + '_{0}'.format(ind)
>>>     atoms.arrays['species'][i] = kind

>>> pt = Batoms(label = 'pt111', from_ase = atoms)
>>> pt['Pt_0'].color = [0.8, 0.8, 0.9]
>>> pt['Pt_1'].color = [0.8, 0.5, 0.8]
>>> pt['Pt_2'].color = [0, 0.7, 0.4]

.. image:: ../_static/figs/pt111-species.png
   :width: 8cm

