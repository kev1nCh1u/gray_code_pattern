from PIL import Image, ImageDraw
import os

#################################################################
# get file path
#################################################################
def GrayCodePattern(w, h, cut, num):
    black = (0, 0, 0)
    white = (255, 255, 255)
    im = Image.new('RGB', (w, h), white)
    draw = ImageDraw.Draw(im)
    count = 1
    
    if(cut % 2):
        color = white
        odd = cut - 1
    else:
        color = black
        odd = cut
    cutLevel = w/odd

    for i in range(1, cut+1):
        draw.rectangle((cutLevel*(i-1), 0, cutLevel*i, h), color)
        count += 1
        if(count == 2):
            if(color == black):
                color = white
            else:
                color = black
            count = 0

    # im.show() # debug
    savePath = filePath + '/img/' + str(num) + '.jpg'
    im.save(savePath, quality=95)

#################################################################
# get file path
#################################################################
def BlackWhitePattern(w, h, cut, num):
    black = (0, 0, 0)
    white = (255, 255, 255)
    im = Image.new('RGB', (w, h), white)
    draw = ImageDraw.Draw(im)
    count = 1
    cutLevel = w/cut

    if(cut % 2):
        color = white
        odd = cut - 1
    else:
        color = black
        odd = cut

    for i in range(1, cut+1):
        if(i % 2):
            draw.rectangle((cutLevel*(i-1), 0, cutLevel*i, h), white)
        else:
            draw.rectangle((cutLevel*(i-1), 0, cutLevel*i, h), black)

    # im.show() # debug
    savePath = filePath + '/img/' + str(num) + '.jpg'
    im.save(savePath, quality=95)

#################################################################
# get file path
#################################################################
filePath = os.path.abspath(os.getcwd())
print(filePath)

#################################################################
# get file path
#################################################################
num = 500
genList = []
i = 2
while (i < num):
    genList.append(i)
    genList.append(i+1)
    i = i * 2

#################################################################
# main
#################################################################
w, h = 912, 1140
for i, j in zip(genList, range(1, len(genList))):
    GrayCodePattern(w, h, i, j)
