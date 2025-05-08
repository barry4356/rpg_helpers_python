import argparse
import os
import pdf2dicts
import logging
import json

from unit_class import unit
logger = logging.getLogger()
def pdf2json(pdfFile, outDir):
    dicts = pdf2dicts.convertPdf(pdfFile, outDir)
    for unitDict in dicts:
        pass
        #Load into unit objects
    return

def meleeCharge(attacker, defender, simulationCount):
    pass
    #TODO Build Results and return




### __MAIN__ ###
parser = argparse.ArgumentParser(description="Tool for deriving AoF odds and statistics through simulations")


#TODO: Implement the following:
#import list and create unit JSONs in outputdir(req)
#import unit JSONs and simulate X number of melee attacks
#
#
#
#
#import 2 lists and run full battery of statistical analyses
parser.add_argument('--pdf2json', action='store_true', help='Import PDF files and Export JSONs', required=False)
parser.add_argument('--meleeCharge', action='store_true', help='Simulate a melee charge (attack and defense)', required=False)
parser.add_argument('-o', '--outputFolder', type=str, help='Directory to export results into', required=True)
parser.add_argument('-v', '--verbose', action='store_true', help='Log everything we\'re doing to terminal and logfile', required=False)
parser.add_argument('-i', '--inputFile', type=str, help='File to import into tool', required=False)
parser.add_argument('--attackerJson', type=str, help='File to import into attacker model', required=False)
parser.add_argument('--defenderJson', type=str, help='File to import into defender model', required=False)
parser.add_argument('--simulationCount', type=int, help='Number of Simulations to run to collect data', required=False)


args = parser.parse_args()

outDir = None
inFile = None
logFile = None
verbose = False
simulationCount = 10000

if args.outputFolder:
    outDir = args.outputFolder
    os.makedirs(outDir, exist_ok=True)
if args.inputFile:
    inFile = args.inputFile
if args.simulationCount:
    simulationCount = args.simulationCount

if args.pdf2json:
    if not inFile or not outDir:
        logger.error('Input File and Output Directory Required for PDF2JSON Conversion')
        exit()
    pdf2json(inFile, outDir)

if args.meleeCharge:
    attacker = unit()
    attacker.from_json(args.attackerJson)
    defender = unit()
    defender.from_json(args.defenderJson)
    meleeCharge(attacker, defender, simulationCount)

