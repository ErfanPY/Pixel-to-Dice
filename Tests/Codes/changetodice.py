from PIL import Image
import random
dice1 = Image.open('1.jpg', 'r')
dice2 = Image.open('2.jpg', 'r')
dice3 = Image.open('3.jpg', 'r')
dice4 = Image.open('4.jpg', 'r')
dice5 = Image.open('5.jpg', 'r')
dice6 = Image.open('6.jpg', 'r')
##This are difined in main program
#dicenumber = 6
dicew, diceh = 100, 177
x = 10
y =10
##
#dicefile = eval('dice%d'%dicenumber)
#dice_w, dice_h = dicefile.size
background = Image.new('RGB', (50*dicew, 50*diceh), (255, 255, 255))
bg_w, bg_h = background.size
#          x\/ y\/
location = (x, y)
#background.paste(dicefile, location)
for y in range(0,10000,50):
    for x in range(0,10000,50):
        dicenumber = random.randint(1,6)
        dicefile = eval('dice%d'%dicenumber)
        background.paste(dicefile, (x,y))


        
background.save('out.png')
print('done')
