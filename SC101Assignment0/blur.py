"""
File: blur.py
Name:黃方易
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage

BLUR_LAYER = 5
# BLUR_LAYER = 10 若需要present 10次，將數字改成10


def blur(img):
    """
    blur the imported image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):

            pixel = new_img.get_pixel(x, y)

            total_red = 0
            total_green = 0
            total_blue = 0
            total_num = 0

            if x == 0:
                r_left = x
            else:
                r_left = x - 1

            if y == 0:
                c_upper = y
            else:
                c_upper = y - 1

            if x == (img.width-1):
                r_right = x
            else:
                r_right = x + 1

            if y == (img.height-1):
                c_down = y
            else:
                c_down = y + 1

            for r in range(r_left, r_right+1):
                for c in range(c_upper, c_down+1):
                    total_red += img.get_pixel(r, c).red
                    total_green += img.get_pixel(r, c).green
                    total_blue += img.get_pixel(r, c).blue
                    total_num += 1

            # RGB average value, put it back separately.
            pixel.red = total_red / total_num
            pixel.blue = total_blue / total_num
            pixel.green = total_green / total_num

    return new_img


def main():
    """
    Blur the images
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(BLUR_LAYER):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
