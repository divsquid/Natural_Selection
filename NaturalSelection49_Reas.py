import sys
import Nlp2Reas
import Nlp2General
import Natural_Selection_49

# really binary combinations
tokenVerboseArg = False
tokenizerVerboseArg = False
txtVerboseArg = False

gramrComplexNegations = Natural_Selection_49.gramrComplexNegations

# simple expressions happens before tokenization
gramrSimpleReplacements = Natural_Selection_49.gramrSimpleReplacements

vectorLookups = Natural_Selection_49.vectorLookups

gramrPronouns = Natural_Selection_49.gramrPronouns

gramrPrepositions = Natural_Selection_49.gramrPrepositions

gramrArticles = Natural_Selection_49.gramrArticles

gramrConditionals = Natural_Selection_49.gramrConditionals

gramrConjunctions = Natural_Selection_49.gramrConjunctions

gramrNegations = Natural_Selection_49.gramrNegations

gramrNouns = Natural_Selection_49.gramrNouns

gramrAdjectives = Natural_Selection_49.gramrAdjectives

gramrVerbs = Natural_Selection_49.gramrVerbs

gramrAdverbs = Natural_Selection_49.gramrAdverbs
patternIV = [
    [
        {"value": 600, "distance": -1, "hint": 'foliage', "pattern": 'foliage: relevant words', "type": 0},
    ],
]

patternDV = [
    [
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],
]

patternIncrease_Foliage = [
    [
        {"value": [700,800], "distance": 3, "hint": 'increase/more', "pattern": 'increase foliage', "type": 1},
        {"value": 600, "distance": 3, "hint": 'foliage', "pattern": 'increase foliage', "type": 0},
    ],

    [
        {"value": 600, "distance": 3, "hint": 'foliage', "pattern": 'increase foliage', "type": 0},
        {"value": [700,800], "distance": 3, "hint": 'increase/more', "pattern": 'increase foliage', "type": 1},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase/more', "pattern": 'increase foliage', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'increase foliage', "type": 0},
        {"value": 600, "distance": 3, "hint": 'foliage', "pattern": 'increase foliage', "type": 0},
    ],
]


patternDecrease_Foliage = [
    [
        {"value": [701,801], "distance": 3, "hint": 'decrease/less', "pattern": 'decrease foliage', "type": 1},
        {"value": 600, "distance": 3, "hint": 'foliage', "pattern": 'decrease foliage', "type": 0},
    ],

    [
        {"value": 600, "distance": 3, "hint": 'foliage', "pattern": 'decrease foliage', "type": 0},
        {"value": [701,801], "distance": 3, "hint": 'decrease/less', "pattern": 'decrease foliage', "type": 1},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'decrease/less', "pattern": 'decrease foliage', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'decrease foliage', "type": 0},
        {"value": 600, "distance": 3, "hint": 'foliage', "pattern": 'decrease foliage', "type": 0},
    ],

]

patternChange_Foliage = [
    [
        {"value": 805, "distance": 3, "hint": 'change', "pattern": 'change foliage', "type": 0},
        {"value": 600, "distance": 3, "hint": 'foliage', "pattern": 'change foliage', "type": 0},
    ],

    [
        {"value": 600, "distance": 3, "hint": 'foliage', "pattern": 'change foliage', "type": 0},
        {"value": 805, "distance": 3, "hint": 'change', "pattern": 'change foliage', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'change', "pattern": 'change foliage', "type": 0},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'change foliage', "type": 0},
        {"value": 600, "distance": 3, "hint": 'foliage', "pattern": 'change foliage', "type": 0},
    ],
]

patternIncrease_GreenLongHairSlinquettes = [
    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],


    [
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'increase green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'increase green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'increase green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'increase green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'increase green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'increase green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": [700,800], "distance": 3, "hint": 'increase', "pattern": 'increase green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'increase green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'increase green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'increase green, long haired slinquettes', "type": 0},
    ],
]

