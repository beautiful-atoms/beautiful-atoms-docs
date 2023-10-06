
==================================================
How to set the camera to focus on specific atoms?
==================================================

One can set the camera to focus on one position by setting the `center` parameter of the `get_image` method.

Here we show an example of focusing on the first atom of a molecule:

>>> from ase.build import molecule
>>> from batoms import Batoms
>>> mol = Batoms("mol", from_ase = molecule("CH3CH2OH"))
>>> # set the camera to focus on the first atom
>>> mol.get_image(padding = 3, center=mol.positions[0], output = "look_at.png")


GUI
=========
It is also possible to rotate the camera directly in the GUI.