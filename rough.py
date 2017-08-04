#!/usr/bin/python
# -*- coding: utf-8 -*-
from Dictionary import *
li2 = []
strFinalString= "o!0!m"
strFinalString99 = ""
newcharString = ""
for i in range(0, len(strFinalString)):
    if ((i + 3) < len(strFinalString) and strFinalString[i] == "!" and strFinalString[i + 1] == "0" and strFinalString[i + 2] == "!"):
        li2.insert(i + 1, li2[i + 3])
        li2[i + 2] = "0"
        strFinalString = strFinalString[:i + 2] + newstr[i + 3:]

    else:
        li2.append(strFinalString[i])

print "strFinalString ----------------------------",strFinalString
for i in range(0, len(li2)):
    if ((i + 3) < len(li2) and li2[i] == "া" and li2[i + 1] == "ি" and li2[i + 2] == "া"):
        print i,"---i,  entered=====================strFinalString99", strFinalString99
        li2.insert(i + 1, li2[i + 3])
        li2[i + 2] = "0"
        li2.pop(i+2)
        li2.pop(i+1)
        #li2.pop(i+3)
        #del li2[i + 3]
        strFinalString99 = ''.join(li2)
        print"entered=====================strFinalString99", strFinalString99
        i = i + 1

strFinalString4=''.join(li2)
print "strFinalString2",strFinalString4


'''
for i in range (2,len(li)-2) :
    if li[i-1] =="!":
        if li[i-2] =="0":
            li[i - 1] = "0"
            li[i-2] = li[i]
            del li[i]


strFinalString=''.join(li)
print "1", strFinalString


for i in range(0, len(li)-1):
    #print i
    if li[i] == '$' :
        print li[i+1]
        li[i] = li[i+1] #ok till here
        li[i+1] = "q"
        i = i+1
print "2",li
for i in range(0, len(li)-5):
    if li[i] == '^':
        if li[i + 1] == 'h':
            li[i] = 'H'

        elif li[i + 1] == 'i':
            li[i] = 'i'

        elif li[i + 1] == 'd':
            li[i] = 'u'

        elif li[i + 1] == 'U':
            li[i] = 'U'

        elif li[i + 1] == 'D':
            li[i] = 't'

        del li[i + 1]
    j=i+2

print "ekar",dict["q"]
strFinalString2=''.join(li)
print "3-->",strFinalString2
for i in range (0,len(strFinalString2)):
    c = strFinalString2[i]
    try :
        if c == "q":
            c = "$"
        newchar = dict[c]  # dict['b']
        newcharString = newcharString + newchar
    except :
        1
'''