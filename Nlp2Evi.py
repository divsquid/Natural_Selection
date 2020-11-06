# shared evi functions

# really binary combinations
tokenVerboseArg = False
tokenizerVerboseArg = False
txtVerboseArg = False

patternsResults = []

# function to print debug text when txtVerboseArg is defined as true
def wr(txt):
    if (txtVerboseArg == True):
        print(txt)
    #eif
#ef

# this functions runs through all patterns and aggregates a list of ones that are found
# it passes this information off to scoring
def processPatterns(txtTokenizer,patternsToRun,patternsScoring):
    # print out findings
    showAll = False
    patternsOn = True
    wordCount = 0
    strLine = ''
    matchPattern = None

    for ltokens in txtTokenizer.sentenceTokens:
        txtTokenizer.vectorizations = []
        txtTokenizer.words = []
        txtTokenizer.tokensFiltered = []
        strLine = ''
        matchPattern = None

        for ltoken in ltokens:
            wordCount += 1
            if (showAll == False):
                if (ltoken.valueVector != 0):
                    txtTokenizer.vectorizations.append(ltoken.valueVector)
                    txtTokenizer.words.append(ltoken.txtLower)
                    txtTokenizer.tokensFiltered.append(ltoken)
                    strLine += "{}[{}-{}]  ".format(ltoken.txtLower, ltoken.valueVector, ltoken.valueSentenceIndex)
                # eif
            else:
                txtTokenizer.vectorizations.append(ltoken.valueVector)
                txtTokenizer.words.append(ltoken.txtLower)
                txtTokenizer.tokensFiltered.append((ltoken))
                strLine += "{}[{}-{}]  ".format(ltoken.txtLower, ltoken.valueVector, ltoken.valueSentenceIndex)
            # eif
        # ew

        if (len(txtTokenizer.vectorizations) >= txtTokenizer.minSentenceLen):
            txtTokenizer.sentenceVectorizations.append(txtTokenizer.vectorizations)
            txtTokenizer.sentenceWords.append(txtTokenizer.words)
            txtTokenizer.sentenceTokensFiltered.append(txtTokenizer.tokensFiltered)

            wr(strLine)

            if (patternsOn):
                #print('')
                for entry in patternsToRun:
                    # pass off to the text tokenizer to actually process the pattern
                    matchPattern = txtTokenizer.processPatterns2(entry['pattern'], txtTokenizer.tokensFiltered)
                    # if pattern was found, add to list
                    if (matchPattern != None):
                        for patterns in matchPattern:
                            for patternEntry in patterns:
                                patternsResults.append({'patternName': entry['name'], 'patternResult': patternEntry, 'patternText': patternEntry['pattern'], 'patternDesc': entry['desc'], 'patternMatchIdx': patternEntry['matchIdx'], 'patternSentenceIdx': patternEntry['matchSentence']})
                                break
                            #efl
                        #efl
                    else:
                        patternsResults.append({'patternName': entry['name'], 'patternResult': None, 'patternText': None, 'patternDesc': None, 'patternMatchIdx': -1, 'patternSentenceIdx': -1})
                    #eif
                #efl
            #eif
        else:
            wr("Response ignored due to relevant word length: {}".format(len(txtTokenizer.vectorizations)))
            patternsResults.append({'patternName': 'sentenceIgnored', 'data': {'wordCount': len(txtTokenizer.vectorizations)}})
        #eif
    #ew

    patternsResults.append({'patternName': 'wordStats', 'data': {'wordCount': wordCount, 'sentenceCount': len(txtTokenizer.sentenceTokens)}})
    wr('Extracted {} words in {} sentence(s) from the input text.'.format(wordCount, len(txtTokenizer.sentenceTokens)))

    patternsResults.append({'patternName': 'sentenceVectorizations', 'data': txtTokenizer.sentenceVectorizations})
    patternsResults.append({'patternName': 'sentenceWords', 'data': txtTokenizer.sentenceWords})
    patternsResults.append({'patternName': 'sentenceTokensFiltered', 'data': txtTokenizer.sentenceTokensFiltered})

    finalResults = []
    maxNameLen = 0
    maxDescLen = 0
    for entry in patternsResults:
        if('patternResult' in entry and not entry['patternResult'] is None and entry['patternName'] != 'patternsConfidence'):
            finalResults.append(entry)
            if len(entry['patternName']) > maxNameLen:
                maxNameLen = len(entry['patternName'])
            #eif

            if len(entry['patternDesc']) > maxDescLen:
                maxDescLen = len(entry['patternDesc'])
            #eif
        #eif
    #efl

    finalResults = sorted(finalResults, key=lambda i: (i['patternSentenceIdx'], i['patternMatchIdx']))
    i = 0
    alen = len(finalResults)
    while i < alen:
        tmp1 = finalResults[i]
        if i + 1 < alen:
            tmp2 = finalResults[i + 1]
            if(tmp1['patternName'] == tmp2['patternName'] and tmp2['patternMatchIdx'] - tmp1['patternMatchIdx'] <= 2):
                finalResults.remove(tmp2)
                alen -= 1
                i -= 1
            elif('_No_IV' in tmp1['patternName'] and '_IV' in tmp2['patternName'] and tmp2['patternMatchIdx'] - tmp1['patternMatchIdx'] <= 2):
                finalResults.remove(tmp2)
                alen -= 1
            elif('_Supports_Hyp' in tmp1['patternName'] and '_Refutes_Hyp' in tmp2['patternName'] and tmp2['patternMatchIdx'] - tmp1['patternMatchIdx'] <= 2):
                finalResults.remove(tmp1)
                alen -= 1
            #eif
        #eif
        i += 1
    #ewl

    for entry in finalResults:
        wr('Name:{: <{width}} Idx:{: <2}-{: <2} Desc:[{: <{width2}}] Val:[{}]'.format(entry['patternName'], entry['patternMatchIdx'], entry['patternSentenceIdx'], entry['patternDesc'], entry['patternText'], width=maxNameLen, width2=maxDescLen))
    #efl
    
    # pass off to scoring function
    processResults(finalResults, patternsScoring)