patternDecrease_GreenLongHairSlinquettes = [
    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],


    [
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Decrease green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Decrease green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Decrease green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Decrease green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Decrease green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'Decrease', "pattern": 'Decrease green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Decrease green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'decrease', "pattern": 'decrease green,long haired slinquettes', "type": 1},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'decrease green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": [701,801], "distance": 3, "hint": 'decrease', "pattern": 'decrease green,long haired slinquettes', "type": 1},
    ],

    [
        {"value": [701,801], "distance": 3, "hint": 'decrease', "pattern": 'decrease green,long haired slinquettes', "type": 1},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'decrease green,long haired slinquettes', "type": 0},{"value": 711, "distance": 2, "hint": 'green', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'decrease green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'decrease green, long haired slinquettes', "type": 0},
    ],
]

patternChange_GreenLongHairSlinquettes = [
    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],


    [
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
    ],

    [
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
    ],

    [
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
    ],

    [
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 2, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'Change', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'Change green,long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'Change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'Change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'change', "pattern": 'change green,long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'change green, long haired slinquettes', "type": 0},
    ],

    [
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 805, "distance": 3, "hint": 'change', "pattern": 'change green,long haired slinquettes', "type": 0},
    ],

    [
        {"value": 805, "distance": 3, "hint": 'change', "pattern": 'change green,long haired slinquettes', "type": 0},
        {"value": 604, "distance": 3, "hint": 'amount', "pattern": 'change green,long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 711, "distance": 2, "hint": 'green', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 601, "distance": 3, "hint": 'slinquettes', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 713, "distance": 2, "hint": 'long', "pattern": 'change green, long haired slinquettes', "type": 0},
        {"value": 602, "distance": 2, "hint": 'hair', "pattern": 'change green, long haired slinquettes', "type": 0},
    ],
]

patternChange = [
    [
        {"value": 805, "distance": -1, "hint": 'change', "pattern": 'change', "type": 0},
    ],
]

patternFoliage_None = [
    [
        {"value": 714, "distance": 4, "hint": 'none', "pattern": 'None foliage', "type": 0},
        {"value": 600, "distance": 4, "hint": 'foliage', "pattern": 'None foliage', "type": 0},
    ],

    [
        {"value": 600, "distance": 4, "hint": 'foliage', "pattern": 'None foliage', "type": 0},
        {"value": 714, "distance": 4, "hint": 'None', "pattern": 'None foliage', "type": 0},
    ],

    [
        {"value": [100, 106], "distance": 2, "hint": 'preposition', "pattern": 'none foliage', "type": 1},
        {"value": 714, "distance": 4, "hint": 'None', "pattern": 'None foliage', "type": 0},
    ],
]

patternFoliage_Some = [
    [
        {"value": 715, "distance": 4, "hint": 'some', "pattern": 'some foliage', "type": 0},
        {"value": 600, "distance": 4, "hint": 'foliage', "pattern": 'some foliage', "type": 0},
    ],

    [
        {"value": 600, "distance": 4, "hint": 'foliage', "pattern": 'some foliage', "type": 0},
        {"value": 715, "distance": 4, "hint": 'some', "pattern": 'some foliage', "type": 0},
    ],

    [
        {"value": [100, 106], "distance": 2, "hint": 'preposition', "pattern": 'some foliage', "type": 1},
        {"value": 715, "distance": 4, "hint": 'some', "pattern": 'some foliage', "type": 0},
    ],
]

patternFoliage_Lots = [
    [
        {"value": 716, "distance": 4, "hint": 'lots', "pattern": 'lots foliage', "type": 0},
        {"value": 600, "distance": 4, "hint": 'foliage', "pattern": 'lots foliage', "type": 0},
    ],

    [
        {"value": 600, "distance": 4, "hint": 'foliage', "pattern": 'some foliage', "type": 0},
        {"value": 716, "distance": 4, "hint": 'lots', "pattern": 'lots foliage', "type": 0},
    ],

    [
        {"value": [100, 106], "distance": 2, "hint": 'preposition', "pattern": 'lots foliage', "type": 1},
        {"value": 716, "distance": 4, "hint": 'lots', "pattern": 'lots foliage', "type": 0},
    ],
]

