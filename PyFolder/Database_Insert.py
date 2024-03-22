from PIL import Image # from Python Imaging Library
from pytesseract import pytesseract #Python wrapper for Google's Tesseract-OCR Engine. This allows for optical character recognition (OCR) of text within images.
import sqlite3


# Defining paths to tesseract.exe 
path_to_tesseract = "/opt/homebrew/bin/tesseract"

# # # Providing the tesseract executable location to pytesseract library 
pytesseract.tesseract_cmd = path_to_tesseract 

#create an empty list to store the values of the multiplers sequentially 
multiplierList = []

#loop through elements and print out text in each image 
for i in range(0, 47581 , 390) : #2nd element is subject to change after each test
    image_path = f"/Users/ny/Documents/FLYX_PROJECT/Extracted_Frames/2024-03-21_8PM/{i}.png" #directory to image
    img = Image.open(image_path) # Opening the image & storing it in an img object 
    text = pytesseract.image_to_string(img) #Passing the image object to image_to_string() function. This function will extract the text from the image 
    
    if text == '' : 
        continue #handling empty strings

    # extract only numbers and decimals
    str_Multiplier = '' #initializing variable
    dot_found = False #handles bad timed extractions, flag to check for .

    for char in text : 
        if char.isdigit() or char == '.' : 
            str_Multiplier +=char #building each multiplier essentially 
            if char == '.':
                dot_found = True
        else : 
            # Append number to the list if it contains a dot and reset variables for next number
            if str_Multiplier and dot_found:
                float_Multiplier = float(str_Multiplier)
                multiplierList.append(float_Multiplier)
            str_Multiplier = ''
            dot_found = False

    # Check one last time after the loop in case the text ends with a number
    if str_Multiplier and dot_found:
        float_Multiplier = float(str_Multiplier)
        multiplierList.append(float_Multiplier)
    
#remove any repeats 
listOf_values = []  # Initialize an empty list to store unique elements in order
nextElement = 0

for element in multiplierList:
    if element != nextElement:
        listOf_values.append(element)  # Add the element to the unique list
    nextElement = element
print(listOf_values)

db_path = '2024-03-21_8PM.db' #name of the database
insert_query = 'INSERT INTO data (iteration, multiplier) VALUES (? ,?)'

insert_values = [(i + 1, value) for i, value in enumerate(listOf_values)]

connection = sqlite3.connect('2024-03-21_8PM.db')
cursor = connection.cursor()

cursor.executemany(insert_query , insert_values)

connection.commit()
connection.close()




