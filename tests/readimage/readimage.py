from PIL import Image
import png, array
import numpy
#https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
#https://www.w3schools.com/colors/colors_rgb.asp
def test_image():
    im = Image.open('test.png') # Can be many different formats.
    pix = im.load()
    print(im.size)  # Get the width and hight of the image for iterating over
    #white sigin on> S
    print("white"+str(pix[381,280]))  # Get the RGBA Value of the a pixel of an image
    # green user ->U
    print("green"+str(pix[832, 134]))  # Get the RGBA Value of the a pixel of an image
    # black
    print("black"+str(pix[279, 146]))  # Get the RGBA Value of the a pixel of an image
    #blue
    print("blue"+str(pix[324, 21]))  # Get the RGBA Value of the a pixel of an image
    #pix[3,4] = value  # Set the RGBA Value of the image (tuple)
    #im.save('alive_test.png')  # Save the modified pixels as .png

def test_image2():


    point = (2, 10)  # coordinates of pixel to be painted red

    reader = png.Reader(filename='test.png')
    w, h, pixels, metadata = reader.read_flat()
    pixel_byte_width = 4 if metadata['alpha'] else 3
    pixel_position = point[0] + point[1] * w
    new_pixel_value = (255, 0, 0, 0) if metadata['alpha'] else (255, 0, 0)
    pixels[
    pixel_position * pixel_byte_width:
    (pixel_position + 1) * pixel_byte_width] = array.array('B', new_pixel_value)

    output = open('image-with-red-dot.png', 'wb')
    writer = png.Writer(w, h, **metadata)
    writer.write_array(output, pixels)
    output.close()


def test_get_image():
        """Get a numpy array of an image so that one can access values[x][y]."""
        image = Image.open('test.png', 'r')
        width, height = image.size
        pixel_values = list(image.getdata())
        if image.mode == 'RGB':
            channels = 3
        elif image.mode == 'L':
            channels = 1
        else:
            print("Unknown mode: %s" % image.mode)
            return None
        pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
        print(pixel_values)

def test_image4():
    FILENAME = 'test.png'  # image can be in gif jpeg or png format
    im = Image.open(FILENAME).convert('RGB')
    pix = im.load()
    w = 94
    h = 23
    for i in range(377,471):
        for j in range(268,291):
            print(pix[i, j])

