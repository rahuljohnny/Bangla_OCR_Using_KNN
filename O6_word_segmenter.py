from importer import *
arr2=[]
def word_segmenter(count2):

   imgTestingNumbers2 = cv2.imread("words.png")
   if imgTestingNumbers2 is None:
       print "error: image not read from file \n\n"
       os.system("pause")
       return
   #######################################################<<<<<========  Main Image Segmenting ========>>>>>>########################################################

   height, width, channels = imgTestingNumbers2.shape
   print "Height:"
   print height
   print "Width:"
   print width
   wordRatio = float(width) / float(height)
   print "Ratio:"
   print wordRatio
   if wordRatio >= 0.9 :
       maxi = 9999
       inew0 =-999
       c = array.array('i', (0,) * 100)
       for i in range(0, int(height) / 2):
           for j in range(0, width):
               if np.any(imgTestingNumbers2[i, j] == 0):   #if longest white line(matra) found
                   c[i] = c[i] + 1
                   # cv2.imshow("le_loop_janala_cropped ",imgTestingNumbers2[i,j])

          # print c[i]
           if c[i] <maxi:
               maxi = c[i]
               inew=i
           elif c[i]-maxi <= int(width /3):
               inew0=i
       if inew0>inew:
           irange=inew0
       else:
           irange=inew
       #newrange=abs((inew+irange)/2)

       for i in range(inew - 2, irange + 2):  # check out c[9] to c[13]  inew-2,irange+2
           for j in range(0, width):
               imgTestingNumbers2[i, j] = 1

   imgGray1 = cv2.cvtColor(imgTestingNumbers2, cv2.COLOR_BGR2GRAY)
   #imgBlurred1 = cv2.GaussianBlur(imgGray1, (5, 5), 0)  # blur @2

   #cv2.imshow("After operation blur", imgBlurred1)
   imgThresh1 = cv2.adaptiveThreshold(imgGray1,  # input image  @3
                                      255,  # make pixels that pass the threshold full white
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      # use gaussian rather than mean, seems to give better results
                                      cv2.THRESH_BINARY_INV,
                                      # invert so foreground will be white, background will be black
                                      111,  #Increasing this level worked! size of a pixel neighborhood used to calculate threshold value
                                      2
                                      )  # constant subtracted from the mean or weighted mean
   arr2.append(imgThresh1)

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
       cv2.imwrite("CreS2//c7.png", arr2[count2 - 1])
   elif count2 == 9:
       cv2.imwrite("CreS2//c8.png", arr2[count2 - 1])
   elif count2 == 10:
       cv2.imwrite("CreS2//c9.png", arr2[count2 - 1])
   elif count2 == 0:
       cv2.imwrite("CreS2//c-1.png", arr2[count2 - 1])

   cv2.imwrite("wordseg.png", arr2[count2])

   cv2.imshow("shown",imgThresh1)
   cv2.waitKey(0)  # wait for user key press
   #cv2.destroyAllWindows()
   return imgThresh1
