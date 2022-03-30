.. module:: batoms.bspecies

===================
The Species object
===================
The :class:`Species` object is a collection of species. Here is how to define a H\ :sub:`2`\ O molecule:


Possible keywords for a species are: ``scale``, ``color``, ``materials``, ``material_style``.


>>> h2o['H'].scale = 1.5
>>> h2o['H'].color = [1, 1, 0, 0.5]

  
Material style
===================

Set materials style for atoms. Select materials style from ['default', 'glass', 'ceramic', 'plastic', 'mirror'].

>>> h2o['O'].material_style = 'mirror'
>>> h2o['H'].material_style = 'mirror'

.. image:: /images/h2o-mirror.png
   :width: 3cm


Or set your own materials by setting the bsdf_inputs dict.

>>> h2o['H'].materials = {'Metallic': 0.9, 'Specular': 1.0, 'Roughness': 0.01}



List of all Methods
===================

.. autoclass:: Bspecies
   :members: