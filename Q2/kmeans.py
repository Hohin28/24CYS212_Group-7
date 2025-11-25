from PIL import Image  #1
import numpy as np  #2
def compute_rate(labels,K):  #3
    prob=np.array([(labels==i).mean() for i in range(K)])  #4
    prob=np.maximum(prob,1e-12)  #5
    rate=-np.log2(prob)  #6
    return rate  #7
def rd_kmeans(pixels,K,lam,iters=10):  #8
    N=len(pixels)  #9
    idx=np.random.choice(N,K,replace=False)  #10
    centroids=pixels[idx]  #11
    labels=np.zeros(N,dtype=int)  #12
    for _ in range(iters):  #13
        rate=compute_rate(labels,K)  #14
        D=np.sum((pixels[:,None]-centroids[None,:])**2,axis=2)  #15
        RD_cost=D+lam*rate  #16
        labels=np.argmin(RD_cost,axis=1)  #17
        new_cent=[]  #18
        for k in range(K):  #19
            pts=pixels[labels==k]  #20
            if len(pts)==0:  #21
                new_cent.append(centroids[k])  #22
            else:  #23
                new_cent.append(pts.mean(axis=0))  #24
        centroids=np.array(new_cent)  #25
    return centroids,labels  #26
def run(image_path,K,lam):  #27
    img=Image.open(image_path).convert("RGB")  #28
    img=img.resize((400,400))  # NEW: Speed up by reducing image size
    arr=np.array(img)  #29
    H,W=arr.shape[:2]  #30
    pixels=arr.reshape(-1,3).astype(float)  #31
    cent,lbl=rd_kmeans(pixels,K,lam)  #32
    out=cent[lbl].reshape(H,W,3).astype(np.uint8)  #33
    Image.fromarray(out).save("rd_output.jpg")  #34
    print("Saved → rd_output.jpg")  #35
K=int(input("Enter the no.of colors: "))  #36
lam=float(input("Enter trade-off factor: "))  #37
run("input.jpg",K,lam)  #38

#1  Import Image from PIL to load and save images.
#2  Import NumPy for numerical operations.
#3  Define function to compute rate (entropy-based cost).
#4  Compute probability of each cluster.
#5  Avoid log(0) by enforcing a minimum probability.
#6  Compute rate term R = -log2(p).
#7  Return rate array.
#8  Define Rate–Distortion K-means function.
#9  Total number of pixels.
#10 Randomly choose K initial centroids.
#11 Initialize centroids from random pixels.
#12 Initialize labels array for clusters.
#13 Loop for the specified number of iterations.
#14 Compute rate term using current labels.
#15 Compute distortion (squared distance) between pixels and centroids.
#16 Combine distortion with λ × rate to form RD cost.
#17 Assign each pixel to the lowest RD cost cluster.
#18 Prepare new centroid list.
#19 Loop through each cluster.
#20 Extract pixels belonging to cluster k.
#21 Check if cluster is empty.
#22 If empty, keep previous centroid.
#23 Otherwise compute new centroid.
#24 New centroid is mean of cluster pixels.
#25 Update centroids array.
#2
