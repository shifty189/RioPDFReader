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


def pageUP():
    global dropVar
    test = dropVar.get() + 1
    print('test is equil to ' + str(test))
    dropVar.set(test)
    rebuildFrame()


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
    # print('draw frame is running')
    PDF = PdfReader(FilePath, False)
    Doc_Length = len(PDF.pages)
    pageVar.set(Doc_Length)
    page = PDF.pages[dropVar.get()]
    text = page.extract_text()

    dropDownList = makeList()
    pageDropdown = tk.OptionMenu(Frame, dropVar, *dropDownList, command=drawFrame)
    displayLabel = tk.Label(Frame, text=text)
    displayLabel.grid(row=1, column=0)
    pageDropdown.grid(row=0, column=0)
    nextPageButton = tk.Button(Frame, text=">", command=pageUP)
    nextPageButton.grid(row=0, column=1)
    lastPageButton = tk.Button(Frame, text=">")
    lastPageButton.grid(row=0, column=1)
    print(text)


def rebuildFrame():
    global Frame, dropVar, open_button
    for widget in Frame.winfo_children():
        widget.destroy()
    open_button.destroy()
    drawFrame()

    # print(dropVar.get())


def openFile():
    global FilePath
    FilePath = askopenfilename(filetypes= [("PDF files","*.pdf"), ("PDF files","*.PDF")])
    rebuildFrame()



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
