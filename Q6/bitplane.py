import cv2                               #1
import numpy as np                       #2

def bitplanes(img):                      #3
    planes=[]                            #4
    for i in range(8):                   #5
        planes.append(((img>>i)&1)*255)  #6
    return planes                        #7

def rec_low3(pln):                       #8
    rec=((pln[0]//255)<<0)+((pln[1]//255)<<1)+((pln[2]//255)<<2)   #9
    return rec.astype(np.uint8)          #10

low=cv2.imread("input_low.jpg",0)        #11
bright=cv2.imread("input_bright.jpg",0)  #12

if low is None or bright is None:        #13
    print("Image missing")               #14
    exit()                               #15

low_p=bitplanes(low)                     #16
low_r=rec_low3(low_p)                    #17
low_d=cv2.absdiff(low,low_r)             #18

cv2.imwrite("output_low_original.jpg",low)      #19
cv2.imwrite("output_low_reconstruct.jpg",low_r) #20
cv2.imwrite("output_low_diff.jpg",low_d)        #21

bright_p=bitplanes(bright)               #22
bright_r=rec_low3(bright_p)              #23
bright_d=cv2.absdiff(bright,bright_r)    #24

cv2.imwrite("output_bright_original.jpg",bright)      #25
cv2.imwrite("output_bright_reconstruct.jpg",bright_r) #26
cv2.imwrite("output_bright_diff.jpg",bright_d)        #27

print("Saved all outputs")               #28


#---------------------------------------------------------------
#1  Import OpenCV library for image processing
#2  Import NumPy for array operations
#3  Define function to extract 8 bitplanes from grayscale image
#4  Create empty list to store bitplanes
#5  Loop through bits 0 to 7 (LSB → MSB)
#6  Extract each bitplane using bitwise shift & mask, scale to 255
#7  Return list of 8 bitplanes
#8  Define function to reconstruct image from lowest 3 bitplanes
#9  Combine bit 0, bit 1, bit 2 using binary weights 1,2,4
#10 Convert result back to uint8 image
#11 Read low-light image in grayscale
#12 Read bright-light image in grayscale
#13 Check if either image is missing
#14 Print error if missing
#15 Exit program to avoid crash
#16 Extract bitplanes of low-light image
#17 Reconstruct low-light image using only lowest 3 bits
#18 Compute absolute difference (original - reconstructed)
#19 Save original low-light image
#20 Save reconstructed low-light image
#21 Save difference image for low-light
#22 Extract bitplanes of bright-light image
#23 Reconstruct bright-light using lowest 3 bitplanes
#24 Compute difference for bright-light
#25 Save original bright-light image
#26 Save reconstructed bright-light image
#27 Save difference image for bright-light
#28 Print confirmation message
#---------------------------------------------------------------
