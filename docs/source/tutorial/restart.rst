======================================
How to load Batoms from a collection?
======================================

When we restart from a ``.blend`` file. We can rebuild the :class:`Batoms` objects from collections. Keyword ``label`` in :class:`Batoms` object is used to load a :class:`Batoms` collection by the name.


Molecule:

>>> from batoms import Batoms
>>> co = Batoms(label = 'co')

.. image:: ../_static/figs/ase-co.png
   :width: 3cm

Crystal:

>>> from batoms import Batoms
>>> fe = Batoms(label = 'fe')

.. image:: ../_static/figs/ase-fe.png
   :width: 3cm

