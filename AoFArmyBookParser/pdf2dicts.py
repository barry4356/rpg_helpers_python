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
import string
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

def stripHtml(inputfile, outputfile):
    # Specialized function to cleanup the HTML output from pdfminer
    with open(inputfile, 'r', errors='ignore') as inFile:
        with open(outputfile, 'w') as outFile:
            lines = inFile.readlines()
            for line in lines:
                if not line.startswith('<'):
                    outFile.write(line)   

def formatHtml(inputfile, outputfile):
    # Specialized function to cleanup the HTML output from pdfminer
    with open(inputfile, 'r', errors='ignore') as inFile:
        with open(outputfile+'_', 'w') as outFile:
            lines = inFile.readlines()
            formattedLines = []
            for line in lines:
                line = line.replace('pts','pts\n')
                line = line.replace('&quot;','"')
                line = line.replace('\u00ef\u00ac\u20ac', 'ff')
                line = line.replace('\u00ef\u00ac\u201a', 'fl')
                outFile.write(line)
    with open(outputfile+'_', 'r', errors='ignore') as inFile:
        with open(outputfile, 'w') as outFile:
            lines = inFile.readlines()
            formattedLines = []
            for line in lines:
                if '[' in line:
                    outFile.write('\n')
                if 'quality' in line.lower():
                    line = line.replace('Replace','\nReplace')
                    line = line.replace('Upgrade','\nUpgrade')
                outFile.write(line) 

def getChunks(inputfile):
    chunks = []
    chunk = []
    with open(inputfile, 'r', errors='ignore') as inFile:
        lines = inFile.readlines()
        for line in lines:
            if line.strip():
                chunk.append(line.strip())
            else:
                chunks.append(chunk)
                chunk=[]
    return chunks
                
    

def createUnitFromChunk(lines):
    unit = {}
    for line in lines:
        if ' [' in line and ']' in line:
            unit['Name'] = line.split(' [')[0]
            unit['ModelCount'] = line.split('[')[1].split(']')[0]
        if 'Quality ' in line:
            unit['Qual'] = line.split('Quality ')[1][0]
        if 'Defense ' in line:
            unit['Def'] = line.split('Defense ')[1][0]
        if 'Tough ' in line:
            unit['Tough'] = line.split('Tough ')[1][0]
        if 'WeaponRNGATKAPSPE' in line:
            unit['Specs'] = line.split('Defense ')[1].split('WeaponRNGATKAPSPE')[0][2:]
            unit['Specs'] = unit['Specs'].replace('Tough ','').lstrip(string.digits).split(', ')
            unit['Weapons'] = weapons_from_string(line.split('WeaponRNGATKAPSPE')[1].replace('&quot;','"'))
    if 'Qual' not in unit:
        return None
    return unit

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

def weapons_from_string(weapon_string):
    weapon_perks = ['Bane', 'Fracture', 'Rending', 'Shred', 'Thrust']
    weapon_perks_scaled = ['Blast']
    weapons = []
    weapon = {}
    for perk in weapon_perks:
        weapon_string = weapon_string.replace(perk, perk+'-')
    for perk in weapon_perks_scaled:
        perk_pattern = re.escape(perk) + re.escape('(') + r"(\d+)" + re.escape(')')
        match = re.search(perk_pattern, weapon_string)
        if match:
            weapon_string = re.sub(perk_pattern, perk+'('+match.group(1)+')-', weapon_string)
    #Break out the weapons
    weaponStrAry = weapon_string.split('-')
    protoweapon = ''
    protoweapons = []
    wep_idx = 0
    for wepStr in weaponStrAry:
        protoweapon += wepStr
        attackStrPattern = re.escape('A') + r"(\d)"
        match = re.search(attackStrPattern, wepStr)
        if match:
            protoweapons.append(protoweapon)
            protoweapon = ''
            wep_idx+=1
        else:
            for perk in weapon_perks:
                if perk in wepStr:
                    protoweapons[wep_idx-1] += wepStr
                    protoweapon = ''
                    break
    if protoweapon:
        protoweapons.append(protoweapon)
        print('ERROR: ORPHAN WEAPON')
        print(protoweapon)
        
    for protoweapon in protoweapons:
        weapons.append(weapon_from_string(protoweapon, weapon_perks, weapon_perks_scaled))
    return weapons
        
def weapon_from_string(protoweapon, weapon_perks, weapon_perks_scaled):
    weapon = {}
    countPattern = r"(\d+)" + re.escape('x ')
    match = re.search(countPattern, protoweapon)
    if match:
        weapon['Count'] = int(match.group(1))
        protoweapon = re.sub(countPattern,"",protoweapon)
    attackapPattern = re.escape('A') + r"(\d)(\d)"
    match = re.search(attackapPattern, protoweapon)
    if match:
        weapon['Attacks'] = int(match.group(1))
        weapon['AP'] = int(match.group(2))
        protoweapon = re.sub(attackapPattern,"",protoweapon)
    else:
        attackPattern = re.escape('A') + r"(\d)"
        match = re.search(attackPattern, protoweapon)
        if match:
            weapon['Attacks'] = int(match.group(1))
            protoweapon = re.sub(attackPattern,"",protoweapon)
        else:
            print("ERROR: Couldn't get attack count for:")
            print(protoweapon)
    rangePattern = r"(\d+)" + re.escape('"')
    match = re.search(rangePattern, protoweapon)
    if match:
        weapon['range'] = int(match.group(1))
        protoweapon = re.sub(rangePattern, "", protoweapon)
    weapon['Specs'] = []
    for perk in weapon_perks:
        if perk in protoweapon:
            weapon['Specs'].append(perk)
            protoweapon = protoweapon.replace(perk, '')
    for perk in weapon_perks_scaled:
        if perk in protoweapon:
            perk_pattern = re.escape(perk) + re.escape('(') + r"(\d+)" + re.escape(')')
            match = re.search(perk_pattern, protoweapon)
            if match:
                weapon['Specs'].append(perk+'('+match.group(1)+')')
                protoweapon = re.sub(perk_pattern, '', protoweapon)
    weapon['Name'] = protoweapon.strip()
    return weapon


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
    units = []
    os.makedirs(outputDir, exist_ok=True)
    htmlOutfile = os.path.join(outputDir, inputfile.replace('.pdf','')+'.html')
    pdfToHtml(inputfile, htmlOutfile)
    prettyHtmlOutFile = htmlOutfile.replace('.html','_pretty.html')
    strippedHtmlOutFile = htmlOutfile.replace('.html','_stripped.html')
    formattedHtmlOutFile = htmlOutfile.replace('.html','_formatted.html')
    cleanupHtmlTags(htmlOutfile, prettyHtmlOutFile)
    stripHtml(prettyHtmlOutFile, strippedHtmlOutFile)
    formatHtml(strippedHtmlOutFile, formattedHtmlOutFile)
    chunkedHtml = getChunks(formattedHtmlOutFile)
    for chunk in chunkedHtml:
        unit = createUnitFromChunk(chunk)
        if unit:
            units.append(unit)
    return units

#TESTBED
#print(json.dumps(convertPdf('ArmyBooks\ChivKin.pdf'), indent=2))

empire = convertPdf('ArmyBooks\Empire.pdf')
chivkin = convertPdf('ArmyBooks\ChivKin.pdf')
with open('chivKin.json', 'w') as f:
    json.dump(chivkin, f, indent=2)
with open('empire.json', 'w') as f:
    json.dump(empire, f, indent=2)
#print(json.dumps(empire, indent=2))