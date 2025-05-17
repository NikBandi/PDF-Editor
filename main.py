# importing the modules
import PyPDF2  # This library is to read the PDF file
import pyttsx3  # Thie library is for Text to speech conversion 

engine = pyttsx3.init() # initializing the pyttsx3 engine

# set the path for the PDF file
# we read as bytes since most PDF files are a binary file and not a solid text file.
path = open('clean_ACM_DANCE_2015_FINAL.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(path)
from_page = pdfReader.pages[2]

text = from_page.extract_text()


# Ser the voice and rate
voices = engine.getProperty('voices')       # getting details of current voice
engine.setProperty('voice', voices[1].id)   # 0 - male || 1 - female
engine.setProperty('rate', 145)            # Speed percent (can go over 100)

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
