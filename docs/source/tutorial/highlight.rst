
================================
Highlight atoms
================================

The :mod:`HighlightSsettings <batoms.plugins.highlight.setting>` object controls various settings related to highlight.


Here we show an example of highlighting one of the H atoms in CH\ :sub:`4`\  molecule. 

>>> from ase.build import molecule
>>> from batoms import Batoms
>>> ch4 = Batoms("ch4", from_ase = molecule("CH4"))
>>> # create a selection with the indices of the atoms to be highlighted.
>>> ch4.selects.add("s1", [2])
>>> # add a highlight with the selection
>>> ch4.highlight.settings["s1"] = {"select": "s1", "scale": 0.5, "color": (0.5, 0.5, 0, 0.4)}
>>> ch4.highlight.draw()
>>> ch4.get_image(padding = 3, output = "highlight_ch4.png")

.. image:: /images/highlight_ch4.png
   :width: 5cm

The default setting uses spheres to highlight atoms. One can change it to a cube by setting ``style`` to 1:

>>> ch4.highlight.settings["s1"] = {"select": "s1", "scale": 0.8, "color": (0.5, 0.5, 0, 0.4), "style": 1}

.. image:: /images/highlight_ch4_cube.png
   :width: 5cm
 
.. warning::
    The length for the name of a selection should not excess 4. Thus 
    
    >>> ch4.selects.add("myselect", [2])
    
    could lead to a wrong result.


One can add multiple highlights.

>>> ch4.selects.add("s1", [2])
>>> ch4.selects.add("s2", [3])
>>> ch4.highlight.settings["s1"] = {"select": "s1", "scale":0.5, "color": (0.5, 0.5, 0, 0.4)}
>>> ch4.highlight.settings["s2"] = {"select": "s2", "scale":0.8, "color": (0, 0.5, 0.5, 0.4)}    

.. image:: /images/highlight_ch4_multi.png
   :width: 5cm

.. note::
    It does not support setting the radius of the highlight sphere by the radius of the atoms. So one has to choose the ``scale`` manually.
    This may be supported in the future.

GUI
=========
It would be easy to highlight atoms in GUI panel. Please refer to the :ref:`gui_highlight`.