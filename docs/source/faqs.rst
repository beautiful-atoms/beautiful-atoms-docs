=======
FAQs
=======

- RuntimeError: Error: Node type GeometryNodeAttributeTransfer undefined
    If you use Blender version >= 3.4, please download the latest version (the main branch) of the batoms.`GeometryNodeAttributeTransfer` is used in the old version of batoms, which belongs to Blender version < 3.2. 

- ValueError: to_mesh(): Mesh 'xxx' is in editmode
    Get error from:

    >>> pt111.replace('Pt', 'Au', range(20))

    Solution: Exit the ``Edit`` mode.


- RuntimeError: Operator bpy.ops.object.select_all.poll() failed, context is incorrect
    Get error from:

    >>> co.translate(t)

    Solution: Exit the ``Edit`` mode.



- Rotate viewport around cursor
    https://blender.stackexchange.com/questions/179289/how-do-i-rotate-my-viewport-around-the-position-of-my-cursor


Grid setting
=======================

https://www.katsbits.com/codex/grid/

