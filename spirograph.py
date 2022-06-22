import math
import turtle
def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x+r, y)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(-r) #draw clockwise
    
'''    turtle.setpos(x + r, y)
    turtle.down()
# draw the circle
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))'''

#draw_circle(0, 0, 50)


'''def draw(R, r, l):
    k = r/R
    turtle.penup()
    x = R*((1-k)*math.cos(0)+l*k*math.cos((1-k)/k*0))
    y = R*((1-k)*math.sin(0)-l*k*math.sin((1-k)/k*0))
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(90)
    for i in range(0, 361*r//math.gcd(r,R), 5):
        t = math.radians(i)  
        x = R*((1-k)*math.cos(t)+l*k*math.cos((1-k)/k*t))
        y = R*((1-k)*math.sin(t)-l*k*math.sin((1-k)/k*t))
        turtle.setpos(x,y)

draw(90,20,1)
turtle.mainloop()'''
STEPS = 3

class Spiro:

    def __init__(self, R, r, l, xc = 0, yc = 0) -> None:
        self.R = R
        self.r = r
        self.l = l
        self.k = self.r/self.R
        self.xc = xc
        self.yc = yc

    def __setup_cursor(self):

        turtle.penup()
        x = self.R*((1-self.k)*math.cos(0)+self.l*self.k*math.cos((1-self.k)/self.k*0))
        y = self.R*((1-self.k)*math.sin(0)-self.l*self.k*math.sin((1-self.k)/self.k*0))
        turtle.goto(x, y)
        turtle.pendown()
        turtle.right(90)

    def draw(self):
        #self.__setup_cursor()
        plot = []
        for i in range(0, 361*self.r//math.gcd(self.r,self.R), STEPS):
            t = math.radians(i)  
            x = self.R*((1-self.k)*math.cos(t)+self.l*self.k*math.cos((1-self.k)/self.k*t))
            y = self.R*((1-self.k)*math.sin(t)-self.l*self.k*math.sin((1-self.k)/self.k*t))
            #turtle.setpos(x,y)
            plot.append([x + self.xc, y + self.yc])
        return plot

#spiro = Spiro(300, 220, 0.8)
#spiro.draw()
#turtle.mainloop()