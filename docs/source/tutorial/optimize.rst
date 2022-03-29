.. _optimize:

===================
Optimization
===================

The function :meth:`~Batoms.optimize` in :mod:`Batoms <batoms>` object is used to optimize the geometry of a molecule.

The optimization method is based on pybel using `localopt <https://openbabel.org/docs/dev/UseTheLibrary/Python_Pybel.html>`_:


Here is a example:

>>> from ase.build import molecule
>>> from batoms import Batoms
>>> c2h6so = molecule("C2H6SO")
>>> c2h6so = Batoms(label = "c2h6so", from_ase = c2h6so)
>>> c2h6so.optimize(forcefield='mmff94', steps=500)


.. .. image:: /images/optmize_c2h6so.png
..    :width: 8cm

