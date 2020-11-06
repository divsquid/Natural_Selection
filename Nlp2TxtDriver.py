import sys
import Nlp2TxtTokenizer
import importlib
import time

# record start time
start = time.time()

# variable definition
txtInput = ''
txtId = ''
txtPatternData = None
txtPatternDataFile = ''
txtVerboseArg = False
pyMyScript = ''
txtTokenizer = None

# patternsResults = []

# function definitions
def convertToBool(b):
    if(b is None):
        return False
    else:
        b = b.lower()
        if(b == "false"):
            return False
        elif(b == "true"):
            return True
       #eif
    #eif
#ef

def wr(txt):
    if (txtVerboseArg == True):
        print(txt)
    #eif
#ef

# cli arg intake
if(len(sys.argv) < 1):
    print('Error! Expects Arguments: [Text to process.] [Complex negations file.]')
    exit(1)
else:
    pyMyScript = sys.argv[0]
    txtInput = sys.argv[1]
    txtPatternDataFile = sys.argv[2]
    txtPatternData = __import__(txtPatternDataFile)

    if(len(sys.argv) > 3):
        txtVerboseArg = convertToBool(sys.argv[3])
    #eif

    if(len(sys.argv) > 4):
        txtId = sys.argv[4]
    #eif

    if(txtVerboseArg):
        print('')
        print('---------------------------------------------')
        print('Found My Python Script: {}'.format(pyMyScript))
        print('Found Execution File: {}'.format(txtPatternData))

        if(not txtPatternData is None):
            print('Found Execution File Test (gramrComplexNegations Count): {}'.format(len(txtPatternData.gramrComplexNegations)))
        #eif

        print('Found Verbose Arg: {}'.format(txtVerboseArg))
        print('Found Input ID: {}'.format(txtId))
        print('Found Input Text: {}'.format(txtInput))
        print('+++++++++++++++++++++++++++++++++++++++++++++')
    #eif

    txtTokenizer = Nlp2TxtTokenizer.Nlp2TxtTokenizer()
    txtTokenizer.txtId = txtId
    txtTokenizer.txtVerboseArg = txtVerboseArg
    txtTokenizer.setData(txtPatternData)
    txtTokenizer.processTxt(txtInput)
    txtPatternData.processPatterns(txtTokenizer)
    #print('---------------------------------------------')
#eif

end = time.time()
#print("Nlp2TxtDriver Execution time: {}".format(end - start))
