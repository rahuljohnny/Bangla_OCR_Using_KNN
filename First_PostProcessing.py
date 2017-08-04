#!/usr/bin/python
# -*- coding: utf-8 -*-
from importer import *
from Dictionary import *
from Second_Post_Processing import Method1_Second_Post_Processing



def Post_Processing(li2, str, imgTestingNumbers):
    #cv2.imshow("imgTestingNumbers",imgTestingNumbers)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    # if str=="NULL":
    # return "NULL" , "NULL" ,li2
    g = 0  # to send them in gutletters
    z = 0
    sho = 0
    print"In 17 th line of FPP"

    li3 = []
    li4 = []
    strFinalString9 = ''
    checker = ''
    strFinalString2 = ''
    ReturnString = ''

    # strFinalString2 , tempLi ,li2

    temp_ikar2 = ''.join(li2)
    if temp_ikar2 == 'নঠ':
        return 'এ', '', li2

    elif temp_ikar2 == 'ঁি':
        return 'ও', '', li2

    if temp_ikar2 == "া":
        return '।', '', li2


    elif temp_ikar2 == "ঁঠ":
        return 'ও', '', li2
        # strCurrentWord = "ও"

    elif temp_ikar2 == "ণুা":
        return 'ণ', '', li2

    elif temp_ikar2 == "ওশ":
        return 'গু', '', li2


    elif temp_ikar2 == "ঢূ" or temp_ikar2 == "ঢূ":
        return '?', '', li2

    ''' " . " after 'র' facts '''
    '''It should take place before e,i kar'''
    '''****************************************************************************************'''
    # '''


    try:

        '''================================================================'''

        for i in range(0, len(li2) - 1):  # ^ + ঢ = ট


            if li2[i] == '^':

                if li2[i + 1] == 'ঢ':
                    li2[i] = 'ট'
                    del li2[i + 1]

                elif li2[i + 1] == 'হ':
                    li2[i] = 'ই'
                    del li2[i + 1]
                    for k in range (0,len(li2)):
                        print"28APRIL li2==>", li2[k]

                elif li2[i + 1] == 'ঈ':
                    li2[i] = 'ঈ'
                    del li2[i + 1]

                if li2[i + 1] == 'হ':
                    li2[i] = 'ই'
                    del li2[i + 1]

                if li2[i + 1] == 'ড':
                    li2[i] = 'উ'
                    del li2[i + 1]

                if li2[i + 1] == 'ঊ':
                    li2[i] = 'ঊ'
                    del li2[i + 1]


                elif li2[i + 1] == 'ঈ':

                    li2[i] = 'ঈ'
                    del li2[i + 1]



                elif li2[i + 1] == 'ঢ':
                    print "Entered into D"
                    li2[i] = 'ট'
                    del li2[i + 1]




                elif li2[i + 1] == 'ঢু':
                    li2[i] = 'টু'

                elif li2[i + 1] == 'ঢূ':
                    li2[i] = 'টূ'
                    del li2[i + 1]



                elif li2[i + 1] == 'ঢ':
                    print "Entered into D"
                    li2[i] = 'ট'
                    del li2[i + 1]




                elif li2[i + 1] == 'ঢু':
                    li2[i] = 'টু'
                    del li2[i + 1]


                elif li2[i + 1] == 'ঢূ':
                    li2[i] = 'টূ'
                    del li2[i + 1]


                elif li2[i + 1] == 'ন্ট':
                    li2[i] = 'ন্ট'
                    del li2[i + 1]


                elif li2[i + 1] == 'ন্টু':
                    li2[i] = 'ন্টু'
                    del li2[i + 1]


                elif li2[i + 1] == 'ন্টূ':
                    li2[i] = 'ন্টূ'
                    del li2[i + 1]


                elif li2[i + 1] == 'প্ট':
                    li2[i] = 'প্ট'
                    del li2[i + 1]






                elif li2[i + 1] == 'ট্ট':

                    li2[i] = 'ট্ট'
                    del li2[i + 1]



                elif li2[i + 1] == 'ট্র':

                    li2[i] = 'ট্র'
                    del li2[i + 1]



                elif li2[i + 1] == 'ট্টু':

                    li2[i] = 'ট্টু'
                    del li2[i + 1]



                elif li2[i + 1] == 'স্ট':

                    li2[i] = 'স্ট'
                    del li2[i + 1]



                elif li2[i + 1] == 'স্টু':

                    li2[i] = 'স্টু'
                    del li2[i + 1]


                elif li2[i + 1] == 'স্টূ':

                    li2[i] = 'স্টূ'
                    del li2[i + 1]


                elif li2[i + 1] == 'স্ট্র':

                    li2[i] = 'স্ট্র'
                    del li2[i + 1]


                elif li2[i + 1] == 'স্ট্রু':

                    li2[i] = 'স্ট্রু'
                    del li2[i + 1]


                elif li2[i + 1] == 'ষ্ট':

                    li2[i] = 'ষ্ট'
                    del li2[i + 1]


                elif li2[i + 1] == 'ষ্ট্র':

                    li2[i] = 'ষ্ট্র'
                    del li2[i + 1]


                elif li2[i + 1] == 'ণ্ট':

                    li2[i] = 'ণ্ট'

                    del li2[i + 1]

                elif li2[i + 1] == 'ড':
                    li2[i] = 'উ'
                    del li2[i + 1]




                elif li2[i + 1] == 'ভ':
                    li2[i] = 'উ'
                    # checker = ''.join(li2[i])
                    del li2[i + 1]





                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''
                '''ADD all others'''

            if li2[i] == 'A' :
                if li2[i + 2] == 'ঢ':
                    if li2[i + 1] == 'া':
                        li2[i] = 'ট'
                        li2[i + 1] = 'ি'
                        del li2[i+2]

                elif li2[i + 2] == 'ঠ':
                    if li2[i + 1] == 'া':
                        li2[i] = 'ঠ'
                        li2[i + 1] = 'ি'
                        del li2[i+2]

        for k in range(0, len(li2)):
            print"28APRIL li2 V2==>", li2[k]

        print"In 271st line of FPP"

        '''EXperimental'''
        for i in range(1, len(li2)):

            if li2[i] == '^' or li2[i] == '%':

                if li2[i - 1] == 'হ':
                    li2[i - 1] = 'ই'
                    del li2[i]

                elif li2[i - 1] == 'ঢ্র':
                    li2[i-1] = 'ট্র'
                    del li2[i]

                if li2[i - 1] == 'ড':
                    li2[i - 1] = 'উ'
                    del li2[i]

                if li2[i - 1] == 'ঊ':
                    li2[i - 1] = 'ঊ'
                    del li2[i]

                elif li2[i - 1] == 'ঈ':
                    li2[i - 1] = 'ঈ'

                    del li2[i]

                elif li2[i - 1] == 'ঢ':
                    print "Entered into D"
                    li2[i - 1] = 'ট'
                    del li2[i]



                elif li2[i - 1] == 'ঢু':
                    li2[i - 1] = 'টু'
                    del li2[i]

                elif li2[i - 1] == 'ঢূ':
                    li2[i - 1] = 'টূ'
                    del li2[i]


                elif li2[i - 1] == 'ঢ':
                    print "Entered into D"
                    li2[i - 1] = 'ট'
                    del li2[i]



                elif li2[i - 1] == 'ঢু':
                    li2[i - 1] = 'টু'
                    del li2[i]

                elif li2[i - 1] == 'ঢূ':
                    li2[i - 1] = 'টূ'
                    del li2[i]



                elif li2[i - 1] == 'ন্টু':
                    li2[i - 1] = 'ন্টু'
                    del li2[i]

                elif li2[i - 1] == 'ন্টূ':
                    li2[i - 1] = 'ন্টূ'
                    del li2[i]
                elif li2[i - 1] == 'প্ট':
                    li2[i - 1] = 'প্ট'
                    del li2[i]





                elif li2[i - 1] == 'ট্ট':

                    li2[i - 1] = 'ট্ট'
                    del li2[i]


                elif li2[i - 1] == 'ট্র':

                    li2[i - 1] = 'ট্র'
                    del li2[i]


                elif li2[i - 1] == 'ট্টু':

                    li2[i - 1] = 'ট্টু'
                    del li2[i]


                elif li2[i - 1] == 'স্ট':

                    li2[i - 1] = 'স্ট'
                    del li2[i]


                elif li2[i - 1] == 'স্টু':

                    li2[i - 1] = 'স্টু'
                    del li2[i]

                elif li2[i - 1] == 'স্টূ':

                    li2[i - 1] = 'স্টূ'
                    del li2[i]

                elif li2[i - 1] == 'স্ট্র':

                    li2[i - 1] = 'স্ট্র'
                    del li2[i]

                elif li2[i - 1] == 'স্ট্রু':

                    li2[i - 1] = 'স্ট্রু'
                    del li2[i]

                elif li2[i - 1] == 'ষ্ট':

                    li2[i - 1] = 'ষ্ট'
                    del li2[i]

                elif li2[i - 1] == 'ষ্ট্র':

                    li2[i - 1] = 'ষ্ট্র'
                    del li2[i]

                elif li2[i - 1] == 'ণ্ট':

                    li2[i - 1] = 'ণ্ট'
                    del li2[i]



                elif li2[i - 1] == 'ড':
                    li2[i - 1] = 'উ'
                    del li2[i]





                elif li2[i - 1] == 'ভ':
                    li2[i - 1] = 'উ'
                    del li2[i]

                    # checker = ''.join(li2[i])

                elif li2[i - 1] == 'U':
                    li2[i - 1] = 'ঊ'

                    del li2[i]

            if li2[i - 1] == 'ণু' and li2[i] == 'া':
                li2[i - 1] = 'ণ'
                del li2[i]
                '''====================================================================='''

                j = i + 1

            if i > 0:
                checker = ''.join(li2[i])
                if li2[i - 1] == 'ড' and li2[i] == '^':

                    li2[i - 1] = 'উ'
                    # checker = ''.join(li2[i])
                    del li2[i]
                    cv2.imshow("u_first_pro")
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()


                elif li2[i - 1] == 'ঊ' and li2[i] == '^':
                    li2[i - 1] = 'ঊ'
                    del li2[i]

                elif li2[i - 1] == 'ঐ' and li2[i]=='ে':
                    del li2[i]

                elif li2[i - 1] == 'ঐ' and li2[i] == '^':
                    del li2[i]

                elif li2[i - 1] == 'ভ' and li2[i] == '^':
                    li2[i - 1] = 'উ'
                    del li2[i]

                if li2[i - 1] == 'ঠ' and li2[i] == '"':
                    del li2[i]

                if li2[i - 1] == '"' and li2[i] == 'ঠ':
                    li2[i - 1] = 'ঠ'
                    del li2[i]

        '''EXperimental'''


        for i in range(1, len(li2)):  # ekar
            if li2[i]=='র্':
                li2[i]=li2[i-1]
                li2[i-1]='র্'



        for i in range(0, len(li2) - 1):

            if li2[i] == 'ন্ট' and li2[i + 1] == '^':
                del li2[i + 1]

            if li2[i] == 'ণ্র' and li2[i + 1] == 'গ':
                li2[i] = 'গ্র'
                del li2[i + 1]



            if i < len(li2) - 1:

                if li2[i] == "গ" and (
                                    li2[i + 1] == "া" or li2[i + 1] == "ষ" or li2[i + 1] == "স" or li2[i + 1] == "প" or
                        li2[i + 1] == "ণু"):
                    '''
                    cv2.imshow("imgTestingNum",imgTestingNumbers)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    '''
                    g = 1
                    del li2[i + 1]

                # bo+.=ro handling

                if li2[i + 1] == '.':

                    if (li2[i] == 'র' or li2[i] == 'য়' or li2[i] == 'ড়' or li2[i] == 'ঢ়'):
                        1

                    elif (li2[i] == 'ব'):
                        li2[i] = 'র'
                    elif li2[i] == 'য':
                        li2[i] = 'য়'
                    elif li2[i] == 'ড':

                        '''
                        cv2.imshow("Entered",imgTestingNumbers)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        '''
                        li2[i] = 'ড়'
                    elif li2[i] == 'ঢ':
                        li2[i] = 'ঢ়'

                    del li2[i + 1]

                elif li2[i + 1] == 'শু':
                    if li2[i] == 'শ':
                        del li2[i + 1]

                try:
                    if li2[i + 1] == 'া':




                        if li2[i] == '^' and li2[i - 2] == 'ে':
                            li2[i - 2] = li2[i - 1]
                            li2[i - 1] = 'ৌ'
                            del li2[i]
                            del li2[i]  # as the firdt one ids deleted,del li2[i + 1] will be changed to del li2[i]

                        if (li2[i] == '.'):
                            li2[i] = 'ণ'
                            del li2[i + 1]

                    if li2[i] == 'ও' and li2[i + 1] == '"':
                        del li2[i + 1]

                    if li2[i] == 'গু' and li2[i + 1] == 'গ':
                        del li2[i + 1]

                    if li2[i] == 'ড' and li2[i - 1] == '^':
                        li2[i - 1] = 'উ'
                        # checker = ''.join(li2[i])
                        del li2[i]

                    if li2[i] == 'ঊ' and li2[i - 1] == '^':
                        li2[i - 1] = 'ঊ'
                        del li2[i]



                except:
                    1

            if i > 1 and i < len(li2) - 1:
                print "li2[i]=========================", li2[i]
                print "li2[i-2]=========================", li2[i - 2]
                print "li2[i+1]=========================", li2[i + 1]
                if (li2[i] == '^' and li2[i - 2] == 'ে' and li2[i + 1] == 'া'):
                    li2[i - 2] = li2[i - 1]
                    li2[i - 1] = 'ৌ'
                    del li2[i]
                    del li2[
                        i]  # it was li2[i+1] but as I deleted the previous element of the list,the i+1 turned into i,i+4 will be changed to i+3

        ''' "া", "ি" facts '''
        '''****************************************************************************************'''
        print"In 574 th line of FPP"

        '''29 APRIL EDITS'''

        for i in range(0, len(li2) - 1):

            if li2[i] == 'ড':
                if i > 0:
                    if li2[i - 1] == '^':
                        li2[i - 1] = 'উ'
                        del li2[i]

                '''
                cv2.imshow("u_first_pro",imgTestingNumbers)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                '''

                if li2[i + 1] == '^':
                    li2[i] = 'উ'
                elif li2[i + 1] == '.':
                    li2[i] = 'ড়'
                    # checker = ''.join(li2[i])
                    del li2[i + 1]

            if li2[i] == 'ঊ' and li2[i + 1] == '^':
                li2[i] = 'ঊ'
                del li2[i + 1]

            if li2[i] == 'ে' and li2[i + 1] == 'া' and sho==0:
                li2[i] = 'শ'
                sho=1
                del li2[i + 1]

        for i in range(0, len(li2) - 1):  # ekar

            if li2[i] == 'ে':
                print li2[i + 1]
                li2[i] = li2[i + 1]  # ok till here
                li2[i + 1] = '$'
                i = i + 1
            # else:
            '''All kars with their refs and to s'''
            if i > 1:
                if li2[i] == 'ঢ' and li2[i - 1] == 'া' and li2[i - 2] == '1268':
                    print"&&&&&&&&&&&&&&&&&&   1268   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
                    li2[i - 1] = 'ি'
                    li2[i - 2] = 'ট'
                    del li2[i]




        for i in range(0, len(li2) - 3):
            if li2[i] == "া" and li2[i + 1] == "ি" and li2[i + 2] == "া":
                li2[i + 1] = li2[i + 3]
                li2[i + 2] = "0"
                del li2[i + 3]
                i = i + 2

        ''' "আ" facts '''
        '''****************************************************************************************'''
        for i in range(0, len(li2) - 2):
            if li2[i] == "অ" and li2[i + 1] == "া":
                # print i, "--i  , Entered 2 ???###----------------------------------"
                li2[i] = "আ"
                del li2[i + 1]
                i = i + 1

        '''Removing "া" after "ি" and "ী"  (1st time)  '''
        '''******************************************************'''

        for i in range(0, len(li2)):  #

            if li2[i] == '$':
                li2[i] = 'ে'

        for i in range(0, len(li2) - 1):  # sho, go

            try:
                print i, "-->i , iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii", li2[i]
                '''
                if li2[i] == "এ" and  ( li2[i + 1] == "া" or  li2[i + 1] == '"'):
                    del li2[i+1]
                    #i = i + 1
                '''
                if li2[i] == "শ" and li2[i + 1] == "া" and sho==0:
                    sho=1
                    del li2[i + 1]
                    # i = i + 1

                if li2[i] == "য":
                    z = 1

                if li2[i] == "এ":
                    if li2[i + 1] == "শ":
                        print" শ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্র "
                        li2[i] = "শ্র"
                        del li2[i + 1]

                    elif li2[i + 2] == "শ":
                        print" শ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্রশ্র "
                        li2[i] = "শ্র"
                        del li2[i + 2]

                if li2[i + 1] == "শ" and li2[i] == "শ্র":
                    del li2[i + 1]
                    # i = i + 1
            except:
                1

        for i in range(0, len(li2) - 3):  #
            if i + 1 < len(li2) - 2:
                # try:
                print "li 1:", li2[i], "             li 2:", li2[i + 1]
                if (li2[i] == '^' or li2[i] == '%') and li2[i + 1] == 'ে':
                    # checker = ''.join(li2[i])
                    print "checker        10:   ", checker
                    li2[i] = li2[i + 2]
                    li2[i + 1] = 'ৈ'
                    del li2[i + 2]
                    i = i + 1

        j = 0



        for i in range(1, len(li2) - 1):  # ikar


            if li2[i] == "া":

                if li2[i - 1] == "ি":
                    # print "bolchi test 1======================================="
                    li2[i - 1] = li2[i + 1]
                    li2[i] = "0"
                    del li2[i + 1]


                elif li2[i - 1] == "ী":
                    # print "bolchi test 1======================================="
                    del li2[i]




        tempLi = ''
        if li2[len(li2) - 1] == 'ে' or li2[len(li2) - 1] == 'গু':
            print "tempekar  "
            # tempLi = li2[len(li2) - 1]
            tempLi = ''.join(li2[len(li2) - 1])
            # del li2[len(li2) - 1]



        for i in range(0, len(li2)):
            if li2[i] == '0':
                li2[i] = 'ি'

            elif li2[i] == '$':
                li2[i] = 'ে'

        '''Removing an extra "া" after "ি" and "ী" (2nd time) '''
        '''******************************************************'''

        for i in range(1, len(li2)-1):  # ikar

                if li2[i] == "া":
                    if li2[i - 1] == "ি":
                        li2[i-1]=li2[i+1]
                        li2[i]='ি'
                        del li2[i]

                if li2[i+1]=='া':
                    if li2[i] == "ী":
                        del li2[i+1]

        for i in range(0, len(li2) - 1):  # ekar
            if li2[i] == '.':
                del li2[i]

        for i in range(0, len(li2) - 1):  # ekar
            if li2[i] == '.':
                del li2[i]

            if i < len(li2):
                if li2[i] == 'এ' and li2[i + 1] == 'ে':
                    del li2[i + 1]

                if li2[i] == 'এ' and li2[i + 1] == 'া':
                    li2[i] = 'গ্রা'
                    del li2[i + 1]

                if li2[i] == 'শু' and li2[i + 1] == 'শ':
                    print"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%eeeeeeEEEEEEEEEEEEEEEEEEEEEEEEEEE"

                    del li2[i + 1]



        for i in range(1, len(li2)):  # if ^ is located before u,U,....

            if li2[i-1] == 'ৎ' and li2[i] == 'ে':
                li2[i-1] = 'চ্ছ'

            if li2[i-1] == 'ৎ' and li2[i] == 'ি':
                li2[i-1] = 'চ্ছ'



        '''VVI
               if(temp_ekar):

                    hoy-
                   strFinalString22[0] = strFinalString2[0]
                   strFinalString22[1] = "ekar"
                   for i in range(0,len(strFinalString2)):
                       strFinalString22[i+2]=strFinalString22[i]

                     li22[0]=li2[0]

                     othoba -

                   li22[1]='ekar'
                   np.roll(li2, 1)
                   for i in range(0, len(li2)-2):
                       li22[i+1] = li2[i]


        '''

        checker = ''
        strFinalString2 = ''.join(li2)

        ReturnString = '-1'

        print"In 808 th line of FPP"


    except:
        if len(strFinalString2)==0:
            new_li2 = Method1_Second_Post_Processing(li2)

            #strFinalString3 = ''.join(li2)#new_lii2
            strFinalString3 = ''.join(new_li2)#new_lii2
            print"hard to decode the image initially ! , len(li2)", len(new_li2), "strFinalString3==>", strFinalString3

            return strFinalString3,"", new_li2

        '''April 20'''


    try:

        print  "4.strFinalString2:   ", strFinalString2
        print  "temp_ikar2:   ", temp_ikar2

        '''
        cv2.imshow("tnt_0_6_imgTestingNumbers",imgTestingNumbers)
        cv2.waitKey(0)
        #cv2.destroyWindow("tnt_0_6_imgTestingNumbers")
        #cv2.destroyAllWindows()
        #'''
        ReturnString = 'Y'

        # return strFinalString2
    except:

        print"hard to decode the image finally!!"
        for ii in range(0, len(li3)):
            li4.append(dict[li3[ii]])
            strFinalString9 = ''.join(li4)

        print strFinalString9
        ReturnString = 'N'
        # return strFinalString9

    if ReturnString == 'Y':

        return strFinalString2, '', li2


    elif ReturnString == 'N':

        return strFinalString9, tempLi, li2

    return strFinalString2, tempLi, li2