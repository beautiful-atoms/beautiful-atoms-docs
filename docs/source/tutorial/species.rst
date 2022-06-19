===================
Species
===================

Why do we use species instead of elements? Because some atoms are special:

* Different colors for one element.
* Different properties for one element, such as: spin up and down.
* ghost atoms: vacancy, highlight sphere, cavity
* atoms with different bondsetting


Color
----------

For example, we want to change the color of one hydrogen atom in CH4 molecule.

>>> from ase.build import molecule
>>> from batoms import Batoms
>>> import numpy as np
>>> ch4 = Batoms("ch4", from_ase = molecule('CH4'))

Here, we replace the first H atom with a new species ("H_1").

>>> ch4.replace([1], "H_1")
>>> ch4["H_1"].color = (1.0, 1.0, 0.0, 1.0)

.. image:: /images/species_ch4.png
   :width: 4cm

Another example:

>>> from ase.build import bulk
>>> from batoms import Batoms
>>> import numpy as np
>>> au = Batoms(label = "au", from_ase = bulk('Au', cubic = True))

>>> for i in range(len(au)):
>>>     au.replace([i], "Au_%i"%i)

>>> au["Au_0"].color = [0.8, 0.8, 0.9, 1.0]
>>> au["Au_1"].color = [0.8, 0.5, 0.8, 1.0]
>>> au["Au_2"].color = [0, 0.7, 0.4, 1.0]
>>> au["Au_2"].color = [0.5, 0.1, 0.4, 1.0]

.. image:: /images/species_au4.png
   :width: 6cm

.. note::

   Be careful, if the name of the new species does not start with "Au\_" (Au is the element to be replaced). Then, use this format:   
   
   >>> au.replace([0, 1], ["a100", {"elements":{"Au":{"occupancy":1.0}}}])

   The name should not be longer than four characters.

If you only need to change the scale of individule atoms. You can use:

>>> Au[0].scale = 2

.. image:: /images/species_au4_2.png
   :width: 6cm



Polyhedra with different species
------------------------------------
This is an example to show different polyhedras for the same element, but different species.
First, we read a TiO\ :sub:`2`\  structure from file.

>>> from batoms.bio import read
>>> tio2 = read("../tests/datas/tio2.cif")


.. image:: /images/tutorial-species-polyhedra-0.png
   :width: 6cm


There are two ``Ti`` atoms in the unit cell. Swithing to ``Edit`` mode (shortcut key:``Tab``), we find the indices are 0 and 1 for these two ``Ti`` atoms. 


Swithing back to ``Object`` mode (shortcut key:``Tab``). We set the first one to a new species ``Ti_1``.

>>> tio2.replace([0], 'Ti_1')

For the new added ``Ti_1`` species, there is not default setting for the bonds. As shown by:

>>> tio2.bonds.setting
Bondpair    min     max   Search_bond    Polyhedra style
Ti-O        0.000   2.760      1            True        1    
O-O         0.000   1.820      1            False       1    
------------------------------------------------------------

Therefore, when we set the ``model_style`` to ``polyhedra``, there is no bond and polyhedra for this species.

>>> tio2.model_style = 2

.. image:: /images/tutorial-species-polyhedra-1.png
   :width: 6cm


One can add a bond between ``Ti_1`` and ``O`` by:

>>> tio2.bonds.setting.add(('Ti_1', 'O'))
>>> tio2.bonds.setting
Bondpair    min     max   Search_bond    Polyhedra style
Ti-O        0.000   2.760      1            True        1    
O-O         0.000   1.820      1            False       1    
Ti_1-O      0.000   2.760      1            False       1    
------------------------------------------------------------

In the Bondpair ``Ti_1-O``, the ``Polyhedra`` is ``False``, we can set it to ``True`` by:

>>> tio2.bonds.setting[('Ti_1', 'O')].polyhedra = True
>>> tio2.bonds.setting
Bondpair    min     max   Search_bond    Polyhedra style
Ti-O        0.000   2.760      1            True        1    
O-O         0.000   1.820      1            False       1    
Ti_1-O      0.000   2.760      1            True        1    
------------------------------------------------------------

Also add ``Ti_1`` to polyhedras. To make the polyhedra different from another ``Ti`` species, we change its color.

>>> tio2.polyhedras.setting.add('Ti_1')
>>> tio2.polyhedras.setting['Ti_1'].color = (0, 1, 1, 1)

Here we see that there are two different Ti species for polyhedras:

>>> tio2.polyhedras.setting
Center                color         width 
Ti           [0.75  0.76  0.78  1.00]   0.010 
Ti_1         [0.00  1.00  1.00  1.00]   0.010 
------------------------------------------------------------

.. image:: /images/tutorial-species-polyhedra-2.png
   :width: 6cm


If you want to add transparency for the polyhedra, please read :ref:`color` page for more setup.