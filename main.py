import turtle
import pyautogui
import numpy
import cv2
import time
from matplotlib.colors import is_color_like

scrn=turtle.Screen()
scrn.setworldcoordinates(-400,-400,400,400)
scrn.title("My WhiteBoard")
turtle.speed(-1)
turtle.width(5)
turtle.shapesize(1.5,1.5,1.5)

pyautogui.alert(text="Click the Scroll button on your mouse to save screenshot",title="Save SS")

def color():
    global col
    col=input("Enter the colour: ")
    color_check=is_color_like(col)
    while color_check==False:
        col=input("Invalid Input! Enter the color again: ")
        color_check=is_color_like(col)
    turtle.color(col)

def thickness():
    try:
        thickNess=int(input("Enter the thickness: "))
    except ValueError:
        thickNess=int(input("Invalid input! Enter the thickness: "))
    turtle.width(thickNess)

def screen_shot(x,y):

    imgName=turtle.textinput("Name Of Image","Enter the name of the image")
    time.sleep(0.2)
# take screenshot using pyautogui
    img=pyautogui.screenshot()

# since the pyautogui takes as a 
# PIL(pillow) and in RGB we need to 
# convert it to numpy array and BGR 
# so we can write it to the disk

    img=cv2.cvtColor(numpy.array(img),cv2.COLOR_RGB2BGR)
    
# writing it to the disk using opencv
    cv2.imwrite("C:/Users\Lenovo\Pictures\Screenshots\ "+imgName+".png",img)

def setpos(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

def dragging(x,y):
    turtle.down()
    turtle.ondrag(None)
    turtle.setheading(turtle.towards(x,y))
    turtle.goto(x,y)
    turtle.ondrag(dragging)

def clickright(x,y):
    turtle.clear()

def up():
    turtle.setheading(90)
    turtle.fd(50)

def down():
    turtle.setheading(270)
    turtle.fd(50)

def right():
    turtle.setheading(0)
    turtle.fd(50)

def left():
    turtle.setheading(180)
    turtle.fd(50)

def centre():
    turtle.up()
    turtle.home()
    turtle.down()

def text():
    try:
        size=int(input("Enter the size of the text: "))
    except ValueError:
        size=int(input("Invalid Input! Enter the size of the text: "))
    text=input()
    turtle.write(text,align="center",font=("Bahnschrift",size,"normal"))

def enter():
    turtle.up()
    turtle.setheading(270)
    turtle.fd(10)
    turtle.down()


turtle.listen()
turtle.onkey(color,"c")
turtle.onkey(thickness,"t")
turtle.onkey(up,"Up")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.onkey(down,"Down")
turtle.onkey(centre,"h")
turtle.onkey(text," ")
turtle.ondrag(dragging)
turtle.onscreenclick(setpos,1)
turtle.onscreenclick(clickright,3)
turtle.onscreenclick(screen_shot,2)

turtle.mainloop()