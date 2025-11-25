from PIL import Image  #1
def median_cut_quantize(input_path,output_path,num_colors=16):  #2
    img=Image.open(input_path).convert("RGB")  #3
    quantized_img=img.quantize(colors=num_colors,method=0)  #4
    quantized_img=quantized_img.convert("RGB")  #5
    quantized_img.save(output_path)  #6
    print("Saved quantized image:",output_path)  #7
median_cut_quantize("input.jpg","output_median_cut.jpg",num_colors=64)  #8
#1  Import the PIL Image class so Python can open and manipulate images.
#2  Define a function for Median Cut color quantization.
#3  Open the image and convert it to RGB format.
#4  Apply PIL’s Median Cut quantization (method=0).
#5  Convert back to RGB so JPEG/PNG save correctly.
#6  Save the quantized image.
#7  Print confirmation.
#8  Call the function with 64 colors.
