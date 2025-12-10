import cv2                               #1
import numpy as np                       #2
import math                              #3
from scipy.ndimage import uniform_filter #4

def spatial_filter(img_path):            #5
    img=cv2.imread(img_path)             #6
    if img is None:                      #7
        print("Image missing")           #8
        return                           #9

    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   #10
    arr=rgb.astype(float)                #11

    gray=np.mean(arr,axis=2)             #12
    sm=uniform_filter(gray,size=5,mode="reflect")   #13
    noise=gray-sm                        #14

    mad=np.median(np.abs(noise-np.median(noise)))   #15
    sigma=1.4826*mad                     #16

    g_size=2*math.ceil(3*sigma)+1        #17
    g_size=max(g_size,3)                 #18

    print("Correct Sigma =",sigma)       #19
    print("Gaussian Filter Size =",f"{g_size}x{g_size}")   #20

    def box(img,k,norm=True):            #21
        if norm:                         #22
            out=cv2.boxFilter(img,-1,(k,k),normalize=True,
                               borderType=cv2.BORDER_REFLECT)   #23
        else:                            #24
            tmp=cv2.boxFilter(img.astype(np.float32),-1,(k,k),
                               normalize=True,borderType=cv2.BORDER_REFLECT)   #25
            out=tmp*(k*k)                #26
        return np.clip(out,0,255).astype(np.uint8)   #27

    mid=g_size//2                        #28
    axis=np.linspace(-mid,mid,g_size)    #29
    g1d=np.exp(-(axis*axis)/(2*sigma*sigma))   #30

    g1d_n=g1d/np.sum(g1d)                #31
    unnorm_factor=2*math.pi*(sigma*sigma)   #32
    g1d_u=g1d_n*unnorm_factor            #33

    def gauss(img,norm=True):            #34
        if norm:                         #35
            out=cv2.sepFilter2D(img.astype(np.float32),-1,
                                 g1d_n,g1d_n,borderType=cv2.BORDER_REFLECT)   #36
        else:                            #37
            out=cv2.sepFilter2D(img.astype(np.float32),-1,
                                 g1d_u,g1d_u,borderType=cv2.BORDER_REFLECT)   #38
        return np.clip(out,0,255).astype(np.uint8)   #39

    results=[                             #40
        box(arr,5,True),                  #41
        box(arr,5,False),                 #42
        box(arr,20,True),                 #43
        box(arr,20,False),                #44
        gauss(arr,True),                  #45
        gauss(arr,False)                  #46
    ]

    for i,o in enumerate(results):        #47
        bgr=cv2.cvtColor(o,cv2.COLOR_RGB2BGR)   #48
        name=f"output_{i}.jpg"            #49
        cv2.imwrite(name,bgr)             #50
        print("Saved:",name)              #51

spatial_filter("input.jpg")              #52


#-------------------------------------------------------------------
#1  Import OpenCV
#2  Import NumPy
#3  Import math module
#4  Import uniform_filter for noise estimation
#5  Define main filtering function
#6  Load image
#7  Check for missing file
#8  Print error
#9  Exit function
#10 Convert BGR→RGB
#11 Convert image to float
#12 Convert to grayscale
#13 Apply 5x5 smoothing to estimate noise-free signal
#14 Compute noise = gray - smooth
#15 Compute MAD (median absolute deviation)
#16 Sigma estimation
#17 Compute Gaussian kernel size
#18 Ensure minimum size is 3
#19 Print sigma
#20 Print kernel size
#21 Define box filter wrapper
#22-23 Normalized box filter
#24-26 Unnormalized box filter
#27 Return clipped result
#28 Find kernel midpoint
#29 Create axis for Gaussian
#30 Compute 1D Gaussian
#31 Normalize Gaussian
#32 Constant to convert normalized→unnormalized
#33 Create unnormalized Gaussian kernel
#34 Define Gaussian filter wrapper
#35-36 Normalized Gaussian filter
#37-38 Unnormalized Gaussian filter
#39 Return filtered result
#40 Start results list
#41-46 Apply all filters (box 5/20, norm/un-norm, Gaussian norm/un-norm)
#47 Loop over results
#48 Convert RGB→BGR for saving
#49 Create file name
#50 Save file
#51 Print saved name
#52 Run function with input file
#-------------------------------------------------------------------
