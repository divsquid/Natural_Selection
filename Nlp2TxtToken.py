import distance


class Nlp2TxtToken:

    txtOrig = ''
    txtLower = ''
    txtVerboseArg = False
    patternData = None

    vectorLookups = {
                        # pronouns
                        'i': 0, #1,
                        'me': 0, #2,
                        'he': 0, #3,
                        'she': 0, #4,
                        'herself': 0, #5,
                        'himself': 0, #6,
                        'you': 0, #7,
                        'u': 0,
                        'it': 0, #8,
                        'that': 0, #9,
                        'they': 0, #10,
                        'each': 0, #11,
                        'few': 0, #12,
                        'many': 0, #13,
                        'who': 0, #14,
                        'whoever': 0, #15,
                        'whose': 0, #16,
                        'someone': 0, #17,
                        'everybody': 0, #18,

                        # prepositions
                        'in': 100,
                        'near': 0, #101,
                        'beside': 0, #102,
                        'about': 0, #103,
                        'after': 0, #104,
                        'besides': 0, #105,
                        'on': 100,
                        'at': 0, #107,
                        'of': 0, #108,
                        'for': 100,
                        'to': 100,
                        'inside': 100,
                        'from': 100,
                        'into': 100,

                        # articles
                        'the': 200,
                        'a': 200,
                        'an': 200,
                        'that': 200,

                        # conditionals
                        'if': 300,
                        'unless': 300,
                        'when': 300,

                        # conjunctions
                        'for': 0, #400,
                        'and': 0, #401,
                        'nor': 0, #402,
                        'but': 0, #403,
                        'or': 0, #404,
                        'yet': 0, #405,
                        'so': 0, #406,

                        #negations
                        'neither': 500,
                        'not': 500,
                        "don't": 500,
                        "doesn't": 500,
                        "isn't": 500,
                        "no": 500,
                        "didn't": 500,

                        # nouns
                        'plant': 600,
                        'palnt': 600,
                        'plants': 600,
                        "plant's": 600,
                        'water': 600,
                        'data': 600,
                        'flower': 600,
                        'flour': 600,
                        "flower's": 600,
                        'soil': 600,

                        'pedal': 601,
                        'petal': 601,
                        'patel': 601,
                        'petals': 601,
                        'patels': 601,
                        'pedles': 601,

                        'dye': 603,
                        'die': 603,

                        'salt': 604,
                        'stalt': 604,
                        'sat': 604,

                        'redness': 605,
                        'sugar': 606,
                        'amount': 607,

                        'one': 2001,
                        '1': 2001,
                        'two': 2002,
                        '2': 2002,
                        'three': 2003,
                        '3': 2003,
                        'four': 2004,
                        '4': 2004,
                        'five': 2005,
                        '5': 2005,
                        'six': 2006,
                        '6': 2006,

                        # adjectives
                        'more': 700,
                        'positive': 700,
                        'faster': 700,

                        'less': 701,
                        'negative': 701,
                        'slower': 701,

                        'red': 702,
                        'yellow': 703,
                        'same': 704,

                        #verbs
                        'use': 804,
                        'put': 804,
                        'putting': 804,
                        'added': 804,
                        'adding': 804,
                        'add': 804,
                        'work': 804,

                        'increased': 800,
                        'increase': 800,
                        'increasing': 800,
                        'increases': 800,

                        'decreased': 801,
                        'decrease': 801,
                        'decreasing': 801,
                        'decreases': 801,

                        'removed': 802,
                        'removes': 802,
                        'remove': 802,
                        'removing': 802,

                        'kill': 806,
                        'killed': 806,
                        'fall': 806,
                        'loss': 806,
                        'looses': 806,
                        'lose': 806,
                        'loose': 806,
                        'lost': 806,
                        'drops': 806,

                        'stay': 803,
                        'do': 0,

                        'vary': 805,
                        'change': 805,
                        'alter': 805,
                        'adjust': 805,

                        #adverbs
                        'rapidly': 900,
                        'greatly': 900,
                        'slowly': 901,
                    }

    gramrPronouns = ['i', 'me', 'he', 'she', 'herself', 'himself', 'you', 'it', 'that', 'they', 'each', 'few', 'many', 'who', 'whoever', 'whose', 'someone', 'everybody']
    gramrPrepositions = ['in', 'near', 'beside', 'about', 'after', 'besides', 'on', 'at', 'of', 'for', 'into']
    gramrArticles = ['the', 'a', 'an', 'that']
    gramrConditionals = ['if', 'unless', 'when']
    gramrConjunctions = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
    gramrNegations = ['neither', 'not', "don't", "doesn't", "isn't", "won't", 'no', "didn't"]

    # activity specific customization
    gramrNouns = [
                    'plant', 'palnt', 'plants', "plant's", 'water', 'data', 'flower', 'flour', "flower's", 'soil',
                    'pedal', 'petal', 'patel', 'petals', 'patels', 'pedles',
                    'dye', 'die',
                    'salt', 'stalt', 'sat',
                    'redness', 'sugar', 'amount',
                    'one', '1', 'two', '2', 'three', '3', 'four', '4', 'five', '5', 'six', '6'
                ]

    gramrAdjectives = [
                    'more', 'positive', 'faster',
                    'less', 'negative', 'slower',
                    'red', 'yellow', 'same'
                ]

    gramrVerbs = [
                    'use', 'put', 'putting', 'added', 'adding', 'add',
                    'increased', 'increase', 'increasing', 'increases',
                    'decreased', 'decrease', 'decreasing', 'decreases',
                    'removed', 'removes', 'remove', 'removing',
                    'kill', 'killed', 'fall', 'loss', 'looses', 'loose', 'lose', 'lost', 'drops',
                    'stay', 'do', 'work',
                    'vary', 'change', 'alter', 'adjust'
                ]

    gramrAdverbs = []

    lvtThreshold = 0.22
    lvtUseThreshold = 4
    lvtTxtMatch = 'N/A'

    # special chars
    hasStartingPeriod = False
    hasEndingPeriod = False
    hasPeriod = False
    wordIdxPeriod = 0

    hasStartingQuestion = False
    hasEndingQuestion = False
    hasQuestion = False
    wordIdxQuestion = 0

    hasStartingExclamation = False
    hasEndingExclamation = False
    hasExclamation = False
    wordIdxExclamation = 0

    hasStartingComma = False
    hasEndingComma = False
    hasComma = False
    wordIdxComma = 0

    hasSpellingConfidence = 1.0
    hasStartingCaps = False
    hasEndingCaps = False
    hasCaps = False
    wordIdxCaps = 0

    hasStartingDoubleQuote = False
    hasEndingDoubleQuote = False
    hasDoubleQuote = False
    wordIdxDoubleQuote = 0

    hasStartingSingleQuote = False
    hasEndingSingleQuote = False
    hasSingleQuote = False
    wordIdxSingleQuote = 0

    # grammar detection
    isContraction = False
    isNumber = False
    isPronoun = False
    isNoun = False
    isVerb = False
    isAdverb = False
    isAdjective = False
    isConjunction = False
    isPreposition = False
    isMisspelled = False
    isQuestion = False
    isNegation = False
    isArticle = False
    isNegation = False

    # values
    valueVector = 0
    valueImportance = 1.0
    valueWordIndex = 0
    valueSentenceIndex = 0
    valueLvtScore = 2.0

    def setData(self, lPatternData):
        self.patternData = lPatternData
        self.vectorLookups = self.patternData.vectorLookups
        self.gramrPronouns = self.patternData.gramrPronouns
        self.gramrPrepositions = self.patternData.gramrPrepositions
        self.gramrArticles = self.patternData.gramrArticles
        self.gramrConditionals = self.patternData.gramrConditionals
        self.gramrConjunctions = self.patternData.gramrConjunctions
        self.gramrNegations = self.patternData.gramrNegations
        self.gramrNouns = self.patternData.gramrNouns
        self.gramrAdjectives = self.patternData.gramrAdjectives
        self.gramrVerbs = self.patternData.gramrVerbs
        self.gramrAdverbs = self.patternData.gramrAdverbs
        self.txtVerboseArg = self.patternData.tokenVerboseArg

        if (self.txtVerboseArg == True):
            print('Found {} adverbs.'.format(len(self.gramrAdverbs)))
        # eif
    #ef

    def wr(self, txt):
        if (self.txtVerboseArg == True):
            print(txt)
        #eif
    #ef

    def processTxt(self, lTxt, lWordIdx):
        self.txtOrig = lTxt
        self.txtLower = lTxt.lower()
        self.valueWordIndex = lWordIdx
        self.valueSentenceIndex = 0

        if(len(self.txtOrig) == 0):
            return
        #eif

        # exclamation detection
        self.wordIdxExclamation = -1
        if(self.txtOrig[0] == '!'):
            self.hasStartingExclamation = True
            self.wordIdxExclamation = 0
            self.txtLower = self.txtLower.replace('!', '')
        else:
            self.hasStartingExclamation = False
        #eif

        if(self.txtOrig[-1] == '!'):
            self.hasEndingExclamation = True
            self.wordIdxExclamation = len(self.txtOrig) - 1
            self.txtLower = self.txtLower.replace('!', '')
        else:
            self.hasEndingExclamation = False
        #eif

        if('!' in self.txtOrig[1:-1]):
            self.hasExclamation = True
        else:
            self.hasExclamation = False
        #eif

        if(self.hasExclamation):
            found = False
            i = 1
            for char in self.txtOrig[1:-1]:
                if(char == "!"):
                    self.wordIdxExclamation = i
                    found = True
                    break
                #eif
                i += 1
            #eif
        #eif

        # question detection
        self.wordIdxQuestion = -1
        if(self.txtOrig[0] == '?'):
            self.hasStartingQuestion = True
            self.wordIdxQuestion = 0
            self.txtLower = self.txtLower.replace('?', '')
        else:
            self.hasStartingQuestion = False
        #eif

        if(self.txtOrig[-1] == '?'):
            self.hasEndingQuestion = True
            self.wordIdxQuestion = len(self.txtOrig) - 1
            self.txtLower = self.txtLower.replace('?', '')
        else:
            self.hasEndingQuestion = False
        #eif

        if('?' in self.txtOrig[1:-1]):
            self.hasQuestion = True
        else:
            self.hasQuestion = False
        #eif

        if(self.hasQuestion):
            found = False
            i = 1
            for char in self.txtOrig[1:-1]:
                if(char == "?"):
                    self.wordIdxQuestion = i
                    found = True
                    break
                #eif
                i += 1
            #eif
        #eif

        # dot detection
        self.wordIdxPeriod = -1
        if(self.txtOrig[0] == '.'):
            self.hasStartingPeriod = True
            self.wordIdxPeriod = 0
            self.txtLower = self.txtLower.replace('.', '')
        else:
            self.hasStartingPeriod = False
        #eif

        if(self.txtOrig[-1] == '.'):
            self.hasEndingPeriod = True
            self.wordIdxPeriod = len(self.txtOrig) - 1
            self.txtLower = self.txtLower.replace('.', '')
        else:
            self.hasEndingPeriod = False
        #eif

        if('.' in self.txtOrig[1:-1]):
            self.hasPeriod = True
        else:
            self.hasPeriod = False
        #eif

        if(self.hasPeriod):
            found = False
            i = 1
            for char in self.txtOrig[1:-1]:
                if(char == "."):
                    self.wordIdxPeriod = i
                    found = True
                    break
                #eif
                i += 1
            #eif
        #eif

        # comma detection
        self.wordIdxComma = -1
        if(self.txtOrig[0] == ','):
            self.hasStartingComma = True
            self.wordIdxComma = 0
            self.txtLower = self.txtLower.replace(',', '')
        else:
            self.hasStartingComma = False
        #eif

        if(self.txtOrig[-1] == ','):
            self.hasEndingComma = True
            self.wordIdxComma = len(self.txtOrig) - 1
            self.txtLower = self.txtLower.replace(',', '')
        else:
            self.hasEndingComma = False
        #eif

        if(',' in self.txtOrig[1:-1]):
            self.hasComma = True
        else:
            self.hasComma = False
        #eif

        if(self.hasComma):
            found = False
            i = 1
            for char in self.txtOrig[1:-1]:
                if(char == ","):
                    self.wordIdxComma = i
                    found = True
                    break
                #eif
                i += 1
            #eif
        #eif

        # single quote detection
        self.wordIdxSingleQuote = -1
        if(self.txtOrig[0] == "'"):
            self.hasStartingSingleQuote = True
            self.wordIdxSingleQuote = 0
            self.txtLower = self.txtLower.replace("'", '')
        else:
            self.hasStartingSingleQuote = False
        #eif

        if(self.txtOrig[-1] == "'"):
            self.hasEndingSingleQuote = True
            self.wordIdxSingleQuote = len(self.txtOrig) - 1
            self.txtLower = self.txtLower.replace("'", '')
        else:
            self.hasEndingSingleQuote = False
        #eif

        if("'" in self.txtOrig[1:-1]):
            self.hasSingleQuote = True
        else:
            self.hasSingleQuote = False
        #eif

        if(self.hasSingleQuote):
            found = False
            i = 1
            for char in self.txtOrig[1:-1]:
                if(char == "'"):
                    self.wordIdxSingleQuote = i
                    found = True
                    break
                #eif
                i += 1
            #eif
        #eif

        # double quote detection
        self.wordIdxDoubleQuote = -1
        if(self.txtOrig[0] == '"'):
            self.hasStartingDoubleQuote = True
            self.wordIdxDoubleQuote = 0
            self.txtLower = self.txtLower.replace('"', '')
        else:
            self.hasStartingDoubleQuote = False
        #eif

        if(self.txtOrig[-1] == '"'):
            self.hasEndingDoubleQuote = True
            self.wordIdxDoubleQuote = len(self.txtOrig) - 1
            self.txtLower = self.txtLower.replace('"', '')
        else:
            self.hasEndingDoubleQuote = False
        #eif

        if('"' in self.txtOrig[1:-1]):
            self.hasDoubleQuote = True
        else:
            self.hasDoubleQuote = False
        #eif

        if(self.hasDoubleQuote):
            found = False
            i = 1
            for char in self.txtOrig[1:-1]:
                if(char == '"'):
                    self.wordIdxDoubleQuote = i
                    found = True
                    break
                #eif
                i += 1
            #eif
        #eif

        # caps detection
        self.wordIdxCaps = -1
        if(self.txtOrig[0].isupper()):
            self.hasStartingCaps = True
            self.wordIdxCaps = 0
        else:
            self.hasStartingCaps = False
        #eif

        if(self.txtOrig[-1].isupper()):
            self.hasEndingCaps = True
            self.wordIdxCaps = len(self.txtOrig) - 1
        else:
            self.hasEndingCaps = False
        #eif

        self.hasCaps = False
        found = False
        i = 1
        for char in self.txtOrig[1:-1]:
            if(char.isupper()):
                self.hasCaps = True
                self.wordIdxCaps = i
                found = True
                break
            #eif
            i += 1
        #eif

        # numbers
        self.isNumber = self.isTxtNumber(self.txtOrig)

        # questions
        self.isQuestion = False
        if(self.valueWordIndex == 0):
            if(self.txtLower == "who"):
               self.isQuestion = True
            #eif

            if(self.txtLower == "why"):
               self.isQuestion = True
            #eif

            if(self.txtLower == "where"):
               self.isQuestion = True
            #eif
        #eif

        # grammar matching
        self.valueLvtScore = 1.0
        prevValueLvtScore = 1.0
        tmpBool = False

        self.isPronoun = False
        if(len(self.txtLower) >= self.lvtUseThreshold):
            prevValueLvtScore = self.valueLvtScore
            tmpBool = self.isMatch(self.txtLower, self.gramrPronouns, self.lvtThreshold)
            if(self.valueLvtScore < prevValueLvtScore):
                self.isPronoun = tmpBool
            #eif
        else:
            if(self.txtLower in self.gramrPronouns):
                self.valueLvtScore = 0.0
                self.lvtTxtMatch = self.txtLower
                self.isPronoun = True
            #eif
        #eif

        self.isPreposition = False
        if(self.valueLvtScore > 0.0):
            if(len(self.txtLower) >= self.lvtUseThreshold):
                prevValueLvtScore = self.valueLvtScore
                tmpBool = self.isMatch(self.txtLower, self.gramrPrepositions, self.lvtThreshold)
                if(self.valueLvtScore < prevValueLvtScore):
                    self.isPreposition = tmpBool
                #eif
            else:
                if (self.txtLower in self.gramrPrepositions):
                    self.valueLvtScore = 0.0
                    self.lvtTxtMatch = self.txtLower
                    self.isPreposition = True
                # eif
            #eif
        #eif

        self.isArticle = False
        if (self.valueLvtScore > 0.0):
            if(len(self.txtLower) >= self.lvtUseThreshold):
                prevValueLvtScore = self.valueLvtScore
                tmpBool = self.isMatch(self.txtLower, self.gramrArticles, self.lvtThreshold)
                if(self.valueLvtScore < prevValueLvtScore):
                    self.isArticle = tmpBool
                #eif
            else:
                if (self.txtLower in self.gramrArticles):
                    self.valueLvtScore = 0.0
                    self.lvtTxtMatch = self.txtLower
                    self.isArticle = True
                # eif
            #eif
        #eif

        self.isConditional = False
        if (self.valueLvtScore > 0.0):
            if(len(self.txtLower) >= self.lvtUseThreshold):
                prevValueLvtScore = self.valueLvtScore
                tmpBool = self.isMatch(self.txtLower, self.gramrConditionals, self.lvtThreshold)
                if (self.valueLvtScore < prevValueLvtScore):
                    self.isConditional = tmpBool
                #eif
            else:
                if (self.txtLower in self.gramrConditionals):
                    self.valueLvtScore = 0.0
                    self.lvtTxtMatch = self.txtLower
                    self.isConditional = True
                # eif
            #eif
        #eif

        self.isConjunction = False
        if (self.valueLvtScore > 0.0):
            if(len(self.txtLower) >= self.lvtUseThreshold):
                prevValueLvtScore = self.valueLvtScore
                tmpBool = self.isMatch(self.txtLower, self.gramrConjunctions, self.lvtThreshold)
                if (self.valueLvtScore < prevValueLvtScore):
                    self.isConditional = tmpBool
                #eif
            else:
                if (self.txtLower in self.gramrConjunctions):
                    self.valueLvtScore = 0.0
                    self.lvtTxtMatch = self.txtLower
                    self.isConjunction = True
                # eif
            #eif
        #eif

        self.isVerb = False
        if (self.valueLvtScore > 0.0):
            if(len(self.txtLower) >= self.lvtUseThreshold):
                prevValueLvtScore = self.valueLvtScore
                tmpBool = self.isMatch(self.txtLower, self.gramrVerbs, self.lvtThreshold)
                if (self.valueLvtScore < prevValueLvtScore):
                    self.isVerb = tmpBool
                #eif
            else:
                if (self.txtLower in self.gramrVerbs):
                    self.valueLvtScore = 0.0
                    self.lvtTxtMatch = self.txtLower
                    self.isVerb = True
                # eif
            #eif
        #eif

        self.isNoun = False
        if (self.valueLvtScore > 0.0):
            if(len(self.txtLower) >= self.lvtUseThreshold):
                prevValueLvtScore = self.valueLvtScore
                tmpBool = self.isMatch(self.txtLower, self.gramrNouns, self.lvtThreshold)
                if (self.valueLvtScore < prevValueLvtScore):
                    self.isNoun = tmpBool
                #eif
            else:
                if (self.txtLower in self.gramrNouns):
                    self.valueLvtScore = 0.0
                    self.lvtTxtMatch = self.txtLower
                    self.isNoun = True
                # eif
            #eif
        #eif

        self.isAdjective = False
        if (self.valueLvtScore > 0.0):
            if(len(self.txtLower) >= self.lvtUseThreshold):
                prevValueLvtScore = self.valueLvtScore
                tmpBool = self.isMatch(self.txtLower, self.gramrAdjectives, self.lvtThreshold)
                if (self.valueLvtScore < prevValueLvtScore):
                    self.isAdjective = tmpBool
                #eif
            else:
                if (self.txtLower in self.gramrAdjectives):
                    self.valueLvtScore = 0.0
                    self.lvtTxtMatch = self.txtLower
                    self.isAdjective = True
                # eif
            #eif
        #eif

        self.isAdverb = False
        if (self.valueLvtScore > 0.0):
            if(len(self.txtLower) >= self.lvtUseThreshold):
                prevValueLvtScore = self.valueLvtScore
                tmpBool = self.isMatch(self.txtLower, self.gramrAdverbs, self.lvtThreshold)
                if (self.valueLvtScore < prevValueLvtScore):
                    self.isAdverb = tmpBool
                #eif
            else:
                if (self.txtLower in self.gramrAdverbs):
                    self.valueLvtScore = 0.0
                    self.lvtTxtMatch = self.txtLower
                    self.isAdverb = True
                # eif
            #eif
        #eif

        self.isNegation = False
        if (self.valueLvtScore > 0.0):
            if(len(self.txtLower) >= self.lvtUseThreshold):
                prevValueLvtScore = self.valueLvtScore
                tmpBool = self.isMatch(self.txtLower, self.gramrNegations, self.lvtThreshold)
                if (self.valueLvtScore < prevValueLvtScore):
                    self.isNegation = tmpBool
                #eif
            else:
                if (self.txtLower in self.gramrNegations):
                    self.valueLvtScore = 0.0
                    self.lvtTxtMatch = self.txtLower
                    self.isNegation = True
                # eif
            #eif
        #eif

        # vectorization
        if(self.isMisspelled == False):
            if(self.txtLower in self.vectorLookups.keys()):
                self.valueVector = self.vectorLookups[self.txtLower]
            else:
                self.valueVector = 0
            #eif
        else:
            if(self.lvtTxtMatch in self.vectorLookups.keys()):
                self.valueVector = self.vectorLookups[self.lvtTxtMatch]
            else:
                self.valueVector = 0
            #eif
        #eif
    #ef

    def isTxtNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    #ef

    def isMatch(self, tword, arrayOfWords, threshold):
        res = 1.0
        prevRes = 1.0
        found = False

        for word in arrayOfWords:
            res = distance.nlevenshtein(word, tword, method=2)
            if(res < threshold and res < prevRes):
                found = True
                prevRes = res
                self.valueLvtScore = res
                self.lvtTxtMatch = word

                if (res == 0.0):
                    self.isMisspelled = False
                    return True
                else:
                    self.isMisspelled = True
                # eif
            #eif
        #ef

        if(found):
            return True
        else:
            return False
        #eif
    #ef

    def toString(self):
        if(self.hasStartingQuestion or self.hasEndingQuestion or self.hasQuestion):
            print("Question Mark: {} {} {} {}".format(self.hasStartingQuestion, self.hasEndingQuestion, self.hasQuestion, self.wordIdxQuestion))
        #eif

        if(self.hasStartingExclamation or self.hasEndingExclamation or self.hasExclamation):
            print("Exclamation Mark: {} {} {} {}".format(self.hasStartingExclamation, self.hasEndingExclamation, self.hasExclamation, self.wordIdxExclamation))
        #eif

        if(self.hasStartingPeriod or self.hasEndingPeriod or self.hasPeriod):
            print("Period: {} {} {} {}".format(self.hasStartingPeriod, self.hasEndingPeriod, self.hasPeriod, self.wordIdxPeriod))
        #eif

        if(self.hasStartingComma or self.hasEndingComma or self.hasComma):
            print("Comma: {} {} {} {}".format(self.hasStartingComma, self.hasEndingComma, self.hasComma, self.wordIdxComma))
        #eif

        if(self.hasStartingCaps or self.hasEndingCaps or self.hasCaps):
            print("Caps: {} {} {} {}".format(self.hasStartingCaps, self.hasEndingCaps, self.hasCaps, self.wordIdxCaps))
        #eif

        if(self.hasStartingSingleQuote or self.hasEndingSingleQuote or self.hasSingleQuote):
            print("Single Quote: {} {} {} {}".format(self.hasStartingSingleQuote, self.hasEndingSingleQuote, self.hasSingleQuote, self.wordIdxSingleQuote))
        #eif

        if(self.hasStartingDoubleQuote or self.hasEndingDoubleQuote or self.hasDoubleQuote):
            print("Double Quote: {} {} {} {}".format(self.hasStartingDoubleQuote, self.hasEndingDoubleQuote, self.hasDoubleQuote, self.wordIdxDoubleQuote))
        #eif

        if(self.isNumber):
            print("Is Number: {}".format(self.isNumber))
        #eif

        if(self.isQuestion):
            print("Is Question: {}".format(self.isQuestion))
        #eif

        if(self.isPronoun):
            print("Is Pronoun: {}".format(self.isPronoun))
        #eif

        if(self.isPreposition):
            print("Is Preposition: {}".format(self.isPreposition))
        #eif

        if(self.isArticle):
            print("Is Article: {}".format(self.isArticle))
        #eif

        if(self.isConditional):
            print("Is Conditional: {}".format(self.isConditional))
        #eif

        if(self.isConjunction):
            print("Is Conjuction: {}".format(self.isConjunction))
        #eif

        if(self.isNoun):
            print("Is Noun: {}".format(self.isNoun))
        #eif

        if(self.isAdjective):
            print("Is Adjective: {}".format(self.isAdjective))
        #eif

        if(self.isAdverb):
            print("Is Adverb: {}".format(self.isAdverb))
        #eif

        if(self.isVerb):
            print("Is Verb: {}".format(self.isVerb))
        #eif

        if(self.isMisspelled):
            print("Is Misspelled: {}".format(self.isMisspelled))
        #eif

        if(self.isNegation):
            print("Is Negation: {}".format(self.isNegation))
        #eif

        if(self.valueLvtScore != 2.0):
            print("Lvt Score: {}".format(self.valueLvtScore))
            print("Lvt Match: {}".format(self.lvtTxtMatch))
        #eif

        print("Vector Value: {}".format(self.valueVector))
        print("Word Index: {}".format(self.valueWordIndex))
        print("Sentence Index: {}".format(self.valueSentenceIndex))
    #ef
#ec