patternIn_Trial = [
    [
        {"value": [100, 106], "distance": 3, "hint": 'in', "pattern": 'in trial', "type": 1},
        {"value": 613, "distance": 3, "hint": 'trial', "pattern": 'in trial', "type": 0},
    ]
]

patternVague_Trials = [
    [
        {"value": [613, 616, 816,], "distance": 3, "hint": 'trials, experiments', "pattern": 'vague trial', "type": 1},
    ]
]

patternExtinct = [
    [
        # {"value": [601, 10, 200], "distance": 5, "hint": 'slinquettes/they', "pattern": 'slinquettes extinct', "type": 1},
        {"value": 820, "distance": -1, "hint": 'extinct', "pattern": 'slinquettes extinct', "type": 0},
    ],

    [
        {"value": 604, "distance": 4, "hint": 'population', "pattern": 'slinquettes extinct', "type": 0},
        {"value": 2000, "distance": 4, "hint": 'number', "pattern": 'slinquettes extinct', "type": 0},
    ],

    [
        {"value": 601, "distance": 5, "hint": 'slinquettes', "pattern": 'slinquettes extinct', "type": 0},
        {"value": 2000, "distance": 4, "hint": 'number', "pattern": 'slinquettes extinct', "type": 0},
    ],

    [
        {"value": 2000, "distance": 4, "hint": 'number', "pattern": 'slinquettes extinct', "type": 0},
        {"value": 601, "distance": 5, "hint": 'slinquettes', "pattern": 'slinquettes extinct', "type": 0},
    ],
]

patternEndangered = [
    [
        # {"value": [601, 10, 200], "distance": 5, "hint": 'slinquettes/they', "pattern": 'slinquettes Endangered', "type": 1},
        {"value": 821, "distance": -1, "hint": 'Endangered', "pattern": 'slinquettes Endangered', "type": 0},
    ],

    [
        {"value": 604, "distance": 4, "hint": 'population', "pattern": 'slinquettes endangered', "type": 0},
        {"value": 2001, "distance": 4, "hint": 'number', "pattern": 'slinquettes endangered', "type": 0},
    ],

    [
        {"value": 601, "distance": 5, "hint": 'slinquettes', "pattern": 'slinquettes endangered', "type": 0},
        {"value": 2001, "distance": 4, "hint": 'number', "pattern": 'slinquettes endangered', "type": 0},
    ],

    [
        {"value": 2001, "distance": 4, "hint": 'number', "pattern": 'slinquettes endangered', "type": 0},
        {"value": 601, "distance": 5, "hint": 'slinquettes', "pattern": 'slinquettes endangered', "type": 0},
    ],
]

patternSurviving = [
    [
        # {"value": [601, 10, 200], "distance": 5, "hint": 'slinquettes/they', "pattern": 'slinquettes surive', "type": 1},
        {"value": 822, "distance": -1, "hint": 'survive', "pattern": 'slinquettes survive', "type": 0},
    ],

    [
        {"value": 604, "distance": 4, "hint": 'population', "pattern": 'slinquettes Surviving ', "type": 0},
        {"value": 2005, "distance": 4, "hint": 'number', "pattern": 'slinquettes surviving ', "type": 0},
    ],

    [
        {"value": 601, "distance": 5, "hint": 'population', "slinquettes": 'slinquettes Surviving ', "type": 0},
        {"value": 2005, "distance": 4, "hint": 'number', "pattern": 'slinquettes surviving ', "type": 0},
    ],

    [
        {"value": 2005, "distance": 4, "hint": 'number', "pattern": 'slinquettes surviving ', "type": 0},
        {"value": 601, "distance": 5, "hint": 'population', "slinquettes": 'slinquettes Surviving ', "type": 0},
    ],

]

