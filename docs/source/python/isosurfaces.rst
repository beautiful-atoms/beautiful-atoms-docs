.. module:: batoms.isosurface.isosurfacesetting

=============================
The Isosurface object
=============================

The :class:`Isosurface` object is used to draw isosurface for :class:`Batoms`. It has a ``settings`` attribute (:class:`IsosurfaceSettings` object), which stores and sets all parameters related to volumetric data. Possible keywords for ``settings`` are: ``level``, ``color``. 


Here, we show an example of drawing isosurfaces from a cube file.

>>> from ase.io.cube import read_cube_data
>>> from batoms import Batoms
>>> volumetric_data, atoms = read_cube_data("../tests/datas/h2o-homo.cube")
>>> h2o = Batoms('h2o', from_ase = atoms)
>>> # add volumetric data
>>> h2o.volumetric_data['homo'] = volumetric_data


There is no default setting, as shown by:

>>> h2o.isosurface.settings

One adds settings by. 

>>> h2o.isosurface.settings[1] = {'level': 0.002, 'color': [1, 1, 0, 0.5]}
>>> h2o.isosurface.settings[2] = {'level': -0.002, 'color': [0, 0, 0.8, 0.5]}
>>> h2o.isosurface.draw()

.. image:: /images/volume_h2o_isosurface.png
   :width: 5cm

One can select the volumetric data to be used if multiple volumetric data exist:

>>> h2o.volumetric_data['test'] = h2o.volumetric_data['homo'] + 1
>>> h2o.isosurface.settings["1"] = {'level': -0.015, 'color': [1, 0, 0, 0.5], 'volumetric_data': 'homo'}
>>> h2o.isosurface.settings["2"] = {'level': 1.015, 'color': [0, 0, 1, 0.5], 'volumetric_data': 'test'}


