.. module:: batoms.plugins.crystal_shape

===============================
The CrystalShape object
===============================

The :class:`CrystalShape` object is used to draw molecular surface for :class:`Batoms`. It has a ``settings`` attribute (:class:`CrystalShapeSettings` object), which stores and sets all parameters related to lattice plane data. Possible keywords are: ``indices``, ``distance``, ``crystal``, ``symmetry`` and ``color``. 


Here we show an example of drawing a crystal shape.

>>> from batoms.build import bulk
>>> au = bulk('au', 'Au', cubic = True)
>>> au.crystal_shape.settings[(1, 1, 1)] = {'indices': (1, 1, 1), 'distance': 2.0}
>>> au.crystal_shape.draw()

One change the setting by. 

>>> au.crystal_shape.settings[(1, 1, 1)].distance = 3.0
>>> au.crystal_shape.draw()

.. image:: /images/gallery_planesetting_crystal.png
   :width: 5cm


