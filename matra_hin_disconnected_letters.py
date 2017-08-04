from class_contour import *
imgTestingNumbers2 = cv2.imread("tw44.png")
###################################################################################################
##############################################################################################################################3
arr2=[]
co = 0

def disconnected_letters():
    ''' ###################################################### <<<<<======== Test here ========>>>>>>##################################################################'''
    imgTestingNumbers = cv2.imread("1.png")# read in testing numbers image
    ''' ####################################################### <<<<<======== Test here  ========>>>>>>################################################################'''
    if imgTestingNumbers is None:  # if image was not read successfully
        print "error: Did not get the second image  \n\n"  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit function (which exits program)

    ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''
    gray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)
    ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ret, imgThresh = cv2.threshold(imgThresh, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    imgThreshCopy = imgThresh.copy()  # make a copy of the thresh image, this in necessary b/c findContours modifies the image 4.copyThresh
    cv2.imwrite("2.png",imgThreshCopy)
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
        cv2.imwrite("3_ROI.png", imgROI)
        imgTestingNumbers2 = cv2.imread("3_ROI.png")  # read in testing numbers image
        #=================================== iterative ===================================================================
        if imgTestingNumbers2 is None:  # if image was not read successfully
            print "error: Did not get the third image  \n\n"  # print error message to std out
            os.system("pause")  # pause so user can see error message
            return  # and exit function (which exits program)
        # end if
        # end if
        ''' ####################################################### <<<<<======== Main Image Segmenting ========>>>>>>########################################################'''
        height, width, channels = imgTestingNumbers2.shape
        print "=============================================================================="

        print "Width:"
        print width
        print "Height:"
        print height
        wordRatio = float(width) /float(height)
        print "Ratio:"
        print wordRatio

        print "=============================================================================="
        maxi2 = -999
        maxi3 = -999
        mini = 9998
        #if imgROIs_ratio > .95:



        counter = 0
        ended = 0
        counter2 = 0
        counter_entered_into_zero = 0
        temp_start = 0
        c = array.array('i', (0,) * (width + 20))
        for i in range(0, int(height) / 2):
            for j in range(0, width):
                if np.any(imgTestingNumbers2[i, j] == 0):  # if longest white line(matra) found
                    c[i] = c[i] + 1

                    if c[i] > maxi2:
                        maxi2 = c[i]

        print "The array is:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        print(i, ":i,for c=", c)
        for j in range(0, width):
            if c[j] == 0:
                print "SubCondition 1"
                counter_entered_into_zero = counter_entered_into_zero + 1

                counter = counter + 1
                if counter > 12:
                    ended = 1
                    break

            if c[j] <= mini + 5:
                if ended == 0:
                    if counter2 == 0:
                        start = j
                    counter2 = counter2 + 1

                    print "SubCondition 2"
                    mini = c[j]
                    end = j

        # finding out the minimum value
        print "Entered into 2nd condi,mini:=================================================="
        print mini

        print start, "--Start    ,       End--", end
        #  print start

        print "Entered into 2nd condi,Counter:=================================================="
        print counter

        temps = 1  # take these variables from user
        tempe = 2
        for i in range(start, end):  # check out c[9] to c[13]  inew-2,irange+2
            for j in range(0, width):
                imgTestingNumbers2[i, j] = 1


cv2.imshow("imgTestingNumbers2")