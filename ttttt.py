#!/usr/bin/python
# -*- coding: utf-8 -*-
li2=[]
li3=[]
strFinalString2=''
with open("a.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)


for i in range(0, len(array)):  # ekar

    print "'%s," % (array[i])
