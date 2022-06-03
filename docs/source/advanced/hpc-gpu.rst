.. _hpc_gpu:

==========================================
Rendering on HPC using GPU
==========================================



Please read :ref:`hpc` page for setup on HPC.


Use ``batoms``
==================

Save the following code as a python file (eg. h2o.py). In the ``get_image`` function, set ``gpu = True`` to use the GPU for the rendering.

.. code:: python

    from ase.build import molecule
    from batoms import Batoms
    atoms = molecule("H2O")
    h2o = Batoms(label = "h2o", from_ase = atoms)
    h2o.get_image([1, 0 ,0], engine = "cycles", gpu = True, output = "h2o.png")


Set up a job script to use GPU on HPC, and save it (eg. job.slurm). Here is an example of the SLURM system on the Ubelix cluster at the University of Bern.

.. code:: bash

    #!/bin/bash
    #SBATCH --job-name=batoms-gpu
    #SBATCH --output=test.out
    #SBATCH --error=test.err
    #SBATCH --time=00:20:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=2
    #SBATCH --partition=gpu
    #SBATCH --qos=job_gpu_preempt
    #SBATCH --gres=gpu:gtx1080ti:1
    #SBATCH --account=dcb

    module load libGLU/.9.0.1-GCCcore-10.2.0

    blender -b -P h2o.py > h2o.dat

And then submit the job.

.. code:: bash

    submit job.slurm


Use ``blend`` file
===================

Create your model locally. To set up your GPU rendering, please visit https://docs.blender.org/manual/en/latest/render/cycles/gpu_rendering.html. Save the file to ``myfile.blend``. 

.. code:: bash

    #!/bin/bash
    #SBATCH --job-name=batoms-gpu
    #SBATCH --output=test.out
    #SBATCH --error=test.err
    #SBATCH --time=00:20:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=2
    #SBATCH --partition=gpu
    #SBATCH --qos=job_gpu_preempt
    #SBATCH --gres=gpu:gtx1080ti:1
    #SBATCH --account=dcb

    module load libGLU/.9.0.1-GCCcore-10.2.0

    blender -b myfile.blend -a 
    
This will render an animation of the file ``myfile.blend`` with the settings with which the file was saved.


Performance
============

Here is a test for a system with 63 atoms. The performance is shown below. 1 GPU speed up the rendering a lot.

.. list-table::
   :widths: 25 25

   * - Devices
     - Times  (s)
   * - 32 CPU
     - 11
   * - 64 CPU
     - 8 
   * - 1 gtx1080ti GPU
     - 9  


.. note::
    Blender does not support headless rendering using ``EEVEE``. So please use ``CYCLES`` engine.

    For multi-nodes, you have to build Blender manually. Suggest using the EasyBuild recipes.