patternExpanding = [
    [
        # {"value": [601, 10, 200], "distance": 5, "hint": 'slinquettes/they', "pattern": 'slinquettes expanding', "type": 1},
        {"value": 823, "distance": -1, "hint": 'expandig', "pattern": 'slinquettes expanding', "type": 0},
    ],

    [
        {"value": 604, "distance": 4, "hint": 'population', "pattern": 'slinquettes expanding ', "type": 0},
        {"value": 2009, "distance": 4, "hint": 'number', "pattern": 'slinquettes expanding ', "type": 0},
    ],

    [
        {"value": 601, "distance": 5, "hint": 'slinquettes', "pattern": 'slinquettes expanding ', "type": 0},
        {"value": 2009, "distance": 4, "hint": 'number', "pattern": 'slinquettes expanding ', "type": 0},
    ],

    [
        {"value": 2009, "distance": 4, "hint": 'number', "pattern": 'slinquettes expanding ', "type": 0},
        {"value": 601, "distance": 5, "hint": 'slinquettes', "pattern": 'slinquettes expanding ', "type": 0},
    ],
]

patternThriving = [
    [
        # {"value": [601, 10, 200], "distance": 5, "hint": 'slinquettes/they', "pattern": 'slinquettes thriving', "type": 1},
        {"value": 824, "distance": -1, "hint": 'thriving', "pattern": 'slinquettes thriving', "type": 0},
    ],

    [
        {"value": 604, "distance": 4, "hint": 'population', "pattern": 'slinquettes thriving', "type": 0},
        {"value": 2013, "distance": 4, "hint": 'number', "pattern": 'slinquettes thriving', "type": 0},
    ],

    [
        {"value": 601, "distance": 5, "hint": 'slinquettes', "pattern": 'slinquettes thriving', "type": 0},
        {"value": 2013, "distance": 4, "hint": 'number', "pattern": 'slinquettes thriving', "type": 0},
    ],

    [
        {"value": 2013, "distance": 4, "hint": 'number', "pattern": 'slinquettes thriving', "type": 0},
        {"value": 601, "distance": 5, "hint": 'slinquettes', "pattern": 'slinquettes thriving', "type": 0},
    ],
]

#different ways of saying "supports my claim"
patternEvidence_Supports_Claim = [
    [
        {"value": [614, 613, 616 ], "distance": 4, "hint": 'evidence/experiments/data', "pattern": 'evidence supports my claim', "type": 1},
        {"value": [807, 812], "distance": 4, "hint": 'prove/refute', "pattern": 'evidence supports my claim', "type": 1},
        {"value": [615], "distance": 4, "hint": 'claim', "pattern": 'evidence supports my claim', "type": 1},
    ],

    [
        {"value": [615], "distance": 4, "hint": 'claim', "pattern": 'evidence supports my claim', "type": 1},
        {"value": [807, 812], "distance": 4, "hint": 'prove/refute', "pattern": 'evidence supports my claim', "type": 1},
        {"value": [614, 613, 616 ], "distance": 4, "hint": 'evidence/experiments/data', "pattern": 'evidence supports my claim', "type": 1},
    ],

    [
        {"value": [614, 613, 616 ], "distance": 4, "hint": 'evidence/experiments/data', "pattern": 'evidence supports my claim', "type": 1},
        {"value": 816, "distance": 4, "hint": 'shows', "pattern": 'evidence supports my claim', "type": 0},

    ],

]

patternClaim_Supported = [
    [
        {"value": [807, 812, 850], "distance": 4, "hint": 'prove/refute', "pattern": 'supports claim', "type": 1},
        {"value": [615], "distance": 4, "hint": 'claim', "pattern": 'supports claim', "type": 1},
    ],

    [
        {"value": [615], "distance": 4, "hint": 'claim', "pattern": 'supports claim', "type": 1},
        {"value": [807, 812, 850], "distance": 4, "hint": 'prove/refute', "pattern": 'supports claim', "type": 1},
    ],
]

patternClaim = [
    [
        {"value": 615, "distance": -1, "hint": 'claim', "pattern": 'claim', "type": 0},
    ]
]

#words like prove, hypothesis, claim, evidence are present
patternRelevant_to_Connection = [
    [
        {"value": [807, 615, 614, 613], "distance": -1, "hint": 'prove, hypothesis, claim', "pattern": 'connection: relevant words', "type": 1},
    ],
]

