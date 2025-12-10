import cv2                               #1
import numpy as np                       #2

img_files=["img1.jpg","img2.jpg","img3.jpg","img4.jpg"]        #3
images=[cv2.imread(f) for f in img_files]                      #4

exposure_times=np.array([0.25,1.0,4.0,15.0],dtype=np.float32)  #5

align=cv2.createAlignMTB()               #6
align.process(images,images)             #7

merge_debevec=cv2.createMergeDebevec()   #8
hdr=merge_debevec.process(images,times=exposure_times.copy())  #9

tonemap=cv2.createTonemapReinhard(gamma=1.4,intensity=0,light_adapt=0,color_adapt=0)   #10
ldr=tonemap.process(hdr)                 #11

ldr=(ldr*255).clip(0,255).astype("uint8")   #12

cv2.imwrite("output.jpg",ldr)            #13

print("HDR saved as output.jpg")         #14


#---------------------------------------------------------------
#1  Import OpenCV library for image operations
#2  Import NumPy library for numeric array handling
#3  Create list containing exposure image filenames
#4  Read images from disk and store them into a list
#5  Exposure time values (in seconds) matching each input image
#6  Create object to align image positions
#7  Align the images to reduce camera movement artifacts
#8  Create Debevec HDR merging object
#9  Merge input images into HDR radiance map using exposure times
#10 Create Reinhard tone mapping operator to compress HDR range
#11 Apply tone mapping to produce an LDR image
#12 Convert HDR float image to 8-bit format
#13 Save the final processed HDR output image
#14 Print output confirmation message
#---------------------------------------------------------------
