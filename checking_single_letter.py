from class_contour import *
imgTestingNumbers2 = cv2.imread("tw44.png")
arr2=[]
co = 0


arr = []
cc = 0
allContoursWithData = []  # declare empty lists,
validContoursWithData = []  # we will fill these shortly

''' ###################################################### <<<<<======== Test here ========>>>>>>##################################################################'''
imgTestingNumbers = cv2.imread("simple2.png")# read in testing numbers image
''' ####################################################### <<<<<======== Test here  ========>>>>>>################################################################'''
if imgTestingNumbers is None:  # if image was not read successfully
    print "error: Did not get the second image  \n\n"  # print error message to std out
    os.system("pause")  # pause so user can see error message


''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''
gray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)
ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#ret, imgThresh = cv2.threshold(imgThresh, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

imgThreshCopy = imgThresh.copy()  # make a copy of the thresh image, this in necessary b/c findContours modifies the image 4.copyThresh
cv2.imwrite("3.png",imgThreshCopy)
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
    contourWithData.boundingRect = cv2.boundingRect(contourWithData.npaContour)  # get the bounding rect
    contourWithData.calculateRectTopLeftPointAndWidthAndHeight()  # get bounding rect info
    contourWithData.fltArea = cv2.contourArea(contourWithData.npaContour)  # calculate the contour area
    allContoursWithData.append(contourWithData)  # add contour with data object to list of all contours with data
# end for

for contourWithData in allContoursWithData:  # for all contours
    if contourWithData.checkIfContourIsValid():  # check if valid
        validContoursWithData.append(contourWithData)  # if so, append to valid contour list

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
    cv2.imwrite("4.png", imgROI)
    imgTestingNumbers2 = cv2.imread("4.png")  # read in testing numbers image
    #=================================== iterative ===================================================================
    if imgTestingNumbers2 is None:  # if image was not read successfully
        print "error: Did not get the third image  \n\n"  # print error message to std out
        os.system("pause")  # pause so user can see error message

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
    mini = 999
    cv2.waitKey(0)
    if wordRatio >= 0.9:

        c = array.array('i', (0,) * width)
        for i in range(0, int(height) / 2):
            for j in range(0, width):
                if np.any(imgTestingNumbers2[i, j] == 0):   #if longest white line(matra) found
                    c[i] = c[i] + 1

                    if c[i] > maxi2:
                        maxi2 = c[i]

        print "MaXiIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"
        print maxi2

        try:
            if maxi2 > 10 :
                maxi3 = maxi2 / 4
        except:
            maxi3 = maxi2
        print "The array is:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        print(i, ":i,for c=", c)
        end = 2
        start = 2
        co = 0
        print "maxi3:"
        print maxi3
        for i in range(0, int(height) / 2):

            if c[i] < int(maxi3) + 2: #A new try UNDER TEST
                co = co+1
                if co > 1:
                    end = i
                elif co==1 :
                    start = i


        print "Start:"
        print start
        print "End:"
        print end


        #newrange=abs((inew+irange)/2)
        temps = 2 # take these variables from user
        tempe = 2
        for i in range(start-temps,end+tempe):# check out c[9] to c[13]  inew-2,irange+2
            for j in range(0, width):
                imgTestingNumbers2[i, j] = 1
                ''''''
        #
                # cv2.imshow("test",imgTestingNumbers2)
    #Works for matr
    else :

        c = array.array('i', (0,) * (100))
        for i in range(0, int(height) / 2):
            for j in range(0, width):
                if np.any(imgTestingNumbers2[i, j] == 0):  # if longest white line(matra) found
                    c[i] = c[i] + 1

                    if c[i] > maxi2:
                        maxi2 = c[i]

        print "The array is:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        print(i, ":i,for c=", c)
        for j in range(0, width):
            if c[j] == 0 :
                start = j
                break

            elif c[j] <= mini:
                mini = c[j]
                start = j

        # finding out the minimum value
        print "StartIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII2=================================================="
        print start

        temps = 1  # take these variables from user
        tempe = 2
        for i in range(start,start + 4):  # check out c[9] to c[13]  inew-2,irange+2
            for j in range(0, width):
                imgTestingNumbers2[i, j] = 1
    gray2= cv2.cvtColor(imgTestingNumbers2, cv2.COLOR_BGR2GRAY)
    # imgBlurred = cv2.GaussianBlur(imgGray, (5,5), 0)                    # blur

    ret, imgThresh1 = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    arr2.append(imgThresh1)
    imgTestingNumbers = imgThresh1.copy()
    cv2.imshow("3rd file", imgThresh1)
    cv2.waitKey(0)




