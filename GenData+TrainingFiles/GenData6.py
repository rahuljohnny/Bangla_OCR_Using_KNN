from class_contour import *
imgTestingNumbers2 = cv2.imread("tw44.png")
###################################################################################################
##############################################################################################################################3
arr2=[]
def word_segmenter2(count2):


    arr = []
    cc = 0
    allContoursWithData = []  # declare empty lists,
    validContoursWithData = []  # we will fill these shortly
    CCC = 0
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
    '''
    npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))  # reshape numpy array to 1d, necessary to pass to call to train
    kNearest = cv2.ml.KNearest_create()  # instantiate KNN object
    kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)
    '''
    ''' ###################################################### <<<<<======== Test here ========>>>>>>##################################################################'''

    imgTestingNumbers = cv2.imread("h10.png")# read in testing numbers image

    ''' ####################################################### <<<<<======== Test here  ========>>>>>>################################################################'''

    if imgTestingNumbers is None:  # if image was not read successfully
        print "error: Did not get the second image  \n\n"  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit function (which exits program)
    # end if
    ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''


    gray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)
    ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    gray = cv2.cvtColor(imgThresh, cv2.COLOR_BGR2GRAY)
    ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    imgThreshCopy = imgThresh.copy()  # make a copy of the thresh image, this in necessary b/c findContours modifies the image 4.copyThresh
    cv2.imwrite("ttt\\3.png",imgThreshCopy)
    ##================================================== Iterate the process from here ==========================================================================================================================

    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                              # input image, make sure to use a copy since the function will modify this image in the course of finding contours 5.findContours()
                                                              cv2.RETR_EXTERNAL,  # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE
                                                              )  # compress horizontal, vertical, and diagonal segments and leave only their end points

    # im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for npaContour in npaContours:  # for each contour #for i in the range of npaContours
        contourWithData = ContourWithData()  # instantiate a contour with data object
        contourWithData.npaContour = npaContour  # assign contour to contour with data
        # ## class ContourWithData(){ npaContour = None  # contour;boundingRect = None ;
           # intRectX = 0 ;intRectY = 0;intRectWidth = 0 ;intRectHeight = 0;fltArea = 0.0}
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

    strFinalString = ""  # declare final string, this will have the final number sequence by the end of the program

    for contourWithData in validContoursWithData:  # for each contour
        # draw a green rect around the current char
        cc = cc + 1
        cv2.rectangle(imgTestingNumbers,  # draw rectangle on original testing image
                      (contourWithData.intRectX, contourWithData.intRectY),  # upper left corner
                      (contourWithData.intRectX + contourWithData.intRectWidth,
                       contourWithData.intRectY + contourWithData.intRectHeight),  # lower right corner
                      (0, 255, 0),  # green
                      2)  # thickness

        imgROI = imgThresh[contourWithData.intRectY: contourWithData.intRectY + contourWithData.intRectHeight,
                 contourWithData.intRectX: contourWithData.intRectX + contourWithData.intRectWidth] # ball = img[280:340, 330:390]
        #=========================================sending_imgroi===========================================================
        cv2.imwrite("ttt\\4_ROI.png", imgROI)
        imgTestingNumbers2 = cv2.imread("ttt\\4_ROI.png")  # read in testing numbers image
        #=================================== iterative ===================================================================
        if imgTestingNumbers2 is None:  # if image was not read successfully
            print "error: Did not get the third image  \n\n"  # print error message to std out
            os.system("pause")  # pause so user can see error message
            return  # and exit function (which exits program)
        # end if


        # end if
        ''' ####################################################### <<<<<======== Main Image Segmenting ========>>>>>>########################################################'''

        height, width, channels = imgTestingNumbers2.shape

        wordRatio = float(width) /float(height)
        #if imgROIs_ratio > .95:
        if wordRatio >= 0.9:
            maxi = 9999
            maxi2 = -999
            maxi3 = -999
            inew0 =-999
            #for i in range(0, int(height) / 6):

            c = array.array('i', (0,) * 100)
            for i in range(0, int(height) / 2):
                for j in range(0, width):
                    if np.any(imgTestingNumbers2[i, j] == 0):   #if longest white line(matra) found
                        c[i] = c[i] + 1

                        if c[i] > maxi2:
                            maxi2 = c[i]

            print(i, ":i,for c=", c)

            try:
                if maxi2 > 10 :
                    maxi3 = maxi2 / 4
            except:
                maxi3 = maxi2

            end = 0
            start = 0
            co = 0
            '''
            print "max 3"
            print maxi3
            '''
            for i in range(0, int(height) / 2):

                if c[i] < int(maxi3):
                    co = co+1
                    if co > 1:
                        end = i
                    elif co==1 :
                        start = i
            '''
            print "Start:"
            print start
            print "End:"
            print end
            '''

            #newrange=abs((inew+irange)/2)
            print
            for i in range(start-2,end+2):# check out c[9] to c[13]  inew-2,irange+2
                for j in range(0, width):
                    imgTestingNumbers2[i, j] = 1

        ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''
        ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''
        ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''


        gray = cv2.cvtColor(imgTestingNumbers2, cv2.COLOR_BGR2GRAY)
        ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        arr2.append(imgThresh)
        print "count2:"
        print cc
        cv2.imwrite("4_wordseg.png", arr2[cc - 1])
        count2 = cc
        '''Till here everything is ok>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
        '''============================================================================================================================================================================'''
        '''<<<<<<================================================================ WORD PROCESSING  ============================================================================>>>>>>'''
        '''============================================================================================================================================================================'''


        if count2 == 1:
            cv2.imwrite("CreS2//c0.png", arr2[count2 - 1])
        elif count2 == 3:
            cv2.imwrite("CreS2//c2.png", arr2[count2 - 1])
        elif count2 == 2:
            cv2.imwrite("CreS2//c1.png", arr2[count2 - 1])
        elif count2 == 4:
            cv2.imwrite("CreS2//c3.png", arr2[count2 - 1])
        elif count2 == 5:
            cv2.imwrite("CreS2//c4.png", arr2[count2 - 1])

        elif count2 == 6:
            cv2.imwrite("CreS2//c5.png", arr2[count2 - 1])
        elif count2 == 7:
            cv2.imwrite("CreS2//c6.png", arr2[count2 - 1])
        elif count2 == 8:
            cv2.imwrite("CreS2//c7.png", imgThresh1)
        elif count2 == 9:
            cv2.imwrite("CreS2//c8.png", imgThresh1)
        elif count2 == 10:
            cv2.imwrite("CreS2//c9.png", imgThresh1)
        elif count2 == 11:
            cv2.imwrite("CreS2//c10.png", imgThresh1)
        elif count2 == 12:
            cv2.imwrite("CreS2//c11.png", imgThresh1)
        elif count2 == 13:
            cv2.imwrite("CreS2//c12.png", imgThresh1)
        elif count2 == 14:
            cv2.imwrite("CreS2//c13.png", imgThresh1)
        elif count2 == 15:
            cv2.imwrite("CreS2//c14.png", imgThresh1)


        elif count2 == 0:
            cv2.imwrite("CreS2//c-1.png", arr2[count2 - 1])

       # return
        # EOF for
    #EOF if
    ##=====================================================================================================================================================================================================================
    ##=====================================================================================================================================================================================================================
    ##=====================================================================================================================================================================================================================
    return