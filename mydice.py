from PIL import Image, ImageOps, ImageDraw
img = Image.open('img.jpg')
dice1 = Image.open('1.jpg', 'r')
dice2 = Image.open('2.jpg', 'r')
dice3 = Image.open('3.jpg', 'r')
dice4 = Image.open('4.jpg', 'r')
dice5 = Image.open('5.jpg', 'r')
dice6 = Image.open('6.jpg', 'r')
dice7 = Image.open('6.jpg', 'r')
#Apply Filter
img = ImageOps.grayscale(img)
img = ImageOps.equalize(img)

dicesize = dice1.size[0]
dicew =img.width//dicesize
diceh = img.height//dicesize

nim = Image.new("L",(img.width,img.height),"white")
nimd = ImageDraw.Draw(nim)

##
background = Image.new('RGB', (dicesize*dicew, dicesize*diceh), (255, 255, 255))
##

for y in range(0,img.height-dicesize, dicesize):
    for x in range(0, img.width-dicesize,dicesize):
        thissectorcolor = 0
        for dicex in range (0,dicesize):
            for dicey in range(0,dicesize):
                thiscolor = img.getpixel((x+dicex, y+dicey))
                thissectorcolor += thiscolor
        thissectorcolor /= (dicesize**2)
        nimd.rectangle([(x, y), (x+dicesize, y+dicesize)],int(thissectorcolor))
        dicenumber = (255-thissectorcolor)* 6.0 / 255 + 1 
        ##
        dicefile = eval('dice%d'%dicenumber)
        background.paste(dicefile, (x,y))
        ##
        
        #print(int(dicenumber),end=' ')
    #print()
background.save('out.png')
print('Done')

#nim.show()
#input()
