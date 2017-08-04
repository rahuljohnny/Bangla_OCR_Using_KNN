# import the necessary packages
def HeightMatters(image):
    import cv2
    try:
        h = image[0]
        w = image[1]
        #print h,"Height_matters_                  -height      ","width       ",w

        #how Xs
        #times = 1.5#for u25 = 2.5 #(2* image.shape[1])/ image.shape[1] # r = the ratio of the new width to the old width
        #for u31 it is 3X
        ''' for u30.png  times = 1.5'''
        ''' for BSERIES keep it to = 2.5'''

        times = 2.5

        '''times 2X and min contour 60 works well for u20.png'''

        #choto sizer imager khetre times 1 rekhe min contr area should be decreased
        dim = (int(times* image.shape[1]), int(image.shape[0] * times)) # image.shape[1] = width
        #dim = (900, 300) # image.shape[1] = width

        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized
    except:
        1
