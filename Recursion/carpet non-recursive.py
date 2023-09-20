import turtle
turtle.tracer(10, 0) # Increase the first argument to speed up the drawing. Speed
turtle.setworldcoordinates(0, 0, 700, 700) # Starting position
turtle.hideturtle() # Doesn't show the cursor

MIN_SIZE = 10 # Try changing this to decrease/increase the amount of recursion. # The no: squares printed
DRAW_SOLID = True

def isTooSmall(width, height):
    # Determine if the rectangle is too small to draw.
    return width < MIN_SIZE or height < MIN_SIZE

def drawCarpet(x, y, width, height):
    # The x and y are the lower left corner of the carpet.

    # Move the pen into position.
    turtle.penup()
    turtle.goto(x, y) # Teleportation

    # Draw the outer rectangle. Fill black
    turtle.pendown()
    if DRAW_SOLID:
        turtle.fillcolor('black')
        turtle.begin_fill()
    turtle.goto(x, y + height)
    turtle.goto(x + width, y + height)
    turtle.goto(x + width, y)
    turtle.goto(x, y)
    if DRAW_SOLID:
        turtle.end_fill()
    turtle.penup()

    # Draw the inner rectangles.
    drawInnerRectangle(x, y, width, height)

def drawInnerRectangle(x, y, width, height):
    if isTooSmall(width, height):
        # BASE CASE
        return
    else:
        # RECURSIVE CASE
        # Coordinates to draw inner rectangle
        oneThirdWidth = width / 3
        oneThirdHeight = height / 3
        twoThirdsWidth = 2 * (width / 3)
        twoThirdsHeight = 2 * (height / 3)

        # Move into position.
        turtle.penup()
        turtle.goto(x + oneThirdWidth, y + oneThirdHeight)

        # Draw the center rectangle.

        drawer(x, y, width, height)
        count = 0
        for loop_y in range(3):
            for loop_x in range(3):
                    new_x = x + loop_x * oneThirdWidth
                    new_y = y + loop_y * oneThirdHeight
                    drawer(new_x, new_y, oneThirdWidth, oneThirdHeight)
                    for loop_y1 in range(3):
                        for loop_x1 in range(3):
                            new_x1 = new_x + loop_x1 * (oneThirdWidth/3)
                            new_y1 = new_y + loop_y1 * (oneThirdHeight/3)
                            drawer(new_x1, new_y1, oneThirdWidth/3, oneThirdHeight/3)
                            for loop_y2 in range(3):
                                for loop_x2 in range(3):
                                    new_x2 = new_x1 + loop_x2 * (oneThirdWidth / 9)
                                    new_y2 = new_y1 + loop_y2 * (oneThirdHeight / 9)
                                    drawer(new_x2, new_y2, oneThirdWidth / 9, oneThirdHeight / 9)
                                    for loop_y3 in range(3):
                                        for loop_x3 in range(3):
                                            new_x3 = new_x2 + loop_x3 * (oneThirdWidth / 27)
                                            new_y3 = new_y2 + loop_y3 * (oneThirdHeight / 27)
                                            drawer(new_x3, new_y3, oneThirdWidth / 27, oneThirdHeight / 27)
def drawer(x,y,width,height):
    oneThirdWidth = width / 3
    oneThirdHeight = height / 3
    twoThirdsWidth = 2 * (width / 3)
    twoThirdsHeight = 2 * (height / 3)

    # Move into position.
    turtle.penup()
    turtle.goto(x + oneThirdWidth, y + oneThirdHeight)

    # Draw the inner rectangle.
    if DRAW_SOLID:
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.begin_fill()
    turtle.pendown()
    turtle.goto(x + oneThirdWidth, y + twoThirdsHeight)
    turtle.goto(x + twoThirdsWidth, y + twoThirdsHeight)
    turtle.goto(x + twoThirdsWidth, y + oneThirdHeight)
    turtle.goto(x + oneThirdWidth, y + oneThirdHeight)
    turtle.penup()
    if DRAW_SOLID:
        turtle.end_fill()


# x,y,breath,lengthm 
drawCarpet(50, 50, 600, 600)
turtle.exitonclick()
