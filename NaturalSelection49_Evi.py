import sys
import Nlp2Evi
import Nlp2General
import NaturalSelection49

# really binary combinations
tokenVerboseArg = False
tokenizerVerboseArg = False
txtVerboseArg = False

# binary expressions happens after tokenization
gramrComplexNegations = NaturalSelection49.gramrComplexNegations

# simple expressions happens before tokenization
gramrSimpleReplacements = NaturalSelection49.gramrSimpleReplacements

vectorLookups = NaturalSelection49.vectorLookups

gramrPronouns = NaturalSelection49.gramrPronouns

gramrPrepositions = NaturalSelection49.gramrPrepositions

gramrArticles = NaturalSelection49.gramrArticles

gramrConditionals = NaturalSelection49.gramrConditionals

gramrConjunctions = NaturalSelection49.gramrConjunctions

gramrNegations = NaturalSelection49.gramrNegations

gramrNouns = NaturalSelection49.gramrNouns

gramrAdjectives = NaturalSelection49.gramrAdjectives

gramrVerbs = NaturalSelection49.gramrVerbs

gramrAdverbs = NaturalSelection49.gramrAdverbs


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
]

patternsScoring = [
    {
        "kc": "EVIDENCE_SUFF",
        "score": 0,
        "prevScore": 0,
        "patterns":
            [
                [
                    {"value": ["patternIncrease_Foliage", "patternDecrease_Foliage", "patternChange_Foliage"], "points": 2, "type": 1},
                ],

                [
                    {"value": ["patternFoliage_None","patternFoliage_Some","patternFoliage_Lots"], "points": 1, "type": 1},
                ],

                [
                    {"value": "patternFoliage_None", "points": 2, "type": 4},
                    {"value": ["patternFoliage_Some","patternFoliage_Lots"], "points": 2, "type": 5},
                ],

                [
                    {"value": "patternFoliage_Some", "points": 2, "type": 4},
                    {"value": ["patternFoliage_None","patternFoliage_Lots"], "points": 2, "type": 5},
                ],

                [
                    {"value": "patternFoliage_Lots", "points": 2, "type": 4},
                    {"value": ["patternFoliage_None","patternFoliage_Some"], "points": 2, "type": 5},
                ],
                
                [
                    {"value": "patternIn_Trial", "points": 1, "type": 4},
                ],

                [
                    {"value": "patternIn_Trial", "points": 2, "type": 4},
                    {"value": "patternIn_Trial", "points": 2, "type": 4},
                ],

                [
                    {"value": "patternVague_Trials", "points": 0.5, "type": 0},
                ],

                [
                    {"value": ["patternIV", "patternDV"], "points": -0.0, "type": 3},
                ],
            ]
    },

    {
        "kc": "EVIDENCE_APP_IVR",
        "score": 0,
        "prevScore": 0,
        "patterns":
            [
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
        "kc": "EVIDENCE_APP_DVR",
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
    Nlp2Evi.processPatterns(txtTokenizer,patternsToRun,patternsScoring)
#def

