.. _download_and_install:

============
Installation
============

.. Caution::
   The latest version only support Blender version >= 3.4.


Requirements
============

* Blender_, please install Blender (version >= 3.4) first.
* ASE_
* Scikit-image_

Optional:

* spglib_
* Pymatgen_
* matplotlib_
* openbabel_


Use Cross-Platform Installation Script
========================================
Manually installing dependencies in Blender can be non-trivial.
beautiful-atoms_ provides a cross-platform script `install.py <https://raw.githubusercontent.com/beautiful-atoms/beautiful-atoms/main/install.py>`_ 
to automate the process. We recommend you try it first. 

Alternatively, you may use :ref:`manual installation` or use our :ref:`docker image`.

How it works
------------

The installation script replaces Blender's bundled python distribution with a ``conda`` 
environment.
Before starting, make sure you have a working Anaconda_ or Miniconda_ with 
``Python>=3.6``, and git_ on your system.


For all platforms, the installation workflow contains 3 steps:

1. Clone beautiful-atoms_ to your local machine.
2. Create a new conda environment (e.g. ``beautiful_atoms``) and activate it.
3. Use conda's default python interpreter to run ``install.py``



The detailed steps are slightly per operation system:

.. tabs::

    .. tab:: Linux
        :active:

        Find out where Blender's bundled python is located on your system. 
        For example, if you have installed Blender 3.4.0 at ``~/apps/Blender``, 
        its python bundle is at ``~/apps/Blender/3.4``.

        .. code-block:: bash

            # Step 1
            git clone https://github.com/beautiful-atoms/beautiful-atoms.git && cd beautiful-atoms
            # Step 2
            conda create -n beautiful_atoms && conda activate beautiful_atoms
            # Step 3. The "--use-startup --use-preferences" options are 
            # suggested for a beginner of Blender. However, if you want to keep
            # your own startup and preferences of Blender, please remove these 
            # options.
            $CONDA_PYTHON_EXE install.py ~/apps/Blender/3.4  --use-startup --use-preferences
        
        Change ``~/apps/Blender/3.4`` in step 3 to the path on your system.

        .. note::

            - In step 2, it is important to use a python interpreter **outside** the activated conda environment, 
              such as ``$CONDA_PYTHON_EXE``.
            - In step 3, Blender installed via ``Flatpak`` or ``Snap`` may have complex directory hierachy. 
              Check their documentations for details or try with a portable Blender distribution.

            

    .. tab:: macOS

        If you have installed Blender into ``/Applications`` or ``~/Applications``, 
        ``install.py`` will find the correct Blender python bundle for you. 
        If there are multiple versions, it will prompt your choice.
        
        .. code-block:: zsh

            # Step 1
            git clone https://github.com/beautiful-atoms/beautiful-atoms.git && cd beautiful-atoms
            # Step 2
            conda create -n beautiful_atoms && conda activate beautiful_atoms
            # Step 3 The "--use-startup --use-preferences" options are 
            # suggested for a beginner of Blender. However, if you want to keep
            # your own startup and preferences of Blender, please remove these 
            # options.
            $CONDA_PYTHON_EXE install.py --use-startup --use-preferences

        .. note::

            - In step 2, it is important to use a python interpreter **outside** the activated conda environment, 
              such as ``$CONDA_PYTHON_EXE``.
            - In step 3, if Blender is installed at a non-default location, find its python bundle and
              provide the path to ``install.py``. 
              For example if Blender version 3.4.0 is installed to ``~/apps/Blender.app``, run step 3 with:

              .. code-block:: zsh

                $CONDA_PYTHON_EXE install.py ~/apps/Blender.app/Contents/Resources/3.4

    .. tab:: Windows

        If Blender is installed into ``%PROGRAMFILES%`` (e.g. by the default installer program), 
        ``install.py`` will find the correct Blender python bundle for you. 
        If there are multiple versions, it will prompt your choice. 
        Run the steps in "Anaconda Prompt as Administrator" for the installation
        

        .. code-block:: dosbatch

            :: Step 1
            git clone https://github.com/beautiful-atoms/beautiful-atoms.git && cd beautiful-atoms
            :: Step 2 The "--use-startup --use-preferences" options are 
            :: suggested for a beginner of Blender. However, if you want to keep
            :: your own startup and preferences of Blender, please remove these 
            :: options.
            python install.py --use-pip --use-startup --use-preferences

        .. warning::
            Do not run ``install.py`` in a Windows Subsystem for Linux (WSL) environment 
            while installing into the Blender on the Windows host. 

            - If you want `beautiful-atoms` on Windows but just prefer bash-like prompt, consider using `Git Bash <https://gitforwindows.org>`_ or similar shell emulators.

            - Otherwise if you wish to install ``beautiful-atoms`` inside WSL, follow the steps for Linux systems.
        
        .. note::
            - Due to a `bug in anaconda <https://github.com/ContinuumIO/anaconda-issues/issues/11994>`_,
              replacing conda environment may cause an issue with DLLs. 
              ``install.py`` falls back to use ``pip`` and no new conda envionment is needed in this case.
            - In step 2, if Blender is installed at a non-default location, find its python bundle and
              provide the path to ``install.py``. 
              For example, if Blender 3.4.0 is installed to ``%UserProfile%\Blender``, run step 3 with:

              .. code-block:: dosbatch

                python install.py %UserProfile%\Blender\3.4

            - You may need Visual Studio C++ Build Tools for building ``openbabel`` & ``spglib``,
              check the `tutorial <https://www.scivision.dev/python-windows-visual-c-14-required/>`_ for details
              (requires ~4 GiB disk space).
            - Without the build tools, 
              ``install.py`` will try its best to fetch a compatible ``spglib`` version from ``conda-forge`` so that most
              of Beautiful Atoms' functionalities are usable. 
              Note in this case openbabel utilities (e.g. adding SMILES) will be disabled.

