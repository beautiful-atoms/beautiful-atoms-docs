
Development topics
=====================

Default custom setting
------------------------

- Add a custom configuration file (``~/.batomsrc``), which will be load by batoms to modify the default setting, such as atom color and bond style.
  

Selection
-----------

- use vertex group
- Based on symbols or topology or geometry. 

Protein
-------------

- Display secondary structure

Bond
-----

- add() function, set different options. (1) use default (2) use cutoff to build (3) copy from other.
- test add bond pair separately.
- use skin to update bond list for animation.

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

- draw reciprocal cell


Light
----------

- For perspective view, ``SUN`` light bound to camera is not good.

Material
--------------

- add materials nodes
- add support for mix materials nodes

Volumetric
-------------

- Make 2D slices of volumetric data more beautiful

Molecular surface
---------------------

- solvent accessible surface with respect to each atom


Algorithm
------------------

- Find high order bond for aromatics. (eg. using CSD Python API, https://downloads.ccdc.cam.ac.uk/documentation/API/descriptive_docs/substructure_searching.html#)
- Faster bond-search algorithm.
- More robust cavity search algorithm.

Animations
-------------

- update the shape keys for batoms.replace and so on
- Vibrations

Interface
------------------

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