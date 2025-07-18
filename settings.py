import math

tilesize = 32 # Size of each tile 

rows = 10 # Number of rows in the grid
cols = 15 # Number of columns in the grid

window_width = tilesize * cols 
window_height = tilesize * rows 

FOV = 60 * (math.pi / 180) # Field of view in radians

res = 4 # Resolution
num_rays = window_width // res