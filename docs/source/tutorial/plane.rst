
================================
Lattice Plane and Crystal shape
================================

The :mod:`LatticePlaneSetting <batoms.plugins.lattice_plane.setting>` object controls various settings related with lattice plane data.

Lattice Plane
----------------

Here we show a example of inserting a lattice plane in the unit cell.

>>> from batoms.build import bulk
>>> au = bulk("au", "Au", cubic = True)
>>> au.lattice_plane.settings[(1, 1, 0)] = {"distance": au.cell[0, 0]/np.sqrt(2)}
>>> au.draw()

.. image:: /images/planesetting_au_plane.png
   :width: 8cm



One change a planesetting by. 

>>> au.lattice_plane.settings[(1, 1, 1)].distance = 3.0
>>> au.draw()



Crystal shape
------------------

To build up crystal morphologies, the parameter ``crystal`` should be set to ``True``. To change setting for a plane by:

>>> au.crystal_shape.setting[(1, 1, 1)] = {"distance": 8, 
>>>                               "crystal": True,
>>>                               "symmetry": True,
>>>                               "color": [0, 0.2, 0.8, 1]}
>>> au.crystal_shape.setting[(0, 0, 1)] = {"distance": 10, 
>>>                               "crystal": True,
>>>                               "symmetry": True,
>>>                               "color": [0.6, 0.2, 0, 1]}
>>> au.crystal_shape.draw()

When parameter ``symmetry`` is ``True``, all the symmetrically equivalent indices are automatically generated.


.. image:: /images/gallery_planesetting_crystal.png
   :width: 10cm
