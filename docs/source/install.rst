.. _download_and_install:

============
Installation
============

Requirements
============
* Blender_ 2.93 or newer, please install Blender first.
* ASE_

Optional:

* Scikit-image_
* Pymatgen_


.. _Blender: https://www.blender.org/
.. _Python: https://www.python.org/
.. _ASE: https://wiki.fysik.dtu.dk/ase/index.html
.. _Pymatgen: https://pymatgen.org/
.. _scikit-image: https://scikit-image.org/

Install batoms
======================
On Linux, go to your Blender python directory, e.g. ``blender-2.93-linux-x64/2.93/python/bin``, run::
    
    $ ./python3.9 -m ensurepip
    $ ./pip3 install batoms

On Windows, start Blender, open a Python console and run the following code::

    import sys
    import os
    import subprocess
    path = os.path.join(sys.prefix, 'bin', 'python.exe')
    subprocess.call([path, "-m", "ensurepip"])
    subprocess.call([path, "-m", "pip", "install", "batoms"])
 

Install batoms_addon
========================

- Download the source files from https://github.com/superstar54/batoms_addon. 

- Extract the file, rename the folder to ``batoms_addon``, and move it to ``blender-2.93.4-linux-x64/2.93/scripts/addons/``. 

- Enable the addon in the Preferences setting. Please vist here to learn how to enable an addon. 
https://docs.blender.org/manual/en/latest/editors/preferences/addons.html. Or, you can open a Blender Python console, and run the following code to enable the batoms_addon::

    import addon_utils
    addon_utils.enable('batoms_addon', default_set=True)


Test your installation
======================

Start Blender, in the python console, run:

>>> from batoms import Batoms
>>> h2o = Batoms('h2o', {'O': [[0, 0, 0.40]], 'H': [[0, -0.76, -0.2], [0, 0.76, -0.2]]})


.. image:: _static/figs/batoms-h2o.png
   :width: 3cm
   
If you saw a water molecule, congratulations!


Others
================================


Pymatgen
----------

If you want to use ``batoms`` with ``Pymatgen``. Rename you blender python folder (``blender-2.93-linux-x64/2.93/python``) to ``_python``. Create a virtual environment for your blender using conda::

    conda create --prefix $Path_to_blener/blender-2.93.4-linux-x64/2.93/python python=3.9.2


On Linux, go to the new python directory, e.g. ``blender-2.93-linux-x64/2.93/python/bin``, and install ASE_,  scikit-image_ and Pymatgen_ inside Blender::

    $ ./pip3 install --upgrade ase
    
    $ ./pip3 install scikit-image

    $ ./pip3 install pymatgen
