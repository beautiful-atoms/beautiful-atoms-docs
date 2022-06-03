.. _hpc:

==========================================
Rendering on HPC using multi-process
==========================================

For a basic use (one node with OpenMP), the installation process of Blender on HPC is the same as on a local Linux computer. But you need to load the required modules when running. Blender needs OpenGL library. In a high-performance computing center, there are usually a couple of packages/libraries available. These include Mesa (open-source implementation of OpenGL) and also libGLU for GPU.


Use ``batoms``
==================

Save the following code as a python file (eg. h2o.py):

.. code:: python

    from ase.build import molecule
    from batoms import Batoms
    atoms = molecule('H2O')
    h2o = Batoms(label = 'h2o', from_ase = atoms)
    h2o.get_image([1, 0 ,0], engine = 'cycles', output = 'h2o.png')


Set up a job script on HPC, and save it (eg. job.slurm). Here is an example of the SLURM system on the Ubelix cluster at the University of Bern.

.. code:: bash

    #!/bin/bash
    #SBATCH --job-name=batoms
    #SBATCH --output=test.out
    #SBATCH --error=test.err
    #SBATCH --time=00:20:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=20
    #SBATCH --partition=epyc2
    #SBATCH --mem-per-cpu=5GB

    module load Mesa/.20.2.1-GCCcore-10.2.0

    blender -b -P h2o.py > h2o.dat

And then submit the job.

.. code:: bash

    submit job.slurm


Use ``blend`` file
===================

Create your model locally, and save the file to ``myfile.blend``. 

.. code:: bash

    #!/bin/bash
    #SBATCH --job-name=batoms
    #SBATCH --output=test.out
    #SBATCH --error=test.err
    #SBATCH --time=00:20:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=20
    #SBATCH --partition=epyc2
    #SBATCH --mem-per-cpu=5GB

    module load Mesa/.20.2.1-GCCcore-10.2.0

    blender -b myfile.blend -a 
    
This will render an animation of the file ``myfile.blend`` with the settings with which the file was saved.


Performance
============

Here is a test for a system with 63 atoms. The performance is shown below. The speed scales well with the number of CPUs.

.. list-table::
   :widths: 25 25

   * - Number of CPU
     - Times (s)
   * - 2
     - 97
   * - 4
     - 40
   * - 8
     - 25 
   * - 16
     - 13
   * - 32
     - 11
   * - 64
     - 8 



.. note::
    Blender does not support headless rendering using ``EEVEE``. So please use ``CYCLES`` engine.

    For multi-nodes, you have to build Blender manually. Suggest using the EasyBuild recipes.



