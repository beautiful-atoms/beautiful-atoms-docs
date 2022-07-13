.. _gui-batoms:


==============
Batoms panel
==============

.. tip::

   :Panel:     :menuselection:`Sidebar region --> Batoms`


This panel is used to set the overall properties related with :class:`Batoms` object.

.. image:: /images/gui_batoms.png
   :width: 5 cm



Style
==============


Model style
----------------


Here, four models are supported.

.. list-table::
   :widths: 25 25 25 25

   * - **Space-filling**
     - **Ball-and-stick**
     - **Polyhedral**
     - **Stick**
   * -  .. image:: /images/batoms_model_style_0.png 
     -  .. image:: /images/batoms_model_style_1.png 
     -  .. image:: /images/batoms_model_style_2.png 
     -  .. image:: /images/batoms_model_style_3.png 


Radius style 
----------------

Supported style are:

#. **Covalent**
#. **VDW**
#. **Ionic**


Radii are imported from `ase.data`:

https://wiki.fysik.dtu.dk/ase/ase/data.html?highlight=radii#ase.data.covalent_radii





Color style
----------------
Supported style are:


#. **JMOL**: http://jmol.sourceforge.net/jscolors/#color_U
#. **VESTA**: https://jp-minerals.org/vesta/en/
#. **CPK**: https://en.wikipedia.org/wiki/CPK_coloring



Polyhedra style
----------------

Four polyhedra model are supported.

.. list-table::
   :widths: 25 25 25 25

   * - **atoms, bonds and polyhedra**
     - **atoms, polyhedra**
     - **central atoms, polyhedra**
     - **polyhedra**
   * -  .. image:: /images/batoms_polyhedra_style_0.png 
     -  .. image:: /images/batoms_polyhedra_style_1.png 
     -  .. image:: /images/batoms_polyhedra_style_2.png 
     -  .. image:: /images/batoms_polyhedra_style_3.png
  




Label
===========
One can add label for each atoms.

You can input string like:

#. `index`
#. `specie symbol`
#. `charge`

Here is a example of CH4 molecule with `index` label:

.. image:: /images/gui_batoms_2.png
   :width: 5 cm


Other parameters:
===================

**Scale**: change scale for all atoms.

**show**: show or hide the structure.
