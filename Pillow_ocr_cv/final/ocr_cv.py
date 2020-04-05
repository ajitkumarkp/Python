import zipfile
import cv2 as cv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import pytesseract
import os

def find_string_in_file(input_string, file):
    """@param input_string: The string that you want to find in file- file_name
       @param file: The file you want to search through
       @return: True if string found, else None.
    """
    image = Image.open(file)
    all_string = pytesseract.image_to_string (image)   
    if input_string in all_string:
        found_string = True
        return found_string


def detect_faces (file):
    """@param file : The input image file to detect faces in
       @return faces_list : List of (x,y,w,h) for all faces detected
    """
    image_cv = cv.imread(file)
    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces_list = face_cascade.detectMultiScale(image_cv, 1.28)
    return faces_list

def draw_text(image, file, text, x, y):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf",size=40)
    draw.text((x,y), text, fill= "black", font= font)

x,y = 0,0
zip = zipfile.ZipFile("small_img.zip")
zip.extractall("Extract//")

files = os.listdir("Extract")

# files = ['a-0.png', 'a-1.png', 'a-2.png', 'a-3.png']
# files = ['a-3.png']

input_string = "Christopher"

found_string = False

sheet = Image.new("RGB", (1000, 2000), color="white")

for file in files:
    file_name = file
    file = "Extract//"+ file
    image = Image.open(file)
    found_string = find_string_in_file(input_string, file)

    if found_string:
        text = "Results found in file {}".format(file_name)
        draw_text(sheet, file, text, x, y)
        y+=50
        faces_list = detect_faces(file)
        if len(faces_list): 
            for x1,y1,w,h in faces_list:
                face_cropped = image.crop((x1, y1, x1+w, y1+h))  
                face_resized = face_cropped.resize((200,200))              
                sheet.paste(face_resized, (x,y))
                x+=200
                if x==sheet.width:
                    x=0
                    y+=200
            x=0
            y+=200

        else:
            draw_text(sheet, file, "But there were no faces in that file!", x, y)
            y+=50
    else:
        print ("Not found in file {}".format(file_name))

sheet.show()

# import zipfile
# import cv2 as cv
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
# import numpy as np
# import pytesseract
# import os

# def find_string_in_file(input_string, file):
#     """:param input_string: The string that you want to find in file- file_name
#        :param file: The file you want to search through
#        :return: True if string found, else None.
#     """
#     image = Image.open(file)
#     all_string = pytesseract.image_to_string (image)   
#     if input_string in all_string:
#         found_string = True
#         return found_string

# def detect_faces (file):
#     """:param file : The input image file to detect faces in
#        :return faces_list : List of (x,y,w,h) for all faces detected
#     """
#     image_cv = cv.imread(file)
#     face_cascade = cv.CascadeClassifier("readonly/haarcascade_frontalface_default.xml")
#     faces_list = face_cascade.detectMultiScale(image_cv, 1.28)
#     return faces_list

# def draw_text(image, text, x, y):
#     """:param image: The input image file to draw the text on
#        :param text: The text to be drawn
#        :param x,y: The coordinates on the image where the text will be drawn
#        :return None
#     """
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("readonly/fanwood-webfont.ttf",size=40)
#     draw.text((x,y), text, fill= "black", font= font)

# x,y = 0,0

# #Extract the contents of the zip file into the "Extract" directory
# # zip = zipfile.ZipFile("readonly/small_img.zip")
# zip = zipfile.ZipFile("readonly/images.zip")
# zip.extractall("Extract")

# # Creat a list with the names of all files in the directory
# files = os.listdir("Extract")

# #sort the list of files  
# files.sort() 

# # input_string = "Christopher"
# input_string = "Mark"

# found_string = False

# # Creat a 1000x2000 white background worksheet
# sheet = Image.new("RGB", (1000, 2000), color="white")

# #Loop for each file in the files list 
# for file in files:
#     file_name = file
#     file = "Extract/"+ file
#     image = Image.open(file)
    
#     found_string = find_string_in_file(input_string, file)

#     if found_string:
#         text = "Results found in file {}".format(file_name)
#         draw_text(sheet, text, x, y)
#         y+=50 # new line
#         faces_list = detect_faces(file)
#         if len(faces_list): 
#             for x1,y1,w,h in faces_list:
#                 face_cropped = image.crop((x1, y1, x1+w, y1+h))  
#                 face_resized = face_cropped.resize((100,100))              
#                 sheet.paste(face_resized, (x,y))
#                 x+=100
#                 if x==sheet.width:
#                     x=0
#                     y+=100
#             x=0
#             y+=100

#         else:
#             draw_text(sheet, file, "But there were no faces in that file!", x, y)
#             y+=50 # new line

# display(sheet)
























