from importer import *
import GenData_C
imgTestingNumbers2 = cv2.imread("tw44.png")
###################################################################################################
###################################################################################################
arr2=[]
co = 0

def word_segmenter2(imgTestingNumbers,count2):


    ''' ####################################################### <<<<<======== Test here  ========>>>>>>################################################################'''
    if imgTestingNumbers is None:  # if image was not read successfully
        print "error: Did not get the second image  \n\n"  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit function (which exits program)
    imgThresh = imgTestingNumbers.copy()

    imgThreshCopy = imgThresh.copy()  # make a copy of the thresh image, this in necessary b/c findContours modifies the image 4.copyThresh
    imgTestingNumbers2 = imgTestingNumbers.copy()

    #=================================== iterative ===================================================================
    if imgTestingNumbers2 is None:  # if image was not read successfully
        print "error: Did not get the third image  \n\n"  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit function (which exits program)

    ''' ####################################################### <<<<<======== Main Image Segmenting ========>>>>>> ########################################################'''
    height, width = imgTestingNumbers2.shape
    print "=============================================================================="
    print "Width:",width,"Height:",height

    wordRatio = float(width) /float(height)
    print "Ratio:",wordRatio,"          Area:",width*height

    print "=============================================================================="
    maxi2 = -999
    maxi3 = -999

    area = width*height
    if area<1 :
        1

    elif area >= 2: #the perfect word segmenter,it was 0.9

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

        print "Start:", start, "  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        end", end

        temps = 2  # take these variables from user
        tempe = 2



        if start >= end -1 :
            end = start

        if end - start > 6 :
            print "Start:", start, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          end", end
            end = start

        print "Start:", start, "  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        end", end

        start = start - temps
        end = end + tempe

        if start < 0 and end <=3 :
            end = end + 2



        print "Start:",start,"  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        end",end

        try:
            for i in range(start , end):  # check out c[9] to c[13]  inew-2,irange+2
                for j in range(0, width):
                    imgTestingNumbers2[i, j] = 0 #as its a grayscal image,0 is the closest to black, 255 is the nearest to white
        except :

            1
    cv2.imshow("Cloud_no_B",imgTestingNumbers2)
    cv2.waitKey(0)
    GenData_C.C(imgTestingNumbers2)


    cv2.imwrite("seg.png", imgTestingNumbers) #this thing is fuckiung important
    return



