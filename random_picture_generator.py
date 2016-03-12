import numpy as np
import scipy.misc as sm
import random

width = 1024
height = 1024

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros( (height,width,3), dtype=np.uint8 )

for i in range(width):
	for j in range (height):
		data[i][j] = [0,0,0] if random.choice( [0] * 50 + [1] ) == 0 else [255,255,255] #[random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)]

sm.imsave('picture.jpg', data)

# OR:
#img = sm.toimage( data ).save("outfile.jpg")  # Create a PIL image
#img.show()                                    # View in default viewers
