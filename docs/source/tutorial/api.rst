
============================
The render function
============================

The :meth:`render` function is to run batoms and blender in the background.

>>> from ase.build import molecule
>>> from batoms import render
>>> atoms = molecule('C2H6SO')
>>> render_input = {'output': 'figs/c2h6so.png',}
>>> render(atoms = atoms, render_input = render_input)

Here, the first keyword ``batoms`` specifies the ASE atomic structure for :class:`Batoms`, and 
second keyword ``batoms`` keywords to specify the setting for :class:`batoms`.  Other
possible keywords are: ``display``.

