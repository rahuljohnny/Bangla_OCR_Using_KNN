from importer import *
from class_contour import *
from Height_matters import *
import word_segmenter3
import tnt_0_O6_compound
imgTestingNumbers2 = cv2.imread("tw44.png")
count4 = 0

###################################################################################################


##############################################################################################################################3
def main():

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




    npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))  # reshape numpy array to 1d, necessary to pass to call to train
    kNearest = cv2.ml.KNearest_create()  # instantiate KNN object
    kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)

    ''' ###################################################### <<<<<======== TestBox ========>>>>>>##################################################################'''

    imgTestingNumbers = cv2.imread("e16.png")

    ''' ####################################################### <<<<<======== TestBox  ========>>>>>>################################################################'''

    if imgTestingNumbers is None:  # if image was not read successfully
        print "error: Did not get the first image  \n\n"  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit function (which exits program)
    # end if
    ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''

    '''Otsu's thresh'''

    gray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)
    #imgBlurred = cv2.GaussianBlur(gray, (5, 5), 0)  #  Must be inactive for semilevel images like pdf-ramkrishna vivekananda
    ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    imgThreshCopy = imgThresh.copy()  # make a copy of the thresh image, this in necessary b/c findContours modifies the image 4.copyThresh

    cv2.imwrite("ttt\\1.png", imgThresh)

    ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>> ########################################################'''
    ##================================================== Iterate the process from here ==========================================================================================================================

    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                              # input image, make sure to use a copy since the function will modify this image in the course of finding contours 5.findContours()
                                                              cv2.RETR_EXTERNAL,  # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE
                                                              )  # compress horizontal, vertical, and diagonal segments and leave only their end points

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

    #validContoursWithData.sort(key=operator.attrgetter( "intRectY","intRectX")) # sort contours from left to right  validContoursWithData.sort(key=operator.attrgetter("intRectX-10"))
    validContoursWithData.sort(key=operator.attrgetter("intRectY"))  # sort contours from up to down


    strFinalString = ""  # declare final string, this will have the final number sequence by the end of the program
    strCurrentWord= ""
    count = 0
    max_height = -99
    arr = []
    for contourWithData in validContoursWithData:  # for each contour

        #validContoursWithData.sort(key=operator.attrgetter("intRectX"))  # sort contours from up to down
        ''' It worked ! '''
        # rect aktesi
        count = count + 1
        cv2.rectangle(imgTestingNumbers,  # draw rectangle on original testing image
                      (contourWithData.intRectX-1, contourWithData.intRectY-1),  # upper left corner
                      (contourWithData.intRectX + contourWithData.intRectWidth+1,
                       contourWithData.intRectY + contourWithData.intRectHeight+1),  # lower right corner
                      (0, 255, 0),  # green
                      2)  # thickness

        imgROI = imgThresh[contourWithData.intRectY-1: contourWithData.intRectY + contourWithData.intRectHeight+1,
                 contourWithData.intRectX-1: contourWithData.intRectX + contourWithData.intRectWidth+1] # ball = img[280:340, 330:390]
        #cv2.imshow("ImgROI",imgROI)
        h, w = imgROI.shape
        if h > max_height :
            max_height = h
        #=========================================sending_imgroi===========================================================
        print"count:",count, "NOVICE h:", contourWithData.intRectY + contourWithData.intRectHeight,"Real Height:",h, "NOVICE w:", contourWithData.intRectX + contourWithData.intRectWidth
        #validContoursWithData.sort(key=operator.attrgetter("intRectX"))  # sort contours from up to down

        arr.append(imgROI)

        #validContoursWithData.sort(key=operator.attrgetter("intRectY"))  # sort contours from up to down

    cv2.imshow("imgTestingNumbers", imgTestingNumbers)      # show input image with green boxes drawn around found digits

    #cv2.waitKey(0)                                          # wait for user key press

    #cv2.destroyAllWindows()             # remove windows from memory

    for i in range(0, count): #count = 21 = total segments including dots
        cv2.imshow("NEW", arr[i])

        #print "NOVICE h:" ,h,"NOVICE w:", w
        cv2.imwrite("ttt\\2_Words.png", arr[i])
        image = cv2.imread("ttt\\2_Words.png")
        HeightMatters()
        word_segmenter3.word_segmenter2(i)
        imggg = cv2.imread("4_wordseg.png")
        #cv2.imshow("SegMented",imggg) #doesnt show the last two
        #cv2.waitKey(0)
        strCurrentWord = tnt_0_O6_compound.Mega_Segmenter2(i)
        strFinalString = strFinalString + strCurrentWord + " "


    print  "The Final String is:"
    print "======================\n" + strFinalString + "\n"
    return

if __name__ == '__main__':
    main()




