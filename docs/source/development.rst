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

- boundary search when some atoms are outside the unit cell.



Development topics
=====================

Default custom setting
--------------------

- Add a custom configuration file (``~/.batomsrc``), which will be load by batoms to modify the default setting, such as atom color and bond style.
  

Bond
----------

- Draw high order bonds.


Polyhedra
----------------
  
- Information about coordination polyhedra: volumes
  
Atom
-----------

- Add vectors (arrows) to atoms to represent magnetic moments and so on
- boundary cut the original atoms in batoms, how to handle?
- Add particle system

Light
----------

- For perspective view, ``SUN`` light bound to camera is not good.



Algorithm
------------------

- Add 2D slices of volumetric data in their 3D image.
- Find high order bond for aromatics. (eg. using CSD Python API, https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/substructure_searching.html#)
- Faster bond-search algorithm.
- More robust cavity search algorithm.
  
Occupancy
---------------

- How to handle fractional occupancy site?


Interface
------------------

- add support for open-babel. (PyBel)

GUI
------------------

- Add ``batoms`` commands in the menu (eg. right click menu)
