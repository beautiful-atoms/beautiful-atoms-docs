.. module:: batoms.plugins.lattice_plane

================================
The LatticePlane object
================================

The :class:`LatticePlane` object is used draw molecular surface for :class:`Batoms`. It has a ``settings`` attribute (:class:`LatticePlaneSettings` object), which store and set all parameters related with lattice plane data. It should always bind with a :class:`Batoms` object. Possible keywords are: ``indices``, ``distance``, ``crystal``, ``symmetry`` and ``color``. 


Here we show a example of insert a lattice plane in the unit cell.

>>> from batoms.build import bulk
>>> au = bulk('au', 'Au', cubic = True)
>>> au.lattice_plane.settings[(1, 1, 1)] = {'indices': (1, 1, 1), 'distance': 2.0}
>>> au.draw_lattice_plane()

One change a setting by. 

>>> au.lattice_plane.settings[(1, 1, 1)].distance = 3.0
>>> au.draw_lattice_plane()

.. image:: /images/planesetting_au_plane.png
   :width: 5cm

