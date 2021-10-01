p= turtle.Turtle()
s= turtle.Screen()
s.bgcolor("black")
p.pencolor("white")
p.speed(0)
c=0
while 1:
    for i in range(3):
        p.forward(250)
        p.right(120)
    p.right(5)
    c+=1
    if c>=360/5:
        continue
