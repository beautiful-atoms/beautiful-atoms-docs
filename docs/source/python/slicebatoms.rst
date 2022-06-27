.. module:: batoms.slicebatoms

===================
The SliceBatoms object
===================

The :class:`SliceBatoms` object store the information of sliced Batoms object.

.. code:: python
   
   from batoms import Batoms
   h2o = Batoms("h2o",
               species = ["O", "H", "H"], 
               positions= [[0, 0, 0], [0, -0.76, -0.6], [0, 0.76, -0.6]])

.. image:: /images/batoms-h2o.png
   :width: 3cm


One get the positions of the first atoms by:

>>> h2o[0].positions

One get the positions of the first two atoms by:

>>> h2o[0:2].positions
