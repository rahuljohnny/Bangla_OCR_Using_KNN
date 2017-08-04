from class_contour import *
from importer import *
imgTestingNumbers2 = cv2.imread("tw44.png")
###################################################################################################
###################################################################################################
arr2=[]
co = 0
def word_segmenter2(count2,imgTestingNumbers):


    try:

        cv2.imwrite("ttt\\2_Words.png", imgTestingNumbers)
        imgTestingNumbers2 = cv2.imread("ttt\\2_Words.png")
        imgTestingNumbersT = imgTestingNumbers2.copy()
        ''' ####################################################### <<<<<======== Main Image Segmenting ========>>>>>>########################################################'''
        try:
            height, width, channels = imgTestingNumbers2.shape


            #print "Width:",width,"Height:",height

            wordRatio = float(width) /float(height)
            #print "Ratio:",wordRatio,"          Area:",width*height
            #   print "=============================================================================="
            maxi2 = -999
            maxi3 = -999
            mini = 9998
            area = width*height
            if area<5 :
                print "Too small image to work with"


            elif area >= 5: #the perfect word segmenter,it was 0.9

                if height / width <5  :

                    '''
                    if height > width:
                        size = height
                    else :
                        size = width
                    '''
                    c = array.array('i', (0,) *(width+20))

                    for i in range(0, int(height) / 2):
                        d = 0
                        for j in range(0, width):
                            if np.any(imgTestingNumbers2[i, j] == 0):  # if longest white line(matra) found

                                if d==0:
                                    c[i]=0
                                d = d + 1
                                c[i] = c[i] + 1

                                if c[i] > maxi2:
                                    maxi2 = c[i]

                    try:
                        if maxi2 > 10:
                            maxi3 = maxi2 / 4
                    except:
                        maxi3 = maxi2
                    print "The array is:::::::::   1    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
                    print(i, ":i,for c=", c)

                    '''================================================================================================================='''
                    '''================================================================================================================='''
                    '''
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
                    tempe = 3



                    if start >= end -1 :
                        end = start

                    if end - start > 6 :
                        print "Start:", start, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          end", end
                        end = start

                    '''
                    starting = 0
                    jindex = 0
                    ii = 0
                    range3=int(width/3)
                    for i in range(0, int(len(c) / 2)):

                        #print "i **************", i, "****** ,start==> ", c[i]
                        if (mini - c[i]) > range3 and (c[i + 2] != 0 or c[i + 3] != 0 or c[i + 4] != 0 or c[i + 5] != 0 or c[i + 6] != 0 or c[i + 7] != 0):
                            #print "i###############", i, "****** ,start==> ", c[i]
                            starting = starting +1
                            mini = c[i]

                            start = i
                            start = start - 1

                    #print c[i], "<==c[i]====================*start=>",start,"********************* mini==>", mini
                    for i in range(start, int(len(c) / 2)):

                        if (abs(mini-c[i]) <= range3) and (c[i + 2] != 0 or c[i + 3] != 0 or c[i + 4] != 0 or c[i + 5] != 0 or c[i + 6] != 0 or c[i + 7] != 0) :

                            if i- ii > 1 :
                                break;
                            #print c[i],"<==c[i]====================*******   2    ********* mini==>", mini,"==========jindex  ==>",jindex
                            jindex = jindex +1
                            ii = i

                    stop = jindex



                    if stop <= start:
                        stop = start + 6

                    if abs(stop - start) <= 3:
                        stop = start + 6
                    '''Start and Stop must be handled properly'''
                    temps = 2
                    tempe = 3
                    start = start - temps
                    stop = stop + tempe


                    ''' for u30.png
                    start = start - 2
                    #stop = stop + 1


                    '''


                    if start < 0:

                        start = 0
                        stop = start + 11  # Manipulating this is a trump card

                    #start =5
                    #stop = 26


                    try:
                        print "Start:", start, "  %%%%%%%%%%% 3  %%%%%%%%%%%%%%%   stop", stop

                    except:
                        1


                    try:
                        for i in range(start, stop):  # check out c[9] to c[13]  inew-2,irange+2
                            for j in range(0, width):
                                imgTestingNumbers2[i, j] = 1

                    except:
                        1


            gray2= cv2.cvtColor(imgTestingNumbers2, cv2.COLOR_BGR2GRAY)
            ret, imgThresh1 = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)



            '''
            cv2.imshow("Word_seg===", imgThresh1)
            cv2.waitKey(0)
            cv2.destroyAllWindows() #Window("Resolved===")
            cv2.destroyWindow("Resolved===")
            #'''

            arr2.append(imgThresh1)
            imgTestingNumbers3 = imgThresh1.copy()
            '''########################################################################################################################'''
            cv2.imwrite("4_wordseg.png", imgTestingNumbers3) #this thing is fuckiung important
            '''
            kernel = np.ones((5, 5), np.uint8)
            eroded = cv2.erode(imgTestingNumbers3, kernel, iterations=1)

            cv2.imshow("eroded",eroded)

            cv2.waitKey(0)
            #'''
            return imgTestingNumbers3
        except:

            return imgTestingNumbersT



    except:
        return 1
