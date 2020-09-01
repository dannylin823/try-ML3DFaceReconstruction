
import os
from PIL import Image
from pylab import *
 
current_path = os.getcwd()  
face_directory_path = current_path + "/input/"
for f in sys.argv[1:]:

	face_path = face_directory_path + f

	im = Image.open(face_path).convert('RGB')
	im.save(face_path)
	t = open(face_path.replace('png','txt'), 'w+')

	imshow(im)
	print ("Please click 5 points")
	x =ginput(5)
	print ('you clicked:',x)
	for p in x:
		t.write('{} {}'.format(str(int(p[0])), str(int(p[1]))) + "\n")
	show()

t.close()
