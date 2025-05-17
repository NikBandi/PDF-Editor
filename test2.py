import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"  # The value can be any non-empty string

from gtts import gTTS
import pygame
import time
import keyboard # pip install keyboard
import PyPDF2  # This library is to read the PDF file

file_path = open('clean_ACM_DANCE_2015_FINAL.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(file_path)
from_page = pdfReader.pages[2]

text = from_page.extract_text()

# Convert text to audio
text_to_speech = gTTS(text=text, lang='en', slow=False)
text_to_speech.save("welcome.mp3")

# Initialize mixer and play audio
pygame.mixer.init()
pygame.mixer.music.load("welcome.mp3")
pygame.mixer.music.play()

print("Playing audio...")
print("Press 'p' to pause/resume. Press 'q' to quit.")

paused = False
p_pressed = False
q_pressed = False

# Keep running while playing or paused
while pygame.mixer.music.get_busy() or paused:
    if keyboard.is_pressed('p'):
        if not p_pressed:
            if not paused:
                pygame.mixer.music.pause()
                paused = True
                print("Paused")
            else:
                pygame.mixer.music.unpause()
                paused = False
                print("Resumed")
            p_pressed = True
    else:
        p_pressed = False

    if keyboard.is_pressed('q'):
        if not q_pressed:
            pygame.mixer.music.stop()
            print("Stopped by user.")
            break
        q_pressed = True
    else:
        q_pressed = False

    time.sleep(0.1)
