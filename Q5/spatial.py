import cv2                               #1
import numpy as np                       #2
import matplotlib.pyplot as plt          #3
import math                              #4

def spatial_filter(img_path):            #5
    img=cv2.imread(img_path)             #6
    if img is None:                      #7
        return                           #8
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   #9

    out={'Original':rgb}                 #10
    
    for k in [5,20]:                     #11
        out[f'Box {k}x{k} (Norm)']=cv2.boxFilter(rgb,-1,(k,k),normalize=True)          #12
        out[f'Box {k}x{k} (Unnorm)']=cv2.boxFilter(rgb,cv2.CV_32F,(k,k),normalize=False) #13

    sigma=3.0                            #14
    ksize=int(2*math.ceil(3*sigma)+1)    #15
    
    mid=ksize//2                         #16
    axis=np.linspace(-mid,mid,ksize)     #17
    g1d=np.exp(-(axis*axis)/(2*sigma*sigma))   #18
    
    g1d_norm=g1d/np.sum(g1d)             #19
    
    out['Gauss (Norm)']=cv2.sepFilter2D(rgb,-1,g1d_norm,g1d_norm)   #20
    out['Gauss (Unnorm)']=cv2.sepFilter2D(rgb,cv2.CV_32F,g1d,g1d)   #21

    i=0                                  #22
    for name,img2 in out.items():        #23
        save_name=f"output_{i}.jpg"      #24
        cv2.imwrite(save_name,img2.astype(np.uint8) if img2.dtype!='float32' else np.clip(img2,0,255).astype(np.uint8)) #25
        i+=1                              #26

    plt.figure(figsize=(15,8))           #27
    for j,(title,im) in enumerate(out.items()):   #28
        plt.subplot(2,4,j+1)             #29
        plt.imshow(im.astype(np.uint8) if im.dtype!='float32' else im/255.0)  #30
        plt.title(title)                 #31
        plt.axis('off')                  #32
    plt.tight_layout()                   #33
    plt.show()                           #34

spatial_filter('input.jpg')              #35


#--------------------------------------------------------------------
#1-4   Import required libraries
#5     Define spatial filtering function
#6     Read input image from disk
#7-8   Exit if missing image
#9     Convert BGR image to RGB
#10    Create dictionary to store filtered results
#11    Loop kernel sizes 5 and 20
#12    Normalized box filter - average blur
#13    Unnormalized box filter - raw summation very bright
#14    Set sigma for Gaussian filter
#15    Compute gaussian filter size using sigma
#16    Compute kernel center
#17    Create gaussian sample axis vector
#18    Apply gaussian formula
#19    Normalize gaussian kernel
#20    Apply separable normalized gaussian blur
#21    Apply separable unnormalized gaussian blur
#22    Initialize counter for saving images
#23    Iterate output dictionary
#24    Create file names output_0.jpg, output_1.jpg, etc.
#25    Save image to file
#26    Increment counter
#27    Create plot window
#28-29 Create subplot layout
#30    Display images correctly by type
#31    Add titles to outputs
#32    Remove axis ticks
#33    Arrange output layout
#34    Show figure
#35    Call function with input.jpg
#--------------------------------------------------------------------
