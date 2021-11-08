from batoms.build import bulk
from batoms.butils import removeAll
from batoms.bdraw import draw_plane
removeAll()
au = bulk('au', 'Au', cubic = True)
au.planesetting[(1, 1, 1)] = {'distance': 8, 'crystal': True,
                        'symmetry': True, 'color': [0, 0.2, 0.8, 1]}
au.planesetting[(0, 0, 1)] = {'distance': 10, 'crystal': True,
                        'symmetry': True, 'color': [0.6, 0.2, 0, 1]}
au.draw_crystal_shape()
au.render.set_world(color = [0.2, 0.2, 0.2, 1.0])
draw_plane(location = [0, 0, min(au.get_all_vertices()[:, 2])], size = 500, color = (0.9, 0.9, 0.9, 1))
au.render.lights['Default'].energy = 40
au.render.lights['Default'].direction = [1, 0.5, 0.5]
au.render.run([0.2, -1, 0.4], padding = 5, engine = 'cycles', 
            output = 'figs/gallery_planesetting_crystal.png')