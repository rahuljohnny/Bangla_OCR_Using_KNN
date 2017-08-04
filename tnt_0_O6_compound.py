#!/usr/bin/python
# -*- coding: utf-8 -*-
from class_contour import *
from Dictionary import *
from importer import *
import GutLetters
import First_PostProcessing

import O6

# module level variables ##########################################################################
list6 = []
arr3 = []
arr4 = []
count = 0
dot = 0
cap = 0
per = 0



###################################################################################################
###################################################################################################

def Mega_Segmenter2(cou, imgTestingNumbers):
    imgTestingNumbersT = imgTestingNumbers.copy()

    ll=0
    ii = 0
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
    try:

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
        cv2.waitKey(600)
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
                          (0, 0, 255),
                          2)  # thickness

            imgROI = imgThresh[contourWithData.intRectY: contourWithData.intRectY + contourWithData.intRectHeight,
                     #Crop char out of threshold image
                     contourWithData.intRectX: contourWithData.intRectX + contourWithData.intRectWidth]


            #if h < 2 and w < 3:
                #return First_PostProcessing.Post_Processing(li2, "NULL", imgTestingNumbersT)

            imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH , RESIZED_IMAGE_HEIGHT))  # resize image, this will be more consistent for recognition and storage
            # keep on for checking

            list6.append(imgROI)

            npaROIResized = imgROIResized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))  # flatten image into 1d numpy array

            npaROIResized = np.float32(npaROIResized)  # convert from 1d numpy array of ints to 1d numpy array of floats



            '''
            cv2.imshow("tnt_piece",imgROIResized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.destroyWindow("tnt")
            #'''

            retval, npaResults, neigh_resp, dists = kNearest.findNearest(npaROIResized, k = 1)  # calling KNN function's find_nearest

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
                    1
            ll = ll + 1

            if strCurrentChar == "$":
                height_of_ROI, width_of_ROI = imgROI.shape
                print height_of_ROI, "<<==height_of_ROI ++++++++++++++++++++++++++++++++++ width_of_ROI==>>", width_of_ROI
                if height_of_ROI < 1.2 * width_of_ROI:  # cause point's size varies
                    strCurrentChar = "."

                else:
                    strCurrentChar = strCurrentChar



                '''==================== The else part ============================================'''


            try:
                li2.append(dict[strCurrentChar])
                #li3.append(strCurrentChar)
            except:
                li2.append(strCurrentChar)

            for i in range(0, len(li2)):
                print "KKR2=============", li2[i]


            if dot==0:
                strFinalStringEng = strFinalStringEng + strCurrentChar
            print "strFinalStringEng", strFinalStringEng
            '''
            if strCurrentChar == 'এ':
                print" \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\",
                index3 = ll
                width_of_ROI_of_e = width_of_ROI
                strCurrentChar = strCurrentChar
            # '''
            print"''''''''''''''''''''''''strCurrentChar '''''",strCurrentChar

        word,tailWord,listR= First_PostProcessing.Post_Processing(li2,strFinalStringEng,imgTestingNumbersT)
        print"tnt_O6 Received word from First_PostProcessing which's len=",len(word)
        if len(word)!=0:
            #return First_PostProcessing.Post_Processing(li2,strFinalStringEng,imgTestingNumbersT)
            return word,tailWord,listR
        #else :
        print"AAAAAAAAAAAAAAAAAAAAAAAAAWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", word
        print"BBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", tailWord
        print"CCCCCCCCCCCCCCCCCCCCCCCCCWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", listR

        '''========================================================================='''

    except:
        print"Got nothin from tnt_O6,got an error while decoding in FPP,len(listR)==>",len(listR)
        print"AAAAAAAAAAAAAAAAAAAAAAAAAWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", word
        print"BBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", tailWord
        strFinalString3 = ''.join(listR)
        #return strFinalString3,"",""
    print"CCCCCCCCCCCCCCCCCCCCCCCCCWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"

    '''Text Generation (do in another function)'''
    ''''''


    '''***********************************************************************************************'''
    '''************************************  POSTPROCESSING  *****************************************'''
    '''***********************************************************************************************'''


###################################################################################################

# end if
