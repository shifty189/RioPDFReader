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
    i = 0
    while size >= 0:
        temp.append(i)
        i += 1
        size -= 1
    return temp

def drawFrame(*args):
    global FilePath, Frame, pageVar, dropVar
    print('draw frame is running')
    PDF = PdfReader(FilePath, False)
    Doc_Length = len(PDF.pages)
    pageVar.set(Doc_Length)
    page = PDF.pages[dropVar.get()]
    text = page.extract_text()

    dropDownList = makeList()
    pageDropdown = tk.OptionMenu(Frame, dropVar, *dropDownList, command=drawFrame)
    displayLabel = tk.Label(Frame, text=text)
    displayLabel.grid(row=0, column=0)
    pageDropdown.grid(row=1, column=0)
    print(text)


def rebuildFrame(self):
    global Frame, dropVar
    for widget in Frame.winfo_children():
        widget.destroy()

    print(dropVar.get())


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
    # windowSetup(Frame)
    drawFrame()

def windowSetup(frame):
    global FilePath, pageVar, dropVar#, pageDropdown
    destroyIntro()


    # PDF = PdfReader(FilePath, False)
    # Doc_Length = len(PDF.pages)
    # pageVar.set(Doc_Length)
    # page = PDF.pages[0]
    # print('page is ' + str(Doc_Length))
    # pageVar.set(8)
    # text = page.extract_text()
    # test = gTTS(text, lang='en', tld='com')
    # main window Tkinter
    # dropDownList = makeList()
    # pageDropdown = tk.OptionMenu(Frame, dropVar, *dropDownList, command=rebuildFrame)
    # displayLabel = tk.Label(frame, text=text)
    # displayLabel.grid(row=0, column=0)
    # pageDropdown.grid(row=1, column=0)
    print('attempting to run drawFrame')
    drawFrame()



# PDF = ''
FilePath = None

root = tk.Tk()

Frame = tk.Frame()
Frame.pack()
#start up Tkinter objects
open_button = tk.Button(Frame, text=f'Open File', command=openFile)
open_button.grid(row=0, column=0)
pageVar = tk.IntVar()
dropVar = tk.IntVar()


# mp3_fp = BytesIO()
# test.write_to_fp(mp3_fp)
# test.save('hello.mp3')
root.mainloop()
# print(text)