patternClaim_Correctness = [
    [
        {"value": 615, "distance": 4, "hint": 'claim', "pattern": 'claim is correct', "type": 0},
        {"value": [620, 619, 851, 807, 812], "distance": 4, "hint": 'correct/wrong', "pattern": 'claim is correct', "type": 0},
    ],
]

patternProves = [
    [
        {"value": [620, 619, 851, 807, 812], "distance": 4, "hint": 'correct/wrong', "pattern": 'concept: prove', "type": 0},
    ],
]

patternIt_Supports_It = [
    [
        {"value": 699, "distance": -1, "hint": 'claim', "pattern": 'partial connection', "type": 0},
    ],
]

patternBecause_Evidence = [
    [
        {"value": 300, "distance": 5, "hint": 'because', "pattern": 'because evidence', "type": 0},
        {"value": [614, 613, 616 ], "distance": 4, "hint": 'evidence/experiments/data', "pattern": 'evidence supports my claim', "type": 1},
    ],
]

patternBecause = [
    [
        {"value": 300, "distance": 5, "hint": 'because', "pattern": 'because something', "type": 0},
    ],
]

patternHelp_Survival = [
    [
        {"value": [825, 700, 800], "distance": 5, "hint": 'help, increase, more', "pattern": 'help suvival', "type": 1},
        {"value": [822, 823, 824, 800], "distance": 5, "hint": 'survival', "pattern": 'help survival', "type": 1},
    ],
]

patternReproduction = [
    [
        {"value": 826, "distance": 5, "hint": 'reproduction', "pattern": 'reproduction', "type": 0},
    ],

    [
        {"value": [825, 700, 800], "distance": 5, "hint": 'help, increase, more', "pattern": 'reproduction', "type": 1},
        {"value": 826, "distance": 5, "hint": 'reproduction', "pattern": 'reproduction', "type": 0},
    ],
]

patternPass_Down_Trait = [
    [
        {"value": [827], "distance": 5, "hint": 'pass down', "pattern": 'passing of a trait', "type": 1},
        {"value": 605, "distance": 5, "hint": 'trait', "pattern": 'passing of a trait', "type": 0},
    ],

    [
        {"value": 605, "distance": 5, "hint": 'trait', "pattern": 'passing of a trait', "type": 0},
        {"value": [827], "distance": 5, "hint": 'pass down', "pattern": 'passing of a trait', "type": 1},
    ],
]

patternTrait = [
    [
        {"value": 711, "distance": 3, "hint": 'GREEN', "pattern": 'trait', "type": 0},
        {"value": 713, "distance": 3, "hint": 'long', "pattern": 'trait', "type": 0},
    ],

    [
        {"value": 713, "distance": 3, "hint": 'long', "pattern": 'trait', "type": 0},
        {"value": 711, "distance": 3, "hint": 'GREEN', "pattern": 'trait', "type": 0},
    ],

    [
        {"value": 605, "distance": 5, "hint": 'trait', "pattern": 'trait', "type": 0},
    ],
]


