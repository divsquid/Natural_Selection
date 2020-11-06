from xlutils.copy import copy
from xlrd import *
from xlwt import *
import sys
import subprocess
import time

# record start time
start = time.time()

# variable definition
xlsFile = ''
xlsAnsColTxt = ''
xlsIdColTxt = ''
xlsHdrRow = 0
xlsFirstRow = 0
xlsLastRow = 0
xlsSheetIdx = 0

verbose = "true"
pyTargetScript = ''
pyMyScript = ''
pyExe = "/Users/divsiii/.pyenv/versions/3.8.1/bin/python3.8"
patternData = 'NaturalSelection49_PatternData'
#pyExe = '/Users/victor/Documents/files/pydocs_workspace/ApprendisNlp2/venv/bin/python3.6'
#/Users/divsiii/Documents/Documentation_Flower_Example/Nlp2XlsDriver.py
#"/Users/divsiii/.pyenv/versions/3.8.1/bin/python3.8"

rb = None
sh = None
wb = None
w_sheet = None

# function definition
def findColumn(lsheet, lxlsColTxt, lxlsHdrRow):
    for col in range(lsheet.ncols):
        if sh.cell(lxlsHdrRow, col).value == lxlsColTxt:
            return col
        #eif
    #efl

    return None
#ef

# cli arg intake
if(len(sys.argv) < 10):
    print('Error! Expects Arguments: [Full path to XLS file.] [Answer column header.] [Unique ID column header.] [Header row.] [First data row.] [Last data row.] [Sheet index.] [Full path to python script taking answer argument.] [Python pattern data file.]')
    exit(1)
else:
    pyMyScript = sys.argv[0];
    xlsFile = sys.argv[1]
    xlsAnsColTxt = sys.argv[2]
    xlsIdColTxt = sys.argv[3]
    xlsHdrRow = int(sys.argv[4])
    xlsFirstRow = int(sys.argv[5])
    xlsLastRow = int(sys.argv[6])
    xlsSheetIdx = int(sys.argv[7])
    pyTargetScript = sys.argv[8]
    patternData = sys.argv[9]

    print('')
    print('Found My Python Script: {}'.format(pyMyScript))
    print('Found XLS File: {}'.format(xlsFile))
    print('Found Answer Column: {}'.format(xlsAnsColTxt))
    print('Found Unique ID Column: {}'.format(xlsIdColTxt))
    print('Found Header Row: {}'.format(xlsHdrRow))
    print('Found First Data Row: {}'.format(xlsFirstRow))
    print('Found Last Data Row: {}'.format(xlsLastRow))
    print('Found Target Python Script: {}'.format(pyTargetScript))
    print('Found Pattern Data File: {}'.format(patternData))
#eif

rb = open_workbook(xlsFile)
rb.sheet_names()
sh = rb.sheet_by_index(xlsSheetIdx)
wb = copy(rb)
w_sheet = wb.get_sheet(xlsSheetIdx)

colAns = findColumn(sh, xlsAnsColTxt, xlsHdrRow)
colId = findColumn(sh, xlsIdColTxt, xlsHdrRow)

if(colAns is None):
    print('Could not find the answer column by provided header text! Exiting.')
    exit(1)
else:
    print('Found the answer column by provided header text, "{}" on line {}.'.format(xlsAnsColTxt, xlsHdrRow))
#eif

if(colId is None):
    print('Could not find the unique ID column by provided header text! Exiting.')
    exit(1)
else:
    print('Found the unique ID column by provided header text, "{}" on line {}.'.format(xlsIdColTxt, xlsHdrRow))
#eif

row = 1
rowFirst = xlsFirstRow
rowLast = xlsLastRow
myString = ''
myId = ''

if(rowLast > sh.nrows):
    rowLast = sh.nrows
#eif

for row in range(rowFirst, rowLast):
    myString = str(sh.cell_value(row, colAns))
    myId = str(sh.cell_value(row, colId))
    if(not pyTargetScript is None):
        subprocess.run([pyExe, pyTargetScript, myString, patternData, verbose, myId])
    #eif
#efl

end = time.time()
print("Nlp2XlsDriver Execution time: {}".format(end - start))