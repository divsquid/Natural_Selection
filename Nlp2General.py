# common nlp2 variables

# binary expressions happens after tokenization
gramrComplexNegations = [
    ['does', 'not', "doesn't"],
    ['will', 'not', "won't"],
    ['is', 'not', "isn't"],
    ['do', 'not', "don't"],
    ['did', 'not', "didn't"]
]

# simple expressions happens before tokenization
gramrSimpleReplacements = [
    ['1-2', 'one to two'],
    ['back up', 'support'],
    ['box2', 'box 2'],
    ['not right', 'wrong']
]

gramrPronouns = ['i', 'me', 'he', 'she', 'herself', 'himself', 'you', 'it', 'they', 'each', 'few', 'many',
                 'who', 'whoever', 'whose', 'someone', 'everybody', 'my']

gramrPrepositions = ['in', 'near', 'beside', 'about', 'after', 'besides', 'on', 'at', 'of', 'for', 'into', 'without', 'with']

gramrArticles = ['the', 'a', 'an', 'that']

gramrConditionals = ['if', 'unless', 'when']

gramrConjunctions = ['and', 'nor', 'but', 'or', 'yet', 'so']

gramrNegations = ['neither', 'not', "don't", "doesn't", "isn't", "won't", 'no', "didn't"]

gramrNouns = [
    'count', 'all', 'result', 'results', 'rate', 'trial', 'trail', 'times', 'test', 'box', 'experiments', 'experimenting', 'experiment', 'evidence',
    'claim', 'conclusion', 'hypothesis', 'stated', 'state', 'reasoning', 'resoning',
    'data', 'nothing',
    '0', 'zero', 'one', '1', 'two', '2', 'three', '3', 'four', '4', 'five', '5', 'six', '6', 'seven', '7',
    'first', '1st', 'second', '2nd', 'third', '3rd', 'fourth', '4th', 'fifth', '5th', 'sixth', '6th', 'seventh', '7th',
    'anything', 'wrong', 'correct', 'right'
]

gramrAdjectives = [
    'more', 'positive', 'faster', 'greater',
    'less', 'negative', 'slower',
]

gramrVerbs = [
    'increased', 'increase', 'increasing', 'increases',
    'decreased', 'decrease', 'decreasing', 'decreases',
    'stay', 'stays', 'stayed', 'do', 'work', 'have',
    'vary', 'change', 'alter', 'adjust', 'changed',
    'ran',
    'prove', 'proves', 'proving', 'support', 'supports',
    'did', 'prevent', 'stop', 'receiving', 'recieving', 'getting',
    'start', 'begin', 'cause', 'refutes',
    'was', 'tried', 'show', 'shows', 'will'
]

gramrAdverbs = ['rapidly', 'greatly', 'slowly', 'then', 'while', 'what']

vectorLookups = {
    # pronouns
    'i': 1,  # 1,
    'me': 0,  # 2,
    'he': 0,  # 3,
    'she': 0,  # 4,
    'herself': 0,  # 5,
    'himself': 0,  # 6,
    'you': 0,  # 7,
    'u': 0,
    'it': 0,  # 8,
    'they': 10,  # 10,
    'each': 0,  # 11,
    'few': 0,  # 12,
    'many': 0,  # 13,
    'who': 0,  # 14,
    'whoever': 0,  # 15,
    'whose': 0,  # 16,
    'someone': 0,  # 17,
    'everybody': 0,  # 18,
    'my': 19,

    # prepositions
    'in': 100,
    'near': 0,  # 101,
    'beside': 0,  # 102,
    'about': 0,  # 103,
    'after': 0,  # 104,
    'besides': 0,  # 105,
    'on': 100,
    'at': 0,  # 107,
    'of': 0,  # 108,
    'for': 100,
    'to': 100,
    'inside': 100,
    'from': 100,
    'into': 100,
    'without': 101,
    'with': 102,

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
    # 'for': 0,  # 400,
    'and': 0,  # 401,
    'nor': 0,  # 402,
    'but': 403,
    'or': 0,  # 404,
    'yet': 0,  # 405,
    'so': 0,  # 406,
    'than': 406,

    # negations
    'neither': 500,
    'not': 500,
    "don't": 500,
    'dont': 500,
    "doesn't": 500,
    'doesnt': 500,
    "isn't": 500,
    'isnt': 500,
    "no": 500,
    "didn't": 500,
    'didnt': 500,

    # nouns
    'result': 611,
    'results': 611,

    
    'trial': 613,
    'trail': 613,
    'times': 613,
    'test': 613,
    'box': 613,

    'experiments': 613,
    'experimenting': 613,
    'experiment': 613,
    'evidence': 614,

    'claim': 615,
    'conclusion': 615,
    'hypothesis': 615,
    'stated': 615,
    'state': 615,
    'reasoning': 615,
    'resoning': 615,

    'data': 616,
    'nothing': 617,

    '0': 2000,
    'zero': 2000,
    'one': 2001,
    '1': 2001,
    'first': 2001,
    '1st': 2001,
    'two': 2002,
    '2': 2002,
    'second': 2002,
    '2nd': 2002,
    'three': 2003,
    '3': 2003,
    'third': 2003,
    '3rd': 2003,
    'four': 2004,
    '4': 2004,
    'fourth': 2004,
    '4th': 2004,
    'five': 2005,
    '5': 2005,
    'fifth': 2005,
    '5th': 2005,
    'six': 2006,
    '6': 2006,
    'sixth': 2006,
    '6th': 2006,
    'seven': 2007,
    '7': 2007,
    'seventh': 2007,
    '7th': 2007,

    'anything': 618,
    'wrong': 619,
    'correct': 620,
    'right': 620,

    # adjectives
    'more': 700,
    'positive': 700,
    'faster': 700,
    'greater': 700,

    'less': 701,
    'negative': 701,
    'slower': 701,

    # verbs
    'increased': 800,
    'increase': 800,
    'increasing': 800,
    'increases': 800,

    'decreased': 801,
    'decrease': 801,
    'decreasing': 801,
    'decreases': 801,

    
    'stay': 803,
    'stays': 803,
    'stayed': 803,
    'do': 0,

    'vary': 805,
    'change': 805,
    'alter': 805,
    'adjust': 805,
    'changed': 805,

    'ran': 806,

    'prove': 807,
    'proves': 807,
    'proving': 807,
    'support': 807,
    'supports': 807,

    'did': 808,

    'prevent': 809,
    'stop': 809,

    'receiving': 810,
    'recieving': 810,
    'getting': 810,

    'start': 811,
    'begin': 811,
    'cause': 811,

    'refutes': 812,
    'said': 813,
    'was': 814,
    'tried': 815,
    'show': 816,
    'shows': 816,
    'match': 817,
    'matches': 817,
    'will': 818,

    # adverbs
    'rapidly': 900,
    'greatly': 900,
    'slowly': 901,
    'then': 902,
    'while': 903,
    'what': 904
}
