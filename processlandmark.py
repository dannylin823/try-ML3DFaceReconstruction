# -*- coding: utf-8 -*-
import sys
import dlib
import cv2
import os
from PIL import Image

current_path = os.getcwd()  
predictor_path = current_path + "/shape_predictor_5_face_landmarks.dat"
face_directory_path = current_path + "/input/"



detector = dlib.get_frontal_face_detector() 
predictor = dlib.shape_predictor(predictor_path)    

for f in sys.argv[1:]:
    face_path = face_directory_path + f

    img = cv2.imread(face_path , cv2.IMREAD_COLOR)

    im = Image.open(face_path).convert('RGB')
    im.save(face_path)

    t = open(face_path.replace('png','txt'), 'w+')
    
	
    


    b, g, r = cv2.split(img)    
    img2 = cv2.merge([r, g, b])   

    dets = detector(img, 1) 
    print("Number of faces detected: {}".format(len(dets)))   
    for index, face in enumerate(dets):
        print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))


        shape = predictor(img, face)  
        for index, pt in enumerate(shape.parts()):
            print(pt.x , pt.y)
            t.write(str(pt.x) + " " + str(pt.y) + "\n")
       
            pt_pos = (pt.x, pt.y)
            cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)

        cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(f, img)

k = cv2.waitKey(0)
cv2.destroyAllWindows()
t.close()
