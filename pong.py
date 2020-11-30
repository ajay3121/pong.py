
#hi this is simple pong game which can be played by two people  

from turtle import*
from random import*
wn = Screen()
wn.bgcolor("black")
wn.screensize(800,600)
wn.title("pong by dark_knight")
wn.tracer()

#points
scor_a = 0
scor_b = 0
#pen
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,280)
pen.write("Player A : {}  Player B : {}".format(scor_a,scor_b),align = "center",font= (30))
#padding_a
padding_a = Turtle()
padding_a.speed(0)
padding_a.color("white")
padding_a.shape("square")
padding_a.penup()
padding_a.shapesize(5,1)
padding_a.goto(350,0)

#padding_b
padding_b = Turtle()
padding_b.speed(0)
padding_b.color("white")
padding_b.shape("square")
padding_b.penup()
padding_b.shapesize(5,1)
padding_b.goto(-350,0)

#ball
ball = Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.goto(0,0)
ball.penup()
ball.dx= 3.5
ball.dy = 3.5

#padding_movement
def padding_b_up():
    y = padding_b.ycor()
    y+=20
    padding_b.sety(y)
def padding_b_down():
    y = padding_b.ycor()
    y-=20
    padding_b.sety(y)
def padding_a_up():
    y = padding_a.ycor()
    y+=20
    padding_a.sety(y)
def padding_a_down():
    y = padding_a.ycor()
    y-=20
    padding_a.sety(y)
#listening
wn.listen()
wn.onkeypress(padding_b_up,"w")
wn.onkeypress(padding_b_down,"s")
wn.onkeypress(padding_a_up,"Up")
wn.onkeypress(padding_a_down,"Down")
while True:
    wn.update()

    #ball movement
    ball.goto(ball.xcor() + ball.dx,ball.ycor() + ball.dy)

    #top and bottom border checks
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1
    #left and right padding



    #leftpadding
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    #ball bounce right padding
    if ball.xcor() >= 330 and ball.xcor() <= 340 and (ball.ycor() < padding_a.ycor() + 40 and ball.ycor() > padding_a.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1
    #ball bounce right padding
    if ball.xcor() <= -330 and ball.xcor() >= -340 and (ball.ycor() < padding_b.ycor() + 40 and ball.ycor() > padding_b.ycor() - 40 ):
        ball.setx(-330)
        ball.dx *= -1

    if ball.xcor() > 350:
        scor_a+=1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(scor_a,scor_b), align="center", font=(30))
    if ball.xcor() < -350:
        scor_b = scor_b + 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(scor_a, scor_b), align="center", font=(30))
    if scor_b > 30 or scor_a > 30:
        pen.goto(0,0)
        pen.write("GAME OVER",align = "center" , font = (40))
        break


wn.exitonclick()




