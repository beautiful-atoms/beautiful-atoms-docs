Pymatgen
================

If you are not familiar with building atomic structure using Pymatgen, please read the following tutorials:

* Building molecule, crystal, surface: https://pymatgen.org/usage.html#structures-and-molecules


Keyword ``structure`` in :class:`Batoms` object is used to load a Pymatgen_ structure.

Molecule:

>>> from batoms import Batoms
>>> from pymatgen.core.structure import Molecule
>>> co = Molecule(["C","O"], [[0.0, 0.0, 0.0], [0.0, 0.0, 1.2]])
>>> co = Batoms(label = 'co', structure=co)

.. image:: ../../_static/figs/ase-co.png
   :width: 3cm

Crystal:

>>> from batoms import Batoms
>>> from pymatgen.core import Lattice, Structure
>>> fe = Structure(Lattice.cubic(2.8), ["Fe", "Fe"], [[0, 0, 0], [0.5, 0.5, 0.5]])
>>> fe = Batoms(label = 'fe', structure=fe)

.. image:: ../../_static/figs/ase-fe.png
   :width: 3cm