#ef

# function that check the scoring patterns and aggregates the final scores
def processResults(finalResults, patternsScoring):
    finalScores = [0]
	
	# iterate through the top level of patternsScoring (e.g. CLAIM_IV, CLAIM_IVR, etc)
    for scoring in patternsScoring:
        #wr ("scoring: {}, scoring['patterns']: {}, patternScoring: {}, len(patternScoring): {}, len(scoring['patterns']): {}".format(scoring,scoring['patterns'],patternsScoring,len(patternsScoring),len(scoring['patterns'])))
        arrayOfPatterns = scoring['patterns']
        k = 0

		# iterate through each pattern set to be checked for the top level.
        for pattern in arrayOfPatterns:
            tokenStartIdx = 0
            inPattern = False
            matchIdx = -1
            matchIdxInitial = -1
            sentenceIdx = -1
            sentenceIdxInitial = -1
            entryCount = 0
            j = 0

			# iterate through each pattern in the set
            while j < len(pattern):
                patternEntry = pattern[j]
                negativeMatch = False
                negativeMatchNegated = False
                negativeMatchFound = False
                i = tokenStartIdx
                
                # iterate through each pattern found when processing the string
                while i < len(finalResults):
                    result = finalResults[i]
                    tmpBool = False
                    
                    # 0 and 1 are positive matches
                    if(patternEntry['type'] == 0):
                        if(result['patternName'] == patternEntry['value']):
                            tmpBool = True
                        else:
                            tmpBool = False
                        #eif
                    elif(patternEntry['type'] == 1):
                        if(result['patternName'] in patternEntry['value']):
                            tmpBool = True
                        else:
                            tmpBool = False
                        #eif

					# 2 and 3 are negative matches
                    elif(patternEntry['type'] == 2):
                        negativeMatch = True
                        if(result['patternName'] == patternEntry['value']):
                            wr("in type 2 pattern was found {},{}".format(result['patternName'],patternEntry['value']))
                            tmpBool = True
                        else:
                            wr("in type 2 pattern was not found {},{}".format(result['patternName'],patternEntry['value']))
                            tmpBool = False
                        #eif

                    elif(patternEntry['type'] == 3):
                        negativeMatch = True
                        if(result['patternName'] in patternEntry['value']):
                            wr("in type 3 pattern was found {},{}".format(result['patternName'],patternEntry['value']))
                            tmpBool = True
                        else:
                            wr("in type 3 pattern was found {},{}".format(result['patternName'],patternEntry['value']))
                            tmpBool = False
                        #eif

					# 4 and 5 are positive matches, sentence agnostic
                    elif(patternEntry['type'] == 4):
                        if(result['patternName'] == patternEntry['value']):
                            tmpBool = True
                        else:
                            tmpBool = False
                        #eif

                    elif(patternEntry['type'] == 5):
                        if(result['patternName'] in patternEntry['value']):
                            tmpBool = True
                        else:
                            tmpBool = False
                        #eif

                    #eif

					# if the pattern was found
                    if(tmpBool == True):
                    	# if this is the first time the pattern has been found
                        if(inPattern == False):
                            matchIdx = i
                            sentenceIdx = result['patternSentenceIdx']
                            matchIdxInitial = matchIdx
                            sentenceIdxInitial = sentenceIdx
                            inPattern = True
                            
                            # if it's a positive match, count it. otherwise, don't
                            if (not negativeMatch):
                            	entryCount += 1
                            elif (negativeMatch) :
                                negativeMatchNegated = True
                                # if this has already been scored as a negative, undo it
                                if (negativeMatchFound):
                                    entryCount -= 1
                                
						# if not types 4 or 5 and a match
                        elif(patternEntry['type'] != 4 and patternEntry['type'] != 5 and inPattern == True and matchIdx != -1 and sentenceIdxInitial == result['patternSentenceIdx']):
                            matchIdx = i
                            sentenceIdx = result['patternSentenceIdx']
                            inPattern = True

                            # if it's a positive match, count it. otherwise, don't
                            if patternEntry['type'] == 0 or patternEntry['type'] == 1:
                                entryCount += 1
                            elif (negativeMatch and not negativeMatchNegated) :
                                negativeMatchNegated = True
                                # if this has already been scored as a negative, undo it
                                if (negativeMatchFound):
                                    entryCount -= 1
                            #eif

						# if types 4 or 5 and a match
                        elif((patternEntry['type'] == 4 or patternEntry['type'] == 5) and inPattern == True and matchIdx != -1):
                            matchIdx = i
                            sentenceIdx = result['patternSentenceIdx']
                            inPattern = True

                            if patternEntry['type'] == 4 or patternEntry['type'] == 5:
                                entryCount += 1
                            #eif
                           
                        # error catch 
                        else:
                            matchIdx = -1
                            sentenceIdx = -1
                            inPattern = False
                            entryCount = 0
                            # i = matchIdxInitial
                            # j -= 1

                        #eif

                        i += 1
                        tokenStartIdx = i
                        break
                        
                    # if pattern wasn't found and it's a negative match type (2 or 3)
                    elif (negativeMatch):
                        wr("negativeMatch: {}, negativeMatchFound: {}, negativeMatchNegated: {}".format(negativeMatch,negativeMatchFound,negativeMatchNegated))
                        # if this hasn't yet been scored as a negative and also no pattern has yet been found, then score it as a negative
                        if (not negativeMatchFound and not negativeMatchNegated) :
                            negativeMatchFound = True
                            entryCount += 1
                    #eif

                    i += 1
                #ewl

                j += 1
            #ewl

            wr("inPattern: {}, entryCount: {}, len(pattern): {}".format(inPattern, entryCount,len(pattern)))
            #if(inPattern == True and entryCount == len(pattern)):
            # if every entry in the pattern was found, then apply the score
            if(entryCount == len(pattern)):
                if(pattern[0]['points'] > 0.0):
                    if(scoring['score'] <= pattern[0]['points']):
                        scoring['prevScore'] = scoring['score']
                        scoring['score'] = pattern[0]['points']
                    #eif
                else:
                    scoring['prevScore'] = scoring['score']
                    scoring['score'] = pattern[0]['points'] * -1.0
                #eif
            #eif

            k += 1
        #efl

		# if the score is greater than 0, then update the final score
        if(scoring['score'] >= 0):
            wr("{}: {}".format(scoring['kc'], scoring['score']))
            finalScores[0]+=scoring['score']
            finalScores.append(scoring['score'])
        #eif
    #efl
    # print out (return) final score
    print("%s,%s,%s,%s" % (finalScores[0], finalScores[1], finalScores[2], finalScores[3]))
#def