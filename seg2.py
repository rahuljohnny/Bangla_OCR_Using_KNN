from class_contour import *
from importer import *
imgTestingNumbers2 = cv2.imread("tw44.png")
###################################################################################################
###################################################################################################
arr2=[]
co = 0




def word_segmenter2(imgTestingNumbers,count2):

    cc = 0
    allContoursWithData = []  # declare empty lists,
    validContoursWithData = []  # we will fill these shortly

    ''' ###################################################### <<<<<======== Test here ========>>>>>>##################################################################'''
    #imgTestingNumbers = cv2.imread("oi.png")# read in testing numbers image
    cv2.imshow("segmenter_imgTestingNumbers",imgTestingNumbers)
    cv2.waitKey(0)

    ''' ####################################################### <<<<<======== Test here  ========>>>>>>################################################################'''
    if imgTestingNumbers is None:  # if image was not read successfully
        print "error: Did not get the second image  \n\n"  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit function (which exits program)

    ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''
    #gray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)
    #ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #ret, imgThresh = cv2.threshold(imgThresh, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    imgThresh = imgTestingNumbers.copy()

    imgThreshCopy = imgThresh.copy()  # make a copy of the thresh image, this in necessary b/c findContours modifies the image 4.copyThresh
    cv2.imwrite("ttt\\3.png",imgThreshCopy)
    ##================================================== Iterate the process from here ==========================================================================================================================

    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                              # input image, make sure to use a copy since the function will modify this image in the course of finding contours 5.findContours()
                                                              cv2.RETR_EXTERNAL,  # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE
                                                              )  # compress horizontal, vertical, and diagonal segments and leave only their end points


    for npaContour in npaContours:  # for each contour #for i in the range of npaContours
        contourWithData = ContourWithData()  # instantiate a contour with data object
        contourWithData.npaContour = npaContour  # assign contour to contour with data

        contourWithData.boundingRect = cv2.boundingRect(contourWithData.npaContour)  # get the bounding rect
        contourWithData.calculateRectTopLeftPointAndWidthAndHeight()  # get bounding rect info
        contourWithData.fltArea = cv2.contourArea(contourWithData.npaContour)  # calculate the contour area
        allContoursWithData.append(contourWithData)  # add contour with data object to list of all contours with data

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
        cv2.imwrite("ROI44.png", imgROI)
        imgTestingNumbers2 = cv2.imread("ROI44.png")  # read in testing numbers image
        #=================================== iterative ===================================================================
        if imgTestingNumbers2 is None:  # if image was not read successfully
            print "error: Did not get the third image  \n\n"  # print error message to std out
            os.system("pause")  # pause so user can see error message
            return  # and exit function (which exits program)

        ''' ####################################################### <<<<<======== Main Image Segmenting ========>>>>>>########################################################'''
        height, width, channels = imgTestingNumbers2.shape
        print "=============================================================================="
        print "Width:",width,"Height:",height

        wordRatio = float(width) /float(height)
        print "Ratio:",wordRatio,"          Area:",width*height

        print "=============================================================================="
        maxi2 = -999
        maxi3 = -999
        mini = 9998

        area = width*height
        if area<5 :
            1

        elif area >= 5: #the perfect word segmenter,it was 0.9

            c = array.array('i', (0,) *(width+20))
            for i in range(0, int(height) / 2):
                for j in range(0, width):
                    if np.any(imgTestingNumbers2[i, j] == 0):  # if longest white line(matra) found
                        c[i] = c[i] + 1

                        if c[i] > maxi2:
                            maxi2 = c[i]

            try:
                if maxi2 > 10:
                    maxi3 = maxi2 / 4
            except:
                maxi3 = maxi2
            print "The array is:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
            print(i, ":i,for c=", c)

            '''================================================================================================================='''

            '''================================================================================================================='''

            end = 2
            start = 2
            co = 0
            print "maxi3:"
            print maxi3
            for i in range(0, int(height) / 2):

                if c[i] < int(maxi3) + 2:  # A new try UNDER TEST
                    co = co + 1
                    if co > 1:
                        end = i
                    elif co == 1:
                        start = i

            temps = 2  # take these variables from user
            tempe = 2



            if start >= end -1 :
                end = start

            if end - start > 6 :
                print "Start:", start, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          end", end
                end = start


            start = start - temps
            end = end + tempe
            start = 22
            end = 25
            if start < 0 and end <=3 :
                end = end + 2



            print "Start:",start,"  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        end",end

            try:
                for i in range(start , end):  # check out c[9] to c[13]  inew-2,irange+2
                    for j in range(0, width):
                        imgTestingNumbers2[i, j] = 255 #as its a grayscal image,0 is the closest to black, 255 is the nearest to white
            except :
                1
        cv2.imshow("3rd file", imgTestingNumbers2)
        cv2.waitKey(0)

        gray2= cv2.cvtColor(imgTestingNumbers2, cv2.COLOR_BGR2GRAY)
        # imgBlurred = cv2.GaussianBlur(imgGray, (5,5), 0)                    # blur
        ret, imgThresh1 = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        arr2.append(imgThresh1)
        imgTestingNumbers = imgThresh1.copy()

        '''########################################################################################################################'''


        '''########################################################################################################################'''
        cv2.imwrite("5_wordseg.png", arr2[count2])
    cv2.imwrite("4_wordseg.png", imgTestingNumbers) #this thing is fuckiung important
    return imgTestingNumbers2


'''
def main():
    word_segmenter2(0)

    return


if __name__ == '__main__':
    main()

'''