patternsToRun = [
        {'pattern': patternIV,                       'name': 'patternIV',                     'desc': 'Text relevance check'},
        {'pattern': patternDV,                       'name': 'patternDV',                     'desc': 'Text relevance check'},
        {'pattern': patternIncrease_Foliage,                       'name': 'patternIncrease_Foliage',                     'desc': 'Concept: increase foliage'},
        {'pattern': patternDecrease_Foliage,                       'name': 'patternDecrease_Foliage',                     'desc': 'Concept: decrease foliage'},
        {'pattern': patternChange_Foliage,                       'name': 'patternChange_Foliage',                     'desc': 'Concept: change foliage'},
        {'pattern': patternIncrease_GreenLongHairSlinquettes,                       'name': 'patternIncrease_GreenLongHairSlinquettes',                     'desc': 'Concept: increase GreenLongHairSlinquettes'},
        {'pattern': patternDecrease_GreenLongHairSlinquettes,                       'name': 'patternDecrease_GreenLongHairSlinquettes',                     'desc': 'Concept: decrease GreenLongHairSlinquettes'},
        {'pattern': patternChange_GreenLongHairSlinquettes,                       'name': 'patternChange_GreenLongHairSlinquettes',                     'desc': 'Concept: change GreenLongHairSlinquettes'},
        {'pattern': patternChange,                       'name': 'patternChange',                     'desc': 'Concept: change'},
        {'pattern': patternFoliage_Lots,                       'name': 'patternFoliage_Lots',                     'desc': 'Concept: lots of foliage'},
        {'pattern': patternFoliage_Some,                       'name': 'patternFoliage_Some',                     'desc': 'Concept: some foliage'},
        {'pattern': patternFoliage_None,                       'name': 'patternFoliage_None',                     'desc': 'Concept: none foliage'},
        {'pattern': patternIn_Trial,                       'name': 'patternIn_Trial',                     'desc': 'Concept: trial'},
        {'pattern': patternVague_Trials,                       'name': 'patternVague_Trials',                     'desc': 'Concept: vague trial'},
        {'pattern': patternExtinct,                       'name': 'patternExtinct',                     'desc': 'Concept: slinquettes extinct'},
        {'pattern': patternEndangered,                       'name': 'patternEndangered',                     'desc': 'Concept: slinquettes Endangered'},
        {'pattern': patternSurviving,                       'name': 'patternSurviving',                     'desc': 'Concept: slinquettes Surviving'},
        {'pattern': patternExpanding,                       'name': 'patternExpanding',                     'desc': 'Concept: slinquettes Expanding'},
        {'pattern': patternThriving,                       'name': 'patternThriving',                     'desc': 'Concept: slinquettes Thriving'},
        {'pattern': patternEvidence_Supports_Claim,         'name': 'patternEvidence_Supports_Claim',                     'desc': 'Concept: Evidence SupportsClaim'},
        {'pattern': patternClaim_Supported,                  'name': 'patternClaim_Supported',                     'desc': 'Concept: claim supported'},
        {'pattern': patternClaim,                       'name': 'patternClaim',                     'desc': 'Concept: claim'},
        {'pattern': patternRelevant_to_Connection,                       'name': 'patternRelevant_to_Connection',                     'desc': 'Concept: connection relevance'},
        {'pattern': patternClaim_Correctness,                       'name': 'patternClaim_Correctness',                     'desc': 'Concept: correctness'},
        {'pattern': patternProves,                       'name': 'patternProves',                     'desc': 'Concept: proves'},
        {'pattern': patternIt_Supports_It,                       'name': 'patternIt_Supports_It',                     'desc': 'Concept: something supports'},
        {'pattern': patternBecause_Evidence,                       'name': 'patternBecause_Evidence',                     'desc': 'Concept: evidence provided'},
        {'pattern': patternBecause,                       'name': 'patternBecause',                     'desc': 'Concept: because something'},
        {'pattern': patternHelp_Survival,                       'name': 'patternHelp_Survival',                     'desc': 'Concept: help survival'},
        {'pattern': patternReproduction,                       'name': 'patternReproduction',                     'desc': 'Concept: reproduction'},
        {'pattern': patternPass_Down_Trait,                       'name': 'patternPass_Down_Trait',                     'desc': 'Concept: passing down a trait'},
        {'pattern': patternTrait,                       'name': 'patternTrait',                     'desc': 'Concept: trait/gene'},
]

