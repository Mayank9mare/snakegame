from turtle import Turtle
pos=[(0,0),(-20,0),(-40,0)]
x=20
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.segment=[]
        self.createSnake()
        self.head=self.segment[0]
    def createSnake(self):
        for i in pos:
            self.addSegment(i)

    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            new_x=self.segment[i-1].xcor()
            new_y=self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.segment[0].forward(20)
    def up(self):
        if self.segment[0].heading()!=down:
            self.segment[0].setheading(90)
    def down(self):
        if self.segment[0].heading()!=up:
            self.segment[0].setheading(270)
    def left(self):
        if self.segment[0].heading()!=right:
            self.segment[0].setheading(180)
    def right(self):
        if self.segment[0].heading()!=left:
            self.segment[0].setheading(0)
    def addSegment(self,pos):
        t=Turtle("square")
        t.color("white")
        t.speed("fastest")
        t.penup()
        t.goto(pos)
        self.segment.append(t)


    def extend(self):
        self.addSegment(self.segment[-1].position())




