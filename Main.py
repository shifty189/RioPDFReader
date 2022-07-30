"""
this program will be able to open PDF files with or without encryption (AES) and display its contents, but the main
feature is to produce an MP3 file and or read the contencts. This was orginally designed for as a study aid for a
co-worker of mine this is very much a work in progress. this repo is intended for my persinal use at the moment
"""

from gtts import gTTS
# from io import BytesIO
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter.filedialog import askopenfilename


def makeList():
    global pageVar
    size = pageVar.get()
    temp = []
    for i, x in enumerate(size):
        temp.append(i)
    return temp


#clear intro stuff off the window to make room for the main window
def destroyIntro():
    global open_button
    open_button.destroy()


def openFile():
    global state
    global FilePath
    global Frame
    FilePath = askopenfilename()
    # newWindow= tk.Toplevel(root)
    # newLabel = tk.Label(newWindow, text='its working')
    # newLabel.pack()
    windowSetup(Frame)

def windowSetup(frame):
    global FilePath#, pageVar, pageDropdown
    destroyIntro()
    pageVar = tk.IntVar()
    # pageVar.set(1)
    dropVar = tk.IntVar()
    # dropVar.set(1)
    PDF = PdfReader(FilePath, False)
    Doc_Length = len(PDF.pages)
    pageVar.set(Doc_Length)
    page = PDF.pages[0]
    print('page is ' + str(Doc_Length))
    # pageVar.set(8)
    text = page.extract_text()
    # test = gTTS(text, lang='en', tld='com')
    # main window Tkinter objects
    pageDropdown = tk.OptionMenu(Frame, dropVar, pageVar, command=makeList)
    displayLabel = tk.Label(frame, text=text)
    displayLabel.grid(row=0, column=0)
    pageDropdown.grid(row=1, column=0)

    print(text)




# PDF = ''
FilePath = None

root = tk.Tk()

Frame = tk.Frame()
Frame.pack()
#start up Tkinter objects
open_button = tk.Button(Frame, text=f'Open File', command=openFile)
open_button.grid(row=0, column=0)


# mp3_fp = BytesIO()
# test.write_to_fp(mp3_fp)
# test.save('hello.mp3')
root.mainloop()
# print(text)
