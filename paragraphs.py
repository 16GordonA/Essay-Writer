'''
Takes paragraph as text string, parses for quotes, searches internet to find full quote and verifies with citation

Several different types of paragraphs which will be formed using the inputted quotes
'''
from fileparse import *

qmarks = ['"'] #quotation marks since... there are several for some reason

#sample paragraph follows from an old essay. The program will take paragraphs in from text files in the future

paragraph = 'In his sonnet 90, Shakespeare requests that the Fair Youth end his relationship with the Poet, and "hate [him]...'
paragraph +=' if ever, now" (XC i), in order that he might contribute to the beginning of a cycle of bad fortune, rather than "drop in fo'
paragraph +='r an after-loss" (iv). This theme continues as the Poet mentions further "sorrow" and likens his experiences to a "windy nig'
paragraph +='ht" (v,vii). Finally, Shakespeare concludes that, though a break-up with the Fair Youth would be "the very worst of fortune' + "'"
paragraph +='s might" (xii), it will alleviate the suffering caused by the Poet'+"'"+'s other misfortunes. However, this romantic outlook on th'
paragraph +='eir love is tempered by the use of military language throughout the sonnet.'

def match(quotes, citations):

    matched = [] #[ [ ["quote" , "quote"] , (citation)] , [ ["quote" , "quote"] , (citation)] ]
    temp = []
    
    c = 0
    q = 0
    
    while q < len(quotes):
        #print(q)
        if quotes[q][1] < citations[c][0]: #if quote is before that citation
            temp = temp + [ paragraph[quotes[q][0] : quotes[q][1]] ]
            #print(temp)
            q = q + 1
            
        else:
            matched = matched + [temp , paragraph[citations[c][0] : citations[c][1]] ]
            #print(matched)
            temp = []
            c = c + 1
            #print ('reached')
    
    matched = matched + [temp , paragraph[citations[c][0] : citations[c][1]] ]
    #print(matched)
    
    return matched


paragraphs = parse()
paragraph = paragraphs[0] + ' ' + paragraphs[1]

print(paragraph)

quotes = [] #will hold tuples of <start quote , end quote> values
citations = [] #will hold tuples of <start citation, end citation> values

qbeg = -1 #will store locations of first quote
cbeg = -1 #will store locations of first paren

for i in range(len(paragraph)): #sweeps paragraph
    if paragraph[i:i+1] == '"':
        if qbeg >= 0:
            quotes = quotes + [[qbeg, i]]
            qbeg = -1
        else:
            qbeg = i + 1
    
    elif paragraph[i:i+1] == '(' or paragraph[i:i+1] == ')':
        if cbeg >= 0:
            citations = citations + [[cbeg, i + 1]]
            cbeg = -1
        else:
            cbeg = i

print(quotes)
print(citations)

m = match(quotes, citations)

print(m)
