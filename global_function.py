from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fpdf import FPDF
import time
import os
import secrets
import string
import pyautogui

# Set up the Chrome webdriver
driver = webdriver.Chrome()

def random_string():
    alphabet = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(alphabet) for i in range(10))
    return random_string

def wait(waktu):
    time.sleep(waktu)

def open_browser(url):    
    #maximize the window size 
    driver.maximize_window()
    
    driver.get(url)

    driver.implicitly_wait(10)
    return driver

def convert_pdf(images,word,namePDF):
    pdf = FPDF()

    # Register a font with Unicode support
    pdf.set_font('Times', '', 12)


    for i in range(len(images)):
        # Add a new page to the document
        pdf.add_page()
        # Load the PNG image into the PDF document
        pdf.image('temporary_screenshoot/' + images[i], x=10, y=10, w=180, h=100)
        pdf.cell(0, 215, word[i])


    nameFile = namePDF+'.pdf'

    # Save the PDF document to a file
    pdf.output('report/'+nameFile, 'F')

def remove_png():
    # directory containing the PNG files
    directory = "temporary_screenshoot/"

    # loop through each file in the directory
    for filename in os.listdir(directory):
        # check if the file is a PNG file
        if filename.endswith(".png"):
            # construct the full file path
            filepath = os.path.join(directory, filename)
            # delete the file
            os.remove(filepath)

def call_screenshoot(saveWord,saveImage,word):
    screenshot = pyautogui.screenshot()
    name_hash_ss = random_string()
    fix_name_temporary = name_hash_ss+'.png'
    screenshot.save('temporary_screenshoot/' +fix_name_temporary)
    inputWord = saveWord.append(word)
    inputImage = saveImage.append(fix_name_temporary)
    return inputWord, inputImage

def end(saveImage,saveWord,fileName):
    convert_pdf(saveImage,saveWord,fileName)
    remove_png()
