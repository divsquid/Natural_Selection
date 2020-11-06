import sys
import Nlp2TxtToken
import distance

class Nlp2TxtTokenizer:

    txtInput = ''
    txtId = ''
    txtVerboseArg = True
    txtWordArray = []
    patternData = None
    lvtThreshold = 0.15
    minSentenceLen = 3

    gramrComplexNegations = []
    gramrSimpleReplacements = []

    sentenceVectorizations = []
    vectorizations = []

    sentenceWords = []
    words = []

    sentenceTokens = []
    tokens = []

    sentenceTokensFiltered = []
    tokensFiltered = []

    sentenceCount = 0
    sentenceCountLast = 0

    # sets up structures to be iterated over
    def setData(self, lPatternData):
        self.patternData = lPatternData
        self.gramrComplexNegations = self.patternData.gramrComplexNegations
        self.gramrSimpleReplacements = self.patternData.gramrSimpleReplacements
        self.txtVerboseArg = self.patternData.tokenizerVerboseArg

        if(self.txtVerboseArg == True):
            print('Found {} complex negations.'.format(len(self.gramrComplexNegations)))
        #eif
    #ef

    # checks if word is with acceptable distance to be a match
    def isWordMatch(self, tword, lword, threshold):
        res = distance.nlevenshtein(lword, tword, method=2)
        if(res < threshold):
            return True
        else:
            return False
        #eif
    #ef

	# checks if word is with acceptable distance of a word within the list of tokens
    def isMatch(self, tword, arrayOfTokens, threshold):
        res = 1.0
        prevRes = 1.0
        found = False
        foundIdx = -1
        i = 0

        for token in arrayOfTokens:
            res = distance.nlevenshtein(token.txtLower, tword, method=2)
            if(res < threshold and res < prevRes):
                found = True
                prevRes = res
                foundIdx = i

                if (res == 0.0):
                    return foundIdx
                # eif
            #eif

            i += 1
        #ef

        if(found):
            return foundIdx
        else:
            return -1
        #eif
    #ef

	# checks if patterns are matched within the sentence
    def processPatterns2(self, arrayOfPatterns, arrayOfTokens):
        retPatterns = None

        # check each given pattern
        for pattern in arrayOfPatterns:
            # print("000")
            tokenStartIdx = 0
            inPattern = False
            matchIdx = -1
            matchIdxInitial = -1
            sentenceIdx = -1
            sentenceIdxInitial = -1
            entryCount = 0
            matchDistance = -1
            j = 0

			# go through each entry of the pattern
            while j < len(pattern):
                patternEntry = pattern[j]
                negativeMatch = False
                negativeMatchNegated = False
                negativeMatchFound = False
                i = tokenStartIdx
                #print("{} {} i:{} j:{}".format("111", patternEntry['pattern'], i, j))
                #print("type {}".format(patternEntry['type']))

				# check the type
                while i < len(arrayOfTokens):
                    token = arrayOfTokens[i]
                    #print("{} {} i:{} j:{}".format("222", token.txtLower, i, j))
                    tmpBool = False

					# 0 and 1 are positive matches
                    if(patternEntry['type'] == 0):
                        if(token.valueVector == patternEntry['value']):
                            tmpBool = True
                        else:
                            tmpBool = False
                        #eif
                    elif(patternEntry['type'] == 1):
                        if(token.valueVector in patternEntry['value']):
                            tmpBool = True
                        else:
                            tmpBool = False
                        #eif
                        
                    # 2 and 3 are negative matches
                    elif(patternEntry['type'] == 2):
                        negativeMatch = True
                        if (token.valueVector == patternEntry['value']):
                            tmpBool = True
                        else:
                            tmpBool = False
                        #eif
                    elif(patternEntry['type'] == 3):
                        negativeMatch = True
                        if(token.valueVector in patternEntry['value']):
                            tmpBool = True
                        else:
                            tmpBool = False
                        #eif
                    #eif

					# if the entry was found
                    if(tmpBool == True):
                    	# if this was the first find
                        if(inPattern == False):
                            #print("{} {} i:{} j:{}".format("AAA", token.txtLower, i, j))
                            patternEntry['matchDistance'] = 0
                            matchDistance = patternEntry['distance']
                            matchIdx = token.valueWordIndex
                            sentenceIdx = token.valueSentenceIndex

                            patternEntry['matchIdx'] = matchIdx
                            patternEntry['matchSentence'] = sentenceIdx
                            matchIdxInitial = matchIdx
                            sentenceIdxInitial = sentenceIdx

                            inPattern = True
                            patternEntry['inPattern'] = inPattern
                            patternEntry['word'] = token.txtLower
                            
                            # if not a negative match, count it
                            if (not negativeMatch):
                                entryCount += 1
                            # if negative, negate it
                            elif (negativeMatch) :
                                negativeMatchNegated = True
                                # if it had already been counted as a negative match, remove it
                                if (negativeMatchFound):
                                    entryCount -= 1

						# if matched and not first time
                        elif(inPattern == True and matchIdx != -1 and (matchDistance == -1 or (token.valueWordIndex - matchIdx) <= matchDistance) and sentenceIdxInitial == token.valueSentenceIndex):
                            #print("{} {} i:{} j:{}".format("BBB", token.txtLower, i, j))
                            patternEntry['matchDistance'] = (token.valueWordIndex - matchIdx)
                            matchDistance = patternEntry['distance']
                            matchIdx = token.valueWordIndex
                            sentenceIdx = token.valueSentenceIndex

                            patternEntry['matchIdx'] = matchIdx
                            patternEntry['matchSentence'] = sentenceIdx

                            inPattern = True
                            patternEntry['inPattern'] = inPattern
                            patternEntry['word'] = token.txtLower

                            # if not a negative match, count it
                            if not negativeMatch:
                                entryCount += 1
                            # if negative, negate it
                            elif (negativeMatch) :
                                negativeMatchNegated = True
                                # if it had already been counted as a negative match, remove it
                                if (negativeMatchFound):
                                    entryCount -= 1
                            #eif
                        # failure catch
                        else:
                            #print("{} {} i:{} j:{}".format("CCC", token.txtLower, i, j))
                            patternEntry['matchDistance'] = -1
                            matchIdx = -1
                            sentenceIdx = -1

                            patternEntry['matchIdx'] = matchIdx
                            patternEntry['matchSentence'] = sentenceIdx

                            inPattern = False
                            patternEntry['inPattern'] = inPattern
                            patternEntry['word'] = ''
                            entryCount = 0
                            i = matchIdxInitial
                            j = -1
                        #eif

                        i += 1
                        if(matchDistance != -1):
                            tokenStartIdx = i
                        else:
                            tokenStartIdx = 0
                        #eif

                        #print("DDD i:{} j:{} startIdx:{}".format(i, j, tokenStartIdx))
                        break
                    # if match wasn't found and it's a negative type, mark it as a negative match (unless it's been negated or already been found)
                    elif (negativeMatch):
                        if (not negativeMatchFound and not negativeMatchNegated) :
                            negativeMatchFound = True
                            entryCount += 1
                    #eif

                    #print("EEE i:{} j:{} startIdx:{}".format(i, j, tokenStartIdx))
                    i += 1
                #eif

                j += 1
            #ewl

            #print("Found {} out of {}".format(entryCount, len(pattern)))
            # if matched every entry, then add the pattern to the results
            if(entryCount == len(pattern)):
                if(retPatterns == None):
                    retPatterns = []
                #eif
                # return pattern
                retPatterns.append(pattern)
                # return retPatterns
            #eif
        #efl

        # return None
        return retPatterns
    #ef

	# toggleable write function
    def wr(self, txt):
        if (self.txtVerboseArg == True):
            print(txt)
        #eif
    #ef

	# function to process input text, replacing mistakes and splitting it up into tokens
    def processTxt(self, lTxt):
        self.txtInput = lTxt

        # apply simple replacements
        j = 0
        while j < len(self.gramrSimpleReplacements):
            lsr = self.gramrSimpleReplacements[j]
            lsrFind = lsr[0]
            lsrRepl = lsr[1]
            self.txtInput = self.txtInput.replace(lsrFind, lsrRepl)
            j += 1
        # ew

        # split input text
        self.txtWordArray = self.txtInput.replace('   ', ' ').replace('  ', ' ').replace("\n", " ").replace("\t", " ").split(' ')
        i = 0
        token = None
        self.sentenceVectorizations = []
        self.vectorizations = []

        self.sentenceWords = []
        self.words = []

        self.sentenceTokens = []
        self.tokens = []

        self.sentenceTokensFiltered = []
        self.tokensFiltered = []

        while i < len(self.txtWordArray):
            self.txtWordArray[i] = self.txtWordArray[i].strip()

            if (self.txtWordArray[i] is None or self.txtWordArray[i] == '' or len(self.txtWordArray[i]) == 0):
                del self.txtWordArray[i]

            else:
                token = Nlp2TxtToken.Nlp2TxtToken()
                token.setData(self.patternData)
                token.valueSentenceIndex = self.sentenceCount
                token.processTxt(self.txtWordArray[i], i)

                if (token.hasComma):
                    tmp = self.txtWordArray[i].split(',')
                    self.txtWordArray[i] = tmp[0] + ","
                    self.txtWordArray.insert(i, tmp[1])
                    token = Nlp2TxtToken.Nlp2TxtToken()
                    token.setData(self.patternData)
                    token.valueSentenceIndex = self.sentenceCount
                    token.processTxt(self.txtWordArray[i], i)

                elif (token.hasPeriod):
                    tmp = self.txtWordArray[i].split('.')
                    self.txtWordArray[i] = tmp[0] + "."
                    self.txtWordArray.insert(i, tmp[1])
                    token = Nlp2TxtToken.Nlp2TxtToken()
                    token.setData(self.patternData)
                    token.valueSentenceIndex = self.sentenceCount
                    token.processTxt(self.txtWordArray[i], i)
                    # self.sentenceCount += 1

                # eif

                if (token.hasEndingExclamation or token.hasEndingPeriod or token.hasEndingQuestion):
                    self.sentenceCountLast = self.sentenceCount
                    token.valueSentenceIndex = self.sentenceCount
                    self.sentenceCount += 1
                    self.tokens.append(token)

                    if (token.hasEndingQuestion == False):
                        self.sentenceTokens.append(self.tokens)
                    # eif

                    self.tokens = []

                elif (token.hasStartingExclamation or token.hasStartingPeriod or token.hasStartingQuestion):
                    self.sentenceCountLast = self.sentenceCount
                    self.sentenceCount += 1
                    token.valueSentenceIndex = self.sentenceCount

                    if (token.hasEndingQuestion == False):
                        self.sentenceTokens.append(self.tokens)
                    # eif

                    self.tokens = []
                    self.tokens.append(token)

                else:
                    token.valueSentenceIndex = self.sentenceCount
                    self.tokens.append(token)

                # eif

                i += 1
            # eif
        # ew

        # add remaining tokens
        if (len(self.tokens) > 0):
            self.sentenceTokens.append(self.tokens)
        # eif

        i = 0
        while i < len(self.sentenceTokens):
            ltokens = self.sentenceTokens[i]

            j = 0
            while j < len(self.gramrComplexNegations):
                lneg = self.gramrComplexNegations[j]
                matchIdx = -2
                matchFound = False

                k = 0
                while k < len(lneg) - 1:
                    lnegWord = lneg[k]

                    matchIdx = self.isMatch(lnegWord, ltokens, self.lvtThreshold)
                    if(matchIdx != -1):
                        if(matchIdx + 1 < len(ltokens) and k + 1 < len(lneg) - 1 and self.isWordMatch(ltokens[matchIdx + 1].txtLower, lneg[k + 1], self.lvtThreshold)):
                            # print("found negation starting at {} and ending at {} replace with {}.".format(matchIdx, matchIdx + 1, lneg[len(lneg) - 1]))

                            token = Nlp2TxtToken.Nlp2TxtToken()
                            token.setData(self.patternData)
                            token.processTxt(lneg[len(lneg) - 1], ltokens[matchIdx].valueWordIndex)
                            token.valueSentenceIndex = ltokens[matchIdx].valueSentenceIndex
                            ltokens[matchIdx] = token
                            del ltokens[matchIdx + 1]
                            matchFound = True

                            break
                        #eif
                    #eif

                    k += 1
                #ew

                j += 1
            #ew

            l = 0
            inNegation = False
            negFactor = 1
            negIdx = -1

            while l < len(ltokens):
                ltokens[l].valueWordIndex = l

                if(inNegation and ltokens[l].isNegation == False and ltokens[l].isVerb and (l - negIdx) < 4):
                    ltokens[l].valueVector *= negFactor
                    inNegation = False
                    negFactor = 1
                #eif

                if(ltokens[l].isNegation):
                    inNegation = True
                    negFactor *= -1
                    negIdx = l
                #eif

                l += 1
            #ew
            self.sentenceTokens[i] = ltokens

            i += 1
        #ew
    #ef
#ec