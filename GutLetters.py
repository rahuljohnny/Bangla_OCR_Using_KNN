#!/usr/bin/env python
# coding=utf-8
from importer import *
from Dictionary import *
import LevenShtein_Distance

'''
#!/usr/bin/env python
# coding=utf-8
from importer import *
from Dictionary import *
listy=[]
word='K!c!'
word1=''
print len(word)



#def GutLetters(word):
for i in range (0,len(word)):

    listy.append(dict[word[i]])

for i in range (0,len(listy)):
    print "ya"

    if listy[i]=='খ' or listy[i]=='থ' or listy[i]=='য' or listy[i]=='ষ' or listy[i]=='য়':
    #if word1[i]=='খ' or word1[i]=='থ' or word1[i]=='য' or word1[i]=='ষ' or word1[i]=='য়':

        print LavenShtein_Distance.LavenShtein_Distance(listy)

'''





def GutLetters(WordList):

    listy = []
    word = ''
    word = ''.join(WordList)


    if word == "া":
        word = '।'
        return word

    elif word == "নঠ":
        word = "এ"
        return word


    elif word == "ঁঠ":
        word = "ও"
        return word


    elif word == "ণুা":
        word = "ণ"
        return word

    elif word == "ওশ" or word == "ওঁ":
        word = "গু"
        return word


    for i in range (0,len(WordList)):

        try:
            listy.append(dict[WordList[i]])
        except:
            listy.append(WordList[i])

    for i in range (0,len(listy)):
        print "ya"


        #if word1[i]=='খ' or word1[i]=='থ' or word1[i]=='য' or word1[i]=='ষ' or word1[i]=='য়':
        if listy[i] == 'গ':
            if listy[i-1] != 'ু':

                distance = .8
                print "Entered 1 ----->>>>>>>>>>>>>>>>>>>>>>>>>>>>>------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                #return LavenShtein_Distance.LavenShtein_Distance(listy,distance)

            #print LavenShtein_Distance.LavenShtein_Distance(listy)
        elif listy[i] == 'য':
            print "Not>>>>>>>>>>>>>------Entered 2 ----->>>>>>>>>>>>>>>>>>>>>>>>>>>>>------------>>>>>>>>>>>>>>>>>>>"
            distance = .95

            #return LavenShtein_Distance.LavenShtein_Distance(listy,distance)

    return word