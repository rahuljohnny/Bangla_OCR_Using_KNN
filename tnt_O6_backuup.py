#!/usr/bin/python
# -*- coding: utf-8 -*-
from class_contour import *
from Dictionary import *
from importer import *
import GutLetters

import O6

# module level variables ##########################################################################
list6 = []
arr3 = []
arr4 = []
count = 0


###################################################################################################
###################################################################################################

def Mega_Segmenter2(cou, imgTestingNumbers):
    allContoursWithData = []  # declare empty lists,
    validContoursWithData = []  # we will fill these shortly

    try:
        npaClassifications = np.loadtxt("classifications.txt", np.float32)  # read in training classifications
    except:
        print "error, unable to open classifications.txt, exiting program\n"
        os.system("pause")
        return
    # end try

    try:
        npaFlattenedImages = np.loadtxt("flattened_images.txt", np.float32)  # read in training images
    except:
        print "error, unable to open flattened_images.txt, exiting program\n"
        os.system("pause")
        return
    # end try

    npaClassifications = npaClassifications.reshape(
        (npaClassifications.size, 1))  # reshape numpy array to 1d, necessary to pass to call to train

    kNearest = cv2.ml.KNearest_create()  # instantiate KNN object
    kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)

    # cv2.imwrite("6_wordseg.png",image3)
    # imgTestingNumbers = cv2.imread("6_wordseg.png")          # read in testing numbers image
    # cv2.floodFill(imgTestingNumbers,)



    if imgTestingNumbers is None:  # if image was not read successfully
        print "tnt_O_6_line_49_error: image not read from file \n\n"  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit function (which exits program)
    # end if
    '''
    cv2.imshow("#####TNT",imgTestingNumbers)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #'''
    # gray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)
    # imgBlurred = cv2.GaussianBlur(gray, (5,5), 0)                    # blur
    # cv2.imshow("tnt_blurred",imgBlurred)

    ret, imgThresh = cv2.threshold(imgTestingNumbers, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    imgThreshCopy = imgThresh.copy()  # make a copy of the thresh image, this in necessary b/c findContours modifies the image

    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                              # input image, make sure to use a copy since the function will modify this image in the course of finding contours
                                                              cv2.RETR_EXTERNAL,  # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE)  # compress horizontal, vertical, and diagonal segments and leave only their end points

    for npaContour in npaContours:  # for each contour
        contourWithData = ContourWithData()  # instantiate a contour with data object
        contourWithData.npaContour = npaContour  # assign contour to contour with data
        contourWithData.boundingRect = cv2.boundingRect(contourWithData.npaContour)  # get the bounding rect
        contourWithData.calculateRectTopLeftPointAndWidthAndHeight()  # get bounding rect info
        contourWithData.fltArea = cv2.contourArea(contourWithData.npaContour)  # calculate the contour area
        allContoursWithData.append(contourWithData)  # add contour with data object to list of all contours with data
    # end for

    for contourWithData in allContoursWithData:  # for all contours
        if contourWithData.checkIfContourIsValid():  # check if valid
            validContoursWithData.append(contourWithData)  # if so, append to valid contour list
            # end if
    # end for

    validContoursWithData.sort(key=operator.attrgetter("intRectX"))  # sort contours from left to right

    # strFinalString = ""         # declare final string, this will have the final number sequence by the end of the program
    strFinalStringEng = ""
    strFinalString9 = ""
    # newcharString = ""
    # temp_ikar2 = ""
    checker = ""
    c = 0
    li2 = []
    li3 = []
    li4 = []
    for contourWithData in validContoursWithData:  # for each contour
        # draw a green rect around the current char


        cv2.rectangle(imgTestingNumbers,  # draw rectangle on original testing image
                      (contourWithData.intRectX, contourWithData.intRectY),  # upper left corner
                      (contourWithData.intRectX + contourWithData.intRectWidth,
                       contourWithData.intRectY + contourWithData.intRectHeight),  # lower right corner
                      (0, 255, 0),
                      2)  # thickness

        imgROI = imgThresh[contourWithData.intRectY: contourWithData.intRectY + contourWithData.intRectHeight,
                 # crop char out of threshold image
                 contourWithData.intRectX: contourWithData.intRectX + contourWithData.intRectWidth]

        imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH,
                                            RESIZED_IMAGE_HEIGHT))  # resize image, this will be more consistent for recognition and storage
        # keep on for checking

        list6.append(imgROI)

        npaROIResized = imgROIResized.reshape(
            (1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))  # flatten image into 1d numpy array

        npaROIResized = np.float32(npaROIResized)  # convert from 1d numpy array of ints to 1d numpy array of floats

        '''
        cv2.imshow("tnt_piece",imgROIResized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.destroyWindow("tnt")
        #'''

        retval, npaResults, neigh_resp, dists = kNearest.findNearest(npaROIResized,
                                                                     k=1)  # call KNN function find_nearest

        strCurrentChar = int(npaResults[0][0])  # get character from results

        if strCurrentChar < 500:
            strCurrentChar = str(chr(strCurrentChar))

        else:
            strCurrentChar = str(strCurrentChar)

        if strCurrentChar == "." or strCurrentChar == "!":
            height_of_ROI, width_of_ROI = imgROI.shape
            if height_of_ROI < 2 * width_of_ROI:

                strCurrentChar = "."


            else:
                strCurrentChar = strCurrentChar

        if strCurrentChar == "$":
            height_of_ROI, width_of_ROI = imgROI.shape
            print height_of_ROI, "<<==height_of_ROI ++++++++++++++++++++++++++++++++++ width_of_ROI==>>", width_of_ROI
            if height_of_ROI < 1.2 * width_of_ROI:  # cause point's size varies
                strCurrentChar = "."

            else:
                strCurrentChar = strCurrentChar

        try:
            li2.append(dict[strCurrentChar])
            li3.append(strCurrentChar)
        except:
            li2.append(strCurrentChar)

        strFinalStringEng = strFinalStringEng + strCurrentChar
        print "strFinalStringEng", strFinalStringEng
        '''========================================================================='''
    '''Text Generation (do in another function)'''

    temp_ikar2 = ''.join(li2)

    '''***********************************************************************************************'''
    '''************************************  POSTPROCESSING  *****************************************'''
    '''***********************************************************************************************'''

    ''' " . " after 'র' facts '''
    '''It should take place before e,i kar'''
    '''****************************************************************************************'''
    # '''
    try:

        for i in range(0, len(li2) - 1):
            if i < len(li2) - 1:

                if li2[i + 1] == '.':

                    if (li2[i] == 'র' or li2[i] == 'য়' or li2[i] == 'ড়' or li2[i] == 'ঢ়'):
                        1

                    elif (li2[i] == 'ব'):
                        li2[i] = 'র'
                    elif li2[i] == 'য':
                        li2[i] = 'য়'
                    elif li2[i] == 'ড':
                        li2[i] = 'ড়'
                    elif li2[i] == 'ঢ':
                        li2[i] = 'ঢ়'

                    del li2[i + 1]
                elif li2[i + 1] == 'শু':
                    if li2[i] == 'শ':
                        del li2[i + 1]

                try:
                    if li2[i + 1] == 'া':
                        if (li2[i] == '.'):
                            li2[i] = 'ণ'
                            del li2[i + 1]

                        elif li2[i] == '^':
                            li2[i] = 'ৌ'
                            del li2[i + 1]

                    if li2[i] == 'ও' and li2[i + 1] == '"':
                        del li2[i + 1]

                    if li2[i] == 'গু' and li2[i + 1] == 'গ':
                        del li2[i + 1]



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

        for i in range(0, len(li2) - 1):  # ikar

            try:
                if li2[i] == "া":

                    if li2[i - 1] == "ি":
                        # print "bolchi test 1======================================="
                        li2[i - 1] = li2[i + 1]
                        li2[i] = "0"
                        del li2[i + 1]


                    elif li2[i - 1] == "ী":
                        # print "bolchi test 1======================================="
                        del li2[i]

            except:
                1

        for i in range(0, len(li2) - 1):  # sho, go

            try:
                print i, "-->i , iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii", li2[i]
                '''
                if li2[i] == "এ" and  ( li2[i + 1] == "া" or  li2[i + 1] == '"'):
                    del li2[i+1]
                    #i = i + 1
                '''
                if li2[i] == "শ" and li2[i + 1] == "া":
                    del li2[i + 1]
                    # i = i + 1

                if li2[i] == "গ" and li2[i + 1] == "া":
                    del li2[i + 1]

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

        for i in range(0, len(li2) - 1):  #
            if i <= len(li2) - 1:

                if li2[i] == '^' or li2[i] == '%':
                    checker = ''.join(li2[i])
                    print  "Checker no. 9   ==>", checker
                    # checker = ""

                    if li2[i + 1] == 'হ':
                        li2[i] = 'ই'

                    elif li2[i + 1] == 'ঈ':
                        li2[i] = 'ঈ'

                    elif li2[i + 1] == 'ঢ':
                        print "Entered into D"
                        li2[i] = 'ট'



                    elif li2[i + 1] == 'ঢু':
                        li2[i] = 'টু'

                    elif li2[i + 1] == 'ঢূ':
                        li2[i] = 'টূ'


                    elif li2[i + 1] == 'ঢ':
                        print "Entered into D"
                        li2[i] = 'ট'



                    elif li2[i + 1] == 'ঢু':
                        li2[i] = 'টু'

                    elif li2[i + 1] == 'ঢূ':
                        li2[i] = 'টূ'

                    elif li2[i + 1] == 'ন্ট':
                        li2[i] = 'ন্ট'

                    elif li2[i + 1] == 'ন্টু':
                        li2[i] = 'ন্টু'

                    elif li2[i + 1] == 'ন্টূ':
                        li2[i] = 'ন্টূ'
                    elif li2[i + 1] == 'প্ট':
                        li2[i] = 'প্ট'





                    elif li2[i + 1] == 'ট্ট':

                        li2[i] = 'ট্ট'


                    elif li2[i + 1] == 'ট্র':

                        li2[i] = 'ট্র'


                    elif li2[i + 1] == 'ট্টু':

                        li2[i] = 'ট্টু'


                    elif li2[i + 1] == 'স্ট':

                        li2[i] = 'স্ট'


                    elif li2[i + 1] == 'স্টু':

                        li2[i] = 'স্টু'

                    elif li2[i + 1] == 'স্টূ':

                        li2[i] = 'স্টূ'

                    elif li2[i + 1] == 'স্ট্র':

                        li2[i] = 'স্ট্র'

                    elif li2[i + 1] == 'স্ট্রু':

                        li2[i] = 'স্ট্রু'

                    elif li2[i + 1] == 'ষ্ট':

                        li2[i] = 'ষ্ট'

                    elif li2[i + 1] == 'ষ্ট্র':

                        li2[i] = 'ষ্ট্র'

                    elif li2[i + 1] == 'ণ্ট':

                        li2[i] = 'ণ্ট'


                    elif li2[i + 1] == 'ড':
                        li2[i] = 'উ'


                    elif li2[i + 1] == 'ভ':
                        li2[i] = 'উ'
                        # checker = ''.join(li2[i])

                    elif li2[i + 1] == 'U':
                        li2[i] = 'ঊ'

                    del li2[i + 1]

                    # i = i+1

                j = i + 1

                try:
                    checker = ''.join(li2[i])
                    if li2[i] == 'ড' and li2[i + 1] == '^':
                        li2[i] = 'উ'
                        # checker = ''.join(li2[i])
                        del li2[i + 1]


                    elif li2[i] == 'U' and li2[i + 1] == '^':
                        li2[i] = 'ঊ'
                        del li2[i + 1]

                    elif li2[i] == 'ভ' and li2[i + 1] == '^':
                        li2[i] = 'উ'
                        del li2[i + 1]

                    if li2[i] == 'ঠ' and  li2[i + 1] == '"':
                        del li2[i + 1]

                    if li2[i] == '' and li2[i + 1] == '1032':
                        del li2[i + 1]




                except:
                    1

            for ii in range(0, len(li2)):
                print i, "i      LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL", li2[
                    ii]  # till here compartment is found

        tempLi = ''
        if li2[len(li2) - 1] == 'ে' or li2[len(li2) - 1] =='গু':
            print "tempekar  "
            #tempLi = li2[len(li2) - 1]
            tempLi = ''.join(li2[len(li2) - 1])
            #del li2[len(li2) - 1]

        for i in range(0, len(li2) - 1):  # ekar

            if  li2[i] == 'ে':
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

        for i in range(0, len(li2)):
            if li2[i] == '0':
                li2[i] = 'ি'

            elif li2[i] == '$':
                li2[i] = 'ে'
        '''
        cv2.imshow("3 #####TNT", imgTestingNumbers)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''
        '''Removing an extra "া" after "ি" and "ী" (2nd time) '''
        '''******************************************************'''

        for i in range(0, len(li2)):  # ikar

            try:
                if li2[i] == "া":
                    if li2[i - 1] == "ি" or li2[i - 1] == "ী":
                        del li2[i]
            except:
                1

        for i in range(0, len(li2) - 1):  # ekar
            if li2[i] == '.':
                del li2[i]

            if i < len(li2):
                if li2[i] == 'এ' and li2[i + 1] == 'ে':
                    print"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%eeeeeeEEEEEEEEEEEEEEEEEEEEEEEEEEE"

                    del li2[i + 1]
                if li2[i] == 'শু' and li2[i + 1] == 'শ':
                    print"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%eeeeeeEEEEEEEEEEEEEEEEEEEEEEEEEEE"

                    del li2[i + 1]

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



        strFinalString2 = ''.join(li2)

        ReturnString = '-1'

    except:
        print"hard to decode the image initially !"

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

        #return strFinalString2
    except:

        print"hard to decode the image finally!!"
        for ii in range(0, len(li3)):

            li4.append(dict[li3[ii]])
            strFinalString9 = ''.join(li4)

        print strFinalString9
        ReturnString = 'N'
        #return strFinalString9


    if ReturnString =='Y':

        strFinalString2 = GutLetters.GutLetters(li2)
        return strFinalString2,tempLi


    elif ReturnString =='N':

        strFinalString9 = GutLetters.GutLetters(li2)
        return strFinalString9,tempLi

###################################################################################################

# end if
