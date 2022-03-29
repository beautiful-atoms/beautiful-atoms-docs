

=============
Engine
=============

One can set the engine by:

>>> h2o.render.engine = 'cycles' # or workbench, or eevee

Three engines can be used:

.. list-table::
   :widths: 25 25 25

   * - BLENDER_WORKBENCH
     - BLENDER_EEVEE
     - CYCLES
   * - Fast
     - Standard
     - Most powerfull, slow
   * -  .. image:: ..//images/render_workbench.png 
     -  .. image:: ..//images/render_eevee.png 
     -  .. image:: ..//images/render_cycles.png 