patternsScoring = [
    {
        "kc": "REASONING_THEORY",
        "score": 0,
        "prevScore": 0,
        "patterns":
            [
                [
                    {"value": ["patternPass_Down_Trait", "patternReproduction", "patternTrait" ], "points": 0.0, "type": 3},
                ],

                [
                    {"value": ["patternIncrease_GreenLongHairSlinquettes", "patternHelp_Survival"], "points": 1, "type": 1},
                    {"value": "patternBecause", "points": 1, "type": 0},
                ],

                [
                    {"value": "patternBecause", "points": 1, "type": 0},
                    {"value": ["patternIncrease_GreenLongHairSlinquettes", "patternHelp_Survival"], "points": 1, "type": 1},
                ],

                [
                    {"value": "patternTrait", "points": 2, "type": 4},
                    {"value": "patternHelp_Survival", "points": 2, "type": 4},
                    {"value": "patternReproduction", "points": 2, "type": 4},
                    {"value": "patternPass_Down_Trait", "points": 2, "type": 4},
                ],

                [
                    {"value": ["patternPass_Down_Trait", "patternReproduction", "patternTrait", "patternHelp_Survival"], "points": 2, "type": 5},
                    {"value": ["patternPass_Down_Trait", "patternReproduction", "patternTrait", "patternHelp_Survival"], "points": 2, "type": 5},
                    {"value": ["patternPass_Down_Trait", "patternReproduction", "patternTrait", "patternHelp_Survival"], "points": 2, "type": 5},
                    {"value": ["patternPass_Down_Trait", "patternReproduction", "patternTrait", "patternHelp_Survival"], "points": 2, "type": 5},
                ],




            ]

    },

    {
        "kc": "REASONING_CONN",
        "score": 0,
        "prevScore": 0,
        "patterns":
            [
                [
                    {"value": "patternEvidence_Supports_Claim", "points": 1, "type": 0},
                ],

                [
                    {"value": "patternClaim_Supported", "points": 1, "type": 0},
                    {"value": ["patternIncrease_Foliage", "patternIncrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": ["patternIncrease_Foliage", "patternIncrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                ],

                [
                    {"value": "patternClaim_Supported", "points": 1, "type": 0},
                    {"value": ["patternDecrease_Foliage", "patternDecrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": ["patternDecrease_Foliage", "patternDecrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                ],

                [
                    {"value": "patternClaim_Supported", "points": 1, "type": 0},
                    {"value": ["patternChange_Foliage", "patternChange_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": ["patternChange_Foliage", "patternChange_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                ],

                [
                    {"value": ["patternIncrease_Foliage", "patternIncrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": ["patternIncrease_Foliage", "patternIncrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": "patternClaim_Supported", "points": 1, "type": 0},
                ],

                [
                    {"value": ["patternDecrease_Foliage", "patternDecrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": ["patternDecrease_Foliage", "patternDecrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": "patternClaim_Supported", "points": 1, "type": 0},
                ],

                [
                    {"value": ["patternChange_Foliage", "patternChange_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": ["patternChange_Foliage", "patternChange_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": "patternClaim_Supported", "points": 1, "type": 0},
                ],

                [
                    {"value": "patternClaim_Supported", "points": 0.8, "type": 0},
                ],

                [
                    {"value": "patternRelevant_to_Connection", "points": 0.8, "type": 0},
                    {"value": "patternRelevant_to_Connection", "points": 0.8, "type": 0},
                ],

                [
                    {"value": "patternClaim_Correctness", "points": 0.8, "type": 0},
                ],

                [
                    {"value": "patternIt_Supports_It", "points": 0.8, "type": 0},
                ],

                [
                    {"value": "patternRelevant_to_Connection", "points": 0.5, "type": 0},
                ],

                [
                    {"value": "patternProves", "points": 1, "type": 0},
                    {"value": ["patternIncrease_Foliage", "patternIncrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": ["patternIncrease_Foliage", "patternIncrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                ],

                [
                    {"value": "patternProves", "points": 1, "type": 0},
                    {"value": ["patternDecrease_Foliage", "patternDecrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": ["patternDecrease_Foliage", "patternDecrease_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                ],

                [
                    {"value": "patternProves", "points": 1, "type": 0},
                    {"value": ["patternChange_Foliage", "patternChange_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                    {"value": ["patternChange_Foliage", "patternChange_GreenLongHairSlinquettes"], "points": 1, "type": 1},
                ],


                [
                    {"value": "patternClaim_Supported", "points": 1, "type": 0},
                    {"value": "patternBecause_Evidence", "points": 1, "type": 0},
                ],

                [
                    {"value": "patternBecause_Evidence", "points": 1, "type": 0},
                    {"value": "patternClaim_Supported", "points": 1, "type": 0},
                ]


            ]
    },

    {
        "kc": "REASONING_IV_IVR",
        "score": 0,
        "prevScore": 0,
        "patterns":
            [
                [
                    {"value": "patternIV", "points": 1, "type": 0},
                ],

                [
                    {"value": ["patternFoliage_None","patternFoliage_Some","patternFoliage_Lots"], "points": 0.5, "type": 1},
                ],

                [
                    {"value": "patternFoliage_None", "points": 1, "type": 4},
                    {"value": ["patternFoliage_Some","patternFoliage_Lots"], "points": 1, "type": 5},
                ],

                [
                    {"value": "patternFoliage_Some", "points": 1, "type": 4},
                    {"value": ["patternFoliage_None","patternFoliage_Lots"], "points": 1, "type": 5},
                ],

                [
                    {"value": "patternFoliage_Lots", "points": 1, "type": 4},
                    {"value": ["patternFoliage_None","patternFoliage_Some"], "points": 1, "type": 5},
                ],

                [
                    {"value": "patternIncrease_Foliage", "points": 1, "type": 0},
                    {"value": "patternIncrease_GreenLongHairSlinquettes", "points": 1, "type": 0},
                ],

                [
                    {"value": "patternIncrease_GreenLongHairSlinquettes", "points": 1, "type": 0},
                    {"value": "patternIncrease_Foliage", "points": 1, "type": 0},
                ],

                [
                    {"value": "patternDecrease_Foliage", "points": 1, "type": 0},
                    {"value": "patternIncrease_GreenLongHairSlinquettes", "points": 1, "type": 0},
                ],

                [
                    {"value": "patternDencrease_GreenLongHairSlinquettes", "points": 1, "type": 0},
                    {"value": "patternDecrease_Foliage", "points": 1, "type": 0},
                ],
            ]
    },

    {
        "kc": "REASONING_DV",
        "score": 0,
        "prevScore": 0,
        "patterns":
            [
                [
                    {"value": "patternDV", "points": 1, "type": 0},
                ],
            ]
    },

    {
        "kc": "REASONING_DVR",
        "score": 0,
        "prevScore": 0,
        "patterns":
            [
[
                    {"value": ["patternExtinct", "patternEndangered","patternSurviving", "patternExpanding", "patternThriving"], "points": 0.5, "type": 1},
                ],

                # [
                #     {"value": "patternEndangered", "points": 1000, "type": 0},
                # ],

                # [
                #     {"value": "patternExtinct", "points": 2000, "type": 0},
                # ],

                # [
                #     {"value": "patternExpanding", "points": 3000, "type": 0},
                # ],

                # [
                #     {"value": "patternSurviving", "points": 4000, "type": 0},
                # ],

                # [
                #     {"value": "patternThriving", "points": 5000, "type": 0},
                # ],

                [
                    {"value": "patternExtinct", "points": 1, "type": 4},
                    {"value": ["patternEndangered","patternSurviving", "patternExpanding", "patternThriving"], "points": 1, "type": 5},
                ],

                [
                    {"value": "patternEndangered", "points": 1, "type": 4},
                    {"value": ["patternExtinct","patternSurviving", "patternExpanding", "patternThriving"], "points": 1, "type": 5},
                ],

                [
                    {"value": "patternSurviving", "points": 1, "type": 4},
                    {"value": ["patternExtinct","patternEndangered", "patternExpanding", "patternThriving"], "points": 1, "type": 5},
                ],

                [
                    {"value": "patternExpanding", "points": 1, "type": 4},
                    {"value": ["patternExtinct","patternEndangered","patternSurviving", "patternThriving"], "points": 1, "type": 5},
                ],

                [
                    {"value": "patternThriving", "points": 1, "type": 4},
                    {"value": ["patternExtinct","patternEndangered","patternSurviving","patternExpanding"], "points": 1, "type": 5},
                ],            

            ]
    }
]

# call out to common process function
def processPatterns(txtTokenizer):
	Nlp2Reas.processPatterns(txtTokenizer,patternsToRun,patternsScoring)
#def