'''import pytesseract
from pdf2image import convert_from_path
import cv2

# set path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# convert PDF to images
pdf_path = r"Telecom Offer Recommendation.pdf"
images = convert_from_path(pdf_path, 350)

# loop over each image and extract text
text = ''
for i, image in enumerate(images):
    # save image as JPEG
    image_name = "Page_" + str(i + 1) + ".jpg"
    image.save(image_name, "JPEG")

    # read image and extract text
    img = cv2.imread(image_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 30)

    # Dilate to combine adjacent text contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    dilate = cv2.dilate(thresh, kernel, iterations=4)

    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)

        if y >= 600 and x <= 1000:
            if area > 10000:
                roi = img[y:y + h, x:x + w]
                roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                roi_thresh = cv2.threshold(roi_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
                text += pytesseract.image_to_string(roi_thresh, config='--psm 6')

        if y >= 2400 and x <= 2000:
            roi = img[y:y + h, x:x + w]
            roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            roi_thresh = cv2.threshold(roi_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            text += pytesseract.image_to_string(roi_thresh, config='--psm 6')

# print extracted text
print(text)'''

import pytesseract
from pdf2image import convert_from_path
import cv2

# set path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# convert PDF to images
pdf_path = r"Telecom Offer Recommendation.pdf"
images = convert_from_path(pdf_path, 350)

# loop over each image and extract text
text = ''
for i, image in enumerate(images):
    # save image as JPEG
    image_name = "Page_" + str(i+1) + ".jpg"
    image.save(image_name, "JPEG")

    # read image and extract text
    img = cv2.imread(image_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9,9), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 30)

    # Dilate to combine adjacent text contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
    dilate = cv2.dilate(thresh, kernel, iterations=4)

    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # Sort contours by their vertical position (top to bottom)
    cnts = sorted(cnts, key=lambda c: cv2.boundingRect(c)[1])

    for c in cnts:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)

        roi = img[y:y+h, x:x+w]
        roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        roi_thresh = cv2.threshold(roi_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        text += pytesseract.image_to_string(roi_thresh, config='--psm 6')

# print extracted text
print(text)

