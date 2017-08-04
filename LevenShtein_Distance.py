#!/usr/bin/python
# -*- coding: utf-8 -*-
import All_Possible_Words
import difflib


def LavenShtein_Distance(word,distance):
    word1 = ''
    word1 = ''.join(word)
    print "ya ",word1

    list = []
    maxi = -99
    for i in range(0,len(All_Possible_Words.words)):
        temp = difflib.SequenceMatcher(None, word1, All_Possible_Words.words[i]).ratio()
        if temp > maxi:
            index = i
            maxi = temp

    if maxi >= distance:

        k=0
        MultiWords=''
        for i in range(0,len(All_Possible_Words.words)):

            temp = difflib.SequenceMatcher(None, word1, All_Possible_Words.words[i]).ratio()
            if temp == maxi and k < 4:

                k=k+1
                list.append(All_Possible_Words.words[i])

                list.append(" / ")
        del list[len(list)-1]
        MultiWords = ''.join(list)

        #print index,"<===index,===========maxi",maxi," word ",All_Possible_Words.words[index]
        if k>1:
            return MultiWords
        else :
            return All_Possible_Words.words[index]

    else:

        return word1



'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
import All_Possible_Words
import difflib
maxi = -99
for i in range(0,len(All_Possible_Words.words)):
    temp = difflib.SequenceMatcher(None, 'আগুন', All_Possible_Words.words[i]).ratio()
    if temp > maxi:
        index = i
        maxi = temp
print index,"<===index,===========maxi",maxi," word ",All_Possible_Words.words[index]

'''