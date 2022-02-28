===============
Linux
===============

Install ASE_ inside Blender
===============================

On Linux and MacOS, go to your Blender python directory, e.g. ``blender-3.0.0-linux-x64/3.0/python/bin``, install pip_::
    
    $ ./python3.9 -m ensurepip
    $ ./python3.9 -m pip install --upgrade pip
    
Install ASE_ and scikit-image_ inside Blender::

    $ ./pip3 install --upgrade ase
    
    $ ./pip3 install scikit-image


Install batoms inside Blender
===============================

- Download the latest stable release (`beautiful-atoms.zip <https://github.com/superstar54/beautiful-atoms/archive/refs/heads/release/2.0.0.zip>`__).

- Extract the file, move the folder ``batoms`` to Blender addons folder ``$HOME/.config/blender/3.0/scripts/addons/``. 

- Enable the addon in the Preferences setting. Please vist here to learn how to enable an addon. https://docs.blender.org/manual/en/latest/editors/preferences/addons.html. Or, you can open a Blender Python console, and run the following code to enable the batoms::

    import addon_utils
    import bpy
    addon_utils.enable('batoms', default_set=True)
    bpy.ops.wm.save_userpref()


Test your installation 
=====================================

Start Blender, in the python console, run:

>>> from batoms import Batoms
>>> h2o = Batoms('h2o', species = ['O', 'H', 'H'], 
...     positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]])


.. image:: ../_static/figs/getting_started_h2o.png
   :width: 15cm
   
If you saw a water molecule, you have run a successful installation, congratulations!


Install batoms-api on your computer (Optional)
==================================================

First install ASE on your computer. On Windows, open Anaconda_ Prompt (suggest to Anaconda_). On Linux, open a terminal, and run::
    
    $ pip3 install --upgrade ase
    $ pip3 install batoms-api

Then set a ``BLENDER_COMMAND`` environment variables. On Linux, set these permanently in your :file:`~/.bashrc` file::

    export BLENDER_COMMAND='<path-to-blender>/blender'



.. _Blender: https://www.blender.org/
.. _Python: https://www.python.org/
.. _pip: https://pypi.org/project/pip/
.. _ASE: https://wiki.fysik.dtu.dk/ase/index.html
.. _Pymatgen: https://pymatgen.org/
.. _scikit-image: https://scikit-image.org/
.. _spglib: https://spglib.github.io/spglib/python-spglib.html
.. _matplotlib: https://matplotlib.org/stable/users/installing.html
.. _Anaconda: https://docs.anaconda.com/anaconda/install
