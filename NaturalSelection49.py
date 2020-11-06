import Nlp2General

# binary expressions happens after tokenization
gramrComplexNegations = [

]
gramrComplexNegations = gramrComplexNegations + Nlp2General.gramrComplexNegations


# simple expressions happens before tokenization
gramrSimpleReplacements = [
    ['At', 'atpreposition'],
    ['trail', 'trial'],
    ['no foliage', 'none foliage'],
    ['It supports it', 'vagueevidenceconnection'],
    ['it supports it', 'vagueevidenceconnection'],
    ['passing down', 'passingdown'],
    ['pass down', 'passdown'],
    #['long, green', 'greenlong long, green'],
    #['green, long', 'greenlong long, green'],
    #['green, long-furred', 'greenlong long furred'],
    #['green, long-furred', 'greenlong long furred'],
]
gramrSimpleReplacements = gramrSimpleReplacements + Nlp2General.gramrSimpleReplacements


gramrPronouns = Nlp2General.gramrPronouns


gramrPrepositions = [
    'by',
    'atpreposition',
]
gramrPrepositions = gramrPrepositions + Nlp2General.gramrPrepositions


gramrArticles = Nlp2General.gramrArticles

gramrConditionals = [
    'because',
] 

gramrConditionals = gramrConditionals + Nlp2General.gramrConditionals

gramrConjunctions = Nlp2General.gramrConjunctions


gramrNegations = [
    'never',
    'wont',
]
gramrNegations = gramrNegations + Nlp2General.gramrNegations


gramrNouns = [
    'foliage',
    'tree',
    'trees',

    'slinquette',
    'slinquettes',
    'Slinquette',
    'Slinquettes',
    'slinq',
    'slinqs',
    'monster',
    'organism',
    'animal',
    'creature',
    'people',

    'fur',
    'furred',
    '-furred',
    'hair',
    'haired',
    '-haired',


    'amount',
    'number',
    'population',

    'trait',
    'gene',
    'characteristic',
    'mutation',
    'greenlong',
    'longgreen',

    'temperature',

    'fur',



    'research',
    'table',

    '9',
    '13',

    'vagueevidenceconnection',

]
gramrNouns = gramrNouns + Nlp2General.gramrNouns


gramrAdjectives = [
    'same',
    'constant',
    'every',
    'each',
    'all',
    'any',
    'different',

     #fur related adj
    'red',
    'green',
    'short',
    'long',
    'long-',

    #foliage levels
    'none',
    'some',
    'lot',
    'lots',   
    'large',    
    'high',

    #other adj
    'long-furred',

]
gramrAdjectives = gramrAdjectives + Nlp2General.gramrAdjectives


gramrVerbs = [
    'add',
    'added',
    'adding',
    'grow',

    'affect',
    'effect',
    'affected',
    'effected',
    'changing',
    'measure',

    'extinct',
    'endangered',
    'survive',
    'survival',
    'surviving',
    'expanding',
    'expanded',
    'thrive',
    'thriving',

    'help',
    'helped',
    'allow',
    'allowed',
    'able',
    'better',

    'reproduce',
    'reproduced',
    'reproducing',
    'reproduction',
    'procreate',
    'passdown',
    'passingdown',
    'pass',
    'inherit',



    'based',

    'makes sense',
]

gramrVerbs = gramrVerbs + Nlp2General.gramrVerbs

gramrAdverbs =[
    'always'
]
gramrAdverbs = gramrAdverbs + Nlp2General.gramrAdverbs


vectorLookups = {
    
    'by': 105,
    'atpreposition': 106,

    'because': 300,
    
    'never': 500,
    'wont': 500,

    'foliage': 600,
    'tree': 600,
    'trees': 600,

    #slinquette nouns
    'slinquette': 601,
    'slinquettes': 601,
    'Slinquette': 601,
    'Slinquettes': 601,
    'slinq': 601,
    'slinqs': 601,
    'monster': 601,
    'organism': 601,
    'animal': 601,
    'creature': 601,
    'people': 601,

    'fur': 602,
    'furred': 602,
    '-furred': 602,
    'hair': 602,
    'haired': 602,
    '-haired': 602,

    'temperature': 603,

    'amount': 604,
    'number': 604,
    'population': 604,

    'trait': 605,
    'gene': 605,
    'characteristic': 605,
    'mutation': 605,
    'greenlong': 605,
    'longgreen': 605,



    'research': 613,
    'table': 616,

    'vagueevidenceconnection': 699,

    'same': 702,
    'constant': 702,

    'every': 705,
    'each': 705,
    'all': 705,
    'any': 705,
    'different': 706,

    #fur related adj
    'red': 710,
    'green': 711,
    'short': 712,
    'long': 713,
    'long-': 713,

    #foliage levels
    'none': 714,
    'some': 715,
    'lots': 716,    
    'lot': 716,    
    'large': 716,    
    'high': 716,

    #other adj
    'long-furred': 720,
    'optimal': 721,






    'add': 800,
    'added': 800,
    'adding': 800,
    'grow': 800,

    'affect': 805,
    'effect': 805,
    'affected': 805,
    'effected': 805,
    'impact': 805,
    'impacts': 805,
    'impacted': 805,
    'changing': 805,

    
    'extinct': 820,
    'endangered': 821,
    'survive': 822,
    'survival': 822,
    'surviving': 822,
    'expanding': 823,
    'expanded': 823,
    'thrive': 824,
    'thriving': 824,

    'help': 825,
    'helped': 825,
    'allow': 825,
    'allowed': 825,
    'able': 825,
    'better': 825,


    'reproduce': 826,
    'reproduced': 826,
    'reproducing': 826,
    'reproduction': 826,
    'procreate': 826,
    'passdown': 827,
    'passingdown': 827,
    'pass': 827,
    'inherit': 827,



    'based': 806,
    'makes sense': 851,

    'measure': 825,

    'always': 906,

    '9': 2009,
    '13': 2013,


}

vectorLookups.update(Nlp2General.vectorLookups)

