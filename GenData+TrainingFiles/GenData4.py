# GenData.py

import sys
import numpy as np
import cv2
import os
from intValidChars import *

# module level variables ##########################################################################
MIN_CONTOUR_AREA = 55

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30


###################################################################################################
def main():
    imgTrainingNumbers = cv2.imread("TrainTestIMG\\Train_sta.png")  # read in training numbers image

    if imgTrainingNumbers is None:  # if image was not read successfully
        print "error: image not read from file \n\n"  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit function (which exits program)
    # end if

    imgGray = cv2.cvtColor(imgTrainingNumbers, cv2.COLOR_BGR2GRAY)  # get grayscale image
    imgBlurred = cv2.GaussianBlur(imgGray, (5, 5), 0)  # blur

    # filter image from grayscale to black and white
    imgThresh = cv2.adaptiveThreshold(imgBlurred,  # input image
                                      255,  # make pixels that pass the threshold full white
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      # use gaussian rather than mean, seems to give better results
                                      cv2.THRESH_BINARY_INV,
                                      # invert so foreground will be white, background will be black
                                      11,  # size of a pixel neighborhood used to calculate threshold value
                                      2)  # constant subtracted from the mean or weighted mean

    cv2.imshow("imgThresh", imgThresh)  # show threshold image for reference

    imgThreshCopy = imgThresh.copy()  # make a copy of the thresh image, this in necessary b/c findContours modifies the image

    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                              # input image, make sure to use a copy since the function will modify this image in the course of finding contours
                                                              cv2.RETR_EXTERNAL,  # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE)  # compress horizontal, vertical, and diagonal segments and leave only their end points

    # declare empty numpy array, we will use this to write to file later
    # zero rows, enough cols to hold all image data
    npaFlattenedImages = np.empty((0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))

    intClassifications = []  # declare empty classifications list, this will be our list of how we are classifying our chars from user input, we will write to file at the end

    # possible chars we are interested in are digits 0 through 9, put these in list intValidChars
    '''
    intValidChars = [
        # LETTERS

        ord('q'), ord('w'), ord('e'), ord('r'), ord('t'), ord('y'), ord('u'), ord('i'), ord('o'), ord('p'), ord('a'),
        ord('s'), ord('d'), ord('f'), ord('g'), ord('h'), ord('j'),
        ord('k'), ord('l'), ord('z'), ord('x'), ord('c'), ord('v'), ord('b'), ord('n'), ord('m'),
        ord('E'), ord('Q'), ord('W'), ord('R'), ord('T'), ord('Y'), ord('U'), ord('I'), ord('O'), ord('P'), ord('A'),
        ord('S'), ord('D'), ord('F'), ord('G'), ord('H'), ord('J'),
        ord('K'), ord('L'), ord('Z'), ord('X'), ord('C'), ord('V'), ord('B'), ord('N'), ord('M'),

        # NUMBERS

        ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9'),

        # SYMBOLS

        ord('~'), ord('!'), ord('#'), ord('$'), ord('%'), ord('^'), ord('&'), ord('*'), ord('('), ord(')'), ord('{'),
        ord('}'), ord(';'), ord(':'), ord('"'), ord(','), ord('?'), ord('%'),
        ord('`'), ord('-'), ord('+'),

        # COMPOUND_CHARACTERS

        1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017,
        1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032,
        1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050,
        1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065,
        1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083,
        1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098,
        1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116,
        1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131,
        1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149,
        1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164,
        1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172
    ]
    '''
    for npaContour in npaContours:  # for each contour
        if cv2.contourArea(npaContour) > MIN_CONTOUR_AREA:  # if contour is big enough to consider
            [intX, intY, intW, intH] = cv2.boundingRect(npaContour)  # get and break out bounding rect

            # draw rectangle around each contour as we ask user for input
            cv2.rectangle(imgTrainingNumbers,  # draw rectangle on original training image
                          (intX, intY),  # upper left corner
                          (intX + intW, intY + intH),  # lower right corner
                          (0, 0, 255),  # red
                          2)  # thickness

            imgROI = imgThresh[intY:intY + intH, intX:intX + intW]  # crop char out of threshold image
            imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH,
                                                RESIZED_IMAGE_HEIGHT))  # resize image, this will be more consistent for recognition and storage

            cv2.imshow("imgROI", imgROI)  # show cropped out char for reference
            cv2.imshow("imgROIResized", imgROIResized)  # show resized image for reference
            cv2.imshow("training_numbers.png",
                       imgTrainingNumbers)  # show training numbers image, this will now have red rectangles drawn on it

            intChar = 1
            intChar = intChar + 1000
            if intChar == 27:  # if esc key was pressed
                sys.exit()  # exit program
            elif intChar in intValidChars:  # else if the char is in the list of chars we are looking for . . .

                intClassifications.append(
                    intChar)  # append classification char to integer list of chars (we will convert to float later before writing to file)

                npaFlattenedImage = imgROIResized.reshape((1,
                                                           RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))  # flatten image to 1d numpy array so we can write to file later
                npaFlattenedImages = np.append(npaFlattenedImages, npaFlattenedImage,
                                               0)  # add current flattened impage numpy array to list of flattened image numpy arrays
                # end if
                # end if
    # end for

    fltClassifications = np.array(intClassifications,
                                  np.float32)  # convert classifications list of ints to numpy array of floats

    npaClassifications = fltClassifications.reshape(
        (fltClassifications.size, 1))  # flatten numpy array of floats to 1d so we can write to file later

    print "\n\ntraining complete !!\n"

    np.savetxt("classifications.txt", npaClassifications)  # write flattened images to file
    np.savetxt("flattened_images.txt", npaFlattenedImages)  #

    cv2.destroyAllWindows()  # remove windows from memory

    return


###################################################################################################
if __name__ == "__main__":
    main()
# end if
