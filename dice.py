from PIL import Image, ImageOps, ImageDraw
img = Image.open('E:\img.jpg')
#img.show()
img = ImageOps.grayscale(img)
img = ImageOps.equalize(img)
print(img.width)
dicew =int(input("DiceW : "))
dicesize = int(img.width *1.0 / dicew)
#
diceh = int(img.height * 1.0 / img.width * dicew)
print(diceh)
nim = Image.new("L",(img.width,img.height),"white")
nimd = ImageDraw.Draw(nim)

for y in range(0,img.height-dicesize, dicesize):
    for x in range(0, img.width-dicesize,dicesize):
        thissectorcolor = 0
        for dicex in range (0,dicesize):
            for dicey in range(0,dicesize):
                thiscolor = img.getpixel((x+dicex, y+dicey))
                thissectorcolor += thiscolor
        #
        thissectorcolor /= (dicesize**2)
        nimd.rectangle([(x, y), (x+dicesize, y+dicesize)],int(thissectorcolor))
        #
        dicenumber = (255-thissectorcolor)* 6.0 / 255 + 1
        print(int(dicenumber),end=' ')
    print()

#nim.show()
input()
