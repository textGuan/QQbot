import cv2
import os
import time
from aip import AipOcr

AppId = 'your appid'
APIKey = 'apikey'
SecretKey = 'secret key'
text = dict()
result = []
# path = 'test.jpg'    

def process_image(image):
    image = cv2.resize(image,(500,1000))
    img1 = image[0:400,0:80]
    img2 = image[300:700,0:80]
    img3 = image[600:1000,0:80]
    cv2.imwrite('temp/img1.png',img1)
    cv2.imwrite('temp/img2.png',img2)
    cv2.imwrite('temp/img3.png',img3)
    pass
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def run(image_input):
    client = AipOcr(AppId, APIKey, SecretKey)
    # image_input = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    process_image(image_input)
    img1 = get_file_content('temp/img1.png')
    img2 = get_file_content('temp/img2.png')
    img3 = get_file_content('temp/img3.png')

    time.sleep(1)
    text = client.basicGeneral(img1)
    if "words_result" not in text:
        return ["ERROR"]
    # print(text)
    text = text["words_result"]
    for i in range(len(text)):
        if text[i]["words"] not in result:
            result.append(text[i]["words"])
    
    
    time.sleep(1)
    text = client.basicGeneral(img2)
    if "words_result" not in text:
        return ["ERROR"]
    # print(text)
    text = text["words_result"]
    for i in range(len(text)):
        if text[i]["words"] not in result:
            result.append(text[i]["words"])

    time.sleep(1)
    text = client.basicGeneral(img3)
    if "words_result" not in text:
        return ["ERROR"]
    # print(text)
    text = text["words_result"]
    for i in range(len(text)):
        if text[i]["words"] not in result:
            result.append(text[i]["words"])

    return result