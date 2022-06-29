.. module:: batoms.plugins.cavity

===============================
The Cavity object
===============================

The :class:`Cavity` object is used to search and draw cavity for :class:`Batoms`. It has a ``settings`` attribute (:class:`CavitySettings` object), which stores and set all parameters related to cavity data. Possible keywords for settings are: ``min``, ``max``, ``scale``, ``material_style`` and ``color``. 


Here we show an example of drawing cavities for MOF-5. First, we read a MOF-5 structure.

>>> from ase.io import read
>>> from batoms import Batoms
>>> atoms = read("mof-5.cif")
>>> mof = Batoms(label = "mof", from_ase = atoms)
>>> # make a supercell in a direction.
>>> mof *= [2, 1, 1]
>>> # change width of cell
>>> mof.cell.width = 0.05

There is no default settings, as shown bellow:

>>> mof.cavity.settings
Name       min   max   scale                color  
------------------------------------------------------------


Auto-search cavity
---------------------
First, we call the `draw` function to auto-search and draw the cavities.

>>> mof.cavity.draw()

.. image:: /images/python_cavity_mof_5_0.png
   :width: 10cm

After that, two different cavities (names are `"0"` and `"1"`) with different radii are found.

>>> mof.cavity.settings
Name       min   max   scale                color  
0      7.000   8.000   1.000   [1.00  0.00  0.00  1.00] 
1      5.000   6.000   1.000   [0.00  1.00  0.00  1.00] 
------------------------------------------------------------

The `min` and `max` parameters are the range of the radius of that cavity. The `scale` parameter is used to change the size of the sphere used to represent the cavity.

One change the settings. 

>>> # change the size of `0` by half of the original.
>>> mof.cavity.settings['0'].scale = 0.5
>>> # change the color of `1`.
>>> mof.cavity.settings['1'].color = [1, 1, 0, 1]
>>> mof.cavity.draw()


.. image:: /images/python_cavity_mof_5_1.png
   :width: 10cm


GUI
---------
One can also set the cavity using GUI panel. Please read :ref:`gui_cavity` page for more setup.


