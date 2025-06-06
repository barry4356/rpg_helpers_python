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
import json
import os

def update_string_at_position(original_string, index, new_char):
    return original_string[:index] + new_char + original_string[index+1:]

def pdfToHtml(inputfile, outputfile):
    # Taken and modified from pdf2txt.py (included in pdfminer install)
    # Function converts PDF into a parseable HTML
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
    # Specialized function to cleanup the HTML output from pdfminer
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

def cleanupUnitNameString(inputString):
    # Specialized function to extract the unit's name from the HTML output from pdfminer
    outputString = inputString.split('[')[0]
    outputString = outputString.split('>')[-1]
    outputString = outputString.lower()
    for index, chrctr in enumerate(outputString):
        if index >= len(outputString)-1:
            continue
        if index == 0 or outputString[index-1] == ' ':
            outputString = update_string_at_position(outputString, index, chrctr.upper())
    outputString = outputString.replace(' ','').replace('\'','')
    return outputString

def numberOfModels(inputString):
    # Specialized function to extract the number of models in a unit from the HTML output from pdfminer
    numberOfModels = 0
    numberOfModels = inputString.split('[')[-1].split(']')[0]
    try:
        numberOfModels = int(numberOfModels)
    except ValueError as e:
        print(f"Error: {e}")
    return numberOfModels

def unitString(inputString):
    # Specialized function to extract the unit's details string from the HTML output from pdfminer
    index = -1
    outputString = inputString
    while index < 0:
        checkstring = inputString.split('<')[index]
        index -= 1
        if 'qua' in checkstring.lower() and 'def' in checkstring.lower():
            outputString = checkstring
            break
    index = -1
    while index < 0:
        checkstring = inputString.split('>')[index]
        index -= 1
        if 'qua' in checkstring.lower() and 'def' in checkstring.lower():
            outputString = checkstring
            break
    outputString = outputString.split('<')[0]
    return outputString

def htmlToDicts(inputfile):
    # Specialized function to convert the cleaned up HTML output from pdfminer into data dictionaries
    unit_string_dicts = []
    with open(inputfile, 'r', errors='ignore') as inFile:
        lines = inFile.readlines()
        for index, line in enumerate(lines):
            if 'qua' in line.lower() and 'def' in line.lower():
                unit_string_dict = {}
                unit_string_dict['name'] = cleanupUnitNameString(lines[index-1])
                unit_string_dict['models'] = numberOfModels(lines[index-1])
                unit_string_dict['string'] = unitString(line)
                unit_string_dicts.append(unit_string_dict)
    return unit_string_dicts
    
    
# Entry point here; this function uses the others to complete a full conversion PDF => DataDicts
def convertPdf(inputfile, outputDir='Logs'):
    os.makedirs(outputDir, exist_ok=True)
    htmlOutfile = os.path.join(outputDir, inputfile.replace('.pdf','')+'.html')
    pdfToHtml(inputfile, htmlOutfile)
    prettyHtmlOutFile = htmlOutfile.replace('.html','_pretty.html')
    cleanupHtmlTags(htmlOutfile, prettyHtmlOutFile)
    return htmlToDicts(prettyHtmlOutFile)