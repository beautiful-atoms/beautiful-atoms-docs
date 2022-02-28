.. batoms documentation master file.

===============================================
Welcome to Beautiful Atoms 2.0's documentation!
===============================================
Beautiful Atoms is a Python package for editing and rendering atoms and molecules objects using Blender. A Python interface that allows for automating workflows.


.. code:: python

   from batoms import Batoms
   h2o = Batoms("h2o",
               species = ["O", "H", "H"], 
               positions= [[0, 0, 0], [0, -0.76, -0.6], [0, 0.76, -0.6]])

|logo|

Features:

* Model: space-filling, ball-stick, polyhedral, cavity and so on.
* Support file: cif, xyz, cube, pdb, json, VASP-out and so on.
* Volumetric data (Isosurface), molecular surface
* Ribbon diagram for protein
* Site occupancy
* Support periodic boundary conditions
* Support structure from ASE and Pymatgen
* Support fetch structures from MaterialProject, Pubchem and RSCB
* Animation
* GUI
* ``Flexible``: Python script, run interactively or in background.
* ``High quality rendering``:  3D models
* ``Free, Open Source``: Easy to download and install.
* ``Cross-platform``: (Linux, Windows, macOS)


.. toctree::
   :maxdepth: 2
   
   install/index
   getting-started
   viewport
   tutorial/index
   module/index
   gui/index
   ops/index
   advanced/index
   gallery
   tips
   contact
   faqs
   development/index



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _feedback: 
.. _affiliated packages: 

.. |logo|  image:: _static/figs/batoms-h2o.png
   :width: 3cm