You can check the usage of ``install.py`` by:

.. code-block:: bash
    
    python install.py --help
   
There are several useful options in ``install.py``. For example, if you're developing the source code for ``batoms``, adding ``--develop`` option 
to the installation process makes a symlink between your local code and the blender plugin folder and keeps the plugin up-to-date.

Uninstallation
------------
``install.py`` allows uninstalling the ``batoms`` with its dependencies 
to revert Blender to its previous state. 

.. tabs::

    .. tab:: Linux and macOS
        :active:

        Remove the ``batoms`` plugin and restore Blender's bundled python.

        .. code-block:: bash

            python install.py --uninstall <path/to/blender/3.x>
        
        (Optional) Remove the conda environment:

        .. code-block:: bash

            conda deactivate
            conda remove -n beautiful_atoms

    .. tab:: Windows

        Remove the ``batoms`` plugin and its dependencies via ``pip``.

        .. code-block:: dosbatch

            python install.py --uninstall --use-pip <path\to\blender\3.x>

You may omit the path to Blender's bundled python on macOS and Windows if installed using the same option.


.. _manual installation:

Manual installations
=====================================
For a basic installation. Please check the OS-specific tutorials below:

.. toctree::
   :maxdepth: 1
   
   linux
   windows
   macos

.. _docker image:

