===============
MacOS
===============

Install Python dependencies
============================================

Go to your Blender python directory, e.g. ``/Applications/Blender.app/Contents/Resources/3.1/python/bin``, install pip_::
    
    $ ./python3.10 -m ensurepip
    $ ./python3.10 -m pip install --upgrade pip
    
Install ASE_ and scikit-image_ inside Blender::

    $ ./pip3 install --upgrade ase
    
    $ ./pip3 install scikit-image




Install batoms
===============================

- Download the latest version (`beautiful-atoms.zip <https://github.com/beautiful-atoms/beautiful-atoms/archive/refs/heads/main.zip>`__).

- Extract the file, move the folder ``batoms`` to Blender addons folder ``/Applications/Blender.app/Contents/Resources/3.1/scripts/addons/``. 

- Enable the addon in the Preferences setting. Please open a Blender Python console, and run the following code to enable the batoms::

    import addon_utils
    import bpy
    addon_utils.enable('batoms', default_set=True)
    bpy.context.preferences.view.use_translate_new_dataname = False
    bpy.ops.wm.save_userpref()

.. note::
    Or, you can visit here to learn how to enable an addon by hand. https://docs.blender.org/manual/en/latest/editors/preferences/addons.html.
    If you can not find the Blender addons folder, please see the directory layout docs. https://docs.blender.org/manual/en/dev/advanced/blender_directory_layout.html#blender-directory-layout



Test your installation
==================================

Start Blender, in the python console, run:

>>> from batoms import Batoms
>>> h2o = Batoms('h2o', species = ['O', 'H', 'H'], 
...     positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]])


.. image:: /images/getting_started_h2o.png
   :width: 15cm
   
If you saw a water molecule, you have run a successful installation, congratulations!


Install batoms-api on your computer (Optional)
==============================================

First install ASE on your computer. Open a terminal, and run::
    
    $ pip3 install --upgrade ase
    $ pip3 install batoms-api

Then set a ``BLENDER_COMMAND`` environment variables. One set these permanently in your :file:`~/.bashrc` file::

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
