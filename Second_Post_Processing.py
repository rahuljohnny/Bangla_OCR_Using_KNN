#!/usr/bin/python
# -*- coding: utf-8 -*-
def Method1_Second_Post_Processing(li2):

    for i in range (0,len(li2)):
        if li2[i]=='.':
            del li2[i]
        if i>0 and li2[i-1]=='ে' and li2[i]=='া':
            li2[i-1]='শ'
            del li2[i]
        if i>1 and li2[i-2]=='ে' and li2[i]=='া':
            li2[i-2]=li2[i-1]
            li2[i-1]='ো'
            del li2[i]


    for i in range (0,len(li2)-2):
        if li2[i]=='ি' and li2[i+1]=='া':
            print i, "===>>", li2[i]

            li2[i]=li2[i+2]
            li2[i+1]='ি'
            del li2[i+2]

        #print i,"===>>",li2[i]


    for i in range (0,len(li2)):
        print i,"===>>",li2[i]

    for i in range (0,len(li2)-2):
        if li2[i] == 'ে':
            li2[i]=li2[i+1]
            li2[i+1]='ে'
            print i, ">>>>>>", li2[i]

    for i in range(0, len(li2)):
        if li2[i] == '$':
            li2[i] = 'ে'
        elif li2[i] == '0':
            li2[i] = 'ি'
        elif li2[i] == '.':
            del li2[i]


    return li2




