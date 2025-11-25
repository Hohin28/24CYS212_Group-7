from PIL import Image  #1
import numpy as np  #2
path = "input.jpg"  #3
img_gray = Image.open(path).convert("L")  #4
img_rgb = Image.open(path).convert("RGB")  #5
gray = np.array(img_gray)  #6
rgb = np.array(img_rgb)  #7
print("Grayscale Resolution :", gray.shape)  #8
print("RGB Resolution       :", rgb.shape)  #9
def freq_sample(im, f):  #10
    F = np.fft.fftshift(np.fft.fft2(im))  #11
    H, W = F.shape  #12
    h2, w2 = max(1, H // f), max(1, W // f)  #13
    F_low = np.zeros_like(F)  #14
    hs, ws = (H // 2) - (h2 // 2), (W // 2) - (w2 // 2)  #15
    F_low[hs:hs+h2, ws:ws+w2] = F[hs:hs+h2, ws:ws+w2]  #16
    out = np.abs(np.fft.ifft2(np.fft.ifftshift(F_low)))  #17
    out = ((out - out.min()) / (out.max() - out.min() + 1e-9) * 255).astype(np.uint8)  #18
    return out  #19
def spatial_sample(im, f):  #20
    return im[::f, ::f].copy()  #21
factors = [2, 4, 8, 16]  #22
for f in factors:  #23
    out_f = freq_sample(gray, f)  #24
    Image.fromarray(out_f).save(f"freq_1_{f}.png")  #25
    print(f"Saved Frequency 1/{f}")  #26
    out_s = spatial_sample(rgb, f)  #27
    Image.fromarray(out_s).save(f"spatial_1_{f}.png")  #28
    print(f"Saved Spatial 1/{f}")  #29
print("All images saved.")  #30

#1  Import Image module for loading and saving.
#2  Import NumPy for matrix operations.
#3  Set the filename of the input image.
#4  Load image and convert to grayscale (L mode).
#5  Load image and convert to RGB mode.
#6  Convert grayscale image to NumPy array.
#7  Convert RGB image to NumPy array.
#8  Print dimensions of grayscale array.
#9  Print dimensions of RGB array.
#10 Define function for Frequency Domain Sampling.
#11 Perform 2D FFT and shift zero frequency to center.
#12 Get height and width of the frequency spectrum.
#13 Calculate crop dimensions based on factor f.
#14 Initialize an empty array for low frequencies.
#15 Calculate start coordinates for centering.
#16 Copy only the center (low freq) region.
#17 Inverse FFT to get back the blurred image.
#18 Normalize pixel values to 0-255 range.
#19 Return the processed image array.
#20 Define function for Spatial Domain Sampling.
#21 Slice array to keep every f-th pixel.
#22 List of downsampling factors to test.
#23 Loop through each factor.
#24 Apply frequency sampling on grayscale image.
#25 Save the resulting frequency image.
#26 Log frequency save status.
#27 Apply spatial sampling on RGB image.
#28 Save the resulting spatial image.
#29 Log spatial save status.
#30 Print final completion message.
