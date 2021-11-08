.. _devel:

============
Development
============

In Blender, when the undo/redo operation system (ctrl+z / ctrl+shift+z) is performed, all objects in the scene are fully recreated. Pointers to the old objects will fail. Therefore, please store list of object names instead of object itself, and then use them by ``bpy.data.objects[name]``. This is same for collection and others.


IDE
=======

``VS Code`` with ``Blender Development`` extenstion is highly recommended to used . Please read : https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development

Known bugs
===================

- ``batoms.Rotate`` crash if not in 'VIEW_3D'
- boundary search when some atoms are outside the unit cell.



Development topics
=====================

Default custom setting
--------------------

- Add a custom configuration file (``~/.batomsrc``), which will be load by batoms to modify the default setting, such as atom color and bond style.
  

bond
-----

- add() function, set different options. (1) use default (2) use cutoff to build (3) copy from other.


Polyhedra
----------------
  
- Information about coordination polyhedra: volumes
  
Atom
-----------

- Add vectors (arrows) to atoms to represent magnetic moments and so on
- boundary cut the original atoms in batoms, how to handle?
- Add particle system
- Ellipsoid

Cell
-------------

- In Gui, use transform matrix instead of supercell
- draw reciprocal cell


Light
----------

- For perspective view, ``SUN`` light bound to camera is not good.

Material
--------------

- add support for mix materials nodes



Volumetric
-------------

- Make 2D slices of volumetric data more beautiful

Algorithm
------------------


- Find high order bond for aromatics. (eg. using CSD Python API, https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/substructure_searching.html#)
- Faster bond-search algorithm.
- More robust cavity search algorithm.

Animations
-------------

- Vibrations

Occupancy
---------------

- How to handle fractional occupancy site? (eg. in ``Batom``, element is a list)


Interface
------------------

- add support for MaterialProject
- add support for NOMAD 
- add support for open-babel. (PyBel)

GUI
------------------

- Add view from unit cell axis (a, b, c)
- Add ``batoms`` commands in the menu (eg. right click menu)

Force field
-----------------

- Can we enforce the force filed while editing (grab rotation)!!!? Could be modal.
- Add force field to relax the structure (by ASE)


Plugin (maybe)
----------------

- Create a new github repository to shafe Plugin


Language
--------------------

- docs translated into other languages