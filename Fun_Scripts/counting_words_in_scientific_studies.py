'''GOAL: determine most common scientific words in a scientific study using Python.

What I need to do:

1. Get the study. DONE
2. Convert the study into a giant list of words. DONE
3. Sort that list such that the most common words, along with their frequency of use, prints in order.
4. Grab the most common 1000 words in the English language from Randal Munroe and remove them from the list
5. Edit this shit so that you can put more than one paper in at once'''

'''
Get the study:
1. Grab it and open the file
2. Extract the words in it on to a list.
'''
import PyPDF2

studyFile = r"C:\Dropbox\School\Cog Neuro\Paper\Memory Transformation & Systems Consolidation.pdf"

def getPdfStudyList(studyFile):  # Returns a huge list with all the words in the PDF file
    import re
    wordList = []  # Makes a blank list to stick the words on to
    study = open(str(studyFile), 'rb')  # Open pdf file in read binary mode
    pdfRead = PyPDF2.PdfFileReader(study)  # Makes a PDF file object out of the binary pdf file
    for i in range(pdfRead.numPages):  # Loop through each page in the PDF
        pageObj = pdfRead.getPage(i)  # inside the loop: Make an object for the page we're at
        txt = pageObj.extractText().replace('\n', '')  # Gets a messy single string of the text without newlines
        for word in txt.split(' '):  # Loop through the words in txt
            wordList.append(word)  # Appends the current word in the loop to wordList
    return [re.sub("[.,'~]", '', i) for i in wordList]  # Returns a cleaned up version of the list without periods or commas.

def sortList(wordList):  # Sort the list such that the most common words, along with their frequency of use, prints in order.
    from collections import Counter  # a module I found in stack overflow that just counts shit.import
    return Counter(wordList)

print(sortList(getPdfStudyList(studyFile)))
