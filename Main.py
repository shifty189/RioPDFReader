"""
this program will be able to open PDF files with or without encryption (AES) and display its contents, but the main feature is to produce an MP3 file 
and or read the contencts. This was orginally designed for as a study aid for a co-worker of mine
this is very much a work in progress. this repo is intended for my persinal use at the moment
"""

from gtts import gTTS
from io import BytesIO
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter.filedialog import askopenfilename


def OpenFile():
    global state
    global FilePath
    FilePath = askopenfilename()
    newWindow= tk.Toplevel(root)
    newLabel = tk.Label(newWindow, text='its working')
    newLabel.pack()
    windowSetup()

def windowSetup():
    global FilePath
    PDF = PdfReader(FilePath, False)
    Doc_Length = len(PDF.pages)
    page = PDF.pages[Doc_Length - 1]
    text = page.extract_text()
    test = gTTS(text, lang='en', tld='com')
    print(text)



# PDF = ''
FilePath = None

root = tk.Tk()


open_button = tk.Button(root, text=f'Open File', command=OpenFile)
open_button.pack()


    # mp3_fp = BytesIO()
    # test.write_to_fp(mp3_fp)
    # test.save('hello.mp3')
root.mainloop()
# print(text)
