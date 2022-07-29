"""
this program will be able to open PDF files with or without encryption (AES) and display its contents, but the main feature is to produce an MP3 file 
and or read the contencts. This was orginally designed for as a study aid for a co-worker of mine
this is very much a work in progress. this repo is intended for my persinal use at the moment
"""

from gtts import gTTS
from io import BytesIO
from PyPDF2 import PdfReader

PDF = PdfReader("audit.pdf", False)
page = PDF.pages[0]
text = page.extract_text()

test = gTTS(text, lang='en', tld='com') 

mp3_fp = BytesIO()
test.write_to_fp(mp3_fp)
test.save('hello.mp3')

print(text)
