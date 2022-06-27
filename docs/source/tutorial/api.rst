
============================
The render function
============================

The :meth:`render` function is to run batoms and blender in the background.

>>> from ase.build import molecule
>>> from batoms_api import render
>>> config = {
    "batoms_input": {"label": "test_batoms"},
    "settings": {
        "model_style": 2,
        "render": {"engine": "cycles", "samples": 1, "resolution": [20, 20]},
        "bonds": {
            "show_search": True,
        },
        "polyhedras": {
            "setting": {"Ti": {"color": [0, 0.5, 0.5, 0.5]}}},
    }
}
>>> render(atoms, **config)


