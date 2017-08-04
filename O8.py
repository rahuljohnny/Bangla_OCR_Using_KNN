from importer import *

'''
from class_contour import *
from Height_matters import *
import word_segmenter3
import tnt_0_O6_compound

'''
imgTestingNumbers2 = cv2.imread("tw44.png")
count4 = 0
arr9 = []
line_counter = []
count_lines2 = 0
###################################################################################################
#########################################################################################################
def main():
    allContoursWithData = []  # declared empty lists,
    validContoursWithData = []
    try:
        npaClassifications = np.loadtxt("classifications.txt", np.float32)
    except:
        print "error, unable to open classifications.txt, exiting program\n"
        os.system("pause")
        return
    # end try

    try:
        npaFlattenedImages = np.loadtxt("flattened_images.txt", np.float32)
    except:
        print "error, unable to open flattened_images.txt, exiting program\n"
        os.system("pause")
        return
    # end try




    npaClassifications = npaClassifications.reshape(
        (npaClassifications.size, 1))  # reshaping numpy array to 1d, necessary to pass to call to train
    kNearest = cv2.ml.KNearest_create()  # instantiate KNN object
    kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)

    ''' ###################################################### <<<<<======== TestBox ========>>>>>>##################################################################'''

    imgTestingNumbers = cv2.imread("kia11.png")

    ''' ####################################################### <<<<<======== TestBox  ========>>>>>>################################################################'''

    if imgTestingNumbers is None:
        print "error: Did not get the first image  \n\n"
        os.system("pause")
        return

    ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>>########################################################'''

    '''Otsu's thresh'''

    gray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)
    # imgBlurred = cv2.GaussianBlur(gray, (5, 5), 0)  #  Must be inactive for semilevel images like pdf-ramkrishna vivekananda
    ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    imgThreshCopy = imgThresh.copy()  #Copying thresh image,this in necessary b/c findContours modifies the image

    cv2.imwrite("ttt\\1.png", imgThresh)

    ''' ####################################################### <<<<<======== Main Image PreProcessing ========>>>>>> ########################################################'''
    ##================================================== Iterate the process from here ==========================================================================================================================

    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                              # input image, must use a copy since the function will modify this image in the course of finding contours
                                                              cv2.RETR_EXTERNAL,  # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE
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
        if contourWithData.checkIfContourIsValid():  # check if valid
            validContoursWithData.append(contourWithData)  # if so, append to valid contour list
            # end if
    # end for
    validContoursWithData.sort(key=operator.attrgetter("intRectY"))  # sort contours from up to down

    strFinalString = ""  # declare final string, this will have the final number sequence by the end of the program
    strCurrentWord = ""
    count = 0

    '''==============================Jhamelar Shuru========================================'''
    '''                                                                                    '''
    '''                         Storing Segmented Words                                    '''
    '''                                                                                    '''
    '''==============================Jhamelar Shuru========================================'''

    height_in_real_image_pre = 0
    height_in_real_image = 0

    j = 0
    max_height = -99
    arr = []
    line = []
    count_lines = 0
    distance_from_y_axis  = []
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
            arr[ii, jj] = 0



    for contourWithData in validContoursWithData:  # for each contour

        # validContoursWithData.sort(key=operator.attrgetter("intRectX"))  # sort contours from up to down
        ''' It worked ! '''
        # rect aktesi
        count = count + 1
        cv2.rectangle(imgTestingNumbers,  # draw rectangle on original testing image
                      (contourWithData.intRectX - 1, contourWithData.intRectY - 1),  # upper left corner
                      (contourWithData.intRectX + contourWithData.intRectWidth + 1,
                       contourWithData.intRectY + contourWithData.intRectHeight + 1),  # lower right corner
                      (0, 255, 0),  # green
                      2)  # thickness

        imgROI = imgThresh[contourWithData.intRectY - 1: contourWithData.intRectY + contourWithData.intRectHeight + 1,
                 contourWithData.intRectX - 1: contourWithData.intRectX + contourWithData.intRectWidth + 1]  # ball = img[280:340, 330:390]
        # cv2.imshow("ImgROI",imgROI)
        h, w = imgROI.shape
        if h > max_height:
            max_height = h

        height_in_real_image_pre = height_in_real_image

        if count == 1 :
            height_in_real_image_pre = contourWithData.intRectY + contourWithData.intRectHeight

        height_in_real_image = contourWithData.intRectY + contourWithData.intRectHeight
        width_in_real_image = contourWithData.intRectX + contourWithData.intRectWidth
        print "height_in_real_image",height_in_real_image,"height_in_real_image_pre",height_in_real_image_pre
        print abs ( height_in_real_image - height_in_real_image_pre ),"  <<  ",int(max_height) / 2
        #cv2.imshow("IMGROI", imgROI)
        #cv2.waitKey(0)

        if abs ( height_in_real_image - height_in_real_image_pre ) <= int(max_height) / 2:

            line[count_lines][j] = imgROI
            arr[count_lines, j] = width_in_real_image
            awidth.append(width_in_real_image)
            j = j+1
            line_counter[count_lines] = j

        else:
            new_list3 = awidth[:]
            awidth.sort()

            for indi in range(0, len(awidth)):
                for jndi in range(0, len(new_list3)):
                    if awidth[indi] == new_list3[jndi]:
                        print "jndi=====================", jndi
                        new_list4.append(jndi)
            print "#####################################################################################"
            print "###########################    New List  ############################################"
            print list(new_list4)
            print list(new_list3)


            for i in range(0,j):
                new_list5[count_lines][i] = line[count_lines][new_list4[i]]

                #cv2.imshow("see0",new_list5[count_lines][i])
                #cv2.waitKey(0)
                cv2.imwrite("009.png",new_list5[count_lines][i])

            #new_list.append(line[count_lines][awidth[i]])
            new_list5.append(count_lines)
            count_lines = count_lines + 1
            j=0
            awidth = []
            new_list3 = []
            new_list4 = []
            '''Experimental'''
            line[count_lines][j] = imgROI
            arr[count_lines, j] = width_in_real_image
            awidth.append(width_in_real_image)
            j = j + 1
            line_counter[count_lines] = j



        # =========================================sending_imgroi===========================================================

        # validContoursWithData.sort(key=operator.attrgetter("intRectX"))  # sort contours from up to down

        arr9.append(imgROI)

    #========================check it on 12 DEC 16
    new_list3 = awidth[:]
    awidth.sort()

    for indi in range(0, len(awidth)):
        for jndi in range(0, len(new_list3)):
            if awidth[indi] == new_list3[jndi]:
                print "jndi=====================", jndi
                new_list4.append(jndi)
    print "#####################################################################################"
    print "###########################    New List  ############################################"
    print list(new_list4)
    print list(new_list3)

    for i in range(0,j):
        new_list5[count_lines][i] = line[count_lines][new_list4[i]]
        #cv2.imshow("see0",new_list5[count_lines][i])
        #cv2.waitKey(0)
        cv2.imwrite("009.png",new_list5[count_lines][i])


        # validContoursWithData.sort(key=operator.attrgetter("intRectY"))  # sort contours from up to down
    count_lines2 = count_lines
    cv2.imshow("imgTestingNumbers", imgTestingNumbers)  # show input image with green boxes drawn around found digits

    


    for i in range(0, count_lines2+1):  # count = 21 = total segments including dots
        for j in range(0, line_counter[i]):

            cv2.imwrite("ttt\\2_Words.png", new_list5[i][j])
            image = cv2.imread("ttt\\2_Words.png")
            #cv2.imshow("imageooo",image)
            #cv2.waitKey(0)
            HeightMatters()
            word_segmenter3.word_segmenter2(i)
            imggg = cv2.imread("4_wordseg.png")
            cv2.imshow("SegMented",imggg) #doesnt show the last two
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            strCurrentWord = tnt_0_O6_compound.Mega_Segmenter2(i)
            strFinalString = strFinalString + strCurrentWord + " "

    print  "The Final String is:"
    print "======================\n" + strFinalString + "\n"
    return


if __name__ == '__main__':
    main()




