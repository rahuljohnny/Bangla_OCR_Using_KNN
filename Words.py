import cv2
import numpy
def MakeImageClearer(image):

    image = cv2.imread("u42.jpg")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # imgBlurred = cv2.GaussianBlur(gray, (5, 5), 0)  #  Must be inactive for semilevel images like pdf-ramkrishna vivekananda
    ret, imgThresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    image = imgThresh.copy()  # Copying thresh image,this in necessary b/c findContours modifies the image

    h = image[0]
    w = image[1]
    print h, "-height      ", "width       ", w
    n = numpy.zeros((3,3))
    s = numpy.zeros((3,3))
    w = numpy.zeros((3,3))
    e = numpy.zeros((3,3))

    n[0][1] = 1
    s[2][1] = 1
    w[1][0] = 1
    e[1][2] = 1

    img_n = cv2.erode(image, n, iterations=1)
    img_s = cv2.erode(image, s, iterations=1)
    img_w = cv2.erode(image, w, iterations=1)
    img_e = cv2.erode(image, e, iterations=1)

    result = img_n + img_s + img_w + img_e + image

    ret, result2 = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #cv2.imshow("res",result2)
    return result2
