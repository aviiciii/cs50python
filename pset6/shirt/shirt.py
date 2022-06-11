from sys import argv, exit
import os
from PIL import ImageOps as imgops, Image as img

def main():
    inpt, outpt = get_filenames(argv)
    check_ext(inpt, outpt)

    # open images
    try:
        shirt = img.open('shirt.png')
        muppet = img.open(inpt)
    except FileNotFoundError:
        exit('Input does not exist')
    except Exception as exp:
        exit(exp)
    # get size of shirt.png
    size = shirt.size
    # crop muppet to fit shirt
    muppet = imgops.fit(muppet, size)
    # overlay shirt on mupper
    muppet.paste(shirt, shirt)
    # save image
    muppet.save(outpt)

def get_filenames(arguments):
    if len(arguments) != 3:
        if len(arguments) < 3:
            exit('Too few command-line arguments')
        else:
            exit('Too mant command-line arguments')
    return [argv[1],argv[2]]

def check_ext(inpt, outpt):
    in_root, in_ext = os.path.splitext(inpt)
    out_root, out_ext = os.path.splitext(outpt)

    # check input and output have same extensions
    if in_ext.lower() != out_ext.lower():
        exit('Input and output have different extensions')

    #check valid input
    if in_ext.lower() == '.jpg' or in_ext.lower() == '.jpeg' or in_ext.lower() == '.png':
        pass
    else:
        exit('Invalid input')

    #check valid output
    if out_ext.lower() == '.jpg' or out_ext.lower() == '.jpeg' or out_ext.lower() == '.png':
        pass
    else:
        exit('Invalid output')

if __name__ == '__main__':
    main()