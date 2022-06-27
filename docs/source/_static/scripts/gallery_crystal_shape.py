from batoms.build import bulk
from batoms.utils.butils import removeAll, set_world
from batoms.draw import draw_plane
removeAll()
au = bulk('au', 'Au', cubic=True)
au.crystal_shape.settings[(1, 1, 1)] = {'distance': 8, 'crystal': True,
                                       'symmetry': True, 'color': [0, 0.2, 0.8, 1]}
au.crystal_shape.settings[(0, 0, 1)] = {'distance': 10, 'crystal': True,
                                       'symmetry': True, 'color': [0.6, 0.2, 0, 1]}
au.crystal_shape.draw()
set_world(color=[0.2, 0.2, 0.2, 1.0])
draw_plane(location=[0, 0, min(au.get_all_vertices()[:, 2])],
           size=500, color=(0.9, 0.9, 0.9, 1))
au.render.viewport = [0.2, -1, 0.4]
au.render.engine = 'cycles'
au.render.lights['Default'].energy = 40
au.render.lights['Default'].direction = [1, 0.5, 0.5]
au.get_image(padding=5, output='gallery_planesetting_crystal.png')
