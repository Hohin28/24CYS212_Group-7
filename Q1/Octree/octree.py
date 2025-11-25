from PIL import Image  #1
def octree_quantize_image(input_path,output_path,maxcolors):  #2
    img=Image.open(input_path).convert('RGB')  #3
    print(f"Quantizing image to max {maxcolors} colors using FASTOCTREE method...")  #4
    quantized_img=img.quantize(colors=maxcolors,method=Image.Quantize.FASTOCTREE)  #5
    quantized_img.save(output_path)  #6
    print(f"Quantized image saved to: {output_path}")  #7
maxcolors=int(input("Enter maximum number of colors (e.g., 256): "))  #8
octree_quantize_image("input.jpg","out.png",maxcolors)  #9
#1  Import the PIL Image class so Python can load and manipulate images.
#2  Define a function that performs Octree color quantization.
#3  Open the input image and convert it to RGB mode.
#4  Print a message showing the number of colors requested.
#5  Apply Pillow's FASTOCTREE quantization method to reduce the colors.
#6  Save the quantized (palette-based) image to the output path.
#7  Print confirmation that the output file has been saved.
#8  Ask the user to input the number of colors to reduce the image to.
#9  Call the quantization function using the provided values.
