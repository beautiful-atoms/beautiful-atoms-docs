.. module:: batoms.planesetting

=============================
The Planesetting object
=============================

The :class:`Planesetting` object is used to store and set all parameters related with lattice plane data. It should always bind with a :class:`Batoms` object. Possible keywords are: ``indices``, ``distance``, ``crystal``, ``symmetry`` and ``color``. 


Here we show a example of insert a lattice plane in the unit cell.

>>> from batoms.build import bulk
>>> au = bulk('au', 'Au', cubic = True)
>>> au.planesetting[(1, 1, 1)] = {'indices': (1, 1, 1), 'distance': 2.0}
>>> au.draw_lattice_plane()

One change a planesetting by. 

>>> au.planesetting[(1, 1, 1)].distance = 3.0
>>> au.draw_lattice_plane()

.. image:: ../_static/figs/volume_h2o.png
   :width: 5cm


List of all Methods
====================

.. autoclass:: Planesetting
   :members: