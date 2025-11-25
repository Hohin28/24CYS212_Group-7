from PIL import Image  #1

def desaturate_grayscale(input_path, output_path):  #2
    img = Image.open(input_path).convert("RGB")  #3
    width, height = img.size  #4
    gray_img = Image.new("RGB", (width, height))  #5

    for x in range(width):  #6
        for y in range(height):  #7
            r, g, b = img.getpixel((x, y))  #8
            max_val = max(r, g, b)  #9
            min_val = min(r, g, b)  #10
            gray = int((max_val + min_val) / 2)  #11
            gray_img.putpixel((x, y), (gray, gray, gray))  #12

    gray_img.save(output_path)  #13
    print("Saved:", output_path)  #14

desaturate_grayscale("input.jpg", "out.jpg")  #15
#1  Import the PIL Image class so Python can open and save images.
#2  Start a function that takes input and output image file paths.
#3  Open the input image and convert it to RGB color mode.
#4  Get the width and height (dimensions) of the image in pixels.
#5  Create a blank new RGB image to store grayscale results.
#6  Loop through each column (x-axis).
#7  Loop through each row (y-axis) inside the column.
#8  Read the pixel’s RGB values at (x, y).
#9  Find the maximum (brightest) of the R, G, B values.
#10 Find the minimum (darkest) of the R, G, B values.
#11 Apply the Lightness/Desaturation grayscale formula: (max + min) / 2.
#12 Store the new grayscale value in the output image (R=G=B=gray).
#13 Save the final grayscale image to the output path.
#14 Print confirmation that the image was saved.
#15 Call the function to convert "input.jpg" into "out.jpg".
