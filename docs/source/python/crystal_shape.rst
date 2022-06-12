.. module:: batoms.crystal_shape.crystal_shape_setting

===============================
The CrystalShapeSetting object
===============================

The :class:`CrystalShapeSetting` object is used to store and set all parameters related with lattice plane data. It should always bind with a :class:`Batoms` object. Possible keywords are: ``indices``, ``distance``, ``crystal``, ``symmetry`` and ``color``. 


Here we show a example of insert a lattice plane in the unit cell.

>>> from batoms.build import bulk
>>> au = bulk('au', 'Au', cubic = True)
>>> au.crystal_shape.setting[(1, 1, 1)] = {'indices': (1, 1, 1), 'distance': 2.0}
>>> au.draw_crystal_shape()

One change the setting by. 

>>> au.crystal_shape.setting[(1, 1, 1)].distance = 3.0
>>> au.draw_crystal_shape()

.. image:: /images/gallery_planesetting_crystal.png
   :width: 5cm


