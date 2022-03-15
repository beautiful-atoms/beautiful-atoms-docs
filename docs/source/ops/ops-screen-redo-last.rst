.. _batoms.ops.ed:

***********
Undo & Redo
***********

The tools listed below will let you roll back an accidental action,
redo your last action, or let you choose to recover to a specific point,
by picking from a list of recent actions recorded by Blender.



.. _bpy.ops.ed.undo:


Undo
====

.. tip::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Undo`
   :Shortcut:  :kbd:`Ctrl-Z`

If you want to undo your last action, just press :kbd:`Ctrl-Z`.


.. _bpy.ops.ed.redo:

Redo
====

.. tip::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Redo`
   :Shortcut:  :kbd:`Shift-Ctrl-Z`

To roll back the Undo action, press :kbd:`Shift-Ctrl-Z`.


.. _bpy.ops.screen.redo_last:

Adjust Last Operation
=====================

.. tip::

   :Mode:      All Modes
   :Menu:      :menuselection:`Edit --> Adjust Last Operation...`
   :Shortcut:  :kbd:`F9`

After an operation is complete you can tweak the parameters of operators afterwards. In editors that support it, there is a "head-up display" panel in the bottom left based on the last performed operation.

For example, if your last operation was adding a fcc111 surface  in *Object Mode*, Blender will show you all the parameters used for setuping the surface.
(see Fig. :ref:`fig-interface-redo-last-object-mode` left),
where you can change the surface completely by editing the parameters. If the panel is hidden, you can create a pop-up with ``F9`` to show the setting panel. 


In the second example (on the right), the last operation was moving a atom in z direction by 3 (See Fig. :ref:`fig-interface-redo-last-edit-mode` right).

.. list-table:: Adjust Last Operation.

   * - .. _fig-interface-redo-last-object-mode:

       .. figure:: ../_static/figs/interface_undo-redo_redo-last-object-mode.png
          :width: 310px

          Add a molecule (Object Mode).

     - .. _fig-interface-redo-last-edit-mode:

       .. figure:: ../_static/figs/interface_undo-redo_redo-last-edit-mode.png
          :width: 310px

          Move a atom (Edit Mode).
