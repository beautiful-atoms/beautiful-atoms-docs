.. module:: batoms.lattice_plane.lattice_plane_setting

================================
The LatticePlanesetting object
================================

The :class:`LatticePlaneSetting` object is used to store and set all parameters related with lattice plane data. It should always bind with a :class:`Batoms` object. Possible keywords are: ``indices``, ``distance``, ``crystal``, ``symmetry`` and ``color``. 


Here we show a example of insert a lattice plane in the unit cell.

>>> from batoms.build import bulk
>>> au = bulk('au', 'Au', cubic = True)
>>> au.lattice_plane.setting[(1, 1, 1)] = {'indices': (1, 1, 1), 'distance': 2.0}
>>> au.draw_lattice_plane()

One change a setting by. 

>>> au.lattice_plane.setting[(1, 1, 1)].distance = 3.0
>>> au.draw_lattice_plane()

.. image:: /images/volume_h2o.png
   :width: 5cm


List of all Methods
====================

.. autoclass:: LatticePlaneSetting
   :members: