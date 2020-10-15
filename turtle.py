import turtle
pen = turtle.Turtle()

pen.pendown() #this line puts the pen on the paper
for side in range(3): #see number three? its what reminds Python,  THREE times!
  pen.forward(100)
  pen.right(90)
pen.forward(100)

wn = turtle.Screen()
wn.listen()

turtle.done() #this just keeps the window open until we close it
