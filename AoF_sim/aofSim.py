import argparse
import os



def pdf2json(pdfFile, outDir):
    return







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
parser.add_argument('-o', '--outputFolder', type=str, help='Directory to export results into', required=True)
parser.add_argument('-v', '--verbose', action='store_true', help='Log everything we\'re doing to terminal and logfile', required=False)

args = parser.parse_args()

outDir = None
logFile = None
verbose = False

if args.outputFolder:
    outDir = args.outputFolder
    os.makedirs(outDir, exist_ok=True)


