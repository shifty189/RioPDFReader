"""
this program will be able to open PDF files with or without encryption (AES) and display its contents, but the main
feature is to produce an MP3 file and or read the contencts. This was orginally designed for as a study aid for a
co-worker of mine this is very much a work in progress. this repo is intended for my persinal use at the moment
"""

import os
from gtts import gTTS
from io import BytesIO
from PyPDF2 import PdfReader
from playsound import playsound
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename
import threading


def changeVoice(x):
    global voice
    voice = x


def endProgram():
    quit()


def first_thread(text, root):
    t1=threading.Thread(target=lambda: readPage(text, root))
    t1.start()


def checkGo():
    global GO
    GO = False
    print('stop pressed')


def readPage(text, root):
    global GO
    GO = True
    print(text)
    splitText = text.splitlines()
    print(len(splitText))
    for line in splitText:
        # print(line)
        if GO:
            try:
                tts = gTTS(text=line, lang='en', tld=voice)
                good = True
            except AssertionError:
                good = False
            if good:
                try:
                    tts.save('test.mp3')
                except AssertionError:
                    good = False
                if good:
                    try:
                        playsound('test.mp3')
                    except:
                        pass
            else:
                pass

def firstPage():
    global dropVar, pageVar
    print(pageVar.get())
    dropVar.set(0)
    rebuildFrame()


def lastPage():
    global dropVar, pageVar
    print(pageVar.get())
    dropVar.set(pageVar.get() - 1)
    rebuildFrame()


def pageUP():
    global dropVar, pageVar
    if dropVar.get() >= pageVar.get() - 1:
        test = dropVar.get()
    else:
        test = dropVar.get() + 1
    print('test is equil to ' + str(test))
    dropVar.set(test)
    rebuildFrame()


def pageDOWN():
    global dropVar, pageVar
    if dropVar.get() > 0 :
        test = dropVar.get() - 1
    else:
        test = dropVar.get()
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
    global FilePath, Frame, pageVar, dropVar, readButton

    buttonFrame = tk.Frame(Frame)
    textFrame = tk.Frame(Frame)
    buttonFrame.grid(row=0, column=0)
    textFrame.grid(row=1, column=0)

    PDF = PdfReader(FilePath, False)
    Doc_Length = len(PDF.pages)
    pageVar.set(Doc_Length)
    page = PDF.pages[dropVar.get()]
    text = page.extract_text()

    dropDownList = makeList()


    readButton = tk.Button(buttonFrame, text="Read Page", command=lambda: first_thread(text, root))
    readButton.grid(row=0, column=2)
    stopButton = tk.Button(buttonFrame, text="Stop Reading", command=checkGo)
    stopButton.grid(row=0, column=3)

    firstPageButton = tk.Button(buttonFrame, text="<<", command=firstPage)
    firstPageButton.grid(row=1, column=0)
    prevPageButton = tk.Button(buttonFrame, text="<", command=pageDOWN)
    prevPageButton.grid(row=1, column=1)
    pageDropdown = tk.OptionMenu(buttonFrame, dropVar, *dropDownList, command=rebuildFrame)
    pageDropdown.grid(row=1, column=2)
    nextPageButton = tk.Button(buttonFrame, text=">", command=pageUP)
    nextPageButton.grid(row=1, column=3)
    lastPageButton = tk.Button(buttonFrame, text=">>", command=lastPage)
    lastPageButton.grid(row=1, column=4)

    displayTextBox = ScrolledText(textFrame, width=75, height=40, wrap=tk.WORD)
    displayTextBox.insert(tk.INSERT, text)
    displayTextBox.configure(state="disabled")
    displayTextBox.grid(row=2, column=0)
    print(text)


def rebuildFrame(*args):
    global Frame, dropVar, open_button
    for widget in Frame.winfo_children():
        widget.destroy()
    open_button.destroy()
    drawFrame()


def openFile():
    global FilePath
    FilePath = askopenfilename(filetypes= [("PDF files","*.pdf"), ("PDF files","*.PDF")])
    rebuildFrame()


FilePath = None
GO = True
voice = 'com'

root = tk.Tk()
#create menu bar File starts here
menuBar = tk.Menu(root)
fileMenuBar = tk.Menu(menuBar)
fileMenuBar.add_command(label='Exit', command=endProgram)
fileMenuBar.add_command(label="Open", command=openFile)
menuBar.add_cascade(label='File', menu=fileMenuBar)
#Add voice manu to the menu bar
voiceMenuBar = tk.Menu(menuBar)
voiceMenuBar.add_command(label='US', command=lambda: changeVoice('com'))
voiceMenuBar.add_command(label='UK', command=lambda: changeVoice('co.uk'))
voiceMenuBar.add_command(label='Australian', command=lambda: changeVoice('com.au'))
voiceMenuBar.add_command(label='Canadian', command=lambda: changeVoice('ca'))
voiceMenuBar.add_command(label='Indian', command=lambda: changeVoice('co.in'))
menuBar.add_cascade(label='voice', menu=voiceMenuBar)

Frame = tk.Frame()
Frame.pack()
#start up Tkinter objects
open_button = tk.Button(Frame, text=f'Open File', command=openFile)
open_button.grid(row=0, column=0)

pageVar = tk.IntVar()
dropVar = tk.IntVar()

root.config(menu=menuBar)
root.mainloop()
os.remove("test.mp3")
