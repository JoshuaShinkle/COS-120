from cImage import *

def sepiaPixel(p):
    red = int((p.getRed()*.393 + p.getGreen()*.769 + p.getBlue()*.189)/3)
    green = int((p.getRed()*.349 + p.getGreen()*.686 + p.getBlue()*.168)/3)
    blue = int((p.getRed()*.272 + p.getGreen()*.534 + p.getBlue()*.131)/3)
    
    return Pixel(red,green,blue)

def blackAndWhite(p, threshold):
    red = p.getRed()
    green = p.getGreen()
    blue = p.getBlue()

    if (red + blue + green)/3 <= threshold:
        nc = 0
    else:
        nc = 255
    return Pixel(nc,nc,nc)

def pixelMapperBlack(rgbFunction,oldImage,title,threshold):
    width = oldImage.getWidth() 
    height = oldImage.getHeight() 
    myImageWindow = ImageWin(title, width*2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width,height)
    for row in range(height):
        for col in range(width):
            originalPixel = oldImage.getPixel(col,row) 
            newPixel = rgbFunction(originalPixel, threshold) 
            newIm.setPixel(col,row,newPixel)
    newIm.setPosition(width + 1, 0) 
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()

def grayPixel(p):
    nc=(p.getRed()+p.getGreen()+p.getBlue())//3
    return Pixel(nc,nc,nc)

def negativePixel(p):
    r=255-p.getRed()
    g=255-p.getGreen()
    b=255-p.getBlue()
    return Pixel(r,g,b)

def RGBAdjust(p,radj,gadj,badj):
    pRed = p.getRed()
    pGreen = p.getGreen()
    pBlue = p.getBlue()
    newPixel = Pixel(int(pRed*radj), int(pGreen*gadj), int(pBlue*badj))
    return newPixel

def pixelMapperAdjust(rgbFunction,oldImage,title,radj,gadj,badj):
    width = oldImage.getWidth() 
    height = oldImage.getHeight() 
    myImageWindow = ImageWin(title, width*2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width,height)
    for row in range(height):
        for col in range(width):
            originalPixel = oldImage.getPixel(col,row) 
            newPixel = rgbFunction(originalPixel,radj,gadj,badj)
            newIm.setPixel(col,row,newPixel)
    newIm.setPosition(width + 1, 0) 
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()

def halfSize(oldImage): 
    oldw = oldImage.getWidth()
    oldh = oldImage.getHeight()
    newim = EmptyImage(oldw//2,oldh//2)
    myimagewindow = ImageWin("Image Processing", oldw+oldw//2,oldh)
    oldImage.draw(myimagewindow)
    for row in range(oldh//2):
        for col in range(oldw//2):
            p1=oldImage.getPixel(2 * col, 2 * row)
            p2=oldImage.getPixel(2 * col + 1, 2 * row)
            p3=oldImage.getPixel(2 * col , 2 * row + 1)
            p4=oldImage.getPixel(2 * col + 1, 2* row+1)
            r=(p1.getRed()+p2.getRed()+p3.getRed()+p4.getRed())//4
            g=(p1.getGreen()+p2.getGreen()+p3.getGreen()+p4.getGreen())//4
            b=(p1.getBlue()+p2.getBlue()+p3.getBlue()+p4.getBlue())//4
            newPixel=Pixel(r,g,b)
            newim.setPixel(col,row,newPixel)
    newim.setPosition(oldw+1,0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()

def pixelMapper(rgbFunction,oldImage,title):
    width = oldImage.getWidth() 
    height = oldImage.getHeight() 
    myImageWindow = ImageWin(title, width*2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width,height)
    for row in range(height):
        for col in range(width):
            originalPixel = oldImage.getPixel(col,row) 
            newPixel = rgbFunction(originalPixel) 
            newIm.setPixel(col,row,newPixel)
    newIm.setPosition(width + 1, 0) 
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()


def imageProc(fname):
    if fname!="":
        myImage=FileImage(fname)
    else:
        myImage=""
    answer=0
    while answer != 9:
        if myImage !="":
            print("1) Load an image\n2) Adjust RGB values\n3) Produce a gray-scale image of the current image\n4) Produce a black and white of the current image\n5) Produce a sepia-toned image of the current image\n6) Produce a negative of the current image\n7) Reduce image size by 1/2 (1/4 the original pixels)\n8) Save the image\n9) Exit")
            answer=int(input("Select a menu choice => "))
            while answer not in [1,2,3,4,5,6,7,8,9]:
                print("1) Load an image\n2) Adjust RGB values\n3) Produce a gray-scale image of the current image\n4) Produce a black and white of the current image\n5) Produce a sepia-toned image of the current image\n6) Produce a negative of the current image\n7) Reduce image size by 1/2 (1/4 the original pixels)\n8) Save the image\n9) Exit")
                answer=int(input("Select a menu choice => "))
        else: #the default image is not present
            print("1) Load an image\n9) Exit")
            answer=int(input("Select a menu choice => "))
            while answer not in [1,9]:
                print("1) Load an image\n9) Exit")
                answer=int(input("Select a menu choice => "))
        if answer==1:
            myWin = ImageWin("Image Processing",600,400)
            fileName = input("Enter filename -> ")
            myImage = FileImage(fileName)
            myImage.draw(myWin)

        elif answer==2:
            radj = float(input("Enter float to adjust red color component -> "))
            gadj = float(input("Enter float to adjust green color component -> "))
            badj = float(input("Enter float to adjust blue color component -> "))
            pixelMapperAdjust(RGBAdjust,myImage,"Ajusting Image",radj,gadj,badj)

        elif answer==3:
            pixelMapper(grayPixel,myImage,"Grayscale Image")
        elif answer==4:
            threshold = int(input("Enter a threshold-> "))
            pixelMapperBlack(blackAndWhite,myImage,"Black and White Image", threshold)
        elif answer==5:
            pixelMapper(sepiaPixel,myImage,"Sepia Image")
        elif answer==6:
            pixelMapper(negativePixel,myImage,"Negative Image")
        elif answer==7:
            halfSize(myImage)
        elif answer==8:
            path = input("Enter filename to save image-> ")
            myImage.save(path)

      
imageProc("pencils.gif")
