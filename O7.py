#!/usr/bin/python
# -*- coding: utf-8 -*-

from importer import *
import copy
#from  skelet import *
from First_PostProcessing import Post_Processing

count4 = 0
arr9 = []
line_counter = []
count_lines2 = 0
onushwar = 0


###################################################################################################
#########################################################################################################
def main():
    allContoursWithData = []  # declared empty lists,
    validContoursWithData = []
    strFinalString2 = []

    ''' ###################################################### <<<<<======== TestBox ========>>>>>>##################################################################'''

    #imgTester = cv2.imread("u31.png") # times = 2
    #imgTester = cv2.imread("9.png") # times = 2
    imgTester = cv2.imread("haripada\\p1.jpg") # times = 2.5 temps=2 tempe = 3
    #imgTester = cv2.imread("BSERIES\\b6.png") # times = 2.5 temps=2 tempe = 3
    #imgTester = cv2.imread("BSERIES\\b1.png") # times = 2.5 temps=2 tempe = 3
    #imgTester = cv2.imread("BSERIES\\b10.png") # times = 2.5 temps=2 tempe = 3
    #imgTester = cv2.imread("pyt.jpg.jpg") # times = 2.5 temps=2 tempe = 3
    #imgTester = cv2.imread("ACCURACY\\type3_1.jpg")




    #imgTester = cv2.imread("S5\\v.jpg") # times = 1 temps=2 tempe = 3



    ''' ####################################################### <<<<<======== TestBox  ========>>>>>>################################################################'''

    if imgTester is None:
        print "error: Could not read the image from given path!!  \n\n"
        os.system("pause")
        return

    ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''

    '''Otsu's thresh'''

    cv2.imshow("basic_image", imgTester)
    cv2.waitKey(0)

    gray = cv2.cvtColor(imgTester, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    cv2.waitKey(0)

    # imgBlurred = cv2.GaussianBlur(gray, (5, 5), 0)  #  Must be inactive for semilevel images like pdf-ramkrishna vivekananda
    ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow("threshed", imgThresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imgThreshCopy = imgThresh.copy()  # Copying thresh image,this in necessary b/c findContours modifies the image

    cv2.imwrite("ttt\\1.png", imgThresh)

    ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>> ########################################################'''
    ##================================================== Iterate the process from here ==========================================================================================================================

    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                              # input image, must use a copy since the function will modify this image in the course of finding contours
                                                              cv2.RETR_EXTERNAL,  # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE #only four points
                                                              )  # compress horizontal, vertical, and diagonal segments and leave only their end points

    for npaContour in npaContours:  # for each contour #for i in the range of npaContours
        contourWithData = ContourWithData()  # instantiate a contour with data object
        contourWithData.npaContour = npaContour
        contourWithData.boundingRect = cv2.boundingRect(contourWithData.npaContour)  # get the bounding rect
        contourWithData.calculateRectTopLeftPointAndWidthAndHeight()  # get bounding rect info
        contourWithData.fltArea = cv2.contourArea(contourWithData.npaContour)  # calculate the contour area
        allContoursWithData.append(contourWithData)  # add contour with data object to list of all contours with data
    # end for

    for contourWithData in allContoursWithData:  # for all contours
        if contourWithData.checkIfContourIsValid():
            validContoursWithData.append(contourWithData)
            # end if
    # end for
    validContoursWithData.sort(key=operator.attrgetter("intRectY"))  # sort contours from up to down

    strFinalString = ""  # declare final string, this will have the final number sequence by the end of the program
    #strCurrentWord = ""
    count = 0

    '''==============================words========================================'''
    '''                                                                           '''
    '''                         Storing Segmented Words                           '''
    '''                                                                           '''
    '''==============================words========================================'''

    height_in_real_image_pre = 0
    height_in_real_image = 0

    j = 0
    max_height = -99
    arr = []
    line = []
    count_lines = 0
    distance_from_y_axis = []
    arr = np.empty((70, 500), dtype=object)
    line_counter = np.empty((70), dtype=object)
    awidth = []
    new_list3 = []
    new_list4 = []
    new_list5 = []

    for ii in xrange(70):
        line.append([])
        distance_from_y_axis.append([])
        new_list5.append([])

        for jj in xrange(500):
            line[ii].append(ii + jj)
            distance_from_y_axis[ii].append([ii + jj])
            new_list5[ii].append(ii + jj)
            arr[ii, jj] = 0 #initializing

    for contourWithData in validContoursWithData:  # for each contour

        # validContoursWithData.sort(key=operator.attrgetter("intRectX"))  # sorting contours from up to down
        ''' It worked ! '''
        # rect aktesi
        count = count + 1
        cv2.rectangle(imgTester,
                      (contourWithData.intRectX - 1, contourWithData.intRectY - 1),  # upper left corner
                      (contourWithData.intRectX + contourWithData.intRectWidth + 1,
                       contourWithData.intRectY + contourWithData.intRectHeight + 1),  # lower right corner
                      (0, 255, 0),  # colour
                      2)  # thickness
        '''Changing these works !'''
        pre = 3
        post = 5

        imgROI = imgThresh[contourWithData.intRectY - pre: contourWithData.intRectY + contourWithData.intRectHeight + post,
                 contourWithData.intRectX : contourWithData.intRectX + contourWithData.intRectWidth ]  # ball = img[280:340, 330:390]
        #cv2.imshow("incresed",imgROI)
        #cv2.waitKey(0)
        h, w = imgROI.shape
        if h > max_height:
            max_height = h

        height_in_real_image_pre = height_in_real_image

        if count == 1:
            height_in_real_image_pre = contourWithData.intRectY + contourWithData.intRectHeight

        height_in_real_image = contourWithData.intRectY + contourWithData.intRectHeight
        width_in_real_image = contourWithData.intRectX + contourWithData.intRectWidth
        print "height_in_real_image", height_in_real_image, "height_in_real_image_pre", height_in_real_image_pre
        #print abs(height_in_real_image - height_in_real_image_pre), "  <<  ", int(max_height) / 2
        # cv2.imshow("IMGROI", imgROI)
        # cv2.waitKey(0)

        if abs(height_in_real_image - height_in_real_image_pre) <= int(max_height) / 2:

            line[count_lines][j] = imgROI
            arr[count_lines, j] = width_in_real_image
            awidth.append(width_in_real_image)
            j = j + 1
            line_counter[count_lines] = j

        else:
            new_list3 = awidth[:]
            awidth.sort()

            for indi in range(0, len(awidth)):
                for jndi in range(0, len(new_list3)):
                    if awidth[indi] == new_list3[jndi]:
                        #print "jndi=====================", jndi
                        new_list4.append(jndi)
            #print "###########################################################################"
            #print "###########################    New List  ##################################"
            #print list(new_list4)
            #print list(new_list3)

            for i in range(0, j):
                new_list5[count_lines][i] = line[count_lines][new_list4[i]]

                #cv2.imshow("see0",new_list5[count_lines][i])
                #cv2.waitKey(600)

            # new_list.append(line[count_lines][awidth[i]])
            new_list5.append(count_lines)
            count_lines = count_lines + 1
            j = 0
            awidth = []
            new_list3 = []
            new_list4 = []




            line[count_lines][j] = imgROI
            arr[count_lines, j] = width_in_real_image
            awidth.append(width_in_real_image)
            j = j + 1
            line_counter[count_lines] = j

        # =========================================sending_imgroi===========================================================
        arr9.append(imgROI)

    # ========================check it on 12 DEC 16
    new_list3 = awidth[:]
    awidth.sort()

    for indi in range(0, len(awidth)):
        for jndi in range(0, len(new_list3)):
            if awidth[indi] == new_list3[jndi]:
                print "jndi=====================", jndi
                new_list4.append(jndi)
    #print "#####################################################################################"
    #print "###########################    New List  ############################################"
    #print list(new_list4)
    #print list(new_list3)

    for i in range(0, j):
        new_list5[count_lines][i] = line[count_lines][new_list4[i]]
        #cv2.imshow("see0",new_list5[count_lines][i])
        #cv2.waitKey(500)

        #cv2.imwrite("009.png", new_list5[count_lines][i])

    count_lines2 = count_lines
    #cv2.imshow("imgTester", imgTester)  # show input image with green boxes drawn around found digits
    #cv2.waitKey(0)
    ar12=[]

    k=-1
    m=-9

    temp2=''
    pre_list33 = []

    list_33 =[]
    temp3 = ''
    temp4 = ''
    for i in range(0, count_lines2+1 ):  # count = 21 = total segments including dots.

        for j in range(0, line_counter[i]+1):

            try:

                '''Passing sorted words to Methods'''
                #if new_list5[i][j]

                cv2.imwrite("ttt\\T_Words.png", new_list5[i][j])
                ima= cv2.imread("ttt\\T_Words.png")

                height2, width2, channels2 = ima.shape
                area = height2 * width2
                print"**************************************  area ****",area

                if area > 5:
                    #print h, "-height      ", "width       ", w

                    #Calling functions one after another

                    image1 = HeightMatters(new_list5[i][j]) # called the function heightmatters to zoom in/out
                    image2 = word_segmenter3.word_segmenter2(i,image1) #Send the zoomed image with count no to abolish the matra
                    k = k + 1

                    #image3 = skele(image2);

                    cv2.imwrite("ttt\\imgROI_small.png", image2)
                    img33 = cv2.imread("ttt\\imgROI_small.png")
                    '''
                    cv2.imshow("O7_WS",img33)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    #'''
                    height2, width2, channels2 = img33.shape
                    area = height2 * width2

                    print"area========================>>>>>>>>>>>>>>>>>>>>>>", area
                    print"w========================>>>>>>>>>>>>>>>>>>>>>>", width2

                    #if area != 0:

                    strCurrentWord = ''
                    temp22 = ''


                    strCurrentWord,temp22,list_33 = tnt_0_O6_compound.Mega_Segmenter2(i,image2) #the matra hin image is send to mega segmenter func to check each segmentation
                    nospace = 0

                    #if strCurrentWord == "NULL" and  temp22=="NULL":



                    #ar12[k+1] = temp
                    if temp22 == 'ে' or temp22 =='গু': #if the last letter of a word is 'ে' or 'গু' or .......
                        print"does it enter_o7?"
                        nospace = 1
                        temp3 = strCurrentWord

                        #if ar12[k]=='ে':

                    print"tempEkar***************************",temp22

                    '''2nd postprocessing'''

                    #'''
                    
                    # Letters like
                    
                    dha=0
                    onushwar=0
                    if strCurrentWord == "ধ":

                        dha=1

                        
                    #'''

                    '''A very effeective initiative'''
                    '''A very effeective initiative'''
                    '''A very effeective initiative'''

                    if strCurrentWord=='র্':

                        if strFinalString2[len(strFinalString2)-2]=='ঁ':
                            print "(((((((((((((((((((((((((((((((((((((((((((((((((", strFinalString2[0]
                            onushwar = 1

                            strFinalString = strFinalString[:len(strFinalString)-4] + 'ং' #VVI  strFinalString[:len(strFinalString)-4]
                            #Unichar(3 char = 1 unichar) fact

                    if strCurrentWord != "ধ" and strCurrentWord !='র্' and strCurrentWord != "ত" and strCurrentWord != "ভ" and strCurrentWord !="ত্র"  and strCurrentWord !="." and strCurrentWord !="ক্র" and dha==0 and onushwar ==0:

                        '''
                        if strCurrentWord == "া":
                            strCurrentWord = '।'

                        elif strCurrentWord =="নঠ":
                            strCurrentWord = "এ"

                        elif strCurrentWord =="ঁঠ":
                            strCurrentWord = "ও"

                        elif strCurrentWord =="ণুা":
                            strCurrentWord = "ণ"
                        elif strCurrentWord =="ওশ":
                            strCurrentWord = "গু"

                        '''


                        if nospace ==0:

                            if k-m==1:

                                if len(pre_list33) > 2 :


                                    strCurrentWord = temp4 +" FROM O7.py "+ strCurrentWord

                                    print"temp4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  : ", temp4
                                    print"temp3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  : ", temp3
                                    '''
                                    pre_list33 = pre_list33[0:len(pre_list33)-2]+list_33[0]+pre_list33[len(pre_list33)-1]+list_33[1:len(pre_list33)-1]
                                    strCurrentWord = ''.join(pre_list33)
                                    print "O7_SS^^^^^^^^^^^^^^^^^SSSSS ", strCurrentWord, "   Nospace==>", nospace, "====k=====", k, " ,m  ", m, "============strFinalString==========", strFinalString

                                    #strCurrentWord = temp2[0:len(strCurrentWord)-2] + strCurrentWord[0]+temp2[len(strCurrentWord)-1]+strCurrentWord[1:len(strCurrentWord)-1]
                                #elif len(pre_list33) > 2 and len(list_33) == 1:
                                    if strCurrentWord=='':
                                        strCurrentWord = ''.join(pre_list33)
                                        strCurrentWord = temp2+strCurrentWord
                                    '''
                                else :

                                    strCurrentWord = strCurrentWord

                                print "strCurrentWordstrCurrentWordstrCurrentWordstrCurrentWord  == >>",strCurrentWord ," temp2==>",strFinalString
                                new_list =[]
                                temp4=''

                            strFinalString = strFinalString + strCurrentWord + " "

                        elif nospace==1:

                            temp4 = strCurrentWord
                            m = k
                            pre_list33 = copy.copy(list_33)
                            #strCurrentWord = strCurrentWord [0:len(strCurrentWord)-1]
                            #strFinalString = strFinalString + strCurrentWord
                        #print "strCurrentWordstrCurrentWordstrCurrentWordstrCurrentWordstrCurrentWordstrCurrentWordstrCurrentWord  == >>", strFinalString

                strFinalString2 = []
                strFinalString2 = strCurrentWord.split(",")
                print"O7_Word ==>",strCurrentWord
            except:
                1




        strFinalString = strFinalString +"\n"



    print "THE FINAL ONE"
    print "=============\n" + strFinalString + "\n"
    #cv2.imshow("imgTester", imgTester)  # show input image with green boxes drawn around found digits
    #cv2.waitKey(0)







    fout = open('result.docx', 'w')

    fout.write(strFinalString)
    fout.close()


    # f = open('Result.txt', 'w')
    # print f

    return


if __name__ == '__main__':
    main()




