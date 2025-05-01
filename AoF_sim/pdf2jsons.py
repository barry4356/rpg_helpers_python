#!/usr/local/bin/python3.7
import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter
import re

def convertPdf(inputfile, outputfile):
    # debug option
    debug = 0
    # input option
    password = b''
    pagenos = set()
    maxpages = 0
    # output option
    outfile = None
    outtype = None
    imagewriter = None
    rotation = 0
    stripcontrol = False
    layoutmode = 'normal'
    encoding = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()
    #
    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFPageInterpreter.debug = debug
    #
    rsrcmgr = PDFResourceManager(caching=caching)
    outtype = 'html'
    if outputfile:
        outfp = open(outputfile, 'w', encoding=encoding)
    else:
        outfp = sys.stdout
    device = HTMLConverter(rsrcmgr, outfp, scale=scale,
                           layoutmode=layoutmode, laparams=laparams,
                           imagewriter=imagewriter, debug=debug)
    with open(inputfile, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, pagenos,
                                      maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            page.rotate = (page.rotate+rotation) % 360
            interpreter.process_page(page)
    device.close()
    outfp.close()
    return

def cleanupHtmlTags(inputfile, outputfile):
    linesToSmash = []
    with open(inputfile, 'r', errors='ignore') as inFile:
        with open(outputfile, 'w') as outFile:
            lines = inFile.readlines()
            linesFlat = []
            for line in lines:
                line = line.replace('\n','')
                linesFlat.append(line)
            for line in linesFlat:
                line = line.replace('</span>','</span>\n').replace('<br>','')
                outFile.write(line)
            #for index, line in enumerate(lines):
                #if not ('<span' in line and '</span' in line):
                    #line = line.replace('<br>','').replace('\n','')
                #outFile.write(line)
                #if index >= len(lines)-1:
                #    continue
                #if re.match(r"<br>.\n", lines[index+1]):
                #    lines[index] = lines[index].replace('<br>','').replace('\n','')
                #outFile.write(lines[index])
                

# TODO:
    # Function to read 2 lines of unit, and parse into JSON
        # cleaned html has 2 lines per unit, Qua +, Def + can be used to find valid unit lines?
#convertPdf('list.pdf', 'test.html')
cleanupHtmlTags('test.html', 'test_clean.html')