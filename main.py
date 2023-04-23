
from generate_polygon import generate_polygon


'''Generate Polygon'''
vertices = generate_polygon(center=(250, 250),
                            avg_radius=100,
                            irregularity=0.35,
                            spikiness=0,
                            num_vertices=4)


# card,xsize,ysize,vertices_bounds,show_grid=True,irregularity_clip=0.8, spikiness_clip=0.8
# error handling when card > canvas size
# when tested with generate_sets(200000,50000,50000,[3,7],False) : its taking more than 3m 12secs and it did not draw the canvas
# we have to parallise it


# generate_sets(64, 10000, 10000, [3, 7], True)
