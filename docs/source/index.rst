.. batoms documentation master file.

===============================================
Welcome to Beautiful Atoms's documentation!
===============================================
Beautiful Atoms is a Python package for editing and rendering atoms and molecules objects using Blender. A Python interface that allows for automating workflows.

>>> from batoms import Batoms
>>> h2o = Batoms('h2o', {'O': [[0, 0, 0.40]], 'H': [[0, -0.76, -0.2], [0, 0.76, -0.2]]})

|logo|

Features:

* Model: space-filling, ball-stick, polyhedral, cavity and so on.
* Support file: cif, xyz, cube, pdb, json, VASP-out and so on.
* Support structure from ASE and Pymatgen
* Volumetric data (Isosurface)
* Animation
* GUI
* ``Flexible``: Python script, run interactively or in background.
* ``High quality rendering``:  3D models
* ``Free, Open Source``: Easy to download and install.
* ``Cross-platform``: (Linux, Windows, macOS)


.. toctree::
   :maxdepth: 2
   
   install
   getting-started
   tutorial/index
   module/index
   gui/index
   advanced/index
   gallery
   tips
   faqs
   development



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _feedback: 
.. _affiliated packages: 

.. |logo|  image:: _static/figs/batoms-h2o.png
   :width: 3cm