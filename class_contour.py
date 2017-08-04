from importer import *
import copy
class ContourWithData():
    # member variables ############################################################################
    npaContour = None  # contour
    boundingRect = None  # bounding rect for contour
    intRectX = 0  # bounding rect top left corner x location
    intRectY = 0  # bounding rect top left corner y location
    intRectWidth = 0  # bounding rect width
    intRectHeight = 0  # bounding rect height
    fltArea = 0.0  # area of contour

    def calculateRectTopLeftPointAndWidthAndHeight(self):  # calculate bounding rect info
        [intX, intY, intWidth, intHeight] = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight

    def checkIfContourIsValid(self):  # this is oversimplified, for a production grade program
        if self.fltArea < MIN_CONTOUR_AREA: return False  # much better validity checking would be necessary
        return True

    intRectY = intRectY-555


def ndlist(init, *args):  # python 2 doesn't have kwarg after *args
    dp = init
    for x in reversed(args):
        dp = [copy.deepcopy(dp) for _ in xrange(x)] # Python 2 xrange
    return dp

'''
class lines2:
     def __init__(self, column, width, img):
         self.column = column
         self.width = width
         self.img = img
     def __repr__(self):
         return repr((self.column, self.width, self.img))
'''