Container image
====================================
We also provide a container image `ghcr.io/beautiful-atoms/beautiful-atoms <https://github.com/beautiful-atoms/beautiful-atoms/pkgs/container/beautiful-atoms>`_
(a mirrored image  `luciusm/beautiful_atoms <https://hub.docker.com/r/luciusm/beautiful_atoms>`_ is hosted at Dockerhub
if you cannot access Github's container registry),
for users familiar with Docker_ or other container platforms. 
You may find it useful if your workflow does not depend on GUI, such as automatic code unit tests, 
high-throughput rendering, and working with HPC systems.

To use the container image in Docker_ (may need to run as admin):

.. code-block:: bash

    docker pull ghcr.io/beautiful-atoms/beautiful-atoms:latest

The container image should be compatible with `Shifter <https://docs.nersc.gov/development/shifter/>`_ 
or `Singularity <https://sylabs.io/guides/3.5/user-guide/index.html>`_ on HPC systems, 
check their manuals for more information.
    
To run a local python script (e.g. `./render.py`) inside the container (may need to run as admin):

.. code-block:: bash

    docker run --rm \
           -v $(pwd):/workdir \
           ghcr.io/beautiful-atoms/beautiful-atoms:latest \
           blender -b -P render.py
           
If you encounter issues with write permission to the output image, this is likely because the owner of your current directory
has different user id (UID) or group id (GID) than the default value (1000:100). You can find the currently owner of the directory using ``ls -ln .``, the UID & GID will be displayed on the 3rd and 4th columns. For example, if the host directory is owned by 1001:101, the docker command becomes:

.. code-block:: bash

    docker run --rm \
           -v $(pwd):/workdir \
           -u 1001:101 \
           ghcr.io/beautiful-atoms/beautiful-atoms:latest \
           blender -b -P render.py

You can find the UID & GID of current directory owner by running ``ls -aln .``.

Use GUI with the docker container
---------------------------------
It is possible to run Blender GUI within the docker container (only tested on Linux) 
by ``X11`` forwarding. 
Please check `this tutorial <https://github.com/nytimes/rd-blender-docker/wiki/Using-the-Blender-GUI-in-containers>`_ 
for more details.

.. warning::

    There are several known limitations with Blender docker container, especially on macOS.

    1. Cannot be run with macOS with ARM processor (`issue <https://github.com/docker/for-mac/issues/6047>`_)
    2. GUI forwarding not working with `XQuartz` (`issue <https://github.com/XQuartz/XQuartz/issues/54>`_)
    3. Blender cannot render using EEVEE without a display. Choose cycles as the renderer if you want to render headlessly.


Other Troubleshooting
======================

Please read :ref:`tips` page for more setup.



..
    Others
    ================================


    Pymatgen
    ----------

    If you want to use ``batoms`` with ``Pymatgen``. Rename you blender python folder (``blender-3.0.0-linux-x64/3.0/python``) to ``_python``. Create a virtual environment for your blender using conda::

        conda create --prefix $Path_to_blener/blender-3.0.0-linux-x64/3.0/python python=3.9.7


    On Linux, go to the new python directory, e.g. ``blender-3.0.0-linux-x64/3.0/python/bin``, and install ASE_,  scikit-image_ and Pymatgen_ inside Blender::

        $ ./pip3 install --upgrade ase
        
        $ ./pip3 install scikit-image

        $ ./pip3 install pymatgen


    Troubleshooting
    ================================

    Windows
    -------------



.. _3.0: https://download.blender.org/release/Blender3.0/blender-3.0.1-linux-x64.tar.xz
.. _3.1: https://download.blender.org/release/Blender3.1/blender-3.1.2-linux-x64.tar.xz
.. _3.2: https://download.blender.org/release/Blender3.2/blender-3.2.2-linux-x64.tar.xz
.. _beautiful-atoms: https://github.com/beautiful-atoms/beautiful-atoms
.. _Blender: https://www.blender.org/
.. _Python: https://www.python.org/
.. _pip: https://pypi.org/project/pip/
.. _ASE: https://wiki.fysik.dtu.dk/ase/index.html
.. _Pymatgen: https://pymatgen.org/
.. _scikit-image: https://scikit-image.org/
.. _spglib: https://spglib.github.io/spglib/python-spglib.html
.. _matplotlib: https://matplotlib.org/stable/users/installing.html
.. _openbabel: https://open-babel.readthedocs.io/en/latest/index.html
.. _Anaconda: https://docs.anaconda.com/anaconda/install
.. _Miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _Docker: https://www.docker.com/get-started/
.. _git: https://git-scm.com/download/
