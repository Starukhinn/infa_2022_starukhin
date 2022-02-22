import turtle
index_square = 1
side_length = 50
bias = 10
position_on_oy = 0
position_on_ox = 0
turtle.shape('turtle')
while index_square < 11:
    turtle.penup()
    turtle.goto(position_on_ox, position_on_oy)
    turtle.pendown()
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    side_length += 20
    position_on_oy -= bias
    position_on_ox -= bias
    index_square += 1